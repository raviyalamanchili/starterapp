# Django Multi-Tenant Application

A minimal Django application with django-tenants support and Django Ninja API.

## Prerequisites

- Docker
- Python 3.10+

## Quick Start

```bash
# Clone and navigate to the repository
git clone <repository-url>
cd starterapp

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start PostgreSQL with Docker
docker compose up -d

# Apply migrations
python manage.py migrate_schemas --shared

# Create a public tenant
python manage.py create_tenant --schema_name=public --name="Public Tenant" --domain-domain=localhost --domain-is_primary=True

# Create a tenant
python manage.py create_tenant --schema_name=tenant1 --name="Tenant 1" --domain-domain=tenant1 --domain-is_primary=True

# Create a superuser for the public schema
python manage.py createsuperuser

# Create a superuser for the tenant1 schema
python manage.py create_tenant_superuser --schema=tenant1

# Run the development server
python manage.py runserver
```

## Admin Endpoints

- `http://localhost:8000/admin/` - Django Admin for public schema
- `http://localhost:8000/client/tenant1/admin/` - Django Admin for tenant1 schema

## API Endpoints

### Shared API (Public Schema)
- `GET /api/clients` - List all tenants
- `GET /api/domains` - List all domains

### Tenant API (Tenant-specific)
- `GET /client/{domain}/api/tenant/items` - List items
- `POST /client/{domain}/api/tenant/items` - Create item
- `GET /client/{domain}/api/tenant/items/{id}` - Get item detail
- `PUT /client/{domain}/api/tenant/items/{id}` - Update item
- `DELETE /client/{domain}/api/tenant/items/{id}` - Delete item

## Structure

- `shared_app` - Contains shared models in the public schema (Client, Domain) accessible from all tenants
- `tenant_app` - Contains tenant-specific models (Member, Provider) and logic for each tenant schema
- Django Ninja APIs in both apps

## Notes

- Access tenant app endpoints via tenant subfolder: `http://localhost:8000/client/tenant1/api/tenant/items`
- Access shared app endpoints via base url: `http://localhost:8000/api/clients`
- Tenant schemas are automatically created and migrated (auto_create_schema = True)