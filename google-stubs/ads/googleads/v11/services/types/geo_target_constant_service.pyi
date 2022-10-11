import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class SuggestGeoTargetConstantsRequest(proto.Message):
    class LocationNames(proto.Message):
        names: Incomplete

    class GeoTargets(proto.Message):
        geo_target_constants: Incomplete
    locale: Incomplete
    country_code: Incomplete
    location_names: Incomplete
    geo_targets: Incomplete

class SuggestGeoTargetConstantsResponse(proto.Message):
    geo_target_constant_suggestions: Incomplete

class GeoTargetConstantSuggestion(proto.Message):
    locale: Incomplete
    reach: Incomplete
    search_term: Incomplete
    geo_target_constant: Incomplete
    geo_target_constant_parents: Incomplete
