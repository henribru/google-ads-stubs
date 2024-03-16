from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.chain_relationship_type import (
    ChainRelationshipTypeEnum,
)
from google.ads.googleads.v16.enums.types.location_ownership_type import (
    LocationOwnershipTypeEnum,
)
from google.ads.googleads.v16.enums.types.location_string_filter_type import (
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
        filter_type: LocationStringFilterTypeEnum.LocationStringFilterType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["business_name", "filter_type"]
    ) -> bool: ...

class BusinessProfileLocationGroup(proto.Message):
    dynamic_business_profile_location_group_filter: (
        DynamicBusinessProfileLocationGroupFilter
    )
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        dynamic_business_profile_location_group_filter: DynamicBusinessProfileLocationGroupFilter = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["dynamic_business_profile_location_group_filter"]
    ) -> bool: ...

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
        business_account_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "http_authorization_token",
            "email_address",
            "business_name_filter",
            "label_filters",
            "listing_id_filters",
            "business_account_id",
        ],
    ) -> bool: ...

class ChainFilter(proto.Message):
    chain_id: int
    location_attributes: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        chain_id: int = ...,
        location_attributes: MutableSequence[str] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["chain_id", "location_attributes"]
    ) -> bool: ...

class ChainLocationGroup(proto.Message):
    dynamic_chain_location_group_filters: MutableSequence[ChainFilter]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        dynamic_chain_location_group_filters: MutableSequence[ChainFilter] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["dynamic_chain_location_group_filters"]
    ) -> bool: ...

class ChainSet(proto.Message):
    relationship_type: ChainRelationshipTypeEnum.ChainRelationshipType
    chains: MutableSequence[ChainFilter]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        relationship_type: ChainRelationshipTypeEnum.ChainRelationshipType = ...,
        chains: MutableSequence[ChainFilter] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["relationship_type", "chains"]
    ) -> bool: ...

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
        listing_id_filters: MutableSequence[int] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal["label_filters", "business_name_filter", "listing_id_filters"],
    ) -> bool: ...

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
        maps_location_set: MapsLocationSet = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "location_ownership_type",
            "business_profile_location_set",
            "chain_location_set",
            "maps_location_set",
        ],
    ) -> bool: ...

class MapsLocationInfo(proto.Message):
    place_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        place_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["place_id"]
    ) -> bool: ...

class MapsLocationSet(proto.Message):
    maps_locations: MutableSequence[MapsLocationInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        maps_locations: MutableSequence[MapsLocationInfo] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["maps_locations"]
    ) -> bool: ...
