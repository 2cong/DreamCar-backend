from django.urls    import path
from .views         import (
    DefaultView,
    SeatView,
    DashboardView,
    CarpetView,
    SteeringView,
    PackageView,
    CustomCarOptionView
)

urlpatterns = [
    path('/default/<int:mvl_id>',DefaultView.as_view()),
    path('/seat/<int:mvl_id>',SeatView.as_view()),
    path('/dashboard/<int:mvl_id>',DashboardView.as_view()),
    path('/carpet/<int:mvl_id>',CarpetView.as_view()),
    path('/steering/<int:mvl_id>',SteeringView.as_view()),
    path('/package/<int:mvl_id>',PackageView.as_view()),
    path('/customcaroption',CustomCarOptionView.as_view())
    ]
