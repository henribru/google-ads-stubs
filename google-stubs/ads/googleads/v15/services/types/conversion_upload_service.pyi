from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v15.common.types.consent import Consent
from google.ads.googleads.v15.common.types.offline_user_data import UserIdentifier
from google.ads.googleads.v15.enums.types.conversion_environment_enum import (
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
    consent: Consent
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
        custom_variables: MutableSequence[CustomVariable] = ...,
        consent: Consent = ...
    ) -> None: ...

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
    consent: Consent
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
        conversion_environment: ConversionEnvironmentEnum.ConversionEnvironment = ...,
        consent: Consent = ...
    ) -> None: ...

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

class UploadClickConversionsRequest(proto.Message):
    customer_id: str
    conversions: MutableSequence[ClickConversion]
    partial_failure: bool
    validate_only: bool
    debug_enabled: bool
    job_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        conversions: MutableSequence[ClickConversion] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        debug_enabled: bool = ...,
        job_id: int = ...
    ) -> None: ...

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
