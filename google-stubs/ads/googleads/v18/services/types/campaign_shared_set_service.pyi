from collections.abc import MutableSequence
from google.rpc.status_pb2 import Status
from google.ads.googleads.v18.enums.types.response_content_type import ResponseContentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.resources.types.campaign_shared_set import CampaignSharedSet
from google.ads.googleads.v18.resources.types.campaign_shared_set import CampaignSharedSet
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CampaignSharedSetOperation(proto.Message):
    create: CampaignSharedSet
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, create: CampaignSharedSet = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["create", "remove"]) -> bool: ...
class MutateCampaignSharedSetResult(proto.Message):
    resource_name: str
    campaign_shared_set: CampaignSharedSet
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., campaign_shared_set: CampaignSharedSet = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "campaign_shared_set"]) -> bool: ...
class MutateCampaignSharedSetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignSharedSetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operations: MutableSequence[CampaignSharedSetOperation] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: ResponseContentTypeEnum.ResponseContentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...
class MutateCampaignSharedSetsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateCampaignSharedSetResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, partial_failure_error: Status = ..., results: MutableSequence[MutateCampaignSharedSetResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error", "results"]) -> bool: ...
