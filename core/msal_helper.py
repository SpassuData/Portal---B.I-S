import msal

from django.conf import settings


def _load_cache(request):
    cache = msal.SerializableTokenCache()
    if request.session.get('token_cache'):
        cache.deserialize(request.session['token_cache'])
    return cache


def _save_cache(request, cache):
    if cache.has_state_changed:
        request.session['token_cache'] = cache.serialize()


def _build_msal_app(cache=None):
    return msal.ConfidentialClientApplication(
        settings.AZURE_CLIENT_ID,
        authority=settings.AZURE_AUTHORITY,
        client_credential=settings.AZURE_CLIENT_SECRET,
        token_cache=cache,
    )


def build_auth_url(state):
    msal_app = _build_msal_app()
    return msal_app.get_authorization_request_url(
        settings.AZURE_SCOPE,
        state=state,
        redirect_uri=settings.REDIRECT_URI,
    )


def acquire_token_by_auth_code(request, code):
    cache = _load_cache(request)
    msal_app = _build_msal_app(cache)
    result = msal_app.acquire_token_by_authorization_code(
        code,
        scopes=settings.AZURE_SCOPE,
        redirect_uri=settings.REDIRECT_URI,
    )
    _save_cache(request, cache)
    return result
