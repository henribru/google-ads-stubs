from typing import overload

from google.oauth2.credentials import Credentials as InstalledAppCredentials
from google.oauth2.service_account import Credentials as ServiceAccountCreds

from google.ads.googleads.config import (
    _InstalledAppConfigDataRequired,
    _ServiceAccountConfigDataRequired,
)

def get_installed_app_credentials(
    client_id: str,
    client_secret: str,
    refresh_token: str,
    http_proxy: str | None,
    token_uri: str = "https://accounts.google.com/o/oauth2/token",
) -> InstalledAppCredentials: ...
def get_service_account_credentials(
    json_key_file_path: str,
    subject: str,
    http_proxy: str | None,
    scopes: list[str] = ["https://www.googleapis.com/auth/adwords"],
) -> ServiceAccountCreds: ...
@overload
def get_credentials(
    config_data: _InstalledAppConfigDataRequired,
) -> InstalledAppCredentials: ...
@overload
def get_credentials(
    config_data: _ServiceAccountConfigDataRequired,
) -> ServiceAccountCreds: ...
