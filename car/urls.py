from django.urls    import path

from .views         import ( DefaultView,
                             MainView,
                             ExteriorView,
                             WheelView,
                             CaliperView,
                             SeatView,
                             DashboardView,
                             CarpetView,
                             SteeringView,
                             PackageView,
                             AccessoryView,
                             SummaryView,
                             LoadView,
                             CustomCarView,
                             ContactChannelView,
                             )

urlpatterns = [
        path('/default/<int:mvl_id>',DefaultView.as_view()),
        path('/customcar', MainView.as_view()),
        path('/exterior/<int:mvl_id>', ExteriorView.as_view()),
        path('/wheel/<int:mvl_id>', WheelView.as_view()),
        path('/caliper/<int:mvl_id>', CaliperView.as_view()),
        path('/seat/<int:mvl_id>',SeatView.as_view()),
        path('/dashboard/<int:mvl_id>',DashboardView.as_view()),
        path('/carpet/<int:mvl_id>',CarpetView.as_view()),
        path('/steering/<int:mvl_id>',SteeringView.as_view()),
        path('/package/<int:mvl_id>',PackageView.as_view()),
        path('/accessory', AccessoryView.as_view()),
        path('/summary', SummaryView.as_view()),
        path('/load',LoadView.as_view()),
        path('/save',CustomCarView.as_view()),
        path('/contactchannel',ContactChannelView.as_view()),
    ]

