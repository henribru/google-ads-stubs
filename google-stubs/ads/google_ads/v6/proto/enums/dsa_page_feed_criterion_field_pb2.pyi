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

class DsaPageFeedCriterionFieldEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _DsaPageFeedCriterionField(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            DsaPageFeedCriterionField.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField.V(0)
        UNKNOWN = DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField.V(1)
        PAGE_URL = DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField.V(2)
        LABEL = DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField.V(3)
    class DsaPageFeedCriterionField(metaclass=_DsaPageFeedCriterionField):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField.V(0)
    UNKNOWN = DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField.V(1)
    PAGE_URL = DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField.V(2)
    LABEL = DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField.V(3)
    def __init__(
        self,
    ) -> None: ...

global___DsaPageFeedCriterionFieldEnum = DsaPageFeedCriterionFieldEnum
