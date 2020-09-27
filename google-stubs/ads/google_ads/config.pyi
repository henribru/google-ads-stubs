from typing import Any, Dict, Optional, Tuple, Union, overload

from typing_extensions import TypedDict

class _ConfigDataRequired(TypedDict):
    developer_token: str

class _ConfigDataOptional(TypedDict, total=False):
    endpoint: str
    logging: Dict[str, Any]

class _ConfigDataParsedOptional(_ConfigDataOptional, total=False):
    login_customer_id: str

class _ConfigDataUnparsedOptional(_ConfigDataOptional, total=False):
    login_customer_id: Union[int, str]

class _InstalledAppConfigDataRequired(TypedDict):
    client_id: str
    client_secret: str
    refresh_token: str

class _ServiceAccountConfigDataRequired(TypedDict):
    path_to_private_key_file: str
    delegated_account: str

class _InstalledAppConfigData(
    _ConfigDataRequired, _ConfigDataParsedOptional, _InstalledAppConfigDataRequired
):
    pass

class _InstalledAppConfigDataUnparsed(
    _ConfigDataRequired, _ConfigDataUnparsedOptional, _InstalledAppConfigDataRequired
):
    pass

class _ServiceAccountConfigData(
    _ConfigDataRequired, _ConfigDataParsedOptional, _ServiceAccountConfigDataRequired
):
    pass

class _ServiceAccountConfigDataUnparsed(
    _ConfigDataRequired, _ConfigDataUnparsedOptional, _ServiceAccountConfigDataRequired
):
    pass

_ConfigData = Union[_InstalledAppConfigData, _ServiceAccountConfigData]
_ConfigDataUnparsed = Union[
    _InstalledAppConfigDataUnparsed, _ServiceAccountConfigDataUnparsed
]

def validate_dict(config_data: _ConfigData) -> None: ...
def validate_login_customer_id(login_customer_id: Optional[str]) -> None: ...
def load_from_yaml_file(path: Optional[str] = ...) -> _ConfigData: ...
@overload
def load_from_dict(
    config_dict: _InstalledAppConfigDataUnparsed,
) -> _InstalledAppConfigData: ...
@overload
def load_from_dict(
    config_dict: _ServiceAccountConfigDataUnparsed,
) -> _ServiceAccountConfigData: ...
def parse_yaml_document_to_dict(yaml_doc: bytes) -> _ConfigData: ...
def load_from_env() -> _ConfigData: ...
def get_oauth2_installed_app_keys() -> Tuple[str, str, str]: ...
def get_oauth2_service_account_keys() -> Tuple[str, str]: ...
@overload
def convert_login_customer_id_to_str(
    config_data: _InstalledAppConfigDataUnparsed,
) -> _InstalledAppConfigData: ...
@overload
def convert_login_customer_id_to_str(
    config_data: _ServiceAccountConfigDataUnparsed,
) -> _ServiceAccountConfigData: ...
