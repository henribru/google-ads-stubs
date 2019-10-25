# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.enums.month_of_year_pb2 import (
    MonthOfYearEnum as google___ads___googleads___v2___enums___month_of_year_pb2___MonthOfYearEnum,
)

from google.ads.google_ads.v2.proto.resources.invoice_pb2 import (
    Invoice as google___ads___googleads___v2___resources___invoice_pb2___Invoice,
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


class ListInvoicesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id = ... # type: typing___Text
    billing_setup = ... # type: typing___Text
    issue_year = ... # type: typing___Text
    issue_month = ... # type: google___ads___googleads___v2___enums___month_of_year_pb2___MonthOfYearEnum.MonthOfYear

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        billing_setup : typing___Optional[typing___Text] = None,
        issue_year : typing___Optional[typing___Text] = None,
        issue_month : typing___Optional[google___ads___googleads___v2___enums___month_of_year_pb2___MonthOfYearEnum.MonthOfYear] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListInvoicesRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"billing_setup",u"customer_id",u"issue_month",u"issue_year"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"billing_setup",b"billing_setup",u"customer_id",b"customer_id",u"issue_month",b"issue_month",u"issue_year",b"issue_year"]) -> None: ...

class ListInvoicesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def invoices(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___ads___googleads___v2___resources___invoice_pb2___Invoice]: ...

    def __init__(self,
        *,
        invoices : typing___Optional[typing___Iterable[google___ads___googleads___v2___resources___invoice_pb2___Invoice]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListInvoicesResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"invoices"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"invoices",b"invoices"]) -> None: ...
