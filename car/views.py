import json
import uuid

from django.http             import HttpResponse, JsonResponse
from django.views            import View
from django.core.exceptions  import ObjectDoesNotExist
from django.db               import transaction

from .models                 import *

def image_format(image_name, params):
    formats = {
         'exterior'  : { 'mvl' : params['mvl'], 'caliper_code' : params['caliper_code'], 'wheel_code' : params['wheel_code'], 'exterior_code' : params['exterior_code']},
         'interior1' : { 'mvl' : params['mvl'], 'carpet_code' : params['carpet_code'], 'dashboard_code2' : params['dashboard_code2'], 'dashboard_code1' : params['dashboard_code1'], 'steering_code' : params['steering_code'], 'seat_code2' : params['seat_code2'], 'seat_code1' : params['seat_code1']},
         'interior2' : { 'mvl' : params['mvl'], 'seat_code2' : params['seat_code2'], 'seat_code1' : params['seat_code1'], 'dashboard_code1' : params['dashboard_code1'], 'dashboard_code2' : params['dashboard_code2'], 'steering_code' : params['steering_code']},
         'interior3' : { 'mvl' : params['mvl'], 'carpet_code' : params['carpet_code'], 'seat_code2' : params['seat_code2'], 'seat_code1' : params['seat_code1'], 'dashboard_code1' : params['dashboard_code1'], 'dashboard_code2' : params['dashboard_code2']},
         'interior4' : { 'mvl' : params['mvl'], 'carpet_code' : params['carpet_code'], 'seat_code2' : params['seat_code2'], 'seat_code1' : params['seat_code1'], 'dashboard_code1' : params['dashboard_code1'], 'dashboard_code2' : params['dashboard_code2'], 'steering_code' : params['steering_code'], 'exterior_code' : params['exterior_code']}
        }

    return formats.get(image_name, "Invalid_name")

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

class MainView(View):
    def get(self, request):
        try:
            mvl       = ModelVersionLine.objects.get(id = request.GET.get('mvl')).code
            exterior  = ExteriorGroup.objects.select_related('exterior', 'wheel', 'caliper').get(exterior = request.GET.get('exterior'), wheel = request.GET.get('wheel'), caliper = request.GET.get('caliper'))
            interior  = InteriorGroup.objects.select_related('seat', 'dashboard', 'carpet', 'steering').get(seat = request.GET.get('seat'), dashboard = request.GET.get('dashboard'), carpet = request.GET.get('carpet'), steering = request.GET.get('steering'))

            one_dict = {}
            one_dict['mvl'] = mvl; one_dict['caliper_code'] = exterior.caliper.code; one_dict['wheel_code'] = exterior.wheel.code; one_dict['exterior_code'] = exterior.exterior.code;
            one_dict['carpet_code'] = interior.carpet.code; one_dict['dashboard_code1'] = interior.dashboard.code1; one_dict['dashboard_code2'] = interior.dashboard.code2;
            one_dict['steering_code'] = interior.steering.code; one_dict['seat_code1'] = interior.seat.code1; one_dict['seat_code2'] = interior.seat.code2

            image_url = lambda img_name: ImageUrl.objects.get(name = img_name).image_url

            exterior_url = [
             {   'Exterior1'  : image_url("main_exterior1").format(**image_format('exterior', one_dict)),
                 'Exterior2'  : image_url("main_exterior2").format(**image_format('exterior', one_dict)),
                 'Exterior3'  : image_url("main_exterior3").format(**image_format('exterior',one_dict)),
                 'Exterior4'  : image_url("main_exterior4").format(**image_format('exterior',one_dict)),
                 'Interior1'  : image_url("main_interior1").format(**image_format('interior1',one_dict)),
                 'Interior2'  : image_url("main_interior2").format(**image_format('interior2',one_dict)),
                 'Interior3'  : image_url("main_interior3").format(**image_format('interior3',one_dict)),
                 'Interior4'  : image_url("main_interior4").format(**image_format('interior4',one_dict)),
                 'preview'    : image_url("main_preview_url").format(**image_format('exterior',one_dict))
              }
          ]
            return JsonResponse({'rendering_url': exterior_url}, status = 200)

        except KeyErrorr:
            return HttpResponse(status = 400)
        except ObjectDoesNotExist:
            return HttpResponse(status = 400)

class SummaryView(View):
    def get(self, request):
        try:
            mvl       = ModelVersionLine.objects.get(id = request.GET.get('mvl')).code
            exterior  = ExteriorGroup.objects.select_related('exterior', 'wheel', 'caliper').get(exterior = request.GET.get('exterior'), wheel = request.GET.get('wheel'), caliper = request.GET.get('caliper'))
            interior  = InteriorGroup.objects.select_related('seat', 'dashboard', 'carpet', 'steering').get(seat = request.GET.get('seat'), dashboard = request.GET.get('dashboard'), carpet = request.GET.get('carpet'), steering = request.GET.get('steering'))
            spec      = Spec.objects.prefetch_related('modelversionline_set').filter(modelversionline__id = request.GET.get('mvl')).values().first()
            dimension = Dimension.objects.prefetch_related('modelversionline_set').filter(modelversionline__id = request.GET.get('mvl')).values().first()

            image_url = lambda img_name: ImageUrl.objects.get(name = img_name).image_url

            one_dict = {}
            one_dict['mvl'] = mvl; one_dict['caliper_code'] = exterior.caliper.code; one_dict['wheel_code'] = exterior.wheel.code; one_dict['exterior_code'] = exterior.exterior.code;
            one_dict['carpet_code'] = interior.carpet.code; one_dict['dashboard_code1'] = interior.dashboard.code1; one_dict['dashboard_code2'] = interior.dashboard.code2;
            one_dict['steering_code'] = interior.steering.code; one_dict['seat_code1'] = interior.seat.code1; one_dict['seat_code2'] = interior.seat.code2

            summary_list = [
                             {
                'Exterior1' : image_url("summary_exterior1").format(**image_format('exterior', one_dict)),
                'Exterior2' : image_url("summary_exterior2").format(**image_format('exterior', one_dict)),
                'Interior1' : image_url("summary_interior1").format(**image_format('interior2', one_dict)),
                'preview'   : image_url("summary_perview").format(**image_format('exterior', one_dict)),
                'spec' : spec,
                'dimension' : dimension
              }
             ]

            return JsonResponse({'summary' : summary_list}, status = 200)

        except KeyError:
            return HttpResponse(status = 400)

        except ObjectDoesNotExist:
            return HttpResponse(status = 400)

class ExteriorView(View):
     def get(self, request, mvl_id):
         exteriors      = ColorType.objects.prefetch_related('exteriortype_set')

         exterior_list = [
             {
               color_type.name : [
               {
                'exterior_id'   : thumb['exterior__id'],
                'exterior_code' : thumb['exterior__code'],
                'thumbnail_url' : thumb['thumbnail_url']
               } for thumb in color_type.exteriortype_set.filter(exterior__model_version_line = mvl_id).values('exterior__id', 'exterior__code', 'thumbnail_url')
             ]
           }for color_type in exteriors
          ]

         return JsonResponse({'exterior_thumbnail' : exterior_list}, status = 200)

class WheelView(View):
     def get(self, request, mvl_id):
        wheel    = Wheel.objects.select_related('wheel_type').filter(model_version_line = mvl_id)

        wheel_list = [
             {
                 'wheel_id'      : thumb.id,
                 'wheel_type'    : thumb.wheel_type.name,
                 'thumbnail_url' : thumb.wheel_type.thumbnail_url
             } for thumb in wheel
        ]

        return JsonResponse({'wheel thumbnail' : wheel_list}, status = 200)

class CaliperView(View):
     def get(self, request, mvl_id):
         caliper  = Caliper.objects.select_related('caliper_type__color').filter(model_version_line = mvl_id)

         caliper_list = [
               {
                   'caliper_id'    : thumb.id,
                   'caliper_color' : thumb.caliper_type.color.name,
                   'thumbnail_url' : thumb.caliper_type.thumbnail_url
               } for thumb in caliper
         ]

         return JsonResponse({'caliper thumbnail' : caliper_list}, status = 200)

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

class AccessoryView(View):
    def get(self, request):

        category   = AccessoryCategory.objects.prefetch_related('accessory_set')

        accessory_list = [
            {
               acc.category : list(acc.accessory_set.values('id', 'name', 'thumbnail_url'))
            } for acc in category
        ]

        return JsonResponse({'accessory' : accessory_list}, status = 200)

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

class ContactChannelView(View):
    def get(self,request):

        contact_list = [
            {"id" : 1,  "name" : "mail"},
            {"id" : 2,  "name" : "call"},
            {"id" : 3,  "name" : "sns"},
            {"id" : 4,  "name" : "sms"},
            {"id" : 5,  "name" : "fax"},
            {"id" : 6,  "name" : "email"}
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
        code = request.GET.get('code')

        try :
            if CustomCar.objects.filter(code=code).exists():
                summary = CustomCar.objects.select_related('custom_car_option','custom_car_option__exterior_group','custom_car_option__interior_group','custom_car_option__model_version_line').get(code=code)

                mvl       = summary.custom_car_option.model_version_line
                exterior  = summary.custom_car_option.exterior_group
                interior  = summary.custom_car_option.interior_group
                spec      = Spec.objects.prefetch_related('modelversionline_set').filter(modelversionline__id = mvl.id).values().first()
                dimension = Dimension.objects.prefetch_related('modelversionline_set').filter(modelversionline__id = mvl.id).values().first()

                exterior1 = ImageUrl.objects.get(id = 10).image_url
                exterior2 = ImageUrl.objects.get(id = 11).image_url
                interior1 = ImageUrl.objects.get(id = 12).image_url
                preview   = ImageUrl.objects.get(id = 13).image_url

                summary_list = [
                                 {
                     "Exterior1"  : exterior1.format(
                                                     mvl            = mvl.code,
                                                     caliper_code   = exterior.caliper.code,
                                                     wheel_code     = exterior.wheel.code,
                                                     exterior_code  = exterior.exterior.code
                                                     ),

                     "Exterior2"  : exterior2.format(
                                                     mvl           = mvl.code,
                                                     caliper_code  = exterior.caliper.code,
                                                     wheel_code    = exterior.wheel.code,
                                                     exterior_code = exterior.exterior.code
                                                     ),

                     "interior1"  : interior1.format(
                                                     mvl             = mvl.code,
                                                     seat_code2      = interior.seat.code2,
                                                     seat_code1      = interior.seat.code1,
                                                     dashboard_code1 = interior.dashboard.code1,
                                                     dashboard_code2 = interior.dashboard.code2,
                                                     steering_code   = interior.steering.code
                                                     ),
                     "preview_url": preview.format(
                                                     mvl            = mvl.code,
                                                     caliper_code   = exterior.caliper.code,
                                                     wheel_code     = exterior.wheel.code,
                                                     exterior_code  = exterior.exterior.code
                                                     ),
                    "model_version_line" : mvl.id,

                    "exterior"    : {
                          "exterior" : exterior.exterior.exterior_type.color.name,
                          "wheel"    : exterior.wheel.wheel_type.name,
                          "caliper"  : exterior.caliper.caliper_type.color.name
                          },

                    "interior" : {
                          "seat"      : interior.seat.seat_type.color.name,
                          "dashboard" : interior.dashboard.dashboard_type.color.name,
                          "carpet"    : interior.carpet.carpet_type.color.name,
                          "steering"  : interior.steering.steering_type.color.name
                           },

                    "spec" : spec,
                    "dimension" : dimension
                          }
                 ]
                return JsonResponse({"summary" : summary_list}, status = 200)

            else:
                return JsonResponse({"message":"INVALID_CODE"}, status = 401)
        except KeyError:
            return HttpResponse(status = 400)
