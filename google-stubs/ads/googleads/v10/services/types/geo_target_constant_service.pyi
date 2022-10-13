from typing import Any

import proto

from google.ads.googleads.v10.resources.types.geo_target_constant import (
    GeoTargetConstant,
)

class GeoTargetConstantSuggestion(proto.Message):
    locale: str
    reach: int
    search_term: str
    geo_target_constant: GeoTargetConstant
    geo_target_constant_parents: list[GeoTargetConstant]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        locale: str = ...,
        reach: int = ...,
        search_term: str = ...,
        geo_target_constant: GeoTargetConstant = ...,
        geo_target_constant_parents: list[GeoTargetConstant] = ...
    ) -> None: ...

class SuggestGeoTargetConstantsRequest(proto.Message):
    class GeoTargets(proto.Message):
        geo_target_constants: list[str]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            geo_target_constants: list[str] = ...
        ) -> None: ...

    class LocationNames(proto.Message):
        names: list[str]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            names: list[str] = ...
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
    geo_target_constant_suggestions: list[GeoTargetConstantSuggestion]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        geo_target_constant_suggestions: list[GeoTargetConstantSuggestion] = ...
    ) -> None: ...
