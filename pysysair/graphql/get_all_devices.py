from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetAllDevices(BaseModel):
    get_account_devices: Optional[List[Optional["GetAllDevicesGetAccountDevices"]]] = (
        Field(alias="GetAccountDevices")
    )


class GetAllDevicesGetAccountDevices(BaseModel):
    identifier: Optional[str]
    name: Optional[str]
    street: Optional[str]
    zipcode: Optional[str]
    city: Optional[str]
    country: Optional[str]
    device_type: Optional["GetAllDevicesGetAccountDevicesDeviceType"] = Field(
        alias="deviceType"
    )
    status: Optional["GetAllDevicesGetAccountDevicesStatus"]


class GetAllDevicesGetAccountDevicesDeviceType(BaseModel):
    entry: Optional[str]
    module: Optional[str]
    scope: Optional[str]
    type: Optional[str]


class GetAllDevicesGetAccountDevicesStatus(BaseModel):
    connection_status: Optional[str] = Field(alias="connectionStatus")
    serial_number: Optional[str] = Field(alias="serialNumber")
    model: Optional[str]
    startup_wizard_required: Optional[bool] = Field(alias="startupWizardRequired")
    update_in_progress: Optional[bool] = Field(alias="updateInProgress")
    filter_locked: Optional[bool] = Field(alias="filterLocked")
    week_schedule_locked: Optional[bool] = Field(alias="weekScheduleLocked")
    service_locked: Optional[bool] = Field(alias="serviceLocked")
    has_alarms: Optional[bool] = Field(alias="hasAlarms")
