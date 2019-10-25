# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    cast as typing___cast,
)


class AdGroupErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class AdGroupError(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> AdGroupErrorEnum.AdGroupError: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[AdGroupErrorEnum.AdGroupError]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, AdGroupErrorEnum.AdGroupError]]: ...
        UNSPECIFIED = typing___cast(AdGroupErrorEnum.AdGroupError, 0)
        UNKNOWN = typing___cast(AdGroupErrorEnum.AdGroupError, 1)
        DUPLICATE_ADGROUP_NAME = typing___cast(AdGroupErrorEnum.AdGroupError, 2)
        INVALID_ADGROUP_NAME = typing___cast(AdGroupErrorEnum.AdGroupError, 3)
        ADVERTISER_NOT_ON_CONTENT_NETWORK = typing___cast(AdGroupErrorEnum.AdGroupError, 5)
        BID_TOO_BIG = typing___cast(AdGroupErrorEnum.AdGroupError, 6)
        BID_TYPE_AND_BIDDING_STRATEGY_MISMATCH = typing___cast(AdGroupErrorEnum.AdGroupError, 7)
        MISSING_ADGROUP_NAME = typing___cast(AdGroupErrorEnum.AdGroupError, 8)
        ADGROUP_LABEL_DOES_NOT_EXIST = typing___cast(AdGroupErrorEnum.AdGroupError, 9)
        ADGROUP_LABEL_ALREADY_EXISTS = typing___cast(AdGroupErrorEnum.AdGroupError, 10)
        INVALID_CONTENT_BID_CRITERION_TYPE_GROUP = typing___cast(AdGroupErrorEnum.AdGroupError, 11)
        AD_GROUP_TYPE_NOT_VALID_FOR_ADVERTISING_CHANNEL_TYPE = typing___cast(AdGroupErrorEnum.AdGroupError, 12)
        ADGROUP_TYPE_NOT_SUPPORTED_FOR_CAMPAIGN_SALES_COUNTRY = typing___cast(AdGroupErrorEnum.AdGroupError, 13)
        CANNOT_ADD_ADGROUP_OF_TYPE_DSA_TO_CAMPAIGN_WITHOUT_DSA_SETTING = typing___cast(AdGroupErrorEnum.AdGroupError, 14)
    UNSPECIFIED = typing___cast(AdGroupErrorEnum.AdGroupError, 0)
    UNKNOWN = typing___cast(AdGroupErrorEnum.AdGroupError, 1)
    DUPLICATE_ADGROUP_NAME = typing___cast(AdGroupErrorEnum.AdGroupError, 2)
    INVALID_ADGROUP_NAME = typing___cast(AdGroupErrorEnum.AdGroupError, 3)
    ADVERTISER_NOT_ON_CONTENT_NETWORK = typing___cast(AdGroupErrorEnum.AdGroupError, 5)
    BID_TOO_BIG = typing___cast(AdGroupErrorEnum.AdGroupError, 6)
    BID_TYPE_AND_BIDDING_STRATEGY_MISMATCH = typing___cast(AdGroupErrorEnum.AdGroupError, 7)
    MISSING_ADGROUP_NAME = typing___cast(AdGroupErrorEnum.AdGroupError, 8)
    ADGROUP_LABEL_DOES_NOT_EXIST = typing___cast(AdGroupErrorEnum.AdGroupError, 9)
    ADGROUP_LABEL_ALREADY_EXISTS = typing___cast(AdGroupErrorEnum.AdGroupError, 10)
    INVALID_CONTENT_BID_CRITERION_TYPE_GROUP = typing___cast(AdGroupErrorEnum.AdGroupError, 11)
    AD_GROUP_TYPE_NOT_VALID_FOR_ADVERTISING_CHANNEL_TYPE = typing___cast(AdGroupErrorEnum.AdGroupError, 12)
    ADGROUP_TYPE_NOT_SUPPORTED_FOR_CAMPAIGN_SALES_COUNTRY = typing___cast(AdGroupErrorEnum.AdGroupError, 13)
    CANNOT_ADD_ADGROUP_OF_TYPE_DSA_TO_CAMPAIGN_WITHOUT_DSA_SETTING = typing___cast(AdGroupErrorEnum.AdGroupError, 14)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AdGroupErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
