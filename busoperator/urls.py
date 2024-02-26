from django.urls import path
from .views import SignUpViewSet,BusMViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router=DefaultRouter()
router.register('bususer',SignUpViewSet,basename='signup')
router.register('busmang',BusMViewSet,basename='busmang')

urlpatterns=[
    path('token',views.obtain_auth_token),

]+router.urls