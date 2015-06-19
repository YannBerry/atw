from map.models import *
from map.forms import *
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib.gis.geos import Point
from django.contrib.auth.decorators import login_required
# Export pdf
from map.printers import Printer
from io import BytesIO
# Export csv
import csv

@login_required
def add_point(request):
	if request.method == 'POST':
		form = AddInitiativeForm(request.POST, request.FILES)
		if form.is_valid(): # Si is_valid() renvoit True alors les données validées sont stockées dans le form.cleaned_data
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
			new_point.save()
			return HttpResponseRedirect(reverse('point_added'))
		else:
			return HttpResponseRedirect(reverse('point_error'))
	else:
		form = AddInitiativeForm()

	args = {}
	args.update(csrf(request))
	args['form'] = AddInitiativeForm()

	return render_to_response('map/add_point.html', args) # si je hardcode l'url : render_to_response('map/add_point.html', args)

def map(request):
	initiatives = Initiative.objects.all()
	return render_to_response('map/map.html', {'initiatives':initiatives})

def gmap(request):
	initiatives = Initiative.objects.all()
	return render_to_response('map/gmap.html', {'initiatives':initiatives})

def form_error(request):
	return render_to_response('map/form_error.html')

def form_success(request):
	return render_to_response('map/form_success.html')

def download_db(request):
	initiatives = Initiative.objects.all()
	return render_to_response('map/download_db.html', {'initiatives':initiatives})

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