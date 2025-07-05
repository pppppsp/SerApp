from django.db import models
from django.contrib.auth.models import AbstractUser

class RoleModel(models.Model):
    name = models.CharField('Название роли', max_length=10)

    def __str__(self):
        return f'{self.name}'

class User(AbstractUser):
    patronymic = models.CharField("Отчество", max_length=100, null=True)
    role = models.ForeignKey(RoleModel, on_delete=models.CASCADE, null=True, verbose_name="Роль")
    date_of_birth = models.DateField("Дата рождения", null=True, blank=True)
    phone_number = models.CharField("Номер телефона", max_length=15, blank=True, null=True)
    email = models.EmailField("Почта",unique=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'
# Create your models here.
