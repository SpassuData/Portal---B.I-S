import msal
from django.conf import settings
from django.shortcuts import render, redirect
from core.decorators import login_required


def _msal_app():
    return msal.ConfidentialClientApplication(
        settings.AZURE_CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{settings.AZURE_TENANT_ID}",
        client_credential=settings.AZURE_CLIENT_SECRET,
    )


def login(request):
    if request.session.get('user'):
        return redirect('/')
    return render(request, 'login.html')


def auth_redirect(request):
    auth_url = _msal_app().get_authorization_request_url(
        scopes=["User.Read"],
        redirect_uri=settings.REDIRECT_URI,
    )
    return redirect(auth_url)


def auth_callback(request):
    code = request.GET.get('code')

    if not code:
        return render(request, 'login.html', {'error': 'Autenticação cancelada ou inválida.'})

    result = _msal_app().acquire_token_by_authorization_code(
        code,
        scopes=["User.Read"],
        redirect_uri=settings.REDIRECT_URI,
    )

    if "access_token" in result:
        request.session['user'] = result.get('id_token_claims')
        return redirect('/')

    return render(request, 'login.html', {'error': 'Falha na autenticação. Tente novamente.'})


def logout(request):
    request.session.flush()
    return redirect('/login/')


@login_required
def home(request):
    return render(request, 'home.html', {'user': request.session.get('user')})


@login_required
def area(request, area):

    areas = {
        'rh': {
            'titulo': 'Gestão de Jornada',
            'cor': 'bg-[#FA4616]',
            'dashboards': [
                {
                    'nome': 'Horas Extras',
                    'descricao': 'Análise de horas extras',
                    'link': settings.DASHBOARD_RH
                },
                {
                    'nome': 'Absenteísmo',
                    'descricao': 'Faltas e atrasos',
                    'link': settings.DASHBOARD_RH
                }
            ]
        },

        'fin': {
            'titulo': 'Gestão Financeira',
            'cor': 'bg-[#201547]',
            'dashboards': [
                {
                    'nome': 'DRE',
                    'descricao': 'Demonstrativo de resultado',
                    'link': settings.DASHBOARD_FIN
                },
                {
                    'nome': 'Fator K',
                    'descricao': 'Indicadores estratégicos',
                    'link': settings.DASHBOARD_FIN
                }
            ]
        },

        'op': {
            'titulo': 'Eficiência Operacional',
            'cor': 'bg-[#DBE442]',
            'dashboards': [
                {
                    'nome': 'Projetos',
                    'descricao': 'Status dos projetos',
                    'link': settings.DASHBOARD_OP
                }
            ]
        }
    }

    data = areas.get(area)

    return render(request, 'area.html', {
        'data': data,
        'user': request.session.get('user'),
    })
