# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import NewType as typing___NewType, cast as typing___cast

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)
from google.protobuf.message import Message as google___protobuf___message___Message

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class SearchEngineResultsPageTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    SearchEngineResultsPageTypeValue = typing___NewType(
        "SearchEngineResultsPageTypeValue", builtin___int
    )
    type___SearchEngineResultsPageTypeValue = SearchEngineResultsPageTypeValue
    SearchEngineResultsPageType: _SearchEngineResultsPageType
    class _SearchEngineResultsPageType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            SearchEngineResultsPageTypeEnum.SearchEngineResultsPageTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            SearchEngineResultsPageTypeEnum.SearchEngineResultsPageTypeValue, 0
        )
        UNKNOWN = typing___cast(
            SearchEngineResultsPageTypeEnum.SearchEngineResultsPageTypeValue, 1
        )
        ADS_ONLY = typing___cast(
            SearchEngineResultsPageTypeEnum.SearchEngineResultsPageTypeValue, 2
        )
        ORGANIC_ONLY = typing___cast(
            SearchEngineResultsPageTypeEnum.SearchEngineResultsPageTypeValue, 3
        )
        ADS_AND_ORGANIC = typing___cast(
            SearchEngineResultsPageTypeEnum.SearchEngineResultsPageTypeValue, 4
        )
    UNSPECIFIED = typing___cast(
        SearchEngineResultsPageTypeEnum.SearchEngineResultsPageTypeValue, 0
    )
    UNKNOWN = typing___cast(
        SearchEngineResultsPageTypeEnum.SearchEngineResultsPageTypeValue, 1
    )
    ADS_ONLY = typing___cast(
        SearchEngineResultsPageTypeEnum.SearchEngineResultsPageTypeValue, 2
    )
    ORGANIC_ONLY = typing___cast(
        SearchEngineResultsPageTypeEnum.SearchEngineResultsPageTypeValue, 3
    )
    ADS_AND_ORGANIC = typing___cast(
        SearchEngineResultsPageTypeEnum.SearchEngineResultsPageTypeValue, 4
    )
    type___SearchEngineResultsPageType = SearchEngineResultsPageType
    def __init__(self,) -> None: ...

type___SearchEngineResultsPageTypeEnum = SearchEngineResultsPageTypeEnum
