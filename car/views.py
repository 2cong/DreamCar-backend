import json

from django.http        import HttpResponse, JsonResponse
from django.views       import View

from .models            import *


class MainModel(View):
     def get(self, requset):
        mvl       = ModelVersionLine.objects.filter(model = 1).filter(version = 1).filter(line = 1)
        mvl       = list(mvl)
        



class ExteriorView(View):
     def post(self, request):
         data = json.loads(request.body)
         
         model_version_line_id = data['mvl_id']
         color_id              = data['color']
         
         exterior = Exterior.objects.select_related('exterior_type__color').filter(model_vsesion_line = model_version_line_id)
         

         exterior_url = [
             {
                 'Exterior1'  :  
                 'Exterior2'  :
                 'Exterior3'  :
                 'Exterior4'  :
                 'interior1'  :
                 'interior2'  :
                 'interior3'  :
                 'interior4'  :
                 'preview_url':
              }
          ]





     def get(self, request, mvl_id):
         exterior      = Exterior.objects.select_related('exterior_type__color').filter(model_version_line = mvl_id)
         
         exterior_list = [
             {
                 'color_name'   : thumb.exterior_type.color.name, 
                 'tumbnail_url' : thumb.exterior_type.thumbnail_url
             } for thumb in exterior
         ]

         return JsonResponse({'exterior_thumbnail' : exterior_list}, status = 200)

class WheelView(View):
     def get(self, request, mvl_id):
        wheel    = Wheel.objects.select_related('wheel_type').filter(model_version_line = mvl_id)
       
        wheel_list = [
             {
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
                   'caliper_color' : thumb.caliper_type.color.name,
                   'thumbnail_url' : thumb.caliper_type.thumbnail_url
               } for thumb in caliper
         ]

         return JsonResponse({'caliper thumbnail' : caliper_list}, status = 200)

class SeatView(View):
     def get(self, request, mvl_id):
         seat     = Seat.objects.select_related('seat_type__color').filter(model_version_line = mvl_id)
         
         seat_list = [
               {
                    'seat_color'     : thumb.seat_type.color.name,
                    'thumbnail_url'  : thumb.seat_type.thumbnail_url
               } for thumb in seat
         ]

         return JsonResponse({'seat Thumbnail' : seat_list}, status = 200)

class DashBoardView(View):
     def get(self, request, mvl_id):
         seat     = Seat.objects.prefetch_related('dashboard_set').filter(model_version_line = mvl_id)
         
         dashboard_list = [
                   {
                       'dashboard_color' : thumb.dashboard_set.values('dashboard_type__color__name')[0]['dashboard_type__color__name'],
                       'thumbnail_url'   : thumb.dashboard_set.values('dashboard_type__thumbnail_url')[0]['dashboard_type__thumbnail_url']
                   } for thumb in seat
         ]


         return JsonResponse({'dashboard thumbnail' : dashboard_list}, status = 200)


         
 
#    def post(self, request):
#        data = json.loads(request.body)
#
#        exterior  = data['exterior']
#        wheel     = data['wheel']
#        caliper   = data['caliper']
#        seat      = data['seat']
#        dashboard = data['dashboard']
#        carpet    = data['carpet']
#        steering  = data['steering']
#
#        image_url = {
#            'exterior1' : 'https://ph.cloud.maserati.com/{8578400(차량라인업)}/{1280(해상도)}/{c720(해상도)}/{gfx6(배경)}?config=background;shadow;CRPT/CRPT/94084217;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;RUF/ROO1/94084295;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;CAL/{KMBC(브레이크)};RIMS/{Q420(휠)};EXT/EXT/{94084200(차량외관)};MEC/Q5EM;glasses_front;MEC/Q400',
#            'exterior2' : 'https://ph.cloud.maserati.com/{8578300(차량라인업)}/{1280(해상도)}/{c720(해상도)}/{gfx7(배경)}?config=background;shadow;CRPT/CRPT/94084217;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;RUF/ROO1/94084295;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/{KMBC(브레이크)};RIMS/{Q420(휠)};EXT/EXT/{94084200(차량외관};glasses_front;MEC/Q400;plates',
#            'exterior3' : 'https://ph.cloud.maserati.com/{8578300(차량라인업)}/{1280(차량)}/{c720(해상도)}/{gfx3(배경)}?config=background;shadow;CRPT/CRPT/94084217;RUF/ROO1/94084295;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;CAL/{KMBC(브레이크)};RIMS/{Q420(휠)};EXT/EXT/{94084200(차량외관)};MEC/Q5EM;glasses_front;MEC/Q400',
#            'exterior4' : 'https://ph.cloud.maserati.com/{8578300(차량라인업)}/{1280(해상도)}/{c720(해상도)}/{gfx5(배경)}?config=background;shadow;CRPT/CRPT/94084217;RUF/ROO1/94084295;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;CAL/{KMBC(브레이크)};RIMS/{Q420(휠)};EXT/EXT/{94084200(차량외관)};MEC/Q5EM;glasses_front;MEC/Q400',
#            'interior1' : 'https://ph.cloud.maserati.com/(mvl)8578300/(해상도)1280/c720/gfx9?config=background;shadow;glasses_front;MEC/Q400;CRPT/CRPT/94084217;BOE/Q728/CRPT/{(카펫)94084217};RUF/ROO1/94084295;INT/INT/94084213;DUMMYOPTS/DOARM/{(대시보드2)94084283};DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/{(대시보드1)94084272};STEERINGWHEEL/STL1/{(스티어링휠)94084213};BOE/Q5ZK;BOE/Q136/INT/{(시트)94084213};BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/94084201',
#            'interior2' : 'https://ph.cloud.maserati.com/8578300/1280/c720/gfx10?config=background;shadow;glasses_front;MEC/Q400;CRPT/CRPT/94084217;RUF/ROO1/94084297;INT/INT/94084213;BOE/Q136/INT/{(시트)94084213};DUMMYOPTS/DOARM/{(대시보드1)94084282};DUMMYOPTS/DOPUH/{(대시보드2)94084282};TRIM/Q4MN;DSH/DSHG/{(대시보드2)94084269};STEERINGWHEEL/STL1/{(스티어링휠,기어봉)94084213};BOE/Q5ZK;BOE/Q4B2;BOE/Q212;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/94084201',
#            'interior3' : 'https://ph.cloud.maserati.com/8578300/1280/c720/gfx11?config=background;shadow;glasses_front;MEC/Q400;CRPT/CRPT/{(카펫)94084217};RUF/ROO1/94084295;INT/INT/94084349;DUMMYOPTS/DOARM/{(대시보드2)94084282};DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/{(대시보드1)94084269};STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q136/INT/{(시트)94084349};BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/94084201',
#            'interior4' : 'https://ph.cloud.maserati.com/{8578300(차량라인업)}/{1280(해상도)}/{c720(해상도}/{gfx12(배경)}?config=background;shadow;CRPT/CRPT/{(카펫)94084217};RUF/ROO1/94084296;INT/INT/94084213;BOE/Q136/INT/{94084213(시트)};DUMMYOPTS/DOARM/{(대시보드2)94084282};DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/{94084269(대시보드1)};STEERINGWHEEL/STL1/{94084213(핸들)};BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/{94084201(차량외관)};glasses_front;MEC/Q400'
#        }

#    def get(self, request):
#
#         image_url = {
#            'exterior1' : 'https://ph.cloud.maserati.com/{8578400(차량라인업)}/{1280(해상도)}/{c720(해상도)}/{gfx6(배경)}?config=background;shadow;CRPT/CRPT/94084217;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;RUF/ROO1/94084295;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;CAL/{KMBC(브레이크)};RIMS/{Q420(휠)};EXT/EXT/{94084200(차량외관)};MEC/Q5EM;glasses_front;MEC/Q400',
#            'exterior2' : 'https://ph.cloud.maserati.com/{8578300(차량라인업)}/{1280(해상도)}/{c720(해상도)}/{gfx7(배경)}?config=background;shadow;CRPT/CRPT/94084217;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;RUF/ROO1/94084295;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/{KMBC(브레이크)};RIMS/{Q420(휠)};EXT/EXT/{94084200(차량외관};glasses_front;MEC/Q400;plates',
#            'exterior3' : 'https://ph.cloud.maserati.com/{8578300(차량라인업)}/{1280(차량)}/{c720(해상도)}/{gfx3(배경)}?config=background;shadow;CRPT/CRPT/94084217;RUF/ROO1/94084295;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;CAL/{KMBC(브레이크)};RIMS/{Q420(휠)};EXT/EXT/{94084200(차량외관)};MEC/Q5EM;glasses_front;MEC/Q400',
#            'exterior4' : 'https://ph.cloud.maserati.com/{8578300(차량라인업)}/{1280(해상도)}/{c720(해상도)}/{gfx5(배경)}?config=background;shadow;CRPT/CRPT/94084217;RUF/ROO1/94084295;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;CAL/{KMBC(브레이크)};RIMS/{Q420(휠)};EXT/EXT/{94084200(차량외관)};MEC/Q5EM;glasses_front;MEC/Q400',   
#            'interior1' : 'https://ph.cloud.maserati.com/(mvl)8578300/(해상도)1280/c720/gfx9?config=background;shadow;glasses_front;MEC/Q400;CRPT/CRPT/94084217;BOE/Q728/CRPT/{(카펫)94084217};RUF/ROO1/94084295;INT/INT/94084213;DUMMYOPTS/DOARM/{(대시보드2)94084283};DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/{(대시보드1)94084272};STEERINGWHEEL/STL1/{(스티어링휠)94084213};BOE/Q5ZK;BOE/Q136/INT/{(시트)94084213};BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/94084201',
#            'interior2' : 'https://ph.cloud.maserati.com/8578300/1280/c720/gfx10?config=background;shadow;glasses_front;MEC/Q400;CRPT/CRPT/94084217;RUF/ROO1/94084297;INT/INT/94084213;BOE/Q136/INT/{(시트)94084213};DUMMYOPTS/DOARM/{(대시보드1)94084282};DUMMYOPTS/DOPUH/{(대시보드2)94084282};TRIM/Q4MN;DSH/DSHG/{(대시보드2)94084269};STEERINGWHEEL/STL1/{(스티어링휠,기어봉)94084213};BOE/Q5ZK;BOE/Q4B2;BOE/Q212;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/94084201',
#            'interior3' : 'https://ph.cloud.maserati.com/8578300/1280/c720/gfx11?config=background;shadow;glasses_front;MEC/Q400;CRPT/CRPT/{(카펫)94084217};RUF/ROO1/94084295;INT/INT/94084349;DUMMYOPTS/DOARM/{(대시보드2)94084282};DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/{(대시보드1)94084269};STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q136/INT/{(시트)94084349};BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/94084201',
#            'interior4' : 'https://ph.cloud.maserati.com/{8578300(차량라인업)}/{1280(해상도)}/{c720(해상도}/{gfx12(배경)}?config=background;shadow;CRPT/CRPT/{(카펫)94084217};RUF/ROO1/94084296;INT/INT/94084213;BOE/Q136/INT/{94084213(시트)};DUMMYOPTS/DOARM/{(대시보드2)94084282};DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/{94084269(대시보드1)};STEERINGWHEEL/STL1/{94084213(핸들)};BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/{94084201(차량외관)};glasses_front;MEC/Q400'
#        }
