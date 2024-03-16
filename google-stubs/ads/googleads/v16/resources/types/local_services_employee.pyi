from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.local_services_employee_status import (
    LocalServicesEmployeeStatusEnum,
)
from google.ads.googleads.v16.enums.types.local_services_employee_type import (
    LocalServicesEmployeeTypeEnum,
)

_M = TypeVar("_M")

class Fellowship(proto.Message):
    institution_name: str
    completion_year: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        institution_name: str = ...,
        completion_year: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["institution_name", "completion_year"]
    ) -> bool: ...

class LocalServicesEmployee(proto.Message):
    resource_name: str
    id: int
    creation_date_time: str
    status: LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatus
    type_: LocalServicesEmployeeTypeEnum.LocalServicesEmployeeType
    university_degrees: MutableSequence[UniversityDegree]
    residencies: MutableSequence[Residency]
    fellowships: MutableSequence[Fellowship]
    job_title: str
    year_started_practicing: int
    languages_spoken: MutableSequence[str]
    category_ids: MutableSequence[str]
    national_provider_id_number: str
    email_address: str
    first_name: str
    middle_name: str
    last_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        creation_date_time: str = ...,
        status: LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatus = ...,
        type_: LocalServicesEmployeeTypeEnum.LocalServicesEmployeeType = ...,
        university_degrees: MutableSequence[UniversityDegree] = ...,
        residencies: MutableSequence[Residency] = ...,
        fellowships: MutableSequence[Fellowship] = ...,
        job_title: str = ...,
        year_started_practicing: int = ...,
        languages_spoken: MutableSequence[str] = ...,
        category_ids: MutableSequence[str] = ...,
        national_provider_id_number: str = ...,
        email_address: str = ...,
        first_name: str = ...,
        middle_name: str = ...,
        last_name: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "creation_date_time",
            "status",
            "type_",
            "university_degrees",
            "residencies",
            "fellowships",
            "job_title",
            "year_started_practicing",
            "languages_spoken",
            "category_ids",
            "national_provider_id_number",
            "email_address",
            "first_name",
            "middle_name",
            "last_name",
        ],
    ) -> bool: ...

class Residency(proto.Message):
    institution_name: str
    completion_year: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        institution_name: str = ...,
        completion_year: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["institution_name", "completion_year"]
    ) -> bool: ...

class UniversityDegree(proto.Message):
    institution_name: str
    degree: str
    graduation_year: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        institution_name: str = ...,
        degree: str = ...,
        graduation_year: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["institution_name", "degree", "graduation_year"]
    ) -> bool: ...
