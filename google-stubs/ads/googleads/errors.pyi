import grpc

from google.ads.googleads.v16 import GoogleAdsFailure as GoogleAdsFailureV16
from google.ads.googleads.v17 import GoogleAdsFailure as GoogleAdsFailureV17
from google.ads.googleads.v18 import GoogleAdsFailure as GoogleAdsFailureV18

GoogleAdsFailure = GoogleAdsFailureV16 | GoogleAdsFailureV17

class GoogleAdsException(Exception):
    error: grpc.RpcError = ...
    call: grpc.Call = ...
    failure: GoogleAdsFailure = ...
    request_id: str = ...
    def __init__(
        self,
        error: grpc.RpcError,
        call: grpc.Call,
        failure: GoogleAdsFailure,
        request_id: str,
    ) -> None: ...
