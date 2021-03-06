# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    overload as typing___overload,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v5.proto.enums.google_ads_field_category_pb2 import (
    GoogleAdsFieldCategoryEnum as google___ads___googleads___v5___enums___google_ads_field_category_pb2___GoogleAdsFieldCategoryEnum,
)
from google.ads.google_ads.v5.proto.enums.google_ads_field_data_type_pb2 import (
    GoogleAdsFieldDataTypeEnum as google___ads___googleads___v5___enums___google_ads_field_data_type_pb2___GoogleAdsFieldDataTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class GoogleAdsField(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    name: typing___Text = ...
    category: google___ads___googleads___v5___enums___google_ads_field_category_pb2___GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategoryValue = ...
    selectable: builtin___bool = ...
    filterable: builtin___bool = ...
    sortable: builtin___bool = ...
    selectable_with: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        typing___Text
    ] = ...
    attribute_resources: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        typing___Text
    ] = ...
    metrics: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        typing___Text
    ] = ...
    segments: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        typing___Text
    ] = ...
    enum_values: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        typing___Text
    ] = ...
    data_type: google___ads___googleads___v5___enums___google_ads_field_data_type_pb2___GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue = ...
    type_url: typing___Text = ...
    is_repeated: builtin___bool = ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        name: typing___Optional[typing___Text] = None,
        category: typing___Optional[
            google___ads___googleads___v5___enums___google_ads_field_category_pb2___GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategoryValue
        ] = None,
        selectable: typing___Optional[builtin___bool] = None,
        filterable: typing___Optional[builtin___bool] = None,
        sortable: typing___Optional[builtin___bool] = None,
        selectable_with: typing___Optional[typing___Iterable[typing___Text]] = None,
        attribute_resources: typing___Optional[typing___Iterable[typing___Text]] = None,
        metrics: typing___Optional[typing___Iterable[typing___Text]] = None,
        segments: typing___Optional[typing___Iterable[typing___Text]] = None,
        enum_values: typing___Optional[typing___Iterable[typing___Text]] = None,
        data_type: typing___Optional[
            google___ads___googleads___v5___enums___google_ads_field_data_type_pb2___GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeValue
        ] = None,
        type_url: typing___Optional[typing___Text] = None,
        is_repeated: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_filterable",
            b"_filterable",
            "_is_repeated",
            b"_is_repeated",
            "_name",
            b"_name",
            "_selectable",
            b"_selectable",
            "_sortable",
            b"_sortable",
            "_type_url",
            b"_type_url",
            "filterable",
            b"filterable",
            "is_repeated",
            b"is_repeated",
            "name",
            b"name",
            "selectable",
            b"selectable",
            "sortable",
            b"sortable",
            "type_url",
            b"type_url",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_filterable",
            b"_filterable",
            "_is_repeated",
            b"_is_repeated",
            "_name",
            b"_name",
            "_selectable",
            b"_selectable",
            "_sortable",
            b"_sortable",
            "_type_url",
            b"_type_url",
            "attribute_resources",
            b"attribute_resources",
            "category",
            b"category",
            "data_type",
            b"data_type",
            "enum_values",
            b"enum_values",
            "filterable",
            b"filterable",
            "is_repeated",
            b"is_repeated",
            "metrics",
            b"metrics",
            "name",
            b"name",
            "resource_name",
            b"resource_name",
            "segments",
            b"segments",
            "selectable",
            b"selectable",
            "selectable_with",
            b"selectable_with",
            "sortable",
            b"sortable",
            "type_url",
            b"type_url",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_filterable", b"_filterable"]
    ) -> typing_extensions___Literal["filterable"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_is_repeated", b"_is_repeated"]
    ) -> typing_extensions___Literal["is_repeated"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_name", b"_name"]
    ) -> typing_extensions___Literal["name"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_selectable", b"_selectable"]
    ) -> typing_extensions___Literal["selectable"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_sortable", b"_sortable"]
    ) -> typing_extensions___Literal["sortable"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_type_url", b"_type_url"]
    ) -> typing_extensions___Literal["type_url"]: ...

type___GoogleAdsField = GoogleAdsField
