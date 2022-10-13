from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.common.types.offline_user_data import UserIdentifier
from google.ads.googleads.v10.enums.types.conversion_adjustment_type import (
    ConversionAdjustmentTypeEnum,
)

class ConversionAdjustment(proto.Message):
    gclid_date_time_pair: GclidDateTimePair
    order_id: str
    conversion_action: str
    adjustment_date_time: str
    adjustment_type: ConversionAdjustmentTypeEnum.ConversionAdjustmentType
    restatement_value: RestatementValue
    user_identifiers: list[UserIdentifier]
    user_agent: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        gclid_date_time_pair: GclidDateTimePair = ...,
        order_id: str = ...,
        conversion_action: str = ...,
        adjustment_date_time: str = ...,
        adjustment_type: ConversionAdjustmentTypeEnum.ConversionAdjustmentType = ...,
        restatement_value: RestatementValue = ...,
        user_identifiers: list[UserIdentifier] = ...,
        user_agent: str = ...
    ) -> None: ...

class ConversionAdjustmentResult(proto.Message):
    gclid_date_time_pair: GclidDateTimePair
    order_id: str
    conversion_action: str
    adjustment_date_time: str
    adjustment_type: ConversionAdjustmentTypeEnum.ConversionAdjustmentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        gclid_date_time_pair: GclidDateTimePair = ...,
        order_id: str = ...,
        conversion_action: str = ...,
        adjustment_date_time: str = ...,
        adjustment_type: ConversionAdjustmentTypeEnum.ConversionAdjustmentType = ...
    ) -> None: ...

class GclidDateTimePair(proto.Message):
    gclid: str
    conversion_date_time: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        gclid: str = ...,
        conversion_date_time: str = ...
    ) -> None: ...

class RestatementValue(proto.Message):
    adjusted_value: float
    currency_code: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        adjusted_value: float = ...,
        currency_code: str = ...
    ) -> None: ...

class UploadConversionAdjustmentsRequest(proto.Message):
    customer_id: str
    conversion_adjustments: list[ConversionAdjustment]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        conversion_adjustments: list[ConversionAdjustment] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class UploadConversionAdjustmentsResponse(proto.Message):
    partial_failure_error: Status
    results: list[ConversionAdjustmentResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[ConversionAdjustmentResult] = ...
    ) -> None: ...
