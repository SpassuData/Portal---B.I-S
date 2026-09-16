import msal

from django.conf import settings


def _build_msal_app():
    return msal.ConfidentialClientApplication(
        settings.AZURE_CLIENT_ID,
        authority=settings.AZURE_AUTHORITY,
        client_credential=settings.AZURE_CLIENT_SECRET,
    )


def build_auth_url(state):
    msal_app = _build_msal_app()
    return msal_app.get_authorization_request_url(
        settings.AZURE_SCOPE,
        state=state,
        redirect_uri=settings.REDIRECT_URI,
    )


def acquire_token_by_auth_code(code):
    msal_app = _build_msal_app()
    return msal_app.acquire_token_by_authorization_code(
        code,
        scopes=settings.AZURE_SCOPE,
        redirect_uri=settings.REDIRECT_URI,
    )
