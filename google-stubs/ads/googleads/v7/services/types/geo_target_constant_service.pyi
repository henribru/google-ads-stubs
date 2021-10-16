from typing import Any

import proto

__protobuf__: Any

class GetGeoTargetConstantRequest(proto.Message):
    resource_name: Any

class SuggestGeoTargetConstantsRequest(proto.Message):
    class LocationNames(proto.Message):
        names: Any
    class GeoTargets(proto.Message):
        geo_target_constants: Any
    locale: Any
    country_code: Any
    location_names: Any
    geo_targets: Any

class SuggestGeoTargetConstantsResponse(proto.Message):
    geo_target_constant_suggestions: Any

class GeoTargetConstantSuggestion(proto.Message):
    locale: Any
    reach: Any
    search_term: Any
    geo_target_constant: Any
    geo_target_constant_parents: Any
