from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.resources.types.geo_target_constant import (
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
        geo_target_constant_parents: MutableSequence[GeoTargetConstant] = ...
    ) -> None: ...

class SuggestGeoTargetConstantsRequest(proto.Message):
    class GeoTargets(proto.Message):
        geo_target_constants: MutableSequence[str]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            geo_target_constants: MutableSequence[str] = ...
        ) -> None: ...

    class LocationNames(proto.Message):
        names: MutableSequence[str]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            names: MutableSequence[str] = ...
        ) -> None: ...
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
        geo_targets: SuggestGeoTargetConstantsRequest.GeoTargets = ...
    ) -> None: ...

class SuggestGeoTargetConstantsResponse(proto.Message):
    geo_target_constant_suggestions: MutableSequence[GeoTargetConstantSuggestion]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        geo_target_constant_suggestions: MutableSequence[
            GeoTargetConstantSuggestion
        ] = ...
    ) -> None: ...
