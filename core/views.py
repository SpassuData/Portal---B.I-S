import uuid

from django.conf import settings
from django.shortcuts import redirect, render

from core import msal_helper
from core.decorators import login_required


@login_required
def home(request):
    return render(request, 'home.html', {
        'user': request.session.get('user'),
        'dashboards': {
            'rh': settings.DASHBOARD_RH,
            'fin': settings.DASHBOARD_FIN,
            'op': settings.DASHBOARD_OP,
        }
    })


def login(request):
    request.session['auth_state'] = str(uuid.uuid4())
    auth_url = msal_helper.build_auth_url(request.session['auth_state'])
    return redirect(auth_url)


def authorized(request):
    if request.GET.get('state') != request.session.get('auth_state'):
        return render(request, 'error.html', {'error': 'Estado inválido. Tente fazer login novamente.'}, status=400)

    if 'error' in request.GET:
        return render(request, 'error.html', {
            'error': request.GET.get('error_description', request.GET['error'])
        }, status=400)

    code = request.GET.get('code')
    if not code:
        return render(request, 'error.html', {'error': 'Código de autorização ausente.'}, status=400)

    result = msal_helper.acquire_token_by_auth_code(request, code)
    if 'error' in result:
        return render(request, 'error.html', {
            'error': result.get('error_description', result['error'])
        }, status=400)

    claims = result.get('id_token_claims', {})
    request.session['user'] = {
        'displayName': claims.get('name', ''),
        'email': claims.get('preferred_username', ''),
    }
    return redirect('/')


def logout(request):
    request.session.flush()
    post_logout_redirect_uri = request.build_absolute_uri('/')
    logout_url = (
        f"{settings.AZURE_AUTHORITY}/oauth2/v2.0/logout"
        f"?post_logout_redirect_uri={post_logout_redirect_uri}"
    )
    return redirect(logout_url)
