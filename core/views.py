from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {
        'user': {
            'displayName': 'Murilo Dias'
        },
        'dashboards': {
            'rh': 'https://app.powerbi.com/groups/16c484dd-1fde-44ee-857e-06627ee01d99/reports/0336e46b-d67c-4e9b-b5d4-b10471623cef/93cdeb5027554930ab01?experience=power-bi',
            'fin': 'https://app.powerbi.com/groups/941e43fd-d3b7-467f-b090-d566237a3913/reports/a1cf9489-2c5a-466f-bae7-489de32fbe9c/a8fb0d499d72e68d054c?experience=power-bi',
            'op': 'https://app.powerbi.com'
        }
    })