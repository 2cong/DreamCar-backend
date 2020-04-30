import json
import uuid

from django.http                import HttpResponse, JsonResponse
from django.views               import View
from django.db                  import transaction

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

        return JsonResponse({'data':default_list},status=200)

class SeatView(View):
    def get(self,request,mvl_id):
        seat_info        = Seat.objects.select_related('seat_type','seat_type__color').filter(model_version_line_id=mvl_id)

        seat_color_list  = [
        {
            'color_id'       : color_info.seat_type.color.id,
            'color'          : color_info.seat_type.color.name,
            'thumnbnail_url' : color_info.seat_type.thumbnail_url
        } for color_info in seat_info]

        return JsonResponse({'data':seat_color_list}, status=200)

class DashboardView(View):
    def get(self,request,mvl_id):

        dashboard_list=[
            { "seat_id"              : dashboard.seat.id,
              "dashboard_id"         : dashboard.id,
              "dashboard_color_id"   : dashboard.dashboard_type.color.id,
              "dashboard_color_name" : dashboard.dashboard_type.color.name,
              "dashboard_thumbnail"  : dashboard.dashboard_type.thumbnail_url
             } for dashboard in Dashboard.objects.select_related('dashboard_type').filter(seat__model_version_line_id=mvl_id)]

        return JsonResponse({'data':dashboard_list},status=200)

class CarpetView(View):
    def get(self,request,mvl_id):

        carpet_list = [
            { "seat_id"           : carpet.dashboard.seat.id,
              "dashboard_id"      : carpet.dashboard.id,
              "carpet_id"         : carpet.id,
              "carpet_color_id"   : carpet.carpet_type.color.id,
              "carpet_color_name" : carpet.carpet_type.color.name,
              "carpet_thumbnail"  : carpet.carpet_type.thumbnail_url
             } for carpet in Carpet.objects.select_related('carpet_type','dashboard','carpet_type__color').filter(dashboard__seat__model_version_line_id=mvl_id)]

        return JsonResponse({'data':carpet_list},status=200)

class SteeringView(View):
    def get(self,request,mvl_id):

        steering_list = [
            { "seat_id"             : steering.dashboard.seat.id,
              "dashboard_id"        : steering.dashboard.id,
              "steering_id"         : steering.id,
              "steering_color_id"   : steering.steering_type.color.id,
              "steering_color_name" : steering.steering_type.color.name,
              "steering_thumbnail"  : steering.steering_type.thumbnail_url
             } for steering in Steering.objects.select_related('steering_type','dashboard','steering_type__color').filter(dashboard__seat__model_version_line_id=mvl_id)]

        return JsonResponse({'data':steering_list},status=200)

class PackageView(View):
    def get(self,request,mvl_id):
        mvl_package=ModelVersionLinePackage.objects.select_related('package').filter(model_version_line_id=mvl_id)

        package_list=[
            { "package_id" : package.package.id,
              "name" : package.package.name,
              "description" : package.package.description,
              "description_list" : package.package.description_list
        }for package in mvl_package ]

        return JsonResponse({"data":package_list},status=200)

class CustomCarOptionView(View):
    @transaction.atomic
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
                exterior_group       = ExteriorGroup.objects.get(exterior_id=exterior,wheel_id=wheel,caliper_id=caliper),
                interior_group       = InteriorGroup.objects.get(seat_id=seat,dashboard_id=dashboard,carpet_id=carpet,steering_id=steering)
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

class ContachChannelView(View):
    def get(self,request):

        contact_list = [
            {"id":1, "name":"mail"},
            {"id":2, "name":"call"},
            {"id":3, "name":"sns"},
        ]

        return JsonResponse({"data":contact_list},status=200)

class CustomCarView(View):
    @transaction.atomic
    def post(self,request):
        data = json.loads(request.body)
        contact_channel = data['contact_channel']
        try:
            for contact in contact_channel :
                ContactChannel.objects.create(
                    mail = contact['mail'],
                    call = contact['call'],
                    sns = contact['sns'],
                    sms = contact['sms'],
                    fax = contact['fax'],
                    email = contact['email']
            )

            code_id = str(CustomCar.objects.count())[-1]
            CustomCar.objects.create(
                email = data['name'],
                name = data['name'],
                code = (str(uuid.uuid4())[0:5]+str(uuid.uuid4)[1:3]+code_id).upper(),
                contact_channel = ContactChannel.objects.last(),
                privacy_check = data['privacy_check'],
                custom_car_option = CustomCarOption.objects.last()
            )
        except KeyError:
            return HttpResponse(statu=400)

        return JsonResponse({"code":CustomCar.objects.last().code},status=200)

class LoadView(View):
    def get(self,request):
        data = json.loads(request.body)
        code = data['code']

        try :
            if CustomCar.objects.filter(code=code).exists():
                summary = CustomCar.objects.select_related('custom_car_option','custom_car_option__exterior_grop','custom_car_option__interior_group','custom_car_option__model_version_line').get(code=code)

                summary_list = [
                    { "mvl_id" : summary.custom_car_option.model_version_line.id,
                      "interior" : summary.interior_group_option.interior_group.id,
                      "exterior" : summary.exterior_group.option.interior
                     }
                ]
                return JsonResponse({"data":summary_list},status=200)

            else:
                return JsonResponse({"message":"INVALID_CODE"}, status = 401)
        except KeyError:
            return HttpResponse(status = 400)
