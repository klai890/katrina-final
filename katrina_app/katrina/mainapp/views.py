from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .ml import getPrediction
from .models import Location, Resources
# Create your views here.

# advertise
def index(request):
    return render(request, 'mainapp/index.html')

# render locations
def howtohelp(request):
    context = {}
    context['dataset'] = Location.objects.all()
    print(context)
    return render(request, 'mainapp/help.html', context)
    
# render single location, resource submission form
def location(request, location_id):
    context = {}
    thisLocationResources = Resources.objects.get(pk=location_id)
    resources_formatted = thisLocationResources.resources.split(',')
    resources = []
    for r in resources_formatted:
        resources.append(r.strip())
    context['resources'] = resources
    context['location'] = Location.objects.all()[location_id - 1]
    return render(request, 'mainapp/location.html', context)

# send resources
def send(request, location_id):
    if (request.method == 'POST'):
        context = {}
        thisLocationResources = Resources.objects.get(pk=location_id)
        context['resources'] = thisLocationResources
        context['location'] = Location.objects.all()[location_id - 1]
        resources = list(request.POST.values())[1:]
        for r in resources:
            thisLocationResources.resources += f", {r}"
        print(thisLocationResources)
        thisLocationResources.save()
        return redirect(f"/mainapp/location/{location_id}")
    return render(request, 'mainapp/404.html')

# render prediction form
def predict(request):
    if (request.method == 'POST'):
        vals = list(request.POST.values())[1:]
        result = getPrediction(vals)
        return render(request, 'mainapp/predict.html', {'result': result})
    
    return render(request, 'mainapp/predict.html')