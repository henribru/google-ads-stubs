# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Optional as typing___Optional, Text as typing___Text

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v2.proto.enums.product_bidding_category_level_pb2 import (
    ProductBiddingCategoryLevelEnum as google___ads___googleads___v2___enums___product_bidding_category_level_pb2___ProductBiddingCategoryLevelEnum,
)
from google.ads.google_ads.v2.proto.enums.product_bidding_category_status_pb2 import (
    ProductBiddingCategoryStatusEnum as google___ads___googleads___v2___enums___product_bidding_category_status_pb2___ProductBiddingCategoryStatusEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class ProductBiddingCategoryConstant(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    level: google___ads___googleads___v2___enums___product_bidding_category_level_pb2___ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevelValue = ...
    status: google___ads___googleads___v2___enums___product_bidding_category_status_pb2___ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatusValue = ...
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def country_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_bidding_category_constant_parent(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def language_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def localized_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        country_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_bidding_category_constant_parent: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        level: typing___Optional[
            google___ads___googleads___v2___enums___product_bidding_category_level_pb2___ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevelValue
        ] = None,
        status: typing___Optional[
            google___ads___googleads___v2___enums___product_bidding_category_status_pb2___ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatusValue
        ] = None,
        language_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        localized_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "country_code",
            b"country_code",
            "id",
            b"id",
            "language_code",
            b"language_code",
            "localized_name",
            b"localized_name",
            "product_bidding_category_constant_parent",
            b"product_bidding_category_constant_parent",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "country_code",
            b"country_code",
            "id",
            b"id",
            "language_code",
            b"language_code",
            "level",
            b"level",
            "localized_name",
            b"localized_name",
            "product_bidding_category_constant_parent",
            b"product_bidding_category_constant_parent",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
        ],
    ) -> None: ...

type___ProductBiddingCategoryConstant = ProductBiddingCategoryConstant
