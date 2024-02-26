from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Bus(models.Model):
    
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    date=models.DateField(blank=True,default='2024-01-16')
    s_time=models.TimeField(blank=True,default='00:00')
    d_time=models.TimeField(blank=True,default='00:00')
    price=models.IntegerField(blank=True,default=500)
    n_of_seats=models.IntegerField(blank=True,default=28)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    

    def seats(self):
        seat_number=[]
        for i in range(1,self.n_of_seats+1):
            seat_number.append(i)
            # print('seat number in model',seat_number)
        return seat_number
    
    def available_seats(self):
        booked_seats = self.bookings.values_list('selected_seat', flat=True)
        print(booked_seats)
        available_seats_list=[]
        for seat in range(1,self.n_of_seats+1):
            if seat not in booked_seats:
                available_seats_list.append(seat)
        return available_seats_list

class Bookings(models.Model):
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE,related_name='bookings')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    selected_seat=models.IntegerField()