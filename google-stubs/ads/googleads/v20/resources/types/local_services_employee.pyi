import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import local_services_employee_status, local_services_employee_type
from typing import MutableSequence

__protobuf__: Incomplete

class LocalServicesEmployee(proto.Message):
    resource_name: str
    id: int
    creation_date_time: str
    status: local_services_employee_status.LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatus
    type_: local_services_employee_type.LocalServicesEmployeeTypeEnum.LocalServicesEmployeeType
    university_degrees: MutableSequence['UniversityDegree']
    residencies: MutableSequence['Residency']
    fellowships: MutableSequence['Fellowship']
    job_title: str
    year_started_practicing: int
    languages_spoken: MutableSequence[str]
    category_ids: MutableSequence[str]
    national_provider_id_number: str
    email_address: str
    first_name: str
    middle_name: str
    last_name: str

class UniversityDegree(proto.Message):
    institution_name: str
    degree: str
    graduation_year: int

class Residency(proto.Message):
    institution_name: str
    completion_year: int

class Fellowship(proto.Message):
    institution_name: str
    completion_year: int
