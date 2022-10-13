from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.bidding_data_exclusion import (
    BiddingDataExclusion,
)

class BiddingDataExclusionOperation(proto.Message):
    update_mask: FieldMask
    create: BiddingDataExclusion
    update: BiddingDataExclusion
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: BiddingDataExclusion = ...,
        update: BiddingDataExclusion = ...,
        remove: str = ...
    ) -> None: ...

class MutateBiddingDataExclusionsRequest(proto.Message):
    customer_id: str
    operations: list[BiddingDataExclusionOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[BiddingDataExclusionOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateBiddingDataExclusionsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateBiddingDataExclusionsResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateBiddingDataExclusionsResult] = ...
    ) -> None: ...

class MutateBiddingDataExclusionsResult(proto.Message):
    resource_name: str
    bidding_data_exclusion: BiddingDataExclusion
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        bidding_data_exclusion: BiddingDataExclusion = ...
    ) -> None: ...
