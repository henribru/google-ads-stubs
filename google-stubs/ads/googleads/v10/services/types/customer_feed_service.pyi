from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.customer_feed import CustomerFeed

class CustomerFeedOperation(proto.Message):
    update_mask: FieldMask
    create: CustomerFeed
    update: CustomerFeed
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CustomerFeed = ...,
        update: CustomerFeed = ...,
        remove: str = ...
    ) -> None: ...

class MutateCustomerFeedResult(proto.Message):
    resource_name: str
    customer_feed: CustomerFeed
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        customer_feed: CustomerFeed = ...
    ) -> None: ...

class MutateCustomerFeedsRequest(proto.Message):
    customer_id: str
    operations: list[CustomerFeedOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CustomerFeedOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCustomerFeedsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateCustomerFeedResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateCustomerFeedResult] = ...
    ) -> None: ...
