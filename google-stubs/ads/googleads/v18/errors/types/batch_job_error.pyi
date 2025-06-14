import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class BatchJobErrorEnum(proto.Message):
    class BatchJobError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CANNOT_MODIFY_JOB_AFTER_JOB_STARTS_RUNNING: int
        EMPTY_OPERATIONS: int
        INVALID_SEQUENCE_TOKEN: int
        RESULTS_NOT_READY: int
        INVALID_PAGE_SIZE: int
        CAN_ONLY_REMOVE_PENDING_JOB: int
        CANNOT_LIST_RESULTS: int
        ASSET_GROUP_AND_ASSET_GROUP_ASSET_TRANSACTION_FAILURE: int
        ASSET_GROUP_LISTING_GROUP_FILTER_TRANSACTION_FAILURE: int
        REQUEST_TOO_LARGE: int
