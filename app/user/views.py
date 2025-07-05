from django.shortcuts import render, redirect
from django.views import View
from core.models import *
from django.views.generic.edit import FormView
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from user.forms import SignUpForm, LoginForm
from jsonpath_ng import parse
import requests
from django.http import HttpResponse


class UpdateDataBaseView(View):

    def check_in_database(self, req, data_of_journals):

        """
            Проверка подлинности данных из различных источников
        """

        for field in data_of_journals:
            temp_object_of_journal = None
            print(field['country_code'][0])
            try:
                temp_object_of_journal = Journal.objects.get(issn=field['issn'][0][0])
                temp_object_of_journal.issn = field['issn'][0][0]
                temp_object_of_journal.title = field['title'][0][0]
                temp_object_of_journal.h_index = field['h_index'][0]
                temp_object_of_journal.open_access= field['is_oa'][0]
                temp_object_of_journal.country = Country.objects.get(name_mal = field['country_code'][0])
                temp_object_of_journal.levels =  Levels.objects.get(number=field['level'][0]) 
                temp_object_of_journal.save()
            except:
                print(f'{field['issn'][0][0]}  не найден')
                continue
        pass

    def get_list_journals(self, req):

        """
            функция получения журнала 
        """

        def get_info_journals(data, fields):
            result = {}
            for field in fields:
                expr = parse(f'$..{field}')
                result[field] = [match.value for match in expr.find(data)]
            return result
        
        list_of_query = Journal.objects.all()
        # поля которые нужны из openalex  индекс хирша, страна, количество цитирований, доступ, состоит ли в скопус
        fields_for_openalex = ['h_index', 'country_code', 'is_oa', 'is_indexed_in_scopus']
        # поля из белого списка название, уровень, иссн
        fields_for_whitelist = ['title', 'level','issn']

    
        result_for_page = []
        for journal in list_of_query:
            issn = journal.issn

            try:
                response_openalex = requests.get(f'https://api.openalex.org/sources/issn:{issn}')
                response_openalex.raise_for_status()
                data_openalex = response_openalex.json()
            except requests.RequestException as e:
                print(f'[OpenAlex] Ошибка для ISSN {issn}: {e}')

            try:
                response_whitelist = requests.get(f'https://journalrank.rcsi.science/api/record-sources/{issn}/level')
                response_whitelist.raise_for_status()
                data_whitelist = response_whitelist.json()
            except requests.RequestException as e:
                print(f'[Whitelist] Ошибка для ISSN {issn}: {e}')
            temp_value = get_info_journals(data_openalex, fields_for_openalex)
            temp_value.update(get_info_journals(data_whitelist, fields_for_whitelist))
            result_for_page.append(temp_value)

        self.check_in_database(req,result_for_page)

        return result_for_page
    
    def get(self, req):
        if req.user.is_superuser:
            self.get_list_journals(req)
            return redirect('user-lc')
        return HttpResponse('Вы не администратор')


class LogoutView(View):
    def get(self, req):
        logout(req)
        return redirect('index')

class AuthView(View):
    """
        Класс с авторизацией пользователя
    """
    template_name='auth/login.html'
    def get(self, req):
        if req.user.is_authenticated:
            return redirect('user-lc')
        form = LoginForm()
        context = { 
            'form' : form
        }
        return render(req, self.template_name, context)
    
    def post(self, req):
        if req.user.is_authenticated:
            return redirect('user-lc')
        form = LoginForm(req, data=req.POST)  # ← Важно передавать request
        if form.is_valid():
            login(req, form.get_user())
            return redirect('user-lc')
        return redirect('login')
    
class RegisterView(View):
    """
        Класс с регистрацией пользователя 
    """
    template_name='auth/reg.html'
    def get(self, req):
        form = SignUpForm()
        context = {
            'form' : form,
        }
        return render(req, self.template_name, context)

class UserMain(View):

    """
        Всё для пользователя
    """

    template_name = 'user.html'

    def get(self, req):
        if req.user.is_authenticated:
            return render(req, self.template_name, {})

        return redirect('index')
    