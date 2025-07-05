from django.shortcuts import render, redirect
from django.views import View
from core.models import *
from core.mixins import JournalSearchMixin
import requests
from jsonpath_ng import parse
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

class MainView(View):

    template_name = 'index.html'

    """
        Класс содержит функционал главной страницы
    """

    def get(self, req):
        """
            получение главной страницы
        """
        return render(req, self.template_name, {})
   
    
class SearchView(JournalSearchMixin, View):
    template_name = "SearchPage.html"

    """
        Класс содержит функционал поиска
    """

    def get(self, req):
        # журналы по умолчанию
        data = {
            'got_journals': Journal.objects.filter(~Q(title=None)),
        }
        context = self.get_context_data()
        context.update(data)
        return render(req, self.template_name, context)



    def post(self, req):
        """
        Функция получения данных из БД
        """
        print(req.POST)
        search_params = {
            'level': req.POST.get('level'),
            'lang': req.POST.get('lang'),
            'country': req.POST.get('country'),
            'open_access': int(req.POST.get('open_access')),
            'h_index': req.POST.get('h_index'), # индекс хирша
        }
    
        # Получаем все журналы, которые соответствуют критериям поиска
        query_journals = Journal.objects.all()
        print(f'h_index: {search_params['h_index']}')
        print(f' Этап 1{query_journals}')
        if search_params['level']: # Уровень
            query_journals = query_journals.filter(levels__number=search_params['level'])
        print(f' Этап 2{query_journals}')
        if search_params['country']:
            query_journals = query_journals.filter(country__name_mal=search_params['country'])
        print(f' Этап 3{query_journals}')
        if search_params['open_access']: # Доступ
            query_journals = query_journals.filter(open_access=True if search_params['open_access'] == 1 else False)
        print(f' Этап 4{query_journals}')
        if search_params['h_index']: # Индекс Хирша
            query_journals = query_journals.filter(h_index__range=(0, search_params['h_index']))
        print(f' Этап 5{query_journals}')

    
        journals_list = list(query_journals.values())
        
        got_data_with_journals = {
            'got_journals': journals_list,
        } 
        return JsonResponse(got_data_with_journals)





# 'https://api.openalex.org/sources/issn:{issn}'





    

# Create your views here.
