import json

from django.http                import HttpResponse, JsonResponse
from django.views               import View
from django.core.exceptions     import ObjectDoesNotExist

from .models                    import *

class DefaultView(View):
    def get(self,request,mvl_id):

        default_info = Default.objects.select_related('exterior_type','wheel_type','caliper_type','seat_type','dashboard_type','carpet_type','steering_type').filter(model_version_line_id=mvl_id)
        default_list = [
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

        seat_info        = Seat.objects.select_related('seat_type').filter(model_version_line_id=mvl_id)
        seat_color_list  = [
        {
            'color_id'       : color_info.seat_type.color.id,
            'color'          : color_info.seat_type.color.name,
            'thumnbnail_url' : color_info.seat_type.thumbnail_url
        } for color_info in seat_info]

        return JsonResponse({'message':seat_color_list}, status=200)

class DashboardView(View):
    def get(self,request,mvl_id):

        possible_seat   = Seat.objects.prefetch_related('dashboard_set').filter(model_version_line_id=mvl_id)
        dashboard_list  = [
         { f"seat_id = {seat.id}" : list(seat.dashboard_set.values('id','dashboard_type__color','dashboard_type__color__name','dashboard_type__thumbnail_url'))} for seat in possible_seat
         ]

        return JsonResponse({'messsage':dashboard_list},status=200)

class CarpetView(View):
    def get(self,request,mvl_id):

        possible_seat = Seat.objects.prefetch_related('dashboard_set').filter(model_version_line_id=mvl_id)
        carpet_list   = [
            {f"seat_id = {seat.id}" :
             {f"dashboard_id = {dashboard.id}" :
              list(dashboard.carpet_set.values('id','carpet_type__color','carpet_type__color__name','carpet_type__thumbnail_url'))for dashboard in Dashboard.objects.prefetch_related('carpet_set').filter(seat_id=seat.id)}} for seat in possible_seat
        ]

        return JsonResponse({'message':carpet_list},status=200)

class SteeringView(View):
    def get(self,request,mvl_id):

        possible_seat = Seat.objects.prefetch_related('dashboard_set').filter(model_version_line_id=mvl_id)
        steering_list =  [
            {f"seat_id = {seat.id}" :
         {f"dashboard_id = {dashboard.id}" :
          list(dashboard.steering_set.values('id','steering_type__color','steering_type__color__name','steering_type__thumbnail_url'))for dashboard in Dashboard.objects.prefetch_related('steering_set').filter(seat_id=seat.id)}}for seat in possible_seat
        ]

        return JsonResponse({'message':steering_list},status=200)

class PackageView(View):
    def get(self,request,mvl_id):

        mvl_package=ModelVersionLinePackage.objects.filter(model_version_line_id=mvl_id)

        package_list=[
            { "package_id" : package.package.id,
              "name" : package.package.name,
              "description" : package.package.description,
              "description_list" : package.package.description_list
        }for package in mvl_package ]

        return JsonResponse({"message":package_list},status=200)

class CustomCarOptionView(View):
    def post(self,request):

        data                = json.loads(request.body)

        model_version_line  = data['mvl']
        exterior            = data['exterior']
        wheel               = data['wheel']
        caliper             = data['caliper']
        seat                = data['seat']
        dashboard           = data['dashboard']
        carpet              = data['carpet']
        steering            = data['steering']
        package_list        = data.get('package',None)
        accessory_list      = data.get('accessory',None)

        CustomCarOption.objects.create(
                model_version_line   = ModelVersionLine.objects.get(id=model_version_line),
                exterior_group       = ExteriorGroup.objects.get(exterior_id=exterior,wheel_id=wheel,  caliper_id=caliper),
                interior_group       = InteriorGroup.objects.get(seat_id=seat,dashboard_id=dashboard,  carpet_id=carpet,steering_id=steering)
            )

        if package_list:
            for packages in package_list:
                PackageCustomCar.objects.create(
                    package           = Package.objects.get(id=packages),
                    custom_car_option = CustomCarOption.objects.last()
                )

        if accessory_list:
            for accessories in accessory_list:
                CustomCarAccessory.objects.create(
                    quantity          = accessories.get('quantity'),
                    accessory         = Accessory.objects.get(id=accessories.get('id')),
                   custom_car_option = CustomCarOption.objects.last()
                )

        return HttpResponse(status=200)
