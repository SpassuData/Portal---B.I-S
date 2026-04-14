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
        'people': {
            'titulo': 'People Analytics',
            'cor': 'bg-[#FA4616]',
            'em_construcao': False,
            'dashboards': [
                {
                    'nome': 'Painel RH',
                    'descricao': 'Visão geral de indicadores de RH',
                    'link': "https://app.powerbi.com/groups/16c484dd-1fde-44ee-857e-06627ee01d99/reports/0336e46b-d67c-4e9b-b5d4-b10471623cef/93cdeb5027554930ab01?experience=power-bi"
                },
                {
                    'nome': 'Currículos',
                    'descricao': 'Análise de banco de talentos',
                    'link': ""
                },
                {
                    'nome': 'Treinamentos',
                    'descricao': 'Acompanhamento de capacitações',
                    'link': "https://app.powerbi.com/groups/16c484dd-1fde-44ee-857e-06627ee01d99/reports/900f6d6c-ef09-454b-aef5-9ca0e8d4d7b1/ReportSection661e3c29aaf256694e5f?experience=power-bi"
                },
                {
                    'nome': 'PCDs',
                    'descricao': 'Indicadores de inclusão e diversidade',
                    'link': "https://app.powerbi.com/groups/16c484dd-1fde-44ee-857e-06627ee01d99/reports/0336e46b-d67c-4e9b-b5d4-b10471623cef/2867187662753bf69123?experience=power-bi"
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
                    'link': "https://app.powerbi.com/groups/941e43fd-d3b7-467f-b090-d566237a3913/reports/a1cf9489-2c5a-466f-bae7-489de32fbe9c?experience=power-bi"
                },
                {
                    'nome': 'Análise DP',
                    'descricao': 'Indicadores do departamento pessoal',
                    'link': "https://app.powerbi.com/groups/c885bc43-9568-4226-a98d-4212ce0e493f/reports/97c3440b-5537-4f2b-b64d-ff0736adacb7/80d96b61b71e5d3755d0?experience=power-bi"
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
