from django.views.generic.base import ContextMixin
from core.models import Levels,Language, OpenAccess, Country


class JournalSearchMixin(ContextMixin):
    """
    Получение данных для шаблона
        -  levels
        -  langs
        -  country
        -  access
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'levels':  Levels.objects.all(),
            'langs':   Language.objects.all(),
            'country': Country.objects.all(),
        })
        return context
    