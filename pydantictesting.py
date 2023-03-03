from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = "Jon Doe"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

external_data = {
    "id": 23,
    "signup_ts": "2021-07-16 17:22",
    "friends": [1, "2", b"3"]
}

user = User(**external_data)
print(user)
print(user.id)
print(user.friends)
