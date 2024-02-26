from django.shortcuts import render

# Create your views here.
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView
from .forms import BusSearchForm
from django.shortcuts import redirect, render
from accounts.models import Bus,Bookings
# Create your views here.



class customerhomeView(View):
    def get(self,request):
        form=BusSearchForm()
        return render(request,'custhome.html',{'form':form})
    
    def post(self,request):
        search_data=BusSearchForm(data=request.POST)
        if search_data.is_valid():
            sr=search_data.cleaned_data.get('source')
            des=search_data.cleaned_data.get('destination')
            dt=search_data.cleaned_data.get('date')
            print('source=',sr)
            print('des=',des)
            res=Bus.objects.filter(source__contains=sr,destination__contains=des,date__contains=dt)
            print(res)
            return render(request,'custhome.html',{'res':res,'form':search_data})
        else:
            return render(request,'custhome.html')
        
class SeatView(View):

    def get(self,request,**kwargs):
        bus_id=kwargs.get('id')
        bus=Bus.objects.get(id=bus_id)
        seat_numbers=bus.seats()
        available_list=bus.available_seats()

        print(seat_numbers)
        context={
            'bus':bus,
            'seat_numbers':seat_numbers,
            'available':available_list
        }
        return render(request,'seat.html',context,)
    
    # def post(self,request,**kwargs):
    #     bus_id=kwargs.get('id')
    #     bus_obj=Bus.objects.get(id=bus_id)
    #     selected_seat=request.POST.get('selected_seats')
    #     # print('selected seat=',selected_seat)
        

    #     # if int(selected_seat) in bus_obj.available_seats():
    #     #     booking=Bookings.objects.create(bus=bus_obj,selected_seat=int(selected_seat))
    #     #     return HttpResponse('success')
    #     # else:
    #     #     return HttpResponse('failed')
    #     selected_seat = [int(seat) for seat in selected_seat]
    #     if int(selected_seat) in bus_obj.available_seats():
    #         booking=Bookings.objects.create(bus=bus_obj,selected_seat=int(selected_seat))
    #         return HttpResponse('success')
    def post(self, request, **kwargs):

        bus_id = kwargs.get('id')
        bus_obj = Bus.objects.get(id=bus_id)
        # user=request.user
        # print(user)
        if request.user.is_authenticated:
            user=request.user
            print('Authenticated user:', user)
            selected_seats = request.POST.getlist('selected_seats')
            print('selected seats',selected_seats)
            for seat in selected_seats:
                try:
                    seat_number = int(seat)
                    print('seat number', seat_number)
                    if seat_number in bus_obj.available_seats():
                        Bookings.objects.create(bus=bus_obj,selected_seat=seat_number,user=user)
                        bus_obj.save()
                    else:
                        return HttpResponse('failed')

                except ValueError:
                    pass
            return HttpResponse('success')
        else:
            return HttpResponse('User not authenticated')
        

class BookingListView(ListView):
    template_name='bookings.html'
    context_object_name='booking'
    queryset=Bookings.objects.all()

    def get_queryset(self):
        return Bookings.objects.filter(user=self.request.user)
    

    

