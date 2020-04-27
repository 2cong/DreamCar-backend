import json

from django.http        import HttpResponse, JsonResponse
from django.views       import View

from .models            import

class ModelView(View):
    def post(self,request):
        data = json.loads(request.body)



class SeatView(View):
    def post(self,request):
        data = json.loads(request.body)




