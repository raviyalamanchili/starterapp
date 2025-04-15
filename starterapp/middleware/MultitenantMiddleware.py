from django_multitenant.utils import set_current_tenant, unset_current_tenant
from django.contrib.auth import logout


class MultitenantMiddleware:
  def __init__(self, get_response):
     self.get_response = get_response

  def __call__(self, request):
      if request.user and not request.user.is_anonymous:
         if not request.user.account and not request.user.is_superuser:
            print(
               "Logging out because user doesnt have account and not a superuser"
            )
            logout(request.user)

         #set_current_tenant(request.user.account)
         # print('Setting current tenant')

      response = self.get_response(request)

      unset_current_tenant()

      return response