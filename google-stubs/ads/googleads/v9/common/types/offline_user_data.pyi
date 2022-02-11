from typing import Any

import proto

__protobuf__: Any

class OfflineUserAddressInfo(proto.Message):
    hashed_first_name: Any
    hashed_last_name: Any
    city: Any
    state: Any
    country_code: Any
    postal_code: Any
    hashed_street_address: Any

class UserIdentifier(proto.Message):
    user_identifier_source: Any
    hashed_email: Any
    hashed_phone_number: Any
    mobile_id: Any
    third_party_user_id: Any
    address_info: Any

class TransactionAttribute(proto.Message):
    transaction_date_time: Any
    transaction_amount_micros: Any
    currency_code: Any
    conversion_action: Any
    order_id: Any
    store_attribute: Any
    custom_value: Any
    item_attribute: Any

class StoreAttribute(proto.Message):
    store_code: Any

class ItemAttribute(proto.Message):
    item_id: Any
    merchant_id: Any
    country_code: Any
    language_code: Any
    quantity: Any

class UserData(proto.Message):
    user_identifiers: Any
    transaction_attribute: Any
    user_attribute: Any

class UserAttribute(proto.Message):
    lifetime_value_micros: Any
    lifetime_value_bucket: Any
    last_purchase_date_time: Any
    average_purchase_count: Any
    average_purchase_value_micros: Any
    acquisition_date_time: Any
    shopping_loyalty: Any

class ShoppingLoyalty(proto.Message):
    loyalty_tier: Any

class CustomerMatchUserListMetadata(proto.Message):
    user_list: Any

class StoreSalesMetadata(proto.Message):
    loyalty_fraction: Any
    transaction_upload_fraction: Any
    custom_key: Any
    third_party_metadata: Any

class StoreSalesThirdPartyMetadata(proto.Message):
    advertiser_upload_date_time: Any
    valid_transaction_fraction: Any
    partner_match_fraction: Any
    partner_upload_fraction: Any
    bridge_map_version_id: Any
    partner_id: Any
