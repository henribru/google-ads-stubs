# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.resources.payments_account_pb2 import (
    PaymentsAccount as google___ads___googleads___v2___resources___payments_account_pb2___PaymentsAccount,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ListPaymentsAccountsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id = ... # type: typing___Text

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListPaymentsAccountsRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",b"customer_id"]) -> None: ...

class ListPaymentsAccountsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def payments_accounts(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___ads___googleads___v2___resources___payments_account_pb2___PaymentsAccount]: ...

    def __init__(self,
        *,
        payments_accounts : typing___Optional[typing___Iterable[google___ads___googleads___v2___resources___payments_account_pb2___PaymentsAccount]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListPaymentsAccountsResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"payments_accounts"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"payments_accounts",b"payments_accounts"]) -> None: ...
