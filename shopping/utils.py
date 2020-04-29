import jwt

from django.http     import HttpResponse, JsonResponse
from .models         import User

def token_ckeck(func):

    def wrapper(self, request, *args, **kwargs):

        if "Authorization" not in request.headers:
            return JsonResponse({'ERROR' : 'INVALID LOGIN'}, status = 401)

        encode_token = request.heades['Authorization']

        try:
            data = jwt.decode(encode_token.encode('utf-8'), SECRET, algorithm = 'HS256')

            user = User.objects.get(user_email = data['usesr_email'])

            request = user

        except jwt.DecodeError:
            return JsonResponse({'ERROR' : 'INVALID_TOKEN'}, status = 401)

        except User.DoesNotExist:
            return JsonResponse({'ERROR' : 'INVALID_USER'}, status = 401)

        return wrapper
