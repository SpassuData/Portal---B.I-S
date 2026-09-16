import uuid

from django.conf import settings
from django.shortcuts import redirect, render

from core import msal_helper
from core.decorators import login_required


def login(request):
    if request.session.get('user'):
        return redirect('/')
    return render(request, 'login.html')


def auth_redirect(request):
    request.session['auth_state'] = str(uuid.uuid4())
    auth_url = msal_helper.build_auth_url(request.session['auth_state'])
    return redirect(auth_url)


def auth_callback(request):
    if request.GET.get('state') != request.session.get('auth_state'):
        return render(request, 'login.html', {'error': 'Estado inválido. Tente fazer login novamente.'})

    if 'error' in request.GET:
        return render(request, 'login.html', {
            'error': request.GET.get('error_description', request.GET['error'])
        })

    code = request.GET.get('code')
    if not code:
        return render(request, 'login.html', {'error': 'Autenticação cancelada ou inválida.'})

    result = msal_helper.acquire_token_by_auth_code(code)
    if 'error' in result:
        return render(request, 'login.html', {
            'error': result.get('error_description', result['error'])
        })

    claims = result.get('id_token_claims', {})
    request.session['user'] = {
        'name': claims.get('name', ''),
        'preferred_username': claims.get('preferred_username', ''),
    }
    return redirect('/')


def logout(request):
    request.session.flush()
    post_logout_redirect_uri = request.build_absolute_uri('/login/')
    logout_url = (
        f"{settings.AZURE_AUTHORITY}/oauth2/v2.0/logout"
        f"?post_logout_redirect_uri={post_logout_redirect_uri}"
    )
    return redirect(logout_url)


@login_required
def home(request):
    return render(request, 'home.html', {'user': request.session.get('user')})


@login_required
def area(request, area):

    areas = {
        'people': {
            'titulo': 'People Analytics',
            'cor': 'bg-[#FA4616]',
            'em_construcao': False,
            'dashboards': [
                {
                    'nome': 'Painel RH',
                    'descricao': 'Visão geral de indicadores de RH',
                    'link': settings.DASHBOARD_PEOPLE_RH
                },
                {
                    'nome': 'Currículos',
                    'descricao': 'Análise de banco de talentos',
                    'link': settings.DASHBOARD_PEOPLE_CURRICULOS
                },
                {
                    'nome': 'Treinamentos',
                    'descricao': 'Acompanhamento de capacitações',
                    'link': settings.DASHBOARD_PEOPLE_TREINAMENTOS
                },
                {
                    'nome': 'PCDs',
                    'descricao': 'Indicadores de inclusão e diversidade',
                    'link': settings.DASHBOARD_PEOPLE_PCDS
                },
            ]
        },

        'dp': {
            'titulo': 'DP Analytics',
            'cor': 'bg-[#201547]',
            'em_construcao': False,
            'dashboards': [
                {
                    'nome': 'Folha de Pagamento',
                    'descricao': 'Análise e evolução da folha',
                    'link': settings.DASHBOARD_DP_FOLHA
                },
                {
                    'nome': 'Análise DP',
                    'descricao': 'Indicadores do departamento pessoal',
                    'link': settings.DASHBOARD_DP_ANALISE
                },
            ]
        },

        'remar': {
            'titulo': 'Performance & Resultados',
            'cor': 'bg-[#201547]',
            'em_construcao': False,
            'dashboards': [
                {
                    'nome': 'Gerentes',
                    'descricao': 'Resultados por gerência — REMAR',
                    'link': settings.DASHBOARD_REMAR_GERENTES
                },
                {
                    'nome': 'Diretoria',
                    'descricao': 'Resultados executivos — REMAR',
                    'link': settings.DASHBOARD_REMAR_DIRETORIA
                },
            ]
        },

        'rampup': {
            'titulo': 'Ramp Up & Performance',
            'cor': 'bg-[#D9D9D6]',
            'em_construcao': True,
            'dashboards': [
                {
                    'nome': 'Acompanhamento',
                    'descricao': 'Evolução e performance de novos colaboradores',
                    'link': settings.DASHBOARD_RAMPUP_ACOMPANHAMENTO
                },
            ]
        },

        'workforce': {
            'titulo': 'Workforce Analytics',
            'cor': 'bg-[#DBE442]',
            'em_construcao': False,
            'dashboards': [
                {
                    'nome': 'Visão Geral',
                    'descricao': 'Panorama da força de trabalho',
                    'link': settings.DASHBOARD_WORKFORCE_VISAO
                },
                {
                    'nome': 'Produtividade',
                    'descricao': 'Dados de produtividade — Meu Spassu',
                    'link': settings.DASHBOARD_WORKFORCE_PRODUTIVIDADE
                },
            ]
        },
    }

    data = areas.get(area)

    return render(request, 'area.html', {
        'data': data,
        'user': request.session.get('user'),
    })
