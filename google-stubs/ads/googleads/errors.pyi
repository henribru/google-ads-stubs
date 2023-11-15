import grpc

from google.ads.googleads.v13 import GoogleAdsFailure as GoogleAdsFailureV13
from google.ads.googleads.v14 import GoogleAdsFailure as GoogleAdsFailureV14
from google.ads.googleads.v15 import GoogleAdsFailure as GoogleAdsFailureV15

GoogleAdsFailure = GoogleAdsFailureV13 | GoogleAdsFailureV14 | GoogleAdsFailureV15

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
