from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def area(request, area):

    areas = {
        'rh': {
            'titulo': 'Gestão de Jornada',
            'cor': 'bg-orange-500',
            'dashboards': [
                {
                    'nome': 'Horas Extras',
                    'descricao': 'Análise de horas extras',
                    'link': 'https://app.powerbi.com'
                },
                {
                    'nome': 'Absenteísmo',
                    'descricao': 'Faltas e atrasos',
                    'link': 'https://app.powerbi.com'
                }
            ]
        },

        'fin': {
            'titulo': 'Gestão Financeira',
            'cor': 'bg-blue-800',
            'dashboards': [
                {
                    'nome': 'DRE',
                    'descricao': 'Demonstrativo de resultado',
                    'link': 'https://app.powerbi.com'
                },
                {
                    'nome': 'Fator K',
                    'descricao': 'Indicadores estratégicos',
                    'link': 'https://app.powerbi.com'
                }
            ]
        },

        'op': {
            'titulo': 'Eficiência Operacional',
            'cor': 'bg-green-500',
            'dashboards': [
                {
                    'nome': 'Projetos',
                    'descricao': 'Status dos projetos',
                    'link': 'https://app.powerbi.com'
                }
            ]
        }
    }

    data = areas.get(area)

    return render(request, 'area.html', {
        'data': data
    })