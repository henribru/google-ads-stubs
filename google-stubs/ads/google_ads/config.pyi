from typing import Any, Optional, Dict, Union
from typing_extensions import TypedDict

class _ConfigDataRequired(TypedDict):
    developer_token: str

class _ConfigDataOptional(TypedDict, total=False):
    login_customer_id: str
    endpoint: str
    logging: Dict[str, Any]

class _UnparsedConfigDataOptional(ConfigDataOptional, total=False):
    login_customer_id: Union[int, str]

class _InstalledAppConfigDataRequired(TypedDict):
    client_id: str
    client_secret: str
    refresh_token: str

class _ServiceAccountConfigDataRequired(TypedDict, total=False):
    path_to_private_key_file: str
    delegated_account: str

class _InstalledAppConfigData(ConfigDataRequired, ConfigDataOptional, InstalledAppConfigDataRequired):
    pass

class _UnparsedInstalledAppConfigData(ConfigDataRequired, UnparsedConfigDataOptional, InstalledAppConfigDataRequired):
    pass

class _ServiceAccountConfigData(ConfigDataRequired, ConfigDataOptional, ServiceAccountConfigDataRequired):
    pass

class _UnparsedServiceAccountConfigData(ConfigDataRequired, UnparsedConfigDataOptional, ServiceAccountConfigDataRequired):
    pass

_ConfigData = Union[_InstalledAppConfigData, _ServiceAccountConfigData]
_UnparsedConfigData = Union[_UnparsedInstalledAppConfigData, _UnparsedServiceAccountConfigData]

def validate_dict(config_data: _ConfigData) -> None: ...
def validate_login_customer_id(login_customer_id: Optional[str]) -> None: ...
def load_from_yaml_file(path: Optional[str] = ...) -> _ConfigData: ...
def load_from_dict(config_dict: ConfigDataWithIntOrStrCustomerId) -> _ConfigData: ...
def parse_yaml_document_to_dict(yaml_doc: bytes) -> _ConfigData: ...
def load_from_env() -> _ConfigData: ...
def get_oauth2_installed_app_keys() -> Tuple[str, str, str]: ...
def get_oauth2_service_account_keys() -> Tuple[str, str]: ...
def convert_login_customer_id_to_str(config_data: _UnparsedConfigData) -> ConfigData: ...
