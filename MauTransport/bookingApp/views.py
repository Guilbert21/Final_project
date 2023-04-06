import googlemaps
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import TaxiBookingForm
from .models import TaxiBooking
from .models import Booking
# from traveltimepy import TravelTimeSdk, Driving, traveltime
import requests

# sdk = TravelTimeSdk("6859fda9", "9895654d4a64b1feae2ade6c75a59d80")

# client = traveltime.ApiClient(traveltime.Configuration(
#     api_key={"6859fda9"}
#     api_id= {"9895654d4a64b1feae2ade6c75a59d80"}

# ))


# def book_taxi(request):
#     form = None
#     if request.method == 'POST':
#         form = TaxiBookingForm(request.POST)
#         if form.is_valid():
            
#             # pick and drop location
#             gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
#             pick_up_geocode = gmaps.geocode(form.cleaned_data['pick_up_location'])[0]['geometry']['location']
#             drop_off_geocode = gmaps.geocode(form.cleaned_data['drop_off_location'])[0]['geometry']['location']

#             # distance and duration
#             distance = gmaps.distance_matrix(origins=(pick_up_geocode['lat'], pick_up_geocode['lng']),
#                                                 destinations=(drop_off_geocode['lat'], drop_off_geocode['lng']),
#                                                 mode='driving')['rows'][0]['elements'][0]
#             distance = distance['distance']['text']
#             duration = distance['duration']['text']

#             # create taxi booking object 
#             booking = TaxiBooking(
#                 pick_up_location=form.cleaned_data['pick_up_location'],
#                 drop_off_location=form.cleaned_data['drop_off_location'],
#                 pick_up_latitide = pick_up_geocode['lat'],
#                 pick_up_longitude = pick_up_geocode['lng'],
#                 drop_off_latitude = drop_off_geocode['lat'],
#                 drop_off_longitude = drop_off_geocode['lng'],
#             )
#             booking.save()
#             return redirect('booking_sucess')
#         else:
#             form = TaxiBookingForm()
#     return render(request, 'templates/booking.html', {'forms': form})

# from django.conf import settings

# def map(request):
#     key = settings.GOOGLE_MAPS_API_KEY
#     context = {
#         'key':key,
#     }
#     return render(request, 'templates/booking.html')

# def booking_view(request):
#     if request.method =="POST":
#         start_location = request.POST.get('start_location')
#         destionation = request.POST.get('destionation')

#         api_instance = traveltime.DefaultApi(client)
#         request_arrival_time = traveltime.RequestArrivalTime(
#             id='1',
#             coords=[traveltime.Coords(x=START_LOCATION_X, y=START_LOCATION_Y), traveltime.Coords(x=DESTINATION_X, y=DESTINATION_Y)],
#             transportation=traveltime.Transportation(mode='walking'),
#             arrival_time='2023-04-07T10:00:00Z'
#         )
#         try:
#             response = api_instance.map_arrival_time(request_arrival_time)
#             duration = response.results[0].locations[1].properties.travel_time
#             distance = response.results[0].locations[1].properties.distance
#         except traveltime.ApiException as e:
#             print("Error calling TravelTime API: %s\n" % e)
#             duration = None
#             distance = None

#         return render(request, 'templates/booking.html', {'duration':duration, 'distance':distance})
    
#     else:
#         return render(request, 'templates/booking.html')


# def calculate_duration_and_distance(request):
#     origin = request.GET.get('origin')
#     destination = request.GET.get('destination')
#     mode = request.GET.get('mode')

#     # Construct the request to the TravelTime API
#     url = 'https://api.traveltime.com/v4/routes'
#     headers = {'Content-Type': 'application/json',
#                'X-Api-Key': '9895654d4a64b1feae2ade6c75a59d80'}
#     data = {'locations': [{'id': 'origin', 'coords': {'lat': origin[0], 'lng': origin[1]}},
#                           {'id': 'destination', 'coords': {'lat': destination[0], 'lng': destination[1]}}],
#             'departure_searches': [{'id': 'search1',
#                                     'departure_location_id': 'origin',
#                                     'arrival_location_ids': ['destination'],
#                                     'transportation': {'type': mode}}]}
#     response = request.post(url, headers=headers, json=data)

#     # Parse the response from the TravelTime API
#     if response.status_code == 200:
#         json_response = response.json()
#         duration = json_response['results'][0]['locations'][1]['arrival_time'] - \
#                    json_response['results'][0]['locations'][0]['departure_time']
#         distance = json_response['results'][0]['locations'][1]['distance']
#     else:
#         duration = None
#         distance = None

#     # Return the results to the HTML file
#     return render(request, 'results.html', {'duration': duration, 'distance': distance})

def booking_f(request):
    if request.method == 'POST':
        location = request.POST['location']
        destination = request.POST['destination']
        date = request.POST['date']
        time = request.POST['time']
        vehicle_type = request.POST['vehicle_type']
        booking = Booking(location=location, destination=destination, date=date, time=time, vehicle_type=vehicle_type)
        booking.save()
        return redirect('booking-page')
    return render(request, 'templates/booking.html')

def history(request):
    bookings = Booking.objects.all()
    return render(request, 'templates/history.html', {'bookings': bookings})
        