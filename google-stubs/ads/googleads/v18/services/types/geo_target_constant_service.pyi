import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.resources.types import geo_target_constant as gagr_geo_target_constant
from typing import MutableSequence

__protobuf__: Incomplete

class SuggestGeoTargetConstantsRequest(proto.Message):
    class LocationNames(proto.Message):
        names: MutableSequence[str]
    class GeoTargets(proto.Message):
        geo_target_constants: MutableSequence[str]
    locale: str
    country_code: str
    location_names: LocationNames
    geo_targets: GeoTargets

class SuggestGeoTargetConstantsResponse(proto.Message):
    geo_target_constant_suggestions: MutableSequence['GeoTargetConstantSuggestion']

class GeoTargetConstantSuggestion(proto.Message):
    locale: str
    reach: int
    search_term: str
    geo_target_constant: gagr_geo_target_constant.GeoTargetConstant
    geo_target_constant_parents: MutableSequence[gagr_geo_target_constant.GeoTargetConstant]
