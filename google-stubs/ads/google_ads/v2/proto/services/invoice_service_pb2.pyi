# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v2.proto.enums.month_of_year_pb2 import (
    MonthOfYearEnum as google___ads___googleads___v2___enums___month_of_year_pb2___MonthOfYearEnum,
)
from google.ads.google_ads.v2.proto.resources.invoice_pb2 import (
    Invoice as google___ads___googleads___v2___resources___invoice_pb2___Invoice,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class ListInvoicesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    billing_setup: typing___Text = ...
    issue_year: typing___Text = ...
    issue_month: google___ads___googleads___v2___enums___month_of_year_pb2___MonthOfYearEnum.MonthOfYearValue = ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        billing_setup: typing___Optional[typing___Text] = None,
        issue_year: typing___Optional[typing___Text] = None,
        issue_month: typing___Optional[
            google___ads___googleads___v2___enums___month_of_year_pb2___MonthOfYearEnum.MonthOfYearValue
        ] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "billing_setup",
            b"billing_setup",
            "customer_id",
            b"customer_id",
            "issue_month",
            b"issue_month",
            "issue_year",
            b"issue_year",
        ],
    ) -> None: ...

type___ListInvoicesRequest = ListInvoicesRequest

class ListInvoicesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def invoices(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___ads___googleads___v2___resources___invoice_pb2___Invoice
    ]: ...
    def __init__(
        self,
        *,
        invoices: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v2___resources___invoice_pb2___Invoice
            ]
        ] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["invoices", b"invoices"]
    ) -> None: ...

type___ListInvoicesResponse = ListInvoicesResponse
