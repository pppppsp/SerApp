from django.urls import path
from user.views import UserMain, RegisterView, AuthView, LogoutView, UpdateDataBaseView
urlpatterns = [
     path('home/', UserMain.as_view(), name='user-lc'),
     path('register/', RegisterView.as_view(), name='reg'),
     path('login/', AuthView.as_view(), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),

     path('updatedb/', UpdateDataBaseView.as_view(), name='update_db'),
]
