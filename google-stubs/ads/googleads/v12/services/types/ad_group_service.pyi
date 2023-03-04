from collections.abc import MutableSequence
from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v12.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v12.resources.types.ad_group import AdGroup

class AdGroupOperation(proto.Message):
    update_mask: FieldMask
    create: AdGroup
    update: AdGroup
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: AdGroup = ...,
        update: AdGroup = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupResult(proto.Message):
    resource_name: str
    ad_group: AdGroup
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group: AdGroup = ...
    ) -> None: ...

class MutateAdGroupsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AdGroupOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[AdGroupOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAdGroupsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateAdGroupResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateAdGroupResult] = ...
    ) -> None: ...
