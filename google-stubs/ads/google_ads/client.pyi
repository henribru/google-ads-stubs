from typing import Any, Dict, Optional, Union

from google.oauth2.credentials import Credentials  # type: ignore
from typing_extensions import Literal

from google.ads.google_ads.config import _ConfigDataUnparsed

_V3 = Literal["v3"]
_V4 = Literal["v4"]
_V5 = Literal["v5"]
_V6 = Literal["v6"]
_V = Union[_V3, _V4, _V5, _V6]

class GoogleAdsClient:
    credentials: Credentials = ...
    developer_token: str = ...
    endpoint: Optional[str] = ...
    login_customer_id: Optional[str] = ...
    @classmethod
    def load_from_env(cls) -> GoogleAdsClient: ...
    @classmethod
    def load_from_string(cls, yaml_str: str) -> GoogleAdsClient: ...
    @classmethod
    def load_from_storage(cls, path: Optional[str] = ...) -> GoogleAdsClient: ...
    @classmethod
    def load_from_dict(cls, config_dict: _ConfigDataUnparsed) -> GoogleAdsClient: ...
    def __init__(
        self,
        credentials: Credentials,
        developer_token: str,
        endpoint: Optional[str] = ...,
        login_customer_id: Optional[str] = ...,
        logging_config: Optional[Dict[Any, Any]] = ...,
    ) -> None: ...
    @classmethod
    def get_type(cls, name: str, version: _V = ...) -> Any: ...
    def get_service(self, name: str, version: _V = ...) -> Any: ...
