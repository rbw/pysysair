from enum import Enum


class COMPANY_TYPE(str, Enum):
    PROFESSIONAL = "PROFESSIONAL"
    TECHNICAL_SUPPORT = "TECHNICAL_SUPPORT"
    UNKNOWN = "UNKNOWN"


class ROLE(str, Enum):
    ROOT = "ROOT"
    ADMIN = "ADMIN"
    LOCAL_ADMIN = "LOCAL_ADMIN"
    TS_ADMIN = "TS_ADMIN"
    PROFESSIONAL = "PROFESSIONAL"
    LOCAL_TS = "LOCAL_TS"
    PROFESSIONAL_SUB_ACCOUNT = "PROFESSIONAL_SUB_ACCOUNT"
    PRIVATE_USER = "PRIVATE_USER"
    TRANSLATOR = "TRANSLATOR"


class NOTIFICATION_TYPE(str, Enum):
    SERVICE_PARTNER_REQUEST = "SERVICE_PARTNER_REQUEST"
    UNIT_ACCESS_REQUEST = "UNIT_ACCESS_REQUEST"
    PROJECT_ASSIGNMENT = "PROJECT_ASSIGNMENT"
    SERVICE_PARTNER_REQUEST_REJECTED = "SERVICE_PARTNER_REQUEST_REJECTED"
    SERVICE_PARTNER_REQUEST_ACCEPTED = "SERVICE_PARTNER_REQUEST_ACCEPTED"
    UNIT_ACCESS_REQUEST_ACCEPTED = "UNIT_ACCESS_REQUEST_ACCEPTED"
    UNIT_ACCESS_REQUEST_REJECTED = "UNIT_ACCESS_REQUEST_REJECTED"
