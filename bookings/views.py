from django.shortcuts import render, redirect
from .models import Seat
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def seat_list(request):
    seats = Seat.objects.all().order_by('number')
    return render(request, 'bookings/seats.html', {'seats': seats})

@login_required
def book_seat(request, seat_id):
    seat = Seat.objects.get(id=seat_id)
    if not seat.is_booked:
        seat.is_booked = True
        seat.booked_by = request.user
        seat.save()
    return redirect('seat_list')

def route_map(request):
    return render(request, 'bookings/route_map.html')