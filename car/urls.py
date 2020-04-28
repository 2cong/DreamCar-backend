from django.urls    import path
from .views         import DefaultView, SeatView

urlpatterns = [
    path('/default/<int:mvl_id>',DefaultView.as_view()),
    path('/seat/<int:mvl_id>',SeatView.as_view()),
        ]
