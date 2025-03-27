# Django Multi-Tenant Application

A minimal Django application with django-tenants support and Django Ninja API.

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
python manage.py create_tenant --schema_name=tenant1 --name="Tenant 1" --domain-domain=tenant1.localhost --domain-is_primary=True

# Add domain to hosts file (requires admin/sudo privileges)
# On macOS/Linux: sudo nano /etc/hosts
# On Windows: edit C:\Windows\System32\drivers\etc\hosts as Administrator
# Add: 127.0.0.1 tenant1.localhost

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

## API Endpoints

### Shared API (Public Schema)
- `GET /api/shared/clients` - List all tenants
- `GET /api/shared/domains` - List all domains

### Tenant API (Tenant-specific)
- `GET /api/tenant/items` - List items
- `POST /api/tenant/items` - Create item
- `GET /api/tenant/items/{id}` - Get item detail
- `PUT /api/tenant/items/{id}` - Update item
- `DELETE /api/tenant/items/{id}` - Delete item

## Structure

- `shared_app` - Contains shared models (Client, Domain) accessible from all tenants
- `tenant_app` - Contains tenant-specific models and logic
- Django Ninja APIs in both apps

## Notes

- Access tenant endpoints via tenant domain: `http://example.localhost:8000/api/tenant/items`
- Access shared endpoints via any domain
- Tenant schemas are automatically created and migrated (auto_create_schema = True) 