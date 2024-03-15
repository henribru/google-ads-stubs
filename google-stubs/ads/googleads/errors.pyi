import grpc

from google.ads.googleads.v14 import GoogleAdsFailure as GoogleAdsFailureV14
from google.ads.googleads.v15 import GoogleAdsFailure as GoogleAdsFailureV15
from google.ads.googleads.v16 import GoogleAdsFailure as GoogleAdsFailureV16

GoogleAdsFailure = GoogleAdsFailureV14 | GoogleAdsFailureV15 | GoogleAdsFailureV16

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
