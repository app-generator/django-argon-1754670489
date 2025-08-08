# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Vehiculo(models.Model):

    #__Vehiculo_FIELDS__
    vehiculo = models.CharField(max_length=255, null=True, blank=True)
    tipo_vehiculo = models.CharField(max_length=255, null=True, blank=True)
    capacidad = models.IntegerField(null=True, blank=True)
    empresa = models.CharField(max_length=255, null=True, blank=True)
    placa = models.CharField(max_length=255, null=True, blank=True)

    #__Vehiculo_FIELDS__END

    class Meta:
        verbose_name        = _("Vehiculo")
        verbose_name_plural = _("Vehiculo")



#__MODELS__END
