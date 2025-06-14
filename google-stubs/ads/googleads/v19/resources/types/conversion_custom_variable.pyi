import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import conversion_custom_variable_status

__protobuf__: Incomplete

class ConversionCustomVariable(proto.Message):
    resource_name: str
    id: int
    name: str
    tag: str
    status: conversion_custom_variable_status.ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus
    owner_customer: str
