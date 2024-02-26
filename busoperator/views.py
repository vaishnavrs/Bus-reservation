from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from .serializers import UserSer,BusSer
from rest_framework.response import Response
from accounts.models import Bus
from rest_framework import authentication
from rest_framework import permissions
# Create your views here.


class SignUpViewSet(ViewSet):
    def create(self,request):
        ser=UserSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'created'},status=201)
        return Response({"msg":"failed"})
    
class BusMViewSet(ModelViewSet):
    serializer_class=BusSer
    queryset=Bus.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        ser=BusSer(data=request.data)
        if ser.is_valid():
            ser.save(user=request.user)
            return Response({"msg":"bus added"})
        return Response(ser.errors, status=400)
    
    def get_queryset(self):
        return Bus.objects.filter(user=self.request.user)