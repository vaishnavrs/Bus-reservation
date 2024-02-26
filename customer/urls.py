from django.urls import path
from .views import customerhomeView,SeatView,BookingListView

urlpatterns=[
    path('cust',customerhomeView.as_view(),name='customerhome'),
    path('seat/<int:id>',SeatView.as_view(),name='seats'),
    path('bookings',BookingListView.as_view(),name='booking')
]