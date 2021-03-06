"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ConversionActionCategoryEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ConversionActionCategory(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            ConversionActionCategory.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = ConversionActionCategoryEnum.ConversionActionCategory.V(0)
        UNKNOWN = ConversionActionCategoryEnum.ConversionActionCategory.V(1)
        DEFAULT = ConversionActionCategoryEnum.ConversionActionCategory.V(2)
        PAGE_VIEW = ConversionActionCategoryEnum.ConversionActionCategory.V(3)
        PURCHASE = ConversionActionCategoryEnum.ConversionActionCategory.V(4)
        SIGNUP = ConversionActionCategoryEnum.ConversionActionCategory.V(5)
        LEAD = ConversionActionCategoryEnum.ConversionActionCategory.V(6)
        DOWNLOAD = ConversionActionCategoryEnum.ConversionActionCategory.V(7)
        ADD_TO_CART = ConversionActionCategoryEnum.ConversionActionCategory.V(8)
        BEGIN_CHECKOUT = ConversionActionCategoryEnum.ConversionActionCategory.V(9)
        SUBSCRIBE_PAID = ConversionActionCategoryEnum.ConversionActionCategory.V(10)
        PHONE_CALL_LEAD = ConversionActionCategoryEnum.ConversionActionCategory.V(11)
        IMPORTED_LEAD = ConversionActionCategoryEnum.ConversionActionCategory.V(12)
        SUBMIT_LEAD_FORM = ConversionActionCategoryEnum.ConversionActionCategory.V(13)
        BOOK_APPOINTMENT = ConversionActionCategoryEnum.ConversionActionCategory.V(14)
        REQUEST_QUOTE = ConversionActionCategoryEnum.ConversionActionCategory.V(15)
        GET_DIRECTIONS = ConversionActionCategoryEnum.ConversionActionCategory.V(16)
        OUTBOUND_CLICK = ConversionActionCategoryEnum.ConversionActionCategory.V(17)
        CONTACT = ConversionActionCategoryEnum.ConversionActionCategory.V(18)
        ENGAGEMENT = ConversionActionCategoryEnum.ConversionActionCategory.V(19)
        STORE_VISIT = ConversionActionCategoryEnum.ConversionActionCategory.V(20)
        STORE_SALE = ConversionActionCategoryEnum.ConversionActionCategory.V(21)
    class ConversionActionCategory(metaclass=_ConversionActionCategory):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = ConversionActionCategoryEnum.ConversionActionCategory.V(0)
    UNKNOWN = ConversionActionCategoryEnum.ConversionActionCategory.V(1)
    DEFAULT = ConversionActionCategoryEnum.ConversionActionCategory.V(2)
    PAGE_VIEW = ConversionActionCategoryEnum.ConversionActionCategory.V(3)
    PURCHASE = ConversionActionCategoryEnum.ConversionActionCategory.V(4)
    SIGNUP = ConversionActionCategoryEnum.ConversionActionCategory.V(5)
    LEAD = ConversionActionCategoryEnum.ConversionActionCategory.V(6)
    DOWNLOAD = ConversionActionCategoryEnum.ConversionActionCategory.V(7)
    ADD_TO_CART = ConversionActionCategoryEnum.ConversionActionCategory.V(8)
    BEGIN_CHECKOUT = ConversionActionCategoryEnum.ConversionActionCategory.V(9)
    SUBSCRIBE_PAID = ConversionActionCategoryEnum.ConversionActionCategory.V(10)
    PHONE_CALL_LEAD = ConversionActionCategoryEnum.ConversionActionCategory.V(11)
    IMPORTED_LEAD = ConversionActionCategoryEnum.ConversionActionCategory.V(12)
    SUBMIT_LEAD_FORM = ConversionActionCategoryEnum.ConversionActionCategory.V(13)
    BOOK_APPOINTMENT = ConversionActionCategoryEnum.ConversionActionCategory.V(14)
    REQUEST_QUOTE = ConversionActionCategoryEnum.ConversionActionCategory.V(15)
    GET_DIRECTIONS = ConversionActionCategoryEnum.ConversionActionCategory.V(16)
    OUTBOUND_CLICK = ConversionActionCategoryEnum.ConversionActionCategory.V(17)
    CONTACT = ConversionActionCategoryEnum.ConversionActionCategory.V(18)
    ENGAGEMENT = ConversionActionCategoryEnum.ConversionActionCategory.V(19)
    STORE_VISIT = ConversionActionCategoryEnum.ConversionActionCategory.V(20)
    STORE_SALE = ConversionActionCategoryEnum.ConversionActionCategory.V(21)
    def __init__(
        self,
    ) -> None: ...

global___ConversionActionCategoryEnum = ConversionActionCategoryEnum
