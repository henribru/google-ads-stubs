from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.resources.types.geo_target_constant import (
    GeoTargetConstant,
)

_M = TypeVar("_M")

class GeoTargetConstantSuggestion(proto.Message):
    locale: str
    reach: int
    search_term: str
    geo_target_constant: GeoTargetConstant
    geo_target_constant_parents: MutableSequence[GeoTargetConstant]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        locale: str = ...,
        reach: int = ...,
        search_term: str = ...,
        geo_target_constant: GeoTargetConstant = ...,
        geo_target_constant_parents: MutableSequence[GeoTargetConstant] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "locale",
            "reach",
            "search_term",
            "geo_target_constant",
            "geo_target_constant_parents",
        ],
    ) -> bool: ...

class SuggestGeoTargetConstantsRequest(proto.Message):
    class GeoTargets(proto.Message):
        geo_target_constants: MutableSequence[str]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            geo_target_constants: MutableSequence[str] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["geo_target_constants"]
        ) -> bool: ...

    class LocationNames(proto.Message):
        names: MutableSequence[str]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            names: MutableSequence[str] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["names"]
        ) -> bool: ...

    locale: str
    country_code: str
    location_names: SuggestGeoTargetConstantsRequest.LocationNames
    geo_targets: SuggestGeoTargetConstantsRequest.GeoTargets
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        locale: str = ...,
        country_code: str = ...,
        location_names: SuggestGeoTargetConstantsRequest.LocationNames = ...,
        geo_targets: SuggestGeoTargetConstantsRequest.GeoTargets = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["locale", "country_code", "location_names", "geo_targets"]
    ) -> bool: ...

class SuggestGeoTargetConstantsResponse(proto.Message):
    geo_target_constant_suggestions: MutableSequence[GeoTargetConstantSuggestion]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        geo_target_constant_suggestions: MutableSequence[
            GeoTargetConstantSuggestion
        ] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["geo_target_constant_suggestions"]
    ) -> bool: ...
