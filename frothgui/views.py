from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.


from django.http import HttpResponse
import datetime


def get_data(grade_threshold):
    current_expected_recovery = 100 - grade_threshold  * 8
    optimal_expected_recovery = 100 - grade_threshold  * 5
    ac = grade_threshold * 1.2
    ao = grade_threshold * 1.1
    fc = grade_threshold * 2.1
    fo = grade_threshold * 1.3
    sc = grade_threshold * 1.1
    so = grade_threshold * 1.3
    actc = grade_threshold * 1.6
    acto = grade_threshold * 1.3
    cc = grade_threshold * 1.5
    co = grade_threshold * 0.4

    data = {
            'grade_threshold': grade_threshold,
            'current_expected_recovery': current_expected_recovery,
            'optimal_expected_recovery': optimal_expected_recovery,
            'air_addition_rate':{
                'current': ac,
                'optimal': ao,
                },
            'frother_addition_rate':{
                'current': fc,
                'optimal': fo,
                },
            'slurry_density':{
                'current': sc,
                'optimal': so,
                },
            'activator_addition_rate':{
                'current': actc,
                'optimal': acto,
                },
            'collector_addition_rate':{
                'current': cc,
                'optimal': co,
                },
            }
    return data

def show_data(request, grade_threshold=0.8):
    if request.method == 'POST':
        grade_threshold = float(request.POST.get("grade_threshold"))
    data = get_data(grade_threshold)

    return render(request, 'frothgui/data.html', {'data':data})
