from typing import List, overload

from google.oauth2.credentials import (  # type: ignore
    Credentials as InstalledAppCredentials,
)
from google.oauth2.service_account import (  # type: ignore
    Credentials as ServiceAccountCreds,
)

from google.ads.google_ads.config import (
    _InstalledAppConfigDataRequired,
    _ServiceAccountConfigDataRequired,
)

def get_installed_app_credentials(
    client_id: str, client_secret: str, refresh_token: str, token_uri: str = ...
) -> InstalledAppCredentials: ...
def get_service_account_credentials(
    path_to_private_key_file: str, subject: str, scopes: List[str] = ...
) -> ServiceAccountCreds: ...
@overload
def get_credentials(
    config_data: _InstalledAppConfigDataRequired,
) -> InstalledAppCredentials: ...
@overload
def get_credentials(
    config_data: _ServiceAccountConfigDataRequired,
) -> ServiceAccountCreds: ...
