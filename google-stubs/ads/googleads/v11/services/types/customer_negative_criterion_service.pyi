from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.customer_negative_criterion import (
    CustomerNegativeCriterion,
)

class CustomerNegativeCriterionOperation(proto.Message):
    create: CustomerNegativeCriterion
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: CustomerNegativeCriterion = ...,
        remove: str = ...
    ) -> None: ...

class MutateCustomerNegativeCriteriaRequest(proto.Message):
    customer_id: str
    operations: list[CustomerNegativeCriterionOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CustomerNegativeCriterionOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCustomerNegativeCriteriaResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateCustomerNegativeCriteriaResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateCustomerNegativeCriteriaResult] = ...
    ) -> None: ...

class MutateCustomerNegativeCriteriaResult(proto.Message):
    resource_name: str
    customer_negative_criterion: CustomerNegativeCriterion
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        customer_negative_criterion: CustomerNegativeCriterion = ...
    ) -> None: ...
