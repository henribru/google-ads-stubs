from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.resources.types.keyword_plan_ad_group import (
    KeywordPlanAdGroup,
)

_M = TypeVar("_M")

class KeywordPlanAdGroupOperation(proto.Message):
    update_mask: FieldMask
    create: KeywordPlanAdGroup
    update: KeywordPlanAdGroup
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: KeywordPlanAdGroup = ...,
        update: KeywordPlanAdGroup = ...,
        remove: str = ...
    ) -> None: ...

class MutateKeywordPlanAdGroupResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...

class MutateKeywordPlanAdGroupsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[KeywordPlanAdGroupOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[KeywordPlanAdGroupOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateKeywordPlanAdGroupsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateKeywordPlanAdGroupResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateKeywordPlanAdGroupResult] = ...
    ) -> None: ...
