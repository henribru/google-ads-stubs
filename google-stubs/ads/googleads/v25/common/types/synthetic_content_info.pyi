from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v25.enums.types.synthetic_content_attestation_status import (
    SyntheticContentAttestationStatusEnum,
)
from google.ads.googleads.v25.enums.types.synthetic_content_source import (
    SyntheticContentSourceEnum,
)

_M = TypeVar("_M")

class SyntheticContentAttestation(proto.Message):
    status: SyntheticContentAttestationStatusEnum.SyntheticContentAttestationStatus
    source: SyntheticContentSourceEnum.SyntheticContentSource
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        status: SyntheticContentAttestationStatusEnum.SyntheticContentAttestationStatus = ...,
        source: SyntheticContentSourceEnum.SyntheticContentSource = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["status", "source"]
    ) -> bool: ...

class SyntheticContentInfo(proto.Message):
    advertiser_attestation: SyntheticContentAttestation
    system_attestation: SyntheticContentAttestation
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        advertiser_attestation: SyntheticContentAttestation = ...,
        system_attestation: SyntheticContentAttestation = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["advertiser_attestation", "system_attestation"]
    ) -> bool: ...
