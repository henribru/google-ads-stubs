import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class OfflineUserAddressInfo(proto.Message):
    hashed_first_name: Incomplete
    hashed_last_name: Incomplete
    city: Incomplete
    state: Incomplete
    country_code: Incomplete
    postal_code: Incomplete
    hashed_street_address: Incomplete

class UserIdentifier(proto.Message):
    user_identifier_source: Incomplete
    hashed_email: Incomplete
    hashed_phone_number: Incomplete
    mobile_id: Incomplete
    third_party_user_id: Incomplete
    address_info: Incomplete

class TransactionAttribute(proto.Message):
    transaction_date_time: Incomplete
    transaction_amount_micros: Incomplete
    currency_code: Incomplete
    conversion_action: Incomplete
    order_id: Incomplete
    store_attribute: Incomplete
    custom_value: Incomplete
    item_attribute: Incomplete

class StoreAttribute(proto.Message):
    store_code: Incomplete

class ItemAttribute(proto.Message):
    item_id: Incomplete
    merchant_id: Incomplete
    country_code: Incomplete
    language_code: Incomplete
    quantity: Incomplete

class UserData(proto.Message):
    user_identifiers: Incomplete
    transaction_attribute: Incomplete
    user_attribute: Incomplete

class UserAttribute(proto.Message):
    lifetime_value_micros: Incomplete
    lifetime_value_bucket: Incomplete
    last_purchase_date_time: Incomplete
    average_purchase_count: Incomplete
    average_purchase_value_micros: Incomplete
    acquisition_date_time: Incomplete
    shopping_loyalty: Incomplete
    lifecycle_stage: Incomplete
    first_purchase_date_time: Incomplete
    event_attribute: Incomplete

class EventAttribute(proto.Message):
    event: Incomplete
    event_date_time: Incomplete
    item_attribute: Incomplete

class EventItemAttribute(proto.Message):
    item_id: Incomplete

class ShoppingLoyalty(proto.Message):
    loyalty_tier: Incomplete

class CustomerMatchUserListMetadata(proto.Message):
    user_list: Incomplete

class StoreSalesMetadata(proto.Message):
    loyalty_fraction: Incomplete
    transaction_upload_fraction: Incomplete
    custom_key: Incomplete
    third_party_metadata: Incomplete

class StoreSalesThirdPartyMetadata(proto.Message):
    advertiser_upload_date_time: Incomplete
    valid_transaction_fraction: Incomplete
    partner_match_fraction: Incomplete
    partner_upload_fraction: Incomplete
    bridge_map_version_id: Incomplete
    partner_id: Incomplete
