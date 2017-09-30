from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def get_data():
    data = {
            'current_expected_recovery': 77,
            'optimal_expected_recovery': 80,
            'air_addition_rate':{
                'current': 1,
                'optimal': 1.1,
                },
            'frother_addition_rate':{
                'current': 12,
                'optimal': 11,
                },
            'slurry_density':{
                'current': 1,
                'optimal': 1.5,
                },
            'activator_addition_rate':{
                'current': 0.6,
                'optimal': 1.2,
                },
            'collector_addition_rate':{
                'current': 3,
                'optimal': 1.1,
                },
            }
    return data

def show_data(request):
    now = datetime.datetime.now()
    data = get_data()
    return render(request, 'frothgui/data.html', {'data':data})
