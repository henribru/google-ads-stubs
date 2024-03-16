from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.access_role import AccessRoleEnum
from google.ads.googleads.v16.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v16.resources.types.customer import Customer

_M = TypeVar("_M")

class CreateCustomerClientRequest(proto.Message):
    customer_id: str
    customer_client: Customer
    email_address: str
    access_role: AccessRoleEnum.AccessRole
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        customer_client: Customer = ...,
        email_address: str = ...,
        access_role: AccessRoleEnum.AccessRole = ...,
        validate_only: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "customer_client",
            "email_address",
            "access_role",
            "validate_only",
        ],
    ) -> bool: ...

class CreateCustomerClientResponse(proto.Message):
    resource_name: str
    invitation_link: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        invitation_link: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "invitation_link"]
    ) -> bool: ...

class CustomerOperation(proto.Message):
    update: Customer
    update_mask: FieldMask
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update: Customer = ...,
        update_mask: FieldMask = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["update", "update_mask"]
    ) -> bool: ...

class ListAccessibleCustomersRequest(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

class ListAccessibleCustomersResponse(proto.Message):
    resource_names: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_names: MutableSequence[str] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_names"]
    ) -> bool: ...

class MutateCustomerRequest(proto.Message):
    customer_id: str
    operation: CustomerOperation
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operation: CustomerOperation = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id", "operation", "validate_only", "response_content_type"
        ],
    ) -> bool: ...

class MutateCustomerResponse(proto.Message):
    result: MutateCustomerResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: MutateCustomerResult = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["result"]
    ) -> bool: ...

class MutateCustomerResult(proto.Message):
    resource_name: str
    customer: Customer
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        customer: Customer = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "customer"]
    ) -> bool: ...
