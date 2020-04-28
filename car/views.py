import json

from django.http        import HttpResponse, JsonResponse
from django.views       import View

from .models            import *

class DefaultView(View):
    def get(self,request,mvl_id):

        default_info=Default.objects.select_related('exterior_type','wheel_type','caliper_type','seat_type','dashboard_type','carpet_type','steering_type').filter(model_version_line_id=mvl_id)
        default_list=[
        {
            'exterior'   : {'color_id' : default.exterior_type.color.id,  'color' : default.exterior_type.color.name ,  'thumbnail_url' : default.exterior_type.thumbnail_url},
            'wheel'      : {'wheel_id' : default.wheel_type.id,           'name'  : default.wheel_type.name,            'thumbnail_url' : default.wheel_type.thumbnail_url},
            'caliper'    : {'color_id' : default.caliper_type.color.id,   'color' : default.caliper_type.color.name,    'thumbnail_url' : default.caliper_type.thumbnail_url},
            'seat'       : {'color_id' : default.seat_type.color.id,      'color' : default.seat_type.color.name,       'thumbnail_url' : default.seat_type.thumbnail_url},
            'dashboard'  : {'color_id' : default.dashboard_type.color.id, 'color' : default.dashboard_type.color.name,  'thumbnail_url' : default.dashboard_type.thumbnail_url},
            'carpet'     : {'color_id' : default.carpet_type.color.id,    'color' : default.carpet_type.color.name,     'thumbnail_url' : default.carpet_type.thumbnail_url},
            'steering'   : {'color_id' : default.steering_type.color.id,  'color' : default.steering_type.color.name,   'thumbnail_url' : default.steering_type.thumbnail_url}}
            for default  in default_info]

        return JsonResponse({'message':default_list},status=200)

class SeatView(View):
    def get(self,request,mvl_id):

        seat_info=Seat.objects.select_related('seat_type').filter(model_version_line_id=mvl_id)
        seat_color_list=[
        {
            'color_id'       : color_info.seat_type.color.id,
            'color'          : color_info.seat_type.color.name,
            'thumnbnail_url' : color_info.seat_type.thumbnail_url
        } for color_info in seat_info]

        return JsonResponse({'message':seat_color_list}, status=200)

    def post(self,request,mvl_id):
        data=json.loads(request.body)
        seat = data['seat']

class DashboardView(View):
    def get(self,request,mvl_id):

        possible_seat=Seat.objects.prefetch_related('dashboard_set').filter(model_version_line_id=mvl_id)
        for seat in possible_seat:
            seat.


