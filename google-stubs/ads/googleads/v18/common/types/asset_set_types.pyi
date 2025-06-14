import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import chain_relationship_type, location_ownership_type as gage_location_ownership_type, location_string_filter_type
from typing import MutableSequence

__protobuf__: Incomplete

class LocationSet(proto.Message):
    location_ownership_type: gage_location_ownership_type.LocationOwnershipTypeEnum.LocationOwnershipType
    business_profile_location_set: BusinessProfileLocationSet
    chain_location_set: ChainSet
    maps_location_set: MapsLocationSet

class BusinessProfileLocationSet(proto.Message):
    http_authorization_token: str
    email_address: str
    business_name_filter: str
    label_filters: MutableSequence[str]
    listing_id_filters: MutableSequence[int]
    business_account_id: str

class ChainSet(proto.Message):
    relationship_type: chain_relationship_type.ChainRelationshipTypeEnum.ChainRelationshipType
    chains: MutableSequence['ChainFilter']

class ChainFilter(proto.Message):
    chain_id: int
    location_attributes: MutableSequence[str]

class MapsLocationSet(proto.Message):
    maps_locations: MutableSequence['MapsLocationInfo']

class MapsLocationInfo(proto.Message):
    place_id: str

class BusinessProfileLocationGroup(proto.Message):
    dynamic_business_profile_location_group_filter: DynamicBusinessProfileLocationGroupFilter

class DynamicBusinessProfileLocationGroupFilter(proto.Message):
    label_filters: MutableSequence[str]
    business_name_filter: BusinessProfileBusinessNameFilter
    listing_id_filters: MutableSequence[int]

class BusinessProfileBusinessNameFilter(proto.Message):
    business_name: str
    filter_type: location_string_filter_type.LocationStringFilterTypeEnum.LocationStringFilterType

class ChainLocationGroup(proto.Message):
    dynamic_chain_location_group_filters: MutableSequence['ChainFilter']
