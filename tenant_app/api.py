from ninja import NinjaAPI, Schema
from typing import List, Optional
from .models import TenantItem

api = NinjaAPI(title="Tenant API", urls_namespace="tenant_api")

class TenantItemSchema(Schema):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None

class TenantItemResponseSchema(TenantItemSchema):
    id: int
    created_at: str

@api.get("/items", response=List[TenantItemResponseSchema])
def list_items(request):
    return TenantItem.objects.all()

@api.post("/items", response=TenantItemResponseSchema)
def create_item(request, payload: TenantItemSchema):
    item = TenantItem.objects.create(
        name=payload.name,
        description=payload.description or ""
    )
    return item

@api.get("/items/{item_id}", response=TenantItemResponseSchema)
def get_item(request, item_id: int):
    return TenantItem.objects.get(id=item_id)

@api.put("/items/{item_id}", response=TenantItemResponseSchema)
def update_item(request, item_id: int, payload: TenantItemSchema):
    item = TenantItem.objects.get(id=item_id)
    item.name = payload.name
    if payload.description is not None:
        item.description = payload.description
    item.save()
    return item

@api.delete("/items/{item_id}")
def delete_item(request, item_id: int):
    item = TenantItem.objects.get(id=item_id)
    item.delete()
    return {"success": True}