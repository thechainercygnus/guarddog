from typing import Union

from pydantic import BaseModel


class UptimeKumaHeartbeat(BaseModel):
    monitorID: int
    status: int
    time: str
    msg: str
    important: bool
    duration: int
    timezone: str
    timezoneOffset: str
    localDateTime: str


class UptimeKumaMonitor(BaseModel):
    id: int
    name: str
    description: Union[str, None]
    pathName: str
    parent: Union[str, None]
    childrenIDs: list
    url: str
    method: str
    hostname: Union[str, None]
    port: Union[str, None]
    maxretries: int
    weight: int
    active: bool
    forceInactive: bool
    type: str
    timeout: int
    interval: int
    retryInterval: int
    resendInterval: int
    keyword: Union[str, None]
    invertKeyword: bool
    expiryNotification: bool
    ignoreTls: bool
    upsideDown: bool
    packetSize: int
    maxredirects: int
    accepted_statuscodes: list[str]
    dns_resolve_type: str
    dns_resolve_server: str
    dns_last_result: None
    docker_container: str
    docker_host: int
    proxyId: None
    notificationIDList: dict
    tags: list
    maintenance: bool
    mqttTopic: str
    mqttSuccessMessage: str
    databaseQuery: None
    authMethod: None
    grpcUrl: None
    grpcProtobuf: None
    grpcMethod: None
    grpcServiceName: None
    grpcEnableTls: bool
    radiusCalledStationId: None
    radiusCallingStationId: None
    game: None
    gamedigGivenPortOnly: bool
    httpBodyEncoding: None
    jsonPath: None
    expectedValue: None
    kafkaProducerTopic: None
    kafkaProducerBrokers: list
    kafkaProducerSsl: bool
    kafkaProducerAllowAutoTopicCreation: bool
    kafkaProducerMessage: None
    screenshot: None
    includeSensitiveData: bool


class IncomingWebhook(BaseModel):
    heartbeat: Union[dict, None] = None
    monitor: Union[dict, None] = None
    msg: Union[str, None] = None
