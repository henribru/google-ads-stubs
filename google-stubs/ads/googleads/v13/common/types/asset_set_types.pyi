from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v13.enums.types.chain_relationship_type import (
    ChainRelationshipTypeEnum,
)
from google.ads.googleads.v13.enums.types.location_ownership_type import (
    LocationOwnershipTypeEnum,
)
from google.ads.googleads.v13.enums.types.location_string_filter_type import (
    LocationStringFilterTypeEnum,
)

class BusinessProfileBusinessNameFilter(proto.Message):
    business_name: str
    filter_type: LocationStringFilterTypeEnum.LocationStringFilterType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        business_name: str = ...,
        filter_type: LocationStringFilterTypeEnum.LocationStringFilterType = ...
    ) -> None: ...

class BusinessProfileLocationGroup(proto.Message):
    dynamic_business_profile_location_group_filter: DynamicBusinessProfileLocationGroupFilter
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        dynamic_business_profile_location_group_filter: DynamicBusinessProfileLocationGroupFilter = ...
    ) -> None: ...

class BusinessProfileLocationSet(proto.Message):
    http_authorization_token: str
    email_address: str
    business_name_filter: str
    label_filters: MutableSequence[str]
    listing_id_filters: MutableSequence[int]
    business_account_id: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        http_authorization_token: str = ...,
        email_address: str = ...,
        business_name_filter: str = ...,
        label_filters: MutableSequence[str] = ...,
        listing_id_filters: MutableSequence[int] = ...,
        business_account_id: str = ...
    ) -> None: ...

class ChainFilter(proto.Message):
    chain_id: int
    location_attributes: MutableSequence[str]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        chain_id: int = ...,
        location_attributes: MutableSequence[str] = ...
    ) -> None: ...

class ChainLocationGroup(proto.Message):
    dynamic_chain_location_group_filters: MutableSequence[ChainFilter]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        dynamic_chain_location_group_filters: MutableSequence[ChainFilter] = ...
    ) -> None: ...

class ChainSet(proto.Message):
    relationship_type: ChainRelationshipTypeEnum.ChainRelationshipType
    chains: MutableSequence[ChainFilter]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        relationship_type: ChainRelationshipTypeEnum.ChainRelationshipType = ...,
        chains: MutableSequence[ChainFilter] = ...
    ) -> None: ...

class DynamicBusinessProfileLocationGroupFilter(proto.Message):
    label_filters: MutableSequence[str]
    business_name_filter: BusinessProfileBusinessNameFilter
    listing_id_filters: MutableSequence[int]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        label_filters: MutableSequence[str] = ...,
        business_name_filter: BusinessProfileBusinessNameFilter = ...,
        listing_id_filters: MutableSequence[int] = ...
    ) -> None: ...

class LocationSet(proto.Message):
    location_ownership_type: LocationOwnershipTypeEnum.LocationOwnershipType
    business_profile_location_set: BusinessProfileLocationSet
    chain_location_set: ChainSet
    maps_location_set: MapsLocationSet
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        location_ownership_type: LocationOwnershipTypeEnum.LocationOwnershipType = ...,
        business_profile_location_set: BusinessProfileLocationSet = ...,
        chain_location_set: ChainSet = ...,
        maps_location_set: MapsLocationSet = ...
    ) -> None: ...

class MapsLocationInfo(proto.Message):
    place_id: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        place_id: str = ...
    ) -> None: ...

class MapsLocationSet(proto.Message):
    maps_locations: MutableSequence[MapsLocationInfo]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        maps_locations: MutableSequence[MapsLocationInfo] = ...
    ) -> None: ...
