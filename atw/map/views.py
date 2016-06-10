from atw.map.models import *
from atw.map.forms import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib.gis.geos import Point
from django.contrib.auth.decorators import login_required
# Export pdf
from atw.map.printers import PrinterTripStages, PrinterTrips
from io import BytesIO
# Export csv
import csv

@login_required
def add_trip_stage(request):
    if request.method == 'POST':
        form = AddTripStageForm(request.POST, request.FILES, label_suffix='')
        if form.is_valid(): # If is_valid() is True then validated data are stored in the form.cleaned_data dictionary nicely converted into python types.
            new_stage = TripStage()
            coordinates = form.cleaned_data['coordinates'].split(',')
            new_stage.geom = Point(float(coordinates[0]), float(coordinates[1]))
            new_stage.stage_name = form.cleaned_data['stage_name']
            new_stage.date = form.cleaned_data['date']
            new_stage.massif = form.cleaned_data['massif']
            new_stage.type = form.cleaned_data['type']
            new_stage.picture_tag = form.cleaned_data['picture_tag']
            new_stage.story = form.cleaned_data['story']
            new_stage.distance = form.cleaned_data['distance']
            new_stage.duration = form.cleaned_data['duration']
            new_stage.email_validation = form.cleaned_data['email_validation']
            new_stage.email = form.cleaned_data['email']
            new_stage.added_by = request.user.username
            new_stage.save()
            for trip in form.cleaned_data['trips']:
                new_stage.trips.add(trip)
            new_stage.save()

            if new_stage.email_validation:
                send_mail('Contemplatio', 'Hi, thank you for adding a new trip stage on the map. Update it whenever you want! Yann', 'berry.yann@free.fr', [new_stage.email], fail_silently=True)
            return HttpResponseRedirect(reverse('trip_stage_added'))
    else:
        form = AddTripStageForm(label_suffix='')

    args = {}
    args['form'] = form

    return render(request, 'map/add_trip_stage.html', args)

def osmap(request):
    #trip_stages = TripStage.objects.all()
    trips = Trip.objects.all()
    return render(request, 'map/map.html', {'trips':trips}) #{'trip_stages':trip_stages, 'trips':trips}

def gmap(request):
    #trip_stages = TripStage.objects.all()
    trips = Trip.objects.all()
    return render(request, 'map/gmap.html', {'trips':trips}) #{'trip_stages':trip_stages, 'trips':trips}

def trip_stage(request, stage_slug):
    trip_stage = TripStage.objects.get(stage_slug=stage_slug)
    return render(request, 'map/trip_stage.html', {'t':trip_stage})

def trip(request, trip_slug):
    trip = Trip.objects.get(trip_slug=trip_slug)
    return render(request, 'map/trip.html', {'t':trip})

def form_success(request):
    return render(request, 'map/form_success.html')

def list_trips(request):
    trip_stages = TripStage.objects.all()
    trips = Trip.objects.all()
    return render(request, 'map/list_trips.html', {'trip_stages':trip_stages, 'trips':trips})

def list_trips_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Trips.pdf"'
    buffer = BytesIO()
    report = PrinterTrips(buffer,'A4') # I defined A4, Landscape and Letter in printers.py
    pdf = report.print_db()
    response.write(pdf)
    return response

def list_trips_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Trips.csv"'
    writer = csv.writer(response)
    writer.writerow(['Trip', 'Duration' ,'Start date', 'End date', 'Stages', 'Localisation'])
    for o in Trip.objects.all():
        writer.writerow([o.trip_name, o.nbr_of_days, o.start_date, o.end_date, o.tripstage_set.values_list('stage_name', flat=True).order_by('date'), o.geom])
    return response

def list_trip_stages_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Trip_stages.pdf"'
    buffer = BytesIO()
    report = PrinterTripStages(buffer,'A4') # I defined A4, Landscape and Letter in printers.py
    pdf = report.print_db()
    response.write(pdf)
    return response

def list_trip_stages_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Trip_stages.csv"'
    writer = csv.writer(response)
    writer.writerow(['Stage', 'Massif', 'Distance', 'Localisation'])
    for o in TripStage.objects.all():
        writer.writerow([o.stage_name, o.massif, o.distance, o.geom])
    return response
