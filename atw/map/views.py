from atw.map.models import *
from atw.map.forms import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib.gis.geos import Point
from django.contrib.auth.decorators import login_required
# Export pdf
from atw.map.printers import Printer
from io import BytesIO
# Export csv
import csv

@login_required
def add_point(request):
    if request.method == 'POST':
        form = AddInitiativeForm(request.POST, request.FILES, label_suffix='')
        if form.is_valid(): # If is_valid() is True then validated data are stored in the form.cleaned_data dictionary nicely converted into python types.
            new_point = Initiative()
            coordinates = form.cleaned_data['coordinates'].split(',')
            new_point.geom = Point(float(coordinates[0]), float(coordinates[1]))
            new_point.project_name = form.cleaned_data['project_name']
            new_point.stage = form.cleaned_data['stage']
            new_point.project_leader = form.cleaned_data['project_leader']
            new_point.picture = form.cleaned_data['picture']
            new_point.description = form.cleaned_data['description']
            new_point.status = form.cleaned_data['status']
            new_point.nbr_installations = form.cleaned_data['nbr_installations']
            new_point.power = form.cleaned_data['power']
            new_point.start = form.cleaned_data['start']
            new_point.email_validation = form.cleaned_data['email_validation']
            new_point.email = form.cleaned_data['email']
            new_point.added_by = request.user.username
            new_point.save()
            
            if new_point.email_validation:
                send_mail('ATW', 'Hi, thank you for adding a new initiative on the map. Update it when necessary! Yann', 'berry.yann@free.fr', [new_point.email], fail_silently=True)
            return HttpResponseRedirect(reverse('point_added'))
    else:
        form = AddInitiativeForm(label_suffix='')

    args = {}
    args['form'] = form

    return render(request, 'map/add_point.html', args)

def osmap(request):
    initiatives = Initiative.objects.all()
    return render(request, 'map/map.html', {'initiatives':initiatives})

def gmap(request):
    initiatives = Initiative.objects.all()
    return render(request, 'map/gmap.html', {'initiatives':initiatives})

def form_success(request):
    return render(request, 'map/form_success.html')

def download_db(request):
    initiatives = Initiative.objects.all()
    return render(request, 'map/download_db.html', {'initiatives':initiatives})

def download_db_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Anaerobic_Digestion_Initiatives_World.pdf"'
    buffer = BytesIO()
    report = Printer(buffer,'A4') # I defined A4, Landscape and Letter in printers.py
    pdf = report.print_db()
    response.write(pdf)
    return response

def download_db_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Country.csv"'
    writer = csv.writer(response)
    writer.writerow(['Project Name', 'Project Leader', 'Number of installations', 'Power', 'Localisation'])
    for o in Initiative.objects.all():
        writer.writerow([o.project_name, o.project_leader, o.nbr_installations, o.power, o.geom])
    return response
