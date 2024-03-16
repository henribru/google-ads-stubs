from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.user_identifier_source import (
    UserIdentifierSourceEnum,
)

_M = TypeVar("_M")

class CustomerMatchUserListMetadata(proto.Message):
    user_list: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_list: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["user_list"]
    ) -> bool: ...

class EventAttribute(proto.Message):
    event: str
    event_date_time: str
    item_attribute: MutableSequence[EventItemAttribute]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        event: str = ...,
        event_date_time: str = ...,
        item_attribute: MutableSequence[EventItemAttribute] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["event", "event_date_time", "item_attribute"]
    ) -> bool: ...

class EventItemAttribute(proto.Message):
    item_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        item_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["item_id"]
    ) -> bool: ...

class ItemAttribute(proto.Message):
    item_id: str
    merchant_id: int
    country_code: str
    language_code: str
    quantity: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        item_id: str = ...,
        merchant_id: int = ...,
        country_code: str = ...,
        language_code: str = ...,
        quantity: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "item_id", "merchant_id", "country_code", "language_code", "quantity"
        ],
    ) -> bool: ...

class OfflineUserAddressInfo(proto.Message):
    hashed_first_name: str
    hashed_last_name: str
    city: str
    state: str
    country_code: str
    postal_code: str
    hashed_street_address: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        hashed_first_name: str = ...,
        hashed_last_name: str = ...,
        city: str = ...,
        state: str = ...,
        country_code: str = ...,
        postal_code: str = ...,
        hashed_street_address: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "hashed_first_name",
            "hashed_last_name",
            "city",
            "state",
            "country_code",
            "postal_code",
            "hashed_street_address",
        ],
    ) -> bool: ...

class ShoppingLoyalty(proto.Message):
    loyalty_tier: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        loyalty_tier: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["loyalty_tier"]
    ) -> bool: ...

class StoreAttribute(proto.Message):
    store_code: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        store_code: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["store_code"]
    ) -> bool: ...

class StoreSalesMetadata(proto.Message):
    loyalty_fraction: float
    transaction_upload_fraction: float
    custom_key: str
    third_party_metadata: StoreSalesThirdPartyMetadata
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        loyalty_fraction: float = ...,
        transaction_upload_fraction: float = ...,
        custom_key: str = ...,
        third_party_metadata: StoreSalesThirdPartyMetadata = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "loyalty_fraction",
            "transaction_upload_fraction",
            "custom_key",
            "third_party_metadata",
        ],
    ) -> bool: ...

class StoreSalesThirdPartyMetadata(proto.Message):
    advertiser_upload_date_time: str
    valid_transaction_fraction: float
    partner_match_fraction: float
    partner_upload_fraction: float
    bridge_map_version_id: str
    partner_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        advertiser_upload_date_time: str = ...,
        valid_transaction_fraction: float = ...,
        partner_match_fraction: float = ...,
        partner_upload_fraction: float = ...,
        bridge_map_version_id: str = ...,
        partner_id: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "advertiser_upload_date_time",
            "valid_transaction_fraction",
            "partner_match_fraction",
            "partner_upload_fraction",
            "bridge_map_version_id",
            "partner_id",
        ],
    ) -> bool: ...

class TransactionAttribute(proto.Message):
    transaction_date_time: str
    transaction_amount_micros: float
    currency_code: str
    conversion_action: str
    order_id: str
    store_attribute: StoreAttribute
    custom_value: str
    item_attribute: ItemAttribute
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        transaction_date_time: str = ...,
        transaction_amount_micros: float = ...,
        currency_code: str = ...,
        conversion_action: str = ...,
        order_id: str = ...,
        store_attribute: StoreAttribute = ...,
        custom_value: str = ...,
        item_attribute: ItemAttribute = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "transaction_date_time",
            "transaction_amount_micros",
            "currency_code",
            "conversion_action",
            "order_id",
            "store_attribute",
            "custom_value",
            "item_attribute",
        ],
    ) -> bool: ...

class UserAttribute(proto.Message):
    lifetime_value_micros: int
    lifetime_value_bucket: int
    last_purchase_date_time: str
    average_purchase_count: int
    average_purchase_value_micros: int
    acquisition_date_time: str
    shopping_loyalty: ShoppingLoyalty
    lifecycle_stage: str
    first_purchase_date_time: str
    event_attribute: MutableSequence[EventAttribute]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        lifetime_value_micros: int = ...,
        lifetime_value_bucket: int = ...,
        last_purchase_date_time: str = ...,
        average_purchase_count: int = ...,
        average_purchase_value_micros: int = ...,
        acquisition_date_time: str = ...,
        shopping_loyalty: ShoppingLoyalty = ...,
        lifecycle_stage: str = ...,
        first_purchase_date_time: str = ...,
        event_attribute: MutableSequence[EventAttribute] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "lifetime_value_micros",
            "lifetime_value_bucket",
            "last_purchase_date_time",
            "average_purchase_count",
            "average_purchase_value_micros",
            "acquisition_date_time",
            "shopping_loyalty",
            "lifecycle_stage",
            "first_purchase_date_time",
            "event_attribute",
        ],
    ) -> bool: ...

class UserData(proto.Message):
    user_identifiers: MutableSequence[UserIdentifier]
    transaction_attribute: TransactionAttribute
    user_attribute: UserAttribute
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_identifiers: MutableSequence[UserIdentifier] = ...,
        transaction_attribute: TransactionAttribute = ...,
        user_attribute: UserAttribute = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal["user_identifiers", "transaction_attribute", "user_attribute"],
    ) -> bool: ...

class UserIdentifier(proto.Message):
    user_identifier_source: UserIdentifierSourceEnum.UserIdentifierSource
    hashed_email: str
    hashed_phone_number: str
    mobile_id: str
    third_party_user_id: str
    address_info: OfflineUserAddressInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_identifier_source: UserIdentifierSourceEnum.UserIdentifierSource = ...,
        hashed_email: str = ...,
        hashed_phone_number: str = ...,
        mobile_id: str = ...,
        third_party_user_id: str = ...,
        address_info: OfflineUserAddressInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "user_identifier_source",
            "hashed_email",
            "hashed_phone_number",
            "mobile_id",
            "third_party_user_id",
            "address_info",
        ],
    ) -> bool: ...
