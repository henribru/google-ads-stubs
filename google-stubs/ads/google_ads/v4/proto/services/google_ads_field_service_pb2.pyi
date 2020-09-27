# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v4.proto.resources.google_ads_field_pb2 import (
    GoogleAdsField as google___ads___googleads___v4___resources___google_ads_field_pb2___GoogleAdsField,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class GetGoogleAdsFieldRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___GetGoogleAdsFieldRequest = GetGoogleAdsFieldRequest

class SearchGoogleAdsFieldsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    query: typing___Text = ...
    page_token: typing___Text = ...
    page_size: builtin___int = ...
    def __init__(
        self,
        *,
        query: typing___Optional[typing___Text] = None,
        page_token: typing___Optional[typing___Text] = None,
        page_size: typing___Optional[builtin___int] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "page_size", b"page_size", "page_token", b"page_token", "query", b"query"
        ],
    ) -> None: ...

type___SearchGoogleAdsFieldsRequest = SearchGoogleAdsFieldsRequest

class SearchGoogleAdsFieldsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    next_page_token: typing___Text = ...
    total_results_count: builtin___int = ...
    @property
    def results(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___ads___googleads___v4___resources___google_ads_field_pb2___GoogleAdsField
    ]: ...
    def __init__(
        self,
        *,
        results: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v4___resources___google_ads_field_pb2___GoogleAdsField
            ]
        ] = None,
        next_page_token: typing___Optional[typing___Text] = None,
        total_results_count: typing___Optional[builtin___int] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "next_page_token",
            b"next_page_token",
            "results",
            b"results",
            "total_results_count",
            b"total_results_count",
        ],
    ) -> None: ...

type___SearchGoogleAdsFieldsResponse = SearchGoogleAdsFieldsResponse
