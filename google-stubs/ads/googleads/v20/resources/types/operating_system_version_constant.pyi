import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import operating_system_version_operator_type

__protobuf__: Incomplete

class OperatingSystemVersionConstant(proto.Message):
    resource_name: str
    id: int
    name: str
    os_major_version: int
    os_minor_version: int
    operator_type: operating_system_version_operator_type.OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType
