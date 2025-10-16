from google.rpc.status_pb2 import Status
from collections.abc import MutableSequence
from google.ads.googleads.v21.enums.types.response_content_type import ResponseContentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v21.resources.types.campaign_group import CampaignGroup
from google.ads.googleads.v21.resources.types.campaign_group import CampaignGroup
from google.ads.googleads.v21.resources.types.campaign_group import CampaignGroup
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CampaignGroupOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignGroup
    update: CampaignGroup
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, update_mask: FieldMask = ..., create: CampaignGroup = ..., update: CampaignGroup = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "create", "update", "remove"]) -> bool: ...
class MutateCampaignGroupResult(proto.Message):
    resource_name: str
    campaign_group: CampaignGroup
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., campaign_group: CampaignGroup = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "campaign_group"]) -> bool: ...
class MutateCampaignGroupsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignGroupOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operations: MutableSequence[CampaignGroupOperation] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: ResponseContentTypeEnum.ResponseContentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...
class MutateCampaignGroupsResponse(proto.Message):
    results: MutableSequence[MutateCampaignGroupResult]
    partial_failure_error: Status
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, results: MutableSequence[MutateCampaignGroupResult] = ..., partial_failure_error: Status = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["results", "partial_failure_error"]) -> bool: ...
