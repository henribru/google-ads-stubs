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
from google.protobuf.wrappers_pb2 import (
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v5.proto.common.keyword_plan_common_pb2 import (
    KeywordPlanHistoricalMetrics as google___ads___googleads___v5___common___keyword_plan_common_pb2___KeywordPlanHistoricalMetrics,
)
from google.ads.google_ads.v5.proto.enums.keyword_plan_network_pb2 import (
    KeywordPlanNetworkEnum as google___ads___googleads___v5___enums___keyword_plan_network_pb2___KeywordPlanNetworkEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class GenerateKeywordIdeasRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    include_adult_keywords: builtin___bool = ...
    page_token: typing___Text = ...
    page_size: builtin___int = ...
    keyword_plan_network: google___ads___googleads___v5___enums___keyword_plan_network_pb2___KeywordPlanNetworkEnum.KeywordPlanNetworkValue = ...
    @property
    def language(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def geo_target_constants(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    @property
    def keyword_and_url_seed(self) -> type___KeywordAndUrlSeed: ...
    @property
    def keyword_seed(self) -> type___KeywordSeed: ...
    @property
    def url_seed(self) -> type___UrlSeed: ...
    @property
    def site_seed(self) -> type___SiteSeed: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        language: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        geo_target_constants: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
        include_adult_keywords: typing___Optional[builtin___bool] = None,
        page_token: typing___Optional[typing___Text] = None,
        page_size: typing___Optional[builtin___int] = None,
        keyword_plan_network: typing___Optional[
            google___ads___googleads___v5___enums___keyword_plan_network_pb2___KeywordPlanNetworkEnum.KeywordPlanNetworkValue
        ] = None,
        keyword_and_url_seed: typing___Optional[type___KeywordAndUrlSeed] = None,
        keyword_seed: typing___Optional[type___KeywordSeed] = None,
        url_seed: typing___Optional[type___UrlSeed] = None,
        site_seed: typing___Optional[type___SiteSeed] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "keyword_and_url_seed",
            b"keyword_and_url_seed",
            "keyword_seed",
            b"keyword_seed",
            "language",
            b"language",
            "seed",
            b"seed",
            "site_seed",
            b"site_seed",
            "url_seed",
            b"url_seed",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "customer_id",
            b"customer_id",
            "geo_target_constants",
            b"geo_target_constants",
            "include_adult_keywords",
            b"include_adult_keywords",
            "keyword_and_url_seed",
            b"keyword_and_url_seed",
            "keyword_plan_network",
            b"keyword_plan_network",
            "keyword_seed",
            b"keyword_seed",
            "language",
            b"language",
            "page_size",
            b"page_size",
            "page_token",
            b"page_token",
            "seed",
            b"seed",
            "site_seed",
            b"site_seed",
            "url_seed",
            b"url_seed",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["seed", b"seed"]
    ) -> typing_extensions___Literal[
        "keyword_and_url_seed", "keyword_seed", "url_seed", "site_seed"
    ]: ...

type___GenerateKeywordIdeasRequest = GenerateKeywordIdeasRequest

class KeywordAndUrlSeed(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def url(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def keywords(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    def __init__(
        self,
        *,
        url: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        keywords: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["url", b"url"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal["keywords", b"keywords", "url", b"url"],
    ) -> None: ...

type___KeywordAndUrlSeed = KeywordAndUrlSeed

class KeywordSeed(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def keywords(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    def __init__(
        self,
        *,
        keywords: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["keywords", b"keywords"]
    ) -> None: ...

type___KeywordSeed = KeywordSeed

class SiteSeed(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def site(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        site: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["site", b"site"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["site", b"site"]
    ) -> None: ...

type___SiteSeed = SiteSeed

class UrlSeed(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def url(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        url: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["url", b"url"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["url", b"url"]
    ) -> None: ...

type___UrlSeed = UrlSeed

class GenerateKeywordIdeaResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    next_page_token: typing___Text = ...
    total_size: builtin___int = ...
    @property
    def results(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___GenerateKeywordIdeaResult
    ]: ...
    def __init__(
        self,
        *,
        results: typing___Optional[
            typing___Iterable[type___GenerateKeywordIdeaResult]
        ] = None,
        next_page_token: typing___Optional[typing___Text] = None,
        total_size: typing___Optional[builtin___int] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "next_page_token",
            b"next_page_token",
            "results",
            b"results",
            "total_size",
            b"total_size",
        ],
    ) -> None: ...

type___GenerateKeywordIdeaResponse = GenerateKeywordIdeaResponse

class GenerateKeywordIdeaResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def text(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def keyword_idea_metrics(
        self,
    ) -> google___ads___googleads___v5___common___keyword_plan_common_pb2___KeywordPlanHistoricalMetrics: ...
    def __init__(
        self,
        *,
        text: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        keyword_idea_metrics: typing___Optional[
            google___ads___googleads___v5___common___keyword_plan_common_pb2___KeywordPlanHistoricalMetrics
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "keyword_idea_metrics", b"keyword_idea_metrics", "text", b"text"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "keyword_idea_metrics", b"keyword_idea_metrics", "text", b"text"
        ],
    ) -> None: ...

type___GenerateKeywordIdeaResult = GenerateKeywordIdeaResult
