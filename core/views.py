from django.conf import settings
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {
        'user': {
            'displayName': 'Murilo Dias'
        },
        'dashboards': {
            'rh': settings.DASHBOARD_RH,
            'fin': settings.DASHBOARD_FIN,
            'op': settings.DASHBOARD_OP,
        }
    })
