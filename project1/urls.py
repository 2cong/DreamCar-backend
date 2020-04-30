from django.urls import path,include

urlpatterns = [
        path('car',include('car.urls')),
        path('shopping', include('shopping.urls')),
]
