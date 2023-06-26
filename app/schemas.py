from pydantic import BaseModel
from typing import List, Dict, Any

class ConsumerRecord(BaseModel):
    topic: str
    partition: int
    offset: int
    timestamp: int
    timestamp_type: int
    key: bytes
    value: Dict[str, Any]
    headers: List
    checksum: Any
    serialized_key_size: int
    serialized_value_size: int
    serialized_header_size: int
    class Config:
        orm_mode = True