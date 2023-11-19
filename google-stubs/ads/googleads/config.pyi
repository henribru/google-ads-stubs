from typing import Any, overload

from typing_extensions import TypedDict

class _ConfigDataRequired(TypedDict):
    developer_token: str

class _ConfigDataOptional(TypedDict, total=False):
    endpoint: str
    http_proxy: str
    use_cloud_org_for_api_access: bool

class _ConfigDataParsedOptional(_ConfigDataOptional, total=False):
    login_customer_id: str
    linked_customer_id: str
    logging: dict[str, Any]

class _ConfigDataUnparsedOptional(_ConfigDataOptional, total=False):
    login_customer_id: int | str
    linked_customer_id: int | str
    logging: dict[str, Any] | str

class _ConfigDataParsedRequired(_ConfigDataRequired):
    use_proto_plus: bool

class _ConfigDataUnparsedRequired(_ConfigDataRequired):
    use_proto_plus: bool | str

class _InstalledAppConfigDataRequired(TypedDict):
    client_id: str
    client_secret: str
    refresh_token: str

class _ServiceAccountConfigDataOptional(TypedDict, total=False):
    impersonated_email: str

class _ServiceAccountConfigDataRequired(TypedDict):
    json_key_file_path: str

class _InstalledAppConfigData(
    _ConfigDataParsedRequired,
    _ConfigDataParsedOptional,
    _InstalledAppConfigDataRequired,
): ...
class _InstalledAppConfigDataUnparsed(
    _ConfigDataUnparsedRequired,
    _ConfigDataUnparsedOptional,
    _InstalledAppConfigDataRequired,
): ...
class _ServiceAccountConfigData(
    _ConfigDataParsedRequired,
    _ConfigDataParsedOptional,
    _ServiceAccountConfigDataOptional,
    _ServiceAccountConfigDataRequired,
): ...
class _ServiceAccountConfigDataUnparsed(
    _ConfigDataUnparsedRequired,
    _ConfigDataUnparsedOptional,
    _ServiceAccountConfigDataOptional,
    _ServiceAccountConfigDataRequired,
): ...

_ConfigData = _InstalledAppConfigData | _ServiceAccountConfigData
_ConfigDataUnparsed = (
    _InstalledAppConfigDataUnparsed | _ServiceAccountConfigDataUnparsed
)

def validate_dict(config_data: _ConfigData) -> None: ...
def validate_login_customer_id(login_customer_id: str | None) -> None: ...
def validate_linked_customer_id(linked_customer_id: str | None) -> None: ...
def load_from_yaml_file(path: str | None = None) -> _ConfigData: ...
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
def get_oauth2_installed_app_keys() -> tuple[str, str, str]: ...
def get_oauth2_required_service_account_keys() -> tuple[str, str]: ...
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
def disambiguate_string_bool(value: str | bool) -> bool: ...
