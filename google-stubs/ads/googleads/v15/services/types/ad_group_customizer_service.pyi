from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v15.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v15.resources.types.ad_group_customizer import (
    AdGroupCustomizer,
)

_M = TypeVar("_M")

class AdGroupCustomizerOperation(proto.Message):
    create: AdGroupCustomizer
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: AdGroupCustomizer = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupCustomizerResult(proto.Message):
    resource_name: str
    ad_group_customizer: AdGroupCustomizer
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        ad_group_customizer: AdGroupCustomizer = ...
    ) -> None: ...

class MutateAdGroupCustomizersRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AdGroupCustomizerOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[AdGroupCustomizerOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAdGroupCustomizersResponse(proto.Message):
    results: MutableSequence[MutateAdGroupCustomizerResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateAdGroupCustomizerResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
