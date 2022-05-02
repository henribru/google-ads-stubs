from typing import Any, Dict, Union

import proto
from google.oauth2.credentials import Credentials
from google.protobuf.message import Message
from typing_extensions import Literal

from google.ads.googleads.config import _ConfigDataUnparsed

_V9 = Literal["v9"]
_V10 = Literal["v10"]
_V = Union[_V9, _V10]

class GoogleAdsClient:
    credentials: Credentials
    developer_token: str
    endpoint: str | None
    login_customer_id: str | None
    linked_customer_id: str | None
    version: str | None
    http_proxy: str | None
    use_proto_plus: bool
    enums: Any  # TODO
    @classmethod
    def copy_from(
        cls,
        destination: Union[proto.Message, Message],
        origin: Union[proto.Message, Message],
    ) -> None: ...
    @classmethod
    def load_from_env(cls, version: str | None = ...) -> GoogleAdsClient: ...
    @classmethod
    def load_from_string(
        cls, yaml_str: str, version: str | None = ...
    ) -> GoogleAdsClient: ...
    @classmethod
    def load_from_storage(
        cls, path: str | None = ..., version: str | None = ...
    ) -> GoogleAdsClient: ...
    @classmethod
    def load_from_dict(
        cls, config_dict: _ConfigDataUnparsed, version: str | None = ...
    ) -> GoogleAdsClient: ...
    def __init__(
        self,
        credentials: Credentials,
        developer_token: str,
        endpoint: str | None = ...,
        login_customer_id: str | None = ...,
        logging_config: Dict[Any, Any] | None = ...,
        linked_customer_id: str | None = ...,
        version: str | None = ...,
        http_proxy: str | None = ...,
        use_proto_plus: bool = ...,
    ) -> None: ...
    def get_type(cls, name: str, version: _V = ...) -> Any: ...
    def get_service(self, name: str, version: _V = ...) -> Any: ...
