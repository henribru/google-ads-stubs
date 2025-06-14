import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import consent as gagc_consent, offline_user_data
from google.ads.googleads.v20.enums.types import conversion_customer_type, conversion_environment_enum
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class UploadClickConversionsRequest(proto.Message):
    customer_id: str
    conversions: MutableSequence['ClickConversion']
    partial_failure: bool
    validate_only: bool
    debug_enabled: bool
    job_id: int

class UploadClickConversionsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['ClickConversionResult']
    job_id: int

class UploadCallConversionsRequest(proto.Message):
    customer_id: str
    conversions: MutableSequence['CallConversion']
    partial_failure: bool
    validate_only: bool

class UploadCallConversionsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['CallConversionResult']

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
    custom_variables: MutableSequence['CustomVariable']
    cart_data: CartData
    user_identifiers: MutableSequence[offline_user_data.UserIdentifier]
    conversion_environment: conversion_environment_enum.ConversionEnvironmentEnum.ConversionEnvironment
    consent: gagc_consent.Consent
    customer_type: conversion_customer_type.ConversionCustomerTypeEnum.ConversionCustomerType
    user_ip_address: str
    session_attributes_encoded: bytes
    session_attributes_key_value_pairs: SessionAttributesKeyValuePairs

class CallConversion(proto.Message):
    caller_id: str
    call_start_date_time: str
    conversion_action: str
    conversion_date_time: str
    conversion_value: float
    currency_code: str
    custom_variables: MutableSequence['CustomVariable']
    consent: gagc_consent.Consent

class ExternalAttributionData(proto.Message):
    external_attribution_credit: float
    external_attribution_model: str

class ClickConversionResult(proto.Message):
    gclid: str
    gbraid: str
    wbraid: str
    conversion_action: str
    conversion_date_time: str
    user_identifiers: MutableSequence[offline_user_data.UserIdentifier]

class CallConversionResult(proto.Message):
    caller_id: str
    call_start_date_time: str
    conversion_action: str
    conversion_date_time: str

class CustomVariable(proto.Message):
    conversion_custom_variable: str
    value: str

class CartData(proto.Message):
    class Item(proto.Message):
        product_id: str
        quantity: int
        unit_price: float
    merchant_id: int
    feed_country_code: str
    feed_language_code: str
    local_transaction_cost: float
    items: MutableSequence[Item]

class SessionAttributeKeyValuePair(proto.Message):
    session_attribute_key: str
    session_attribute_value: str

class SessionAttributesKeyValuePairs(proto.Message):
    key_value_pairs: MutableSequence['SessionAttributeKeyValuePair']
