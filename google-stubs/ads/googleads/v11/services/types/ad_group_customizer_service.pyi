from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.ad_group_customizer import (
    AdGroupCustomizer,
)

class AdGroupCustomizerOperation(proto.Message):
    create: AdGroupCustomizer
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: AdGroupCustomizer = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupCustomizerResult(proto.Message):
    resource_name: str
    ad_group_customizer: AdGroupCustomizer
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_customizer: AdGroupCustomizer = ...
    ) -> None: ...

class MutateAdGroupCustomizersRequest(proto.Message):
    customer_id: str
    operations: list[AdGroupCustomizerOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AdGroupCustomizerOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAdGroupCustomizersResponse(proto.Message):
    results: list[MutateAdGroupCustomizerResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateAdGroupCustomizerResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
