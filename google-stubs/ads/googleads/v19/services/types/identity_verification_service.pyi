import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import identity_verification_program, identity_verification_program_status
from typing import MutableSequence

__protobuf__: Incomplete

class StartIdentityVerificationRequest(proto.Message):
    customer_id: str
    verification_program: identity_verification_program.IdentityVerificationProgramEnum.IdentityVerificationProgram

class GetIdentityVerificationRequest(proto.Message):
    customer_id: str

class GetIdentityVerificationResponse(proto.Message):
    identity_verification: MutableSequence['IdentityVerification']

class IdentityVerification(proto.Message):
    verification_program: identity_verification_program.IdentityVerificationProgramEnum.IdentityVerificationProgram
    identity_verification_requirement: IdentityVerificationRequirement
    verification_progress: IdentityVerificationProgress

class IdentityVerificationProgress(proto.Message):
    program_status: identity_verification_program_status.IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus
    invitation_link_expiration_time: str
    action_url: str

class IdentityVerificationRequirement(proto.Message):
    verification_start_deadline_time: str
    verification_completion_deadline_time: str
