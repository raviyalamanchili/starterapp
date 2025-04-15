from django.db import models

from django_multitenant.models import TenantModel
from django_multitenant.fields import TenantForeignKey
from django_multitenant.mixins import *


class Region(TenantModel):
    tenant_id = 'id'
    name = models.CharField(max_length=100)


class Member(TenantModel):
    tenant_id = 'region_id'
    name = models.CharField(max_length=100)
    email = models.TextField(blank=True)
    phone = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    region = TenantForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['id', 'region']
