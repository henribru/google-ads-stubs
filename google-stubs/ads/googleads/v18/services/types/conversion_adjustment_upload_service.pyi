import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import offline_user_data
from google.ads.googleads.v18.enums.types import conversion_adjustment_type
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class UploadConversionAdjustmentsRequest(proto.Message):
    customer_id: str
    conversion_adjustments: MutableSequence['ConversionAdjustment']
    partial_failure: bool
    validate_only: bool
    job_id: int

class UploadConversionAdjustmentsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['ConversionAdjustmentResult']
    job_id: int

class ConversionAdjustment(proto.Message):
    gclid_date_time_pair: GclidDateTimePair
    order_id: str
    conversion_action: str
    adjustment_date_time: str
    adjustment_type: conversion_adjustment_type.ConversionAdjustmentTypeEnum.ConversionAdjustmentType
    restatement_value: RestatementValue
    user_identifiers: MutableSequence[offline_user_data.UserIdentifier]
    user_agent: str

class RestatementValue(proto.Message):
    adjusted_value: float
    currency_code: str

class GclidDateTimePair(proto.Message):
    gclid: str
    conversion_date_time: str

class ConversionAdjustmentResult(proto.Message):
    gclid_date_time_pair: GclidDateTimePair
    order_id: str
    conversion_action: str
    adjustment_date_time: str
    adjustment_type: conversion_adjustment_type.ConversionAdjustmentTypeEnum.ConversionAdjustmentType
