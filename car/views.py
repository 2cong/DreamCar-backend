import json

from django.http        import HttpResponse, JsonResponse
from django.views       import View

from .models            import *

class ImageUrlView(View):
    def post(self, request):
        data = json.loads(request.body)

        exterior  = data['exterior']
        wheel     = data['wheel']
        caliper   = data['caliper']
        seat      = data['seat']
        dashboard = data['dashboard']
        carpet    = data['carpet']
        steering  = data['steering']

        image_url = {
            'exterior1' : 'https://ph.cloud.maserati.com/{8578400(차량라인업)}/{1280(해상도)}/{c720(해상도)}/{gfx6(배경)}?config=background;shadow;CRPT/CRPT/94084217;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;RUF/ROO1/94084295;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;CAL/{KMBC(브레이크)};RIMS/{Q420(휠)};EXT/EXT/{94084200(차량외관)};MEC/Q5EM;glasses_front;MEC/Q400',
            'exterior2' : 'https://ph.cloud.maserati.com/{8578300(차량라인업)}/{1280(해상도)}/{c720(해상도)}/{gfx7(배경)}?config=background;shadow;CRPT/CRPT/94084217;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;RUF/ROO1/94084295;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/{KMBC(브레이크)};RIMS/{Q420(휠)};EXT/EXT/{94084200(차량외관};glasses_front;MEC/Q400;plates',
            'exterior3' : 'https://ph.cloud.maserati.com/{8578300(차량라인업)}/{1280(차량)}/{c720(해상도)}/{gfx3(배경)}?config=background;shadow;CRPT/CRPT/94084217;RUF/ROO1/94084295;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;CAL/{KMBC(브레이크)};RIMS/{Q420(휠)};EXT/EXT/{94084200(차량외관)};MEC/Q5EM;glasses_front;MEC/Q400',
            'exterior4' : 'https://ph.cloud.maserati.com/{8578300(차량라인업)}/{1280(해상도)}/{c720(해상도)}/{gfx5(배경)}?config=background;shadow;CRPT/CRPT/94084217;RUF/ROO1/94084295;INT/INT/94084310;BOE/Q136/INT/94084310;DUMMYOPTS/DOARM/94084281;DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/94084275;STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;CAL/{KMBC(브레이크)};RIMS/{Q420(휠)};EXT/EXT/{94084200(차량외관)};MEC/Q5EM;glasses_front;MEC/Q400',
            'interior1' : 'https://ph.cloud.maserati.com/(mvl)8578300/(해상도)1280/c720/gfx9?config=background;shadow;glasses_front;MEC/Q400;CRPT/CRPT/94084217;BOE/Q728/CRPT/{(카펫)94084217};RUF/ROO1/94084295;INT/INT/94084213;DUMMYOPTS/DOARM/{(대시보드2)94084283};DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/{(대시보드1)94084272};STEERINGWHEEL/STL1/{(스티어링휠)94084213};BOE/Q5ZK;BOE/Q136/INT/{(시트)94084213};BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/94084201',
            'interior2' : 'https://ph.cloud.maserati.com/8578300/1280/c720/gfx10?config=background;shadow;glasses_front;MEC/Q400;CRPT/CRPT/94084217;RUF/ROO1/94084297;INT/INT/94084213;BOE/Q136/INT/{(시트)94084213};DUMMYOPTS/DOARM/{(대시보드1)94084282};DUMMYOPTS/DOPUH/{(대시보드2)94084282};TRIM/Q4MN;DSH/DSHG/{(대시보드2)94084269};STEERINGWHEEL/STL1/{(스티어링휠,기어봉)94084213};BOE/Q5ZK;BOE/Q4B2;BOE/Q212;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/94084201',
            'interior3' : 'https://ph.cloud.maserati.com/8578300/1280/c720/gfx11?config=background;shadow;glasses_front;MEC/Q400;CRPT/CRPT/{(카펫)94084217};RUF/ROO1/94084295;INT/INT/94084349;DUMMYOPTS/DOARM/{(대시보드2)94084282};DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/{(대시보드1)94084269};STEERINGWHEEL/STL1/94084213;BOE/Q5ZK;BOE/Q136/INT/{(시트)94084349};BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/94084201',
            'interior4' : 'https://ph.cloud.maserati.com/{8578300(차량라인업)}/{1280(해상도)}/{c720(해상도}/{gfx12(배경)}?config=background;shadow;CRPT/CRPT/{(카펫)94084217};RUF/ROO1/94084296;INT/INT/94084213;BOE/Q136/INT/{94084213(시트)};DUMMYOPTS/DOARM/{(대시보드2)94084282};DUMMYOPTS/DOPUH/94084282;TRIM/Q4MN;DSH/DSHG/{94084269(대시보드1)};STEERINGWHEEL/STL1/{94084213(핸들)};BOE/Q5ZK;BOE/Q4B2;BOE/Q407;BOE/QAWS;FUS/Q410;MEC/Q5EM;CAL/KMBC;RIMS/Q420;EXT/EXT/{94084201(차량외관)};glasses_front;MEC/Q400'
        }

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
#         return JsonResponse({'image_url' : image_url}, status = 200)
#
    def get(self, request):
        mvl      = ModelVersionLine.objects.filter(model = 1).filter(version=1).filter(line=1)
        mvl      = list(mvl)
        exterior = Exterior.objects.select_related('exterior_type__color', 'exterior_type__color_type').filter(model_version_line = mvl[0].id)
        wheel    = Wheel.objects.select_related('wheel_type').filter(model_version_line = mvl[0].id)
        caliper  = Caliper.objects.select_related('caliper_type__color').filter(model_version_line = mvl[0].id)
        seat     = Seat.objects.select_related('seat_type__color').filter(model_version_line = mvl[0].id)
           
        exterior_thumbnail_url = {}
        wheel_thumbnail_url = {}
        caliper_thumbnail_url = {}
        seat_thumbnail_url = {}
        dashboard_thumbnail_url = {}
       
      
        for thumb in exterior:
             exterior_thumbnail_url[thumb.exterior_type.color.name] = thumb.exterior_type.thumbnail_url

        for thumb in wheel:
            wheel_thumbnail_url[thumb.wheel_type.name] = thumb.wheel_type.thumbnail_url

        for thumb in caliper:
            caliper_thumbnail_url[thumb.caliper_type.color.name] = thumb.caliper_type.thumbnail_url

        for thumb in seat:
            seat_thumbnail_url[thumb.seat_type.color.name] = thumb.seat_type.thumbnail_url

        for select_seat in seat:
            temp  = select_seat.seat_type.id
            temp2 = Dashboard.objects.filter(seat_id = temp)
            print(temp2)


        

        return JsonResponse({'exterior_thumbnail_url': exterior_thumbnail_url, 'wheel_thumbnail_url' : wheel_thumbnail_url, 'caliper_thumbnail_url' : caliper_thumbnail_url}, status = 200)
