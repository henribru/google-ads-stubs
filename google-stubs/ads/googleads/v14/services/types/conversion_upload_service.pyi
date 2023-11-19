from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.offline_user_data import UserIdentifier
from google.ads.googleads.v14.enums.types.conversion_environment_enum import (
    ConversionEnvironmentEnum,
)

_M = TypeVar("_M")

class CallConversion(proto.Message):
    caller_id: str
    call_start_date_time: str
    conversion_action: str
    conversion_date_time: str
    conversion_value: float
    currency_code: str
    custom_variables: MutableSequence[CustomVariable]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        caller_id: str = ...,
        call_start_date_time: str = ...,
        conversion_action: str = ...,
        conversion_date_time: str = ...,
        conversion_value: float = ...,
        currency_code: str = ...,
        custom_variables: MutableSequence[CustomVariable] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["caller_id", "call_start_date_time", "conversion_action", "conversion_date_time", "conversion_value", "currency_code", "custom_variables"]) -> bool: ...  # type: ignore[override]

class CallConversionResult(proto.Message):
    caller_id: str
    call_start_date_time: str
    conversion_action: str
    conversion_date_time: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        caller_id: str = ...,
        call_start_date_time: str = ...,
        conversion_action: str = ...,
        conversion_date_time: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["caller_id", "call_start_date_time", "conversion_action", "conversion_date_time"]) -> bool: ...  # type: ignore[override]

class CartData(proto.Message):
    class Item(proto.Message):
        product_id: str
        quantity: int
        unit_price: float
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            product_id: str = ...,
            quantity: int = ...,
            unit_price: float = ...
        ) -> None: ...
        def __contains__(self, key: Literal["product_id", "quantity", "unit_price"]) -> bool: ...  # type: ignore[override]
    merchant_id: int
    feed_country_code: str
    feed_language_code: str
    local_transaction_cost: float
    items: MutableSequence[CartData.Item]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        merchant_id: int = ...,
        feed_country_code: str = ...,
        feed_language_code: str = ...,
        local_transaction_cost: float = ...,
        items: MutableSequence[CartData.Item] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["merchant_id", "feed_country_code", "feed_language_code", "local_transaction_cost", "items"]) -> bool: ...  # type: ignore[override]

class ClickConversion(proto.Message):
    gclid: str
    gbraid: str
    wbraid: str
    conversion_action: str
    conversion_date_time: str
    conversion_value: float
    currency_code: str
    order_id: str
    external_attribution_data: ExternalAttributionData
    custom_variables: MutableSequence[CustomVariable]
    cart_data: CartData
    user_identifiers: MutableSequence[UserIdentifier]
    conversion_environment: ConversionEnvironmentEnum.ConversionEnvironment
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        gclid: str = ...,
        gbraid: str = ...,
        wbraid: str = ...,
        conversion_action: str = ...,
        conversion_date_time: str = ...,
        conversion_value: float = ...,
        currency_code: str = ...,
        order_id: str = ...,
        external_attribution_data: ExternalAttributionData = ...,
        custom_variables: MutableSequence[CustomVariable] = ...,
        cart_data: CartData = ...,
        user_identifiers: MutableSequence[UserIdentifier] = ...,
        conversion_environment: ConversionEnvironmentEnum.ConversionEnvironment = ...
    ) -> None: ...
    def __contains__(self, key: Literal["gclid", "gbraid", "wbraid", "conversion_action", "conversion_date_time", "conversion_value", "currency_code", "order_id", "external_attribution_data", "custom_variables", "cart_data", "user_identifiers", "conversion_environment"]) -> bool: ...  # type: ignore[override]

class ClickConversionResult(proto.Message):
    gclid: str
    gbraid: str
    wbraid: str
    conversion_action: str
    conversion_date_time: str
    user_identifiers: MutableSequence[UserIdentifier]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        gclid: str = ...,
        gbraid: str = ...,
        wbraid: str = ...,
        conversion_action: str = ...,
        conversion_date_time: str = ...,
        user_identifiers: MutableSequence[UserIdentifier] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["gclid", "gbraid", "wbraid", "conversion_action", "conversion_date_time", "user_identifiers"]) -> bool: ...  # type: ignore[override]

class CustomVariable(proto.Message):
    conversion_custom_variable: str
    value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        conversion_custom_variable: str = ...,
        value: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["conversion_custom_variable", "value"]) -> bool: ...  # type: ignore[override]

class ExternalAttributionData(proto.Message):
    external_attribution_credit: float
    external_attribution_model: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        external_attribution_credit: float = ...,
        external_attribution_model: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["external_attribution_credit", "external_attribution_model"]) -> bool: ...  # type: ignore[override]

class UploadCallConversionsRequest(proto.Message):
    customer_id: str
    conversions: MutableSequence[CallConversion]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        conversions: MutableSequence[CallConversion] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "conversions", "partial_failure", "validate_only"]) -> bool: ...  # type: ignore[override]

class UploadCallConversionsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[CallConversionResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[CallConversionResult] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["partial_failure_error", "results"]) -> bool: ...  # type: ignore[override]

class UploadClickConversionsRequest(proto.Message):
    customer_id: str
    conversions: MutableSequence[ClickConversion]
    partial_failure: bool
    validate_only: bool
    debug_enabled: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        conversions: MutableSequence[ClickConversion] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        debug_enabled: bool = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "conversions", "partial_failure", "validate_only", "debug_enabled"]) -> bool: ...  # type: ignore[override]

class UploadClickConversionsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[ClickConversionResult]
    job_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[ClickConversionResult] = ...,
        job_id: int = ...
    ) -> None: ...
    def __contains__(self, key: Literal["partial_failure_error", "results", "job_id"]) -> bool: ...  # type: ignore[override]
