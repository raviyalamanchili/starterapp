from ninja import NinjaAPI, Schema
from typing import List, Optional
from .models import Member, Region
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection

from django_multitenant.utils import set_current_tenant, unset_current_tenant

api = NinjaAPI(title="Tenant API", urls_namespace="tenant_api")
    
class RegionUpdateSchema(Schema):
    name: str
    region_id: int

class RegionResponseSchema(Schema):
    id: int
    name: str

class MemberUpdateSchema(Schema):
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None
    region_id: int

class MemberResponseSchema(Schema):
    id: int
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None
    created_at: datetime

class ErrorSchema(Schema):
    detail: str

@api.exception_handler(ObjectDoesNotExist)
def object_does_not_exist_handler(request, exc):
    return api.create_response(
        request,
        {"detail": "Object not found."},
        status=404
    )

@api.get("/region", response=List[RegionResponseSchema])
def list_regions(request):
    # The current tenant schema is already set by django-tenants middleware
    return Region.objects.all()

@api.post("/region", response=RegionResponseSchema)
def create_region(request, payload: RegionUpdateSchema):
    # The current tenant schema is already set by django-tenants middleware
    region = Region.objects.create(
        name=payload.name,
        id=payload.region_id
    )
    return region

@api.get("{region_id}/members", response=List[MemberResponseSchema])
def list_members_region(request, region_id: int):
    # Set the tenant schema based on the region_id
    region = Member.objects.get(region_id=region_id)
    set_current_tenant(region)
    return Member.objects.all()

@api.get("/members", response=List[MemberResponseSchema])
def list_members(request):
    # The current tenant schema is already set by django-tenants middleware
    return Member.objects.all()

@api.post("/members", response=MemberResponseSchema)
def create_member(request, payload: MemberUpdateSchema):
    # The current tenant schema is already set by django-tenants middleware
    member = Member.objects.create(
        name=payload.name,
        phone=payload.phone,
        email=payload.email,
        region_id=payload.region_id
    )
    return member

@api.get("{region_id}/members/{member_id}", response=MemberResponseSchema)
def get_member(request, region_id:int, member_id: int):
    region = Member.objects.get(region_id=region_id)
    set_current_tenant(region)
    member = Member.objects.get(id=member_id)
    return member

@api.put("{region_id}/members/{member_id}", response=MemberResponseSchema)
def update_member(request, region_id:int, member_id: int, payload: MemberUpdateSchema):
    region = Member.objects.get(region_id=region_id)
    set_current_tenant(region)
    member = Member.objects.get(id=member_id)
    member.name = payload.name
    if payload.phone is not None:
        member.phone = payload.phone
    if payload.email is not None:
        member.email = payload.email
    member.save()
    return member

@api.delete("{region_id}/members/{member_id}", response={200: None})
def delete_member(request, region_id:int, member_id: int):
    region = Member.objects.get(region_id=region_id)
    set_current_tenant(region) 
    member = Member.objects.get(id=member_id)
    member.delete()
    return 200