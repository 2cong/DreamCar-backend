from django.urls    import path

from .views         import *

urlpatterns = [
        path('/exterior/<int:mvl_id>', ExteriorView.as_view()),
        path('/wheel/<int:mvl_id>', WheelView.as_view()),
        path('/caliper/<int:mvl_id>', CaliperView.as_view()),
        path('/seat/<int:mvl_id>', SeatView.as_view()),
	path('/dashboard/<int:mvl_id>', DashBoardView.as_view()),
        ]
