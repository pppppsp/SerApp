from django.db import models
# from spiders.scrap import JournalSpider


class Levels(models.Model):

    """
    Уровень научных журналов
    """

    number = models.IntegerField("Уровень журнала")

    def __str__(self):
        return f'{self.number}'
    
    class Meta:
        verbose_name='Уровни журнала'
        verbose_name_plural='Уровни журнала'


class Language(models.Model):

    """
        Хранит в себе список языков
    """

    name = models.CharField('Название языка', max_length=155)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name='Язык журнала'
        verbose_name_plural='Язык журнала'

class OpenAccess(models.Model):

    """
        Открытый доступ либо закрытый или - частично открытый
    """

    name=models.CharField('название', max_length=155)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name='Открытый доступ'
        verbose_name_plural='Открытый доступ'


class Country(models.Model):
    """
        модель стран
    """
    name = models.CharField('Название страны', max_length=255)
    name_mal = models.CharField('Краткая расшифровка', max_length=155)

    def __str__(self):
        return f'{self.name} {self.name_mal}'

    class Meta:
        verbose_name='Страна'
        verbose_name_plural='Страны'


class Journal(models.Model):

    """
        Модель с научными журналами.
    """
    title = models.CharField('Название научного журнала', max_length=250, null=True, blank=True)
    issn=models.CharField("Номер научного журнала", max_length=255)
    levels = models.ForeignKey('Levels', on_delete=models.CASCADE, verbose_name='Уровень научного журнала', null=True, blank=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='Язык', null=True, blank=True)
    subjects = models.JSONField('Тематики', default=list, null=True, blank=True)
    h_index = models.FloatField('Индекс Хирша', null=True, blank=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name='Страна', null=True, blank=True)
    # open_access = models.ForeignKey('OpenAccess', on_delete=models.CASCADE, verbose_name='Доступ')
    open_access = models.BooleanField('Тип доступа', default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # еще будут поля может быть 

    def __str__(self):
        return f"issn:{self.issn} country:{self.country}"

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'

# Create your models here.
