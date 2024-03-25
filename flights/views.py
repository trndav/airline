from django.shortcuts import render, get_object_or_404
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight

def index(request):
    flights = Flight.objects.all()
    return render(request, "flights/index.html", {"flights": flights})
    # return render(request, "flights/index.html", {
    #     "flights": Flight.objects.all()
    # })

def flight(request, flight_id):
    # flight = Flight.objects.get(pk=flight_id)
    flight = get_object_or_404(Flight, pk=flight_id)
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": non_passengers
    })

def book(request, flight_id): # Function to capture form inputs
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        # passenger = Passenger.objects.get(pk=int(request.POST["passenger"])) # Input field will be passenger
        passenger_id = request.POST.get("passenger")
        passenger = Passenger.objects.get(pk=int(passenger_id))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
    return HttpResponseRedirect(reverse("index"))
