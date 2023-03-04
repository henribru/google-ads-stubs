from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v12.resources.types.geo_target_constant import (
    GeoTargetConstant,
)

class GeoTargetConstantSuggestion(proto.Message):
    locale: str
    reach: int
    search_term: str
    geo_target_constant: GeoTargetConstant
    geo_target_constant_parents: MutableSequence[GeoTargetConstant]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            geo_target_constants: MutableSequence[str] = ...
        ) -> None: ...

    class LocationNames(proto.Message):
        names: MutableSequence[str]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            names: MutableSequence[str] = ...
        ) -> None: ...
    locale: str
    country_code: str
    location_names: SuggestGeoTargetConstantsRequest.LocationNames
    geo_targets: SuggestGeoTargetConstantsRequest.GeoTargets
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        locale: str = ...,
        country_code: str = ...,
        location_names: SuggestGeoTargetConstantsRequest.LocationNames = ...,
        geo_targets: SuggestGeoTargetConstantsRequest.GeoTargets = ...
    ) -> None: ...

class SuggestGeoTargetConstantsResponse(proto.Message):
    geo_target_constant_suggestions: MutableSequence[GeoTargetConstantSuggestion]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        geo_target_constant_suggestions: MutableSequence[
            GeoTargetConstantSuggestion
        ] = ...
    ) -> None: ...
