from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v13.enums.types.access_role import AccessRoleEnum
from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.customer import Customer

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

class ListAccessibleCustomersRequest(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    ...

class ListAccessibleCustomersResponse(proto.Message):
    resource_names: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_names: MutableSequence[str] = ...,
    ) -> None: ...

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

class MutateCustomerResponse(proto.Message):
    result: MutateCustomerResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: MutateCustomerResult = ...,
    ) -> None: ...

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
