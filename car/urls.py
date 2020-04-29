from django.urls    import path

from .views         import *

urlpatterns = [
        path('/customcar', MainView.as_view()),
        path('/summary', SummaryView.as_view()),
        path('/default/<int:mvl_id>', DefaultView.as_view()),
        path('/exterior/<int:mvl_id>', ExteriorView.as_view()),
        path('/wheel/<int:mvl_id>', WheelView.as_view()),
        path('/caliper/<int:mvl_id>', CaliperView.as_view()),
        path('/accessory', AccessoryView.as_view())
       ]
