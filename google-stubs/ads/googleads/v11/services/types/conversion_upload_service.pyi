from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.common.types.offline_user_data import UserIdentifier
from google.ads.googleads.v11.enums.types.conversion_environment_enum import (
    ConversionEnvironmentEnum,
)

class CallConversion(proto.Message):
    caller_id: str
    call_start_date_time: str
    conversion_action: str
    conversion_date_time: str
    conversion_value: float
    currency_code: str
    custom_variables: list[CustomVariable]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        caller_id: str = ...,
        call_start_date_time: str = ...,
        conversion_action: str = ...,
        conversion_date_time: str = ...,
        conversion_value: float = ...,
        currency_code: str = ...,
        custom_variables: list[CustomVariable] = ...
    ) -> None: ...

class CallConversionResult(proto.Message):
    caller_id: str
    call_start_date_time: str
    conversion_action: str
    conversion_date_time: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            product_id: str = ...,
            quantity: int = ...,
            unit_price: float = ...
        ) -> None: ...
    merchant_id: int
    feed_country_code: str
    feed_language_code: str
    local_transaction_cost: float
    items: list[CartData.Item]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        merchant_id: int = ...,
        feed_country_code: str = ...,
        feed_language_code: str = ...,
        local_transaction_cost: float = ...,
        items: list[CartData.Item] = ...
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
    custom_variables: list[CustomVariable]
    cart_data: CartData
    user_identifiers: list[UserIdentifier]
    conversion_environment: ConversionEnvironmentEnum.ConversionEnvironment
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        gclid: str = ...,
        gbraid: str = ...,
        wbraid: str = ...,
        conversion_action: str = ...,
        conversion_date_time: str = ...,
        conversion_value: float = ...,
        currency_code: str = ...,
        order_id: str = ...,
        external_attribution_data: ExternalAttributionData = ...,
        custom_variables: list[CustomVariable] = ...,
        cart_data: CartData = ...,
        user_identifiers: list[UserIdentifier] = ...,
        conversion_environment: ConversionEnvironmentEnum.ConversionEnvironment = ...
    ) -> None: ...

class ClickConversionResult(proto.Message):
    gclid: str
    gbraid: str
    wbraid: str
    conversion_action: str
    conversion_date_time: str
    user_identifiers: list[UserIdentifier]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        gclid: str = ...,
        gbraid: str = ...,
        wbraid: str = ...,
        conversion_action: str = ...,
        conversion_date_time: str = ...,
        user_identifiers: list[UserIdentifier] = ...
    ) -> None: ...

class CustomVariable(proto.Message):
    conversion_custom_variable: str
    value: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        conversion_custom_variable: str = ...,
        value: str = ...
    ) -> None: ...

class ExternalAttributionData(proto.Message):
    external_attribution_credit: float
    external_attribution_model: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        external_attribution_credit: float = ...,
        external_attribution_model: str = ...
    ) -> None: ...

class UploadCallConversionsRequest(proto.Message):
    customer_id: str
    conversions: list[CallConversion]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        conversions: list[CallConversion] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class UploadCallConversionsResponse(proto.Message):
    partial_failure_error: Status
    results: list[CallConversionResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[CallConversionResult] = ...
    ) -> None: ...

class UploadClickConversionsRequest(proto.Message):
    customer_id: str
    conversions: list[ClickConversion]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        conversions: list[ClickConversion] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class UploadClickConversionsResponse(proto.Message):
    partial_failure_error: Status
    results: list[ClickConversionResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[ClickConversionResult] = ...
    ) -> None: ...
