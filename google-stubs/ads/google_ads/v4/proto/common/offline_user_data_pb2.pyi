"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class OfflineUserAddressInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HASHED_FIRST_NAME_FIELD_NUMBER: builtins.int
    HASHED_LAST_NAME_FIELD_NUMBER: builtins.int
    CITY_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    COUNTRY_CODE_FIELD_NUMBER: builtins.int
    POSTAL_CODE_FIELD_NUMBER: builtins.int
    @property
    def hashed_first_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def hashed_last_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def city(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def state(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def country_code(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def postal_code(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        hashed_first_name: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        hashed_last_name: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        city: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        state: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        country_code: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        postal_code: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "city",
            b"city",
            "country_code",
            b"country_code",
            "hashed_first_name",
            b"hashed_first_name",
            "hashed_last_name",
            b"hashed_last_name",
            "postal_code",
            b"postal_code",
            "state",
            b"state",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "city",
            b"city",
            "country_code",
            b"country_code",
            "hashed_first_name",
            b"hashed_first_name",
            "hashed_last_name",
            b"hashed_last_name",
            "postal_code",
            b"postal_code",
            "state",
            b"state",
        ],
    ) -> None: ...

global___OfflineUserAddressInfo = OfflineUserAddressInfo

class UserIdentifier(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HASHED_EMAIL_FIELD_NUMBER: builtins.int
    HASHED_PHONE_NUMBER_FIELD_NUMBER: builtins.int
    MOBILE_ID_FIELD_NUMBER: builtins.int
    THIRD_PARTY_USER_ID_FIELD_NUMBER: builtins.int
    ADDRESS_INFO_FIELD_NUMBER: builtins.int
    @property
    def hashed_email(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def hashed_phone_number(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def mobile_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def third_party_user_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def address_info(self) -> global___OfflineUserAddressInfo: ...
    def __init__(
        self,
        *,
        hashed_email: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        hashed_phone_number: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        mobile_id: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        third_party_user_id: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        address_info: typing.Optional[global___OfflineUserAddressInfo] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "address_info",
            b"address_info",
            "hashed_email",
            b"hashed_email",
            "hashed_phone_number",
            b"hashed_phone_number",
            "identifier",
            b"identifier",
            "mobile_id",
            b"mobile_id",
            "third_party_user_id",
            b"third_party_user_id",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "address_info",
            b"address_info",
            "hashed_email",
            b"hashed_email",
            "hashed_phone_number",
            b"hashed_phone_number",
            "identifier",
            b"identifier",
            "mobile_id",
            b"mobile_id",
            "third_party_user_id",
            b"third_party_user_id",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["identifier", b"identifier"]
    ) -> typing_extensions.Literal[
        "hashed_email",
        "hashed_phone_number",
        "mobile_id",
        "third_party_user_id",
        "address_info",
    ]: ...

global___UserIdentifier = UserIdentifier

class TransactionAttribute(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TRANSACTION_DATE_TIME_FIELD_NUMBER: builtins.int
    TRANSACTION_AMOUNT_MICROS_FIELD_NUMBER: builtins.int
    CURRENCY_CODE_FIELD_NUMBER: builtins.int
    CONVERSION_ACTION_FIELD_NUMBER: builtins.int
    ORDER_ID_FIELD_NUMBER: builtins.int
    STORE_ATTRIBUTE_FIELD_NUMBER: builtins.int
    CUSTOM_VALUE_FIELD_NUMBER: builtins.int
    @property
    def transaction_date_time(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def transaction_amount_micros(self) -> google.protobuf.wrappers_pb2.DoubleValue: ...
    @property
    def currency_code(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def conversion_action(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def order_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def store_attribute(self) -> global___StoreAttribute: ...
    @property
    def custom_value(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        transaction_date_time: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        transaction_amount_micros: typing.Optional[
            google.protobuf.wrappers_pb2.DoubleValue
        ] = ...,
        currency_code: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        conversion_action: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        order_id: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        store_attribute: typing.Optional[global___StoreAttribute] = ...,
        custom_value: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "conversion_action",
            b"conversion_action",
            "currency_code",
            b"currency_code",
            "custom_value",
            b"custom_value",
            "order_id",
            b"order_id",
            "store_attribute",
            b"store_attribute",
            "transaction_amount_micros",
            b"transaction_amount_micros",
            "transaction_date_time",
            b"transaction_date_time",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "conversion_action",
            b"conversion_action",
            "currency_code",
            b"currency_code",
            "custom_value",
            b"custom_value",
            "order_id",
            b"order_id",
            "store_attribute",
            b"store_attribute",
            "transaction_amount_micros",
            b"transaction_amount_micros",
            "transaction_date_time",
            b"transaction_date_time",
        ],
    ) -> None: ...

global___TransactionAttribute = TransactionAttribute

class StoreAttribute(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    STORE_CODE_FIELD_NUMBER: builtins.int
    @property
    def store_code(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        store_code: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["store_code", b"store_code"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["store_code", b"store_code"]
    ) -> None: ...

global___StoreAttribute = StoreAttribute

class UserData(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USER_IDENTIFIERS_FIELD_NUMBER: builtins.int
    TRANSACTION_ATTRIBUTE_FIELD_NUMBER: builtins.int
    @property
    def user_identifiers(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___UserIdentifier
    ]: ...
    @property
    def transaction_attribute(self) -> global___TransactionAttribute: ...
    def __init__(
        self,
        *,
        user_identifiers: typing.Optional[
            typing.Iterable[global___UserIdentifier]
        ] = ...,
        transaction_attribute: typing.Optional[global___TransactionAttribute] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "transaction_attribute", b"transaction_attribute"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "transaction_attribute",
            b"transaction_attribute",
            "user_identifiers",
            b"user_identifiers",
        ],
    ) -> None: ...

global___UserData = UserData

class CustomerMatchUserListMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USER_LIST_FIELD_NUMBER: builtins.int
    @property
    def user_list(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        user_list: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["user_list", b"user_list"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["user_list", b"user_list"]
    ) -> None: ...

global___CustomerMatchUserListMetadata = CustomerMatchUserListMetadata

class StoreSalesMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LOYALTY_FRACTION_FIELD_NUMBER: builtins.int
    TRANSACTION_UPLOAD_FRACTION_FIELD_NUMBER: builtins.int
    CUSTOM_KEY_FIELD_NUMBER: builtins.int
    THIRD_PARTY_METADATA_FIELD_NUMBER: builtins.int
    @property
    def loyalty_fraction(self) -> google.protobuf.wrappers_pb2.DoubleValue: ...
    @property
    def transaction_upload_fraction(
        self,
    ) -> google.protobuf.wrappers_pb2.DoubleValue: ...
    @property
    def custom_key(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def third_party_metadata(self) -> global___StoreSalesThirdPartyMetadata: ...
    def __init__(
        self,
        *,
        loyalty_fraction: typing.Optional[
            google.protobuf.wrappers_pb2.DoubleValue
        ] = ...,
        transaction_upload_fraction: typing.Optional[
            google.protobuf.wrappers_pb2.DoubleValue
        ] = ...,
        custom_key: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        third_party_metadata: typing.Optional[
            global___StoreSalesThirdPartyMetadata
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "custom_key",
            b"custom_key",
            "loyalty_fraction",
            b"loyalty_fraction",
            "third_party_metadata",
            b"third_party_metadata",
            "transaction_upload_fraction",
            b"transaction_upload_fraction",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "custom_key",
            b"custom_key",
            "loyalty_fraction",
            b"loyalty_fraction",
            "third_party_metadata",
            b"third_party_metadata",
            "transaction_upload_fraction",
            b"transaction_upload_fraction",
        ],
    ) -> None: ...

global___StoreSalesMetadata = StoreSalesMetadata

class StoreSalesThirdPartyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ADVERTISER_UPLOAD_DATE_TIME_FIELD_NUMBER: builtins.int
    VALID_TRANSACTION_FRACTION_FIELD_NUMBER: builtins.int
    PARTNER_MATCH_FRACTION_FIELD_NUMBER: builtins.int
    PARTNER_UPLOAD_FRACTION_FIELD_NUMBER: builtins.int
    BRIDGE_MAP_VERSION_ID_FIELD_NUMBER: builtins.int
    PARTNER_ID_FIELD_NUMBER: builtins.int
    @property
    def advertiser_upload_date_time(
        self,
    ) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def valid_transaction_fraction(
        self,
    ) -> google.protobuf.wrappers_pb2.DoubleValue: ...
    @property
    def partner_match_fraction(self) -> google.protobuf.wrappers_pb2.DoubleValue: ...
    @property
    def partner_upload_fraction(self) -> google.protobuf.wrappers_pb2.DoubleValue: ...
    @property
    def bridge_map_version_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def partner_id(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    def __init__(
        self,
        *,
        advertiser_upload_date_time: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        valid_transaction_fraction: typing.Optional[
            google.protobuf.wrappers_pb2.DoubleValue
        ] = ...,
        partner_match_fraction: typing.Optional[
            google.protobuf.wrappers_pb2.DoubleValue
        ] = ...,
        partner_upload_fraction: typing.Optional[
            google.protobuf.wrappers_pb2.DoubleValue
        ] = ...,
        bridge_map_version_id: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        partner_id: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "advertiser_upload_date_time",
            b"advertiser_upload_date_time",
            "bridge_map_version_id",
            b"bridge_map_version_id",
            "partner_id",
            b"partner_id",
            "partner_match_fraction",
            b"partner_match_fraction",
            "partner_upload_fraction",
            b"partner_upload_fraction",
            "valid_transaction_fraction",
            b"valid_transaction_fraction",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "advertiser_upload_date_time",
            b"advertiser_upload_date_time",
            "bridge_map_version_id",
            b"bridge_map_version_id",
            "partner_id",
            b"partner_id",
            "partner_match_fraction",
            b"partner_match_fraction",
            "partner_upload_fraction",
            b"partner_upload_fraction",
            "valid_transaction_fraction",
            b"valid_transaction_fraction",
        ],
    ) -> None: ...

global___StoreSalesThirdPartyMetadata = StoreSalesThirdPartyMetadata
