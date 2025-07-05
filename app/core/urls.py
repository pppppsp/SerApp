from django.urls import path, include
from .views import MainView, SearchView


urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('user/', include('user.urls')),
]
