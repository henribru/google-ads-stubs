from google.protobuf.descriptor import FieldDescriptor as FieldDescriptor
from google.protobuf.message import Message as ProtobufMessage
from proto import Message as ProtoPlusMessage

def mask_message(
    message: ProtobufMessage | ProtoPlusMessage, mask: str
) -> ProtobufMessage | ProtoPlusMessage: ...
