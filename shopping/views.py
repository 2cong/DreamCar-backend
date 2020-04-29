import json

from django.http        import HttpResponse,JsonResponse
from django.views       import View

from .models            import *
from car.models         import *

class UserView(View):
    def post(self, request):
        data = Json.load(request.body)

        last_name    = data['last_name']
        family_name  = data['family_name']
        birthdat     = data['birthday']
        phone_number = data['phone_number']
        address1     = data['address1']
        address2     = data['address2']

        
