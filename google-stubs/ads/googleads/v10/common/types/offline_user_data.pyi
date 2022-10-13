from typing import Any

import proto

from google.ads.googleads.v10.enums.types.user_identifier_source import (
    UserIdentifierSourceEnum,
)

class CustomerMatchUserListMetadata(proto.Message):
    user_list: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        user_list: str = ...
    ) -> None: ...

class ItemAttribute(proto.Message):
    item_id: str
    merchant_id: int
    country_code: str
    language_code: str
    quantity: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        item_id: str = ...,
        merchant_id: int = ...,
        country_code: str = ...,
        language_code: str = ...,
        quantity: int = ...
    ) -> None: ...

class OfflineUserAddressInfo(proto.Message):
    hashed_first_name: str
    hashed_last_name: str
    city: str
    state: str
    country_code: str
    postal_code: str
    hashed_street_address: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        hashed_first_name: str = ...,
        hashed_last_name: str = ...,
        city: str = ...,
        state: str = ...,
        country_code: str = ...,
        postal_code: str = ...,
        hashed_street_address: str = ...
    ) -> None: ...

class ShoppingLoyalty(proto.Message):
    loyalty_tier: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        loyalty_tier: str = ...
    ) -> None: ...

class StoreAttribute(proto.Message):
    store_code: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        store_code: str = ...
    ) -> None: ...

class StoreSalesMetadata(proto.Message):
    loyalty_fraction: float
    transaction_upload_fraction: float
    custom_key: str
    third_party_metadata: StoreSalesThirdPartyMetadata
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        loyalty_fraction: float = ...,
        transaction_upload_fraction: float = ...,
        custom_key: str = ...,
        third_party_metadata: StoreSalesThirdPartyMetadata = ...
    ) -> None: ...

class StoreSalesThirdPartyMetadata(proto.Message):
    advertiser_upload_date_time: str
    valid_transaction_fraction: float
    partner_match_fraction: float
    partner_upload_fraction: float
    bridge_map_version_id: str
    partner_id: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        advertiser_upload_date_time: str = ...,
        valid_transaction_fraction: float = ...,
        partner_match_fraction: float = ...,
        partner_upload_fraction: float = ...,
        bridge_map_version_id: str = ...,
        partner_id: int = ...
    ) -> None: ...

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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        transaction_date_time: str = ...,
        transaction_amount_micros: float = ...,
        currency_code: str = ...,
        conversion_action: str = ...,
        order_id: str = ...,
        store_attribute: StoreAttribute = ...,
        custom_value: str = ...,
        item_attribute: ItemAttribute = ...
    ) -> None: ...

class UserAttribute(proto.Message):
    lifetime_value_micros: int
    lifetime_value_bucket: int
    last_purchase_date_time: str
    average_purchase_count: int
    average_purchase_value_micros: int
    acquisition_date_time: str
    shopping_loyalty: ShoppingLoyalty
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        lifetime_value_micros: int = ...,
        lifetime_value_bucket: int = ...,
        last_purchase_date_time: str = ...,
        average_purchase_count: int = ...,
        average_purchase_value_micros: int = ...,
        acquisition_date_time: str = ...,
        shopping_loyalty: ShoppingLoyalty = ...
    ) -> None: ...

class UserData(proto.Message):
    user_identifiers: list[UserIdentifier]
    transaction_attribute: TransactionAttribute
    user_attribute: UserAttribute
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        user_identifiers: list[UserIdentifier] = ...,
        transaction_attribute: TransactionAttribute = ...,
        user_attribute: UserAttribute = ...
    ) -> None: ...

class UserIdentifier(proto.Message):
    user_identifier_source: UserIdentifierSourceEnum.UserIdentifierSource
    hashed_email: str
    hashed_phone_number: str
    mobile_id: str
    third_party_user_id: str
    address_info: OfflineUserAddressInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        user_identifier_source: UserIdentifierSourceEnum.UserIdentifierSource = ...,
        hashed_email: str = ...,
        hashed_phone_number: str = ...,
        mobile_id: str = ...,
        third_party_user_id: str = ...,
        address_info: OfflineUserAddressInfo = ...
    ) -> None: ...
