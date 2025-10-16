from google.ads.googleads.v20.enums.types.data_link_status import DataLinkStatusEnum
from google.ads.googleads.v20.resources.types.data_link import DataLink
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CreateDataLinkRequest(proto.Message):
    customer_id: str
    data_link: DataLink
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., data_link: DataLink = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "data_link"]) -> bool: ...
class CreateDataLinkResponse(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
class RemoveDataLinkRequest(proto.Message):
    customer_id: str
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "resource_name"]) -> bool: ...
class RemoveDataLinkResponse(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
class UpdateDataLinkRequest(proto.Message):
    customer_id: str
    data_link_status: DataLinkStatusEnum.DataLinkStatus
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., data_link_status: DataLinkStatusEnum.DataLinkStatus = ..., resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "data_link_status", "resource_name"]) -> bool: ...
class UpdateDataLinkResponse(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
