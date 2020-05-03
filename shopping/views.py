import json

from django.http            import HttpResponse,JsonResponse
from django.views           import View
from django.core.exceptions import ObjectDoesNotExist
from django.db              import transaction

from car.models         import ModelVersionLine
from .models            import  ( User,
                                  DriveContactChannel,
                                  AddressCity,
                                  Gender,
                                  TestDrive,
                                  TestDriveSchedule,
                                  ExpectDate,
                                  StoreInformation
                                )

class UserView(View):
    @transaction.atomic
    def post(self, request):
        try:
            data = json.loads(request.body)

            DriveContactChannel.objects.create(
                email  = data['email_privacy'],
                fax    = data['fax'],
                mail   = data['mail'],
                sms    = data['sms'],
                call   = data['call'],
                sns    = data['sns']
            )

            User.objects.create(
                first_name            = data['first_name'],
                last_name             = data['last_name'],
                birthday              = data['birthday'],
                phone_number          = data['phone_number'],
                address_city          = AddressCity.objects.get(id = data['city']),
                address_detail        = data['address'],
                email                 = data['email'],
                gender                = Gender.objects.get(id = data['gender']),
                drive_contact_channel = DriveContactChannel.objects.last(),
                privacy_check         = data['privacy_check']
            )

            TestDriveSchedule.objects.create(
                model_version_line  = ModelVersionLine.objects.get(id = data['mvl']),
                store_information   = StoreInformation.objects.get(id = data['store']),
                expect_date         = ExpectDate.objects.get(id = data['expect_date']),
                contact_us          = data['contact_us']
            )

            TestDrive.objects.create(
                test_drive_schedule   = TestDriveSchedule.objects.last(),
                user                  = User.objects.last(),
                current_car_model     = data['current_car'],
            )

            return HttpResponse(status = 200)

        except KeyError:
            return HttpResponse(status = 400)

        except ValueError:
            return HttpResponse(status = 400)

        except ObjectDoesNotExist:
            return HttpResponse(status = 400)

    def get(self, request):
        cities             = AddressCity.objects.all()
        exhibition_centers = list(StoreInformation.objects.filter(exhibition_center = True))

        cities_list = [
                {
                  'city_id'   : city.id,
                  'city_name' : city.city
		} for city in cities
         ]

        exhibition_list =[
                {
                  'exhibition_id'   : exhibition.id,
                  'exhibition_name' : exhibition.name,
                  'exhibition_city' : exhibition.city
                } for exhibition in exhibition_centers
              ]

        return JsonResponse({'city': cities_list, 'exhibition' : exhibition_list }, status = 200)
