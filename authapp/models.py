from django.db import models

from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.dispatch import Signal
#from precise_bbcode.fields import BBCodeTextField
from .utilities import send_activation_notification 


class AdvUser(AbstractUser):
    SEX_VISITOR = (
        ('m', 'Мужской'),
        ('w', 'Женский'),
    )
    sex = models.CharField(max_length=1, choices=SEX_VISITOR, blank=True, default='m', verbose_name = "Пол",
     help_text='Введите пол')
    birstday = models.DateField(auto_now_add = False, blank=True,null=True, db_index = False, verbose_name = "Дата рождения")
    address = models.CharField(max_length=200,  blank=True, verbose_name = "Место жительства")
    phone = models.CharField(max_length=16, blank=True, verbose_name = "Телефон")
    
    is_activated = models.BooleanField(default=True,db_index=True,verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True,verbose_name='Слать оповещения по электронной почте?')

    class Meta(AbstractUser.Meta):
        pass
#--------------------------------------------------------------------------------------------
user_registrated = Signal(providing_args=['instance'])

def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])

user_registrated.connect(user_registrated_dispatcher)
#--------------------------------------------------------------------------------------------from django.db import models

# Create your models here.
