import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import conversion_action_category, conversion_origin

__protobuf__: Incomplete

class CustomerConversionGoal(proto.Message):
    resource_name: str
    category: conversion_action_category.ConversionActionCategoryEnum.ConversionActionCategory
    origin: conversion_origin.ConversionOriginEnum.ConversionOrigin
    biddable: bool
