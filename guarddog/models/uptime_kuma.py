from pydantic import BaseModel

class HeartbeatData(BaseModel):
    monitorID: int
    status: int
    time: str
    msg: str
    important: bool
    duration: int
    timezone: str
    timezoneOffset: str
    localDateTime: str

class MonitorData(BaseModel):
    id: int
    name: str
    description: str
    pathName: str
    # Add more fields as needed

class MsgData(BaseModel):
    msg: str