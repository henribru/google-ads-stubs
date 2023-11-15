from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.chain_relationship_type import (
    ChainRelationshipTypeEnum,
)
from google.ads.googleads.v15.enums.types.location_ownership_type import (
    LocationOwnershipTypeEnum,
)
from google.ads.googleads.v15.enums.types.location_string_filter_type import (
    LocationStringFilterTypeEnum,
)

_M = TypeVar("_M")

class BusinessProfileBusinessNameFilter(proto.Message):
    business_name: str
    filter_type: LocationStringFilterTypeEnum.LocationStringFilterType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        business_name: str = ...,
        filter_type: LocationStringFilterTypeEnum.LocationStringFilterType = ...
    ) -> None: ...

class BusinessProfileLocationGroup(proto.Message):
    dynamic_business_profile_location_group_filter: DynamicBusinessProfileLocationGroupFilter
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        chain_id: int = ...,
        location_attributes: MutableSequence[str] = ...
    ) -> None: ...

class ChainLocationGroup(proto.Message):
    dynamic_chain_location_group_filters: MutableSequence[ChainFilter]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        dynamic_chain_location_group_filters: MutableSequence[ChainFilter] = ...
    ) -> None: ...

class ChainSet(proto.Message):
    relationship_type: ChainRelationshipTypeEnum.ChainRelationshipType
    chains: MutableSequence[ChainFilter]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        relationship_type: ChainRelationshipTypeEnum.ChainRelationshipType = ...,
        chains: MutableSequence[ChainFilter] = ...
    ) -> None: ...

class DynamicBusinessProfileLocationGroupFilter(proto.Message):
    label_filters: MutableSequence[str]
    business_name_filter: BusinessProfileBusinessNameFilter
    listing_id_filters: MutableSequence[int]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        location_ownership_type: LocationOwnershipTypeEnum.LocationOwnershipType = ...,
        business_profile_location_set: BusinessProfileLocationSet = ...,
        chain_location_set: ChainSet = ...,
        maps_location_set: MapsLocationSet = ...
    ) -> None: ...

class MapsLocationInfo(proto.Message):
    place_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        place_id: str = ...
    ) -> None: ...

class MapsLocationSet(proto.Message):
    maps_locations: MutableSequence[MapsLocationInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        maps_locations: MutableSequence[MapsLocationInfo] = ...
    ) -> None: ...
