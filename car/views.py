import json

from django.http             import HttpResponse, JsonResponse
from django.views            import View
from django.core.exceptions  import ObjectDoesNotExist

from .models                 import *

class MainView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
                
            model_version_line_id = data['mvl_id']
            exterior_id           = data['exterior']
            wheel_id	          = data['wheel']
            caliper_id            = data['caliper']
            seat_id	          = data['seat']
            dashboard_id          = data['dashboard']
            carpet_id             = data['carpet']
            steering_id           = data['steering']

            mvl       = ModelVersionLine.objects.get(id = model_version_line_id).code
            exterior  = ExteriorGroup.objects.select_related('exterior', 'wheel', 'caliper').get(exterior = exterior_id, wheel = wheel_id, caliper = caliper_id)
            interior  = InteriorGroup.objects.select_related('seat', 'dashboard', 'carpet', 'steering').get(seat = seat_id, dashboard = dashboard_id, carpet = carpet_id, steering = steering_id)
           

            exterior_url = [
             {
                'Exterior1'  : f'https://ph.cloud.maserati.com/{mvl}/1280/c720/gfx6?config=background;shadow;CRPT/CRPT/94084217;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;RUF/ROO1/94084295;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;CAL/{exterior.caliper.code};RIMS/{exterior.wheel.code};EXT/EXT/{exterior.exterior.code};MEC/Q5EM;glasses_front;MEC/Q400', 

                'Exterior2'  : f'https://ph.cloud.maserati.com/{mvl}/1280/c720/gfx7?config=background;shadow;CRPT/CRPT/94084217;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;RUF/ROO1/94084295;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/{exterior.caliper.code};RIMS/{exterior.wheel.code};EXT/EXT/{exterior.exterior.code};glasses_front;MEC/Q400;plates',

                'Exterior3'  : f'https://ph.cloud.maserati.com/{mvl}/1280/c720/gfx3?config=background;shadow;CRPT/CRPT/94084217;RUF/ROO1/94084295;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;CAL/{exterior.caliper.code};RIMS/{exterior.wheel.code};EXT/EXT/{exterior.exterior.code};MEC/Q5EM;glasses_front;MEC/Q400',

                'Exterior4'  : f'https://ph.cloud.maserati.com/{mvl}/1280/c720/gfx5?config=background;shadow;CRPT/CRPT/94084217;RUF/ROO1/94084295;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;CAL/{exterior.caliper.code};RIMS/{exterior.wheel.code};EXT/EXT/{exterior.exterior.code};MEC/Q5EM;glasses_front;MEC/Q400',

                'interior1'  : f'https://ph.cloud.maserati.com/{mvl}/1280/c720/gfx9?config=background;shadow;glasses_front;MEC/Q400;CRPT/CRPT/94084217;BOE/Q728/CRPT/{interior.carpet.code};RUF/ROO1/94084295;INT/INT/94084213;DUMMYOPTS/DOARM/{interior.dashboard.code2};DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/{interior.dashboard.code1};STEERINGWHEEL/STL1/{interior.steering.code};BOE/Q5ZK;BOE/{interior.seat.code2}/INT/{interior.seat.code1};BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/94084201',

                'interior2'  : f'https://ph.cloud.maserati.com/{mvl}/1280/c720/gfx10?config=background;shadow;glasses_front;MEC/Q400;CRPT/CRPT/94084217;RUF/ROO1/94084297;INT/INT/94084213;BOE/{interior.seat.code2}/INT/{interior.seat.code1};DUMMYOPTS/DOARM/{interior.dashboard.code1};DUMMYOPTS/DOPUH/{interior.dashboard.code2};TRIM/Q4MN;DSH/DSHG/{interior.dashboard.code2};STEERINGWHEEL/STL1/{interior.steering.code};BOE/Q5ZK;BOE/Q4B2;BOE/Q212;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/94084201',

                'interior3'  : f'https://ph.cloud.maserati.com/{mvl}/1280/c720/gfx11?config=background;shadow;glasses_front;MEC/Q400;CRPT/CRPT/{interior.carpet.code};RUF/ROO1/94084295;INT/INT/94084349;DUMMYOPTS/DOARM/{interior.dashboard.code2};DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/{interior.dashboard.code1};STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/{interior.seat.code2}/INT/{interior.seat.code1};BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/9408420',
    
                'interior4'  : f'https://ph.cloud.maserati.com/{mvl}/1280/c720/gfx12?config=background;shadow;CRPT/CRPT/{interior.carpet.code};RUF/ROO1/94084296;INT/INT/94084213;BOE/{interior.seat.code2}/INT/{interior.seat.code1};DUMMYOPTS/DOARM/{interior.dashboard.code2};DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/{interior.dashboard.code1};STEERINGWHEEL/STL1/{interior.steering.code};BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/{exterior.exterior.code};glasses_front;MEC/Q400',

                'preview_url': f'https://ph.cloud.maserati.com/{mvl}/400/c225/gfx6?config=background;shadow;CRPT/CRPT/94084217;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;RUF/ROO1/94084295;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;CAL/{exterior.caliper.code};RIMS/{exterior.wheel.code};EXT/EXT/{exterior.exterior.code};MEC/Q5EM;glasses_front;MEC/Q400'
              }
          ]
            return JsonResponse({'rendering_url': exterior_url}, status = 200)

        except KeyError:
            return HttpResponse(status = 400)
        except ObjectDoesNotExist:
            return HttpResponse(status = 400)

class SummaryView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            model_version_line_id = data['mvl_id']
            exterior_id           = data['exterior']
            wheel_id              = data['wheel']
            caliper_id            = data['caliper']
            seat_id               = data['seat']
            dashboard_id          = data['dashboard']
            carpet_id             = data['carpet']
            steering_id           = data['steering']

            mvl       = ModelVersionLine.objects.get(id = model_version_line_id)
            exterior  = ExteriorGroup.objects.select_related('exterior', 'wheel', 'caliper').get(exterior = exterior_id, wheel = wheel_id, caliper = caliper_id)
            interior  = InteriorGroup.objects.select_related('seat', 'dashboard', 'carpet', 'steering').get(seat = seat_id, dashboard = dashboard_id, carpet = carpet_id, steering = steering_id)
            spec      = list(Spec.objects.prefetch_related('ModelVersionLine_set').filter(modelversionline__id = model_version_line_id).values())[0]
            dimension = list(Dimension.objects.prefetch_related('ModelVersionLine_set').filter(modelversionline__id = model_version_line_id).values())[0]

            summary_list = [
                             {
                'Exterior1'  : f'https://ph.cloud.maserati.com/{mvl.code}/1280/c720/gfx6?config=background;shadow;CRPT/CRPT/94084217;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;RUF/ROO1/94084295;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;CAL/{exterior.caliper.code};RIMS/{exterior.wheel.code};EXT/EXT/{exterior.exterior.code};MEC/Q5EM;glasses_front;MEC/Q400',

                'Exterior2'  : f'https://ph.cloud.maserati.com/{mvl.code}/533/c300/gfx7?config=background;shadow;CRPT/CRPT/94084217;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;RUF/ROO1/94084295;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/{exterior.caliper.code};RIMS/{exterior.wheel.code};EXT/EXT/{exterior.exterior.code};glasses_front;MEC/Q400;plates',

                'interior1'  : f'https://ph.cloud.maserati.com/{mvl.code}/533/c300/gfx10?config=background;shadow;glasses_front;MEC/Q400;CRPT/CRPT/94084217;RUF/ROO1/94084297;INT/INT/94084213;BOE/{interior.seat.code2}/INT/{interior.seat.code1};DUMMYOPTS/DOARM/{interior.dashboard.code1};DUMMYOPTS/DOPUH/{interior.dashboard.code2};TRIM/Q4MN;DSH/DSHG/{interior.dashboard.code2};STEERINGWHEEL/STL1/{interior.steering.code};BOE/Q5ZK;BOE/Q4B2;BOE/Q212;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/94084201',

                'preview_url': f'https://ph.cloud.maserati.com/{mvl.code}/533/c300/gfx6?config=background;shadow;CRPT/CRPT/94084217;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;RUF/ROO1/94084295;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;CAL/{exterior.caliper.code};RIMS/{exterior.wheel.code};EXT/EXT/{exterior.exterior.code};MEC/Q5EM;glasses_front;MEC/Q400',

                'exterior' : {
                     'exterior' : exterior.exterior.exterior_type.color.name,
                     'wheel'    : exterior.wheel.wheel_type.name,
                     'caliper'  : exterior.caliper.caliper_type.color.name
                },
                
                'interior' : {
                     'seat'      : interior.seat.seat_type.color.name,
                     'dashboard' : interior.dashboard.dashboard_type.color.name,
                     'carpet'    : interior.carpet.carpet_type.color.name,
                     'steering'  : interior.steering.steering_type.color.name
                },
               
                'spec' : spec,
                'dimension' : dimension
              }
             ]

            return JsonResponse({'summary' : summary_list}, status = 200)
        except KeyError:
            return HttpResponse(status = 400)
        except ObjectDoesNotExist:
            return HttpResponse(status = 400)

class DefaultView(View):
     def get(self, request, mvl_id):
         default_info = Default.objects.select_related('exterior_type','wheel_type','caliper_type','seat_type','dashboard_type','carpet_type', 'steering_type').filter(model_version_line_id = mvl_id)

         default_list = [
         {
             'exterior'   : {'color_id' : default.exterior_type.color.id,  'color' : default.exterior_type.color.name ,  'thumbnail_url' : default.exterior_type.thumbnail_url},
             'wheel'      : {'wheel_id' : default.wheel_type.id,           'name'  : default.wheel_type.name,            'thumbnail_url' : default.wheel_type.thumbnail_url},
             'caliper'    : {'color_id' : default.caliper_type.color.id,   'color' : default.caliper_type.color.name,    'thumbnail_url' : default.caliper_type.thumbnail_url},
             'seat'       : {'color_id' : default.seat_type.color.id,      'color' : default.seat_type.color.name,       'thumbnail_url' : default.seat_type.thumbnail_url},
             'dashboard'  : {'color_id' : default.dashboard_type.color.id, 'color' : default.dashboard_type.color.name,  'thumbnail_url' : default.dashboard_type.thumbnail_url},
             'carpet'     : {'color_id' : default.carpet_type.color.id,    'color' : default.carpet_type.color.name,     'thumbnail_url' : default.carpet_type.thumbnail_url},
             'steering'   : {'color_id' : default.steering_type.color.id,  'color' : default.steering_type.color.name,   'thumbnail_url' : default.steering_type.thumbnail_url}
         } for default  in default_info
          ]
         
         return JsonResponse({'message':default_list},status=200)

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

class AccessoryView(View):
    def get(self, request):

        category   = AccessoryCategory.objects.prefetch_related('accessory_set')

        accessory_list = [
            { 
               acc.category : list(acc.accessory_set.values('id', 'name', 'thumbnail_url'))
            } for acc in category
        ]

        print(accessory_list)

        return JsonResponse({'accessory' : accessory_list}, status = 200)
