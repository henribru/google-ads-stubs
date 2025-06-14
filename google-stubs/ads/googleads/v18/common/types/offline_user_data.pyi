import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import consent as gagc_consent
from google.ads.googleads.v18.enums.types import user_identifier_source as gage_user_identifier_source
from typing import MutableSequence

__protobuf__: Incomplete

class OfflineUserAddressInfo(proto.Message):
    hashed_first_name: str
    hashed_last_name: str
    city: str
    state: str
    country_code: str
    postal_code: str
    hashed_street_address: str

class UserIdentifier(proto.Message):
    user_identifier_source: gage_user_identifier_source.UserIdentifierSourceEnum.UserIdentifierSource
    hashed_email: str
    hashed_phone_number: str
    mobile_id: str
    third_party_user_id: str
    address_info: OfflineUserAddressInfo

class TransactionAttribute(proto.Message):
    transaction_date_time: str
    transaction_amount_micros: float
    currency_code: str
    conversion_action: str
    order_id: str
    store_attribute: StoreAttribute
    custom_value: str
    item_attribute: ItemAttribute

class StoreAttribute(proto.Message):
    store_code: str

class ItemAttribute(proto.Message):
    item_id: str
    merchant_id: int
    country_code: str
    language_code: str
    quantity: int

class UserData(proto.Message):
    user_identifiers: MutableSequence['UserIdentifier']
    transaction_attribute: TransactionAttribute
    user_attribute: UserAttribute
    consent: gagc_consent.Consent

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
    event_attribute: MutableSequence['EventAttribute']

class EventAttribute(proto.Message):
    event: str
    event_date_time: str
    item_attribute: MutableSequence['EventItemAttribute']

class EventItemAttribute(proto.Message):
    item_id: str

class ShoppingLoyalty(proto.Message):
    loyalty_tier: str

class CustomerMatchUserListMetadata(proto.Message):
    user_list: str
    consent: gagc_consent.Consent

class StoreSalesMetadata(proto.Message):
    loyalty_fraction: float
    transaction_upload_fraction: float
    custom_key: str
    third_party_metadata: StoreSalesThirdPartyMetadata

class StoreSalesThirdPartyMetadata(proto.Message):
    advertiser_upload_date_time: str
    valid_transaction_fraction: float
    partner_match_fraction: float
    partner_upload_fraction: float
    bridge_map_version_id: str
    partner_id: int
