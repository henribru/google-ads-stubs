from typing import Any, Dict, Optional, Union

import proto
from google.oauth2.credentials import Credentials
from google.protobuf.message import Message
from typing_extensions import Literal

from google.ads.googleads.config import _ConfigDataUnparsed

_V7 = Literal["v7"]
_V8 = Literal["v8"]
_V9 = Literal["v9"]
_V = Union[_V7, _V8, _V9]

class GoogleAdsClient:
    credentials: Credentials
    developer_token: str
    endpoint: Optional[str]
    login_customer_id: Optional[str]
    linked_customer_id: Optional[str]
    version: Optional[str]
    http_proxy: Optional[str]
    use_proto_plus: bool
    enums: Any  # TODO
    @classmethod
    def copy_from(
        cls,
        destination: Union[proto.Message, Message],
        origin: Union[proto.Message, Message],
    ) -> None: ...
    @classmethod
    def load_from_env(cls, version: Optional[str] = ...) -> GoogleAdsClient: ...
    @classmethod
    def load_from_string(
        cls, yaml_str: str, version: Optional[str] = ...
    ) -> GoogleAdsClient: ...
    @classmethod
    def load_from_storage(
        cls, path: Optional[str] = ..., version: Optional[str] = ...
    ) -> GoogleAdsClient: ...
    @classmethod
    def load_from_dict(
        cls, config_dict: _ConfigDataUnparsed, version: Optional[str] = ...
    ) -> GoogleAdsClient: ...
    def __init__(
        self,
        credentials: Credentials,
        developer_token: str,
        endpoint: Optional[str] = ...,
        login_customer_id: Optional[str] = ...,
        logging_config: Optional[Dict[Any, Any]] = ...,
        linked_customer_id: Optional[str] = ...,
        version: Optional[str] = ...,
        http_proxy: Optional[str] = ...,
        use_proto_plus: bool = ...,
    ) -> None: ...
    def get_type(cls, name: str, version: _V = ...) -> Any: ...
    def get_service(self, name: str, version: _V = ...) -> Any: ...
