from typing import Any, Dict, Tuple, Union, overload

from typing_extensions import TypedDict

class _ConfigDataRequired(TypedDict):
    developer_token: str

class _ConfigDataOptional(TypedDict, total=False):
    endpoint: str
    http_proxy: str

class _ConfigDataParsedOptional(_ConfigDataOptional, total=False):
    login_customer_id: str
    linked_customer_id: str
    logging: Dict[str, Any]

class _ConfigDataUnparsedOptional(_ConfigDataOptional, total=False):
    login_customer_id: Union[int, str]
    linked_customer_id: Union[int, str]
    logging: Union[Dict[str, Any], str]

class _ConfigDataParsedRequired(_ConfigDataRequired):
    use_proto_plus: bool

class _ConfigDataUnparsedRequired(_ConfigDataRequired):
    use_proto_plus: Union[bool, str]

class _InstalledAppConfigDataRequired(TypedDict):
    client_id: str
    client_secret: str
    refresh_token: str

class _ServiceAccountConfigDataRequired(TypedDict):
    json_key_file_path: str
    impersonated_email: str

class _InstalledAppConfigData(
    _ConfigDataParsedRequired,
    _ConfigDataParsedOptional,
    _InstalledAppConfigDataRequired,
):
    pass

class _InstalledAppConfigDataUnparsed(
    _ConfigDataUnparsedRequired,
    _ConfigDataUnparsedOptional,
    _InstalledAppConfigDataRequired,
):
    pass

class _ServiceAccountConfigData(
    _ConfigDataParsedRequired,
    _ConfigDataParsedOptional,
    _ServiceAccountConfigDataRequired,
):
    pass

class _ServiceAccountConfigDataUnparsed(
    _ConfigDataUnparsedRequired,
    _ConfigDataUnparsedOptional,
    _ServiceAccountConfigDataRequired,
):
    pass

_ConfigData = Union[_InstalledAppConfigData, _ServiceAccountConfigData]
_ConfigDataUnparsed = Union[
    _InstalledAppConfigDataUnparsed, _ServiceAccountConfigDataUnparsed
]

def validate_dict(config_data: _ConfigData) -> None: ...
def validate_login_customer_id(login_customer_id: str | None) -> None: ...
def validate_linked_customer_id(linked_customer_id: str | None) -> None: ...
def load_from_yaml_file(path: str | None = ...) -> _ConfigData: ...
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
@overload
def convert_linked_customer_id_to_str(
    config_data: _InstalledAppConfigDataUnparsed,
) -> _InstalledAppConfigData: ...
@overload
def convert_linked_customer_id_to_str(
    config_data: _ServiceAccountConfigDataUnparsed,
) -> _ServiceAccountConfigData: ...
def disambiguate_string_bool(value: Union[str, bool]) -> bool: ...
