import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import call_tracking_display_location as gage_call_tracking_display_location, call_type, google_voice_call_status

__protobuf__: Incomplete

class CallView(proto.Message):
    resource_name: str
    caller_country_code: str
    caller_area_code: str
    call_duration_seconds: int
    start_call_date_time: str
    end_call_date_time: str
    call_tracking_display_location: gage_call_tracking_display_location.CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation
    type_: call_type.CallTypeEnum.CallType
    call_status: google_voice_call_status.GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus
