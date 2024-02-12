from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel
from .enums import COMPANY_TYPE, ROLE


class GetAccountsWhereInput(BaseModel):
    role: Optional[ROLE] = None


class GetCompaniesWhereInput(BaseModel):
    parent_id: Optional[int] = Field(alias="parentId", default=None)
    country: Optional[str] = None
    type: Optional[str] = None


class WaitForDeviceConfirmationEventInput(BaseModel):
    device_id: Optional[str] = Field(alias="deviceId", default=None)


class GetDeviceMonitoringInput(BaseModel):
    search: str
    page_size: int = Field(alias="pageSize")
    page_number: int = Field(alias="pageNumber")
    sorting_field: str = Field(alias="sortingField")
    sorting_direction: str = Field(alias="sortingDirection")


class GetEntityLogsInput(BaseModel):
    entity_id: str = Field(alias="entityId")


class GetDevicesFilterInfoInput(BaseModel):
    device_ids: Optional[List[Optional[str]]] = Field(alias="deviceIds", default=None)


class NotificationsWhere(BaseModel):
    unread_only: Optional[bool] = Field(alias="unreadOnly", default=None)


class GetDeviceOwnersInput(BaseModel):
    external_access_ids: Optional[List[Optional[int]]] = Field(
        alias="externalAccessIds", default=None
    )


class GetWebshopInfoInput(BaseModel):
    device_ids: Optional[List[Optional[str]]] = Field(alias="deviceIds", default=None)
    email: str


class CreateAccountInput(BaseModel):
    email: str
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    phone_number: str = Field(alias="phoneNumber")
    role: ROLE
    address: "CreateAddressInput"
    company_id: Optional[int] = Field(alias="companyId", default=None)
    locale: Optional[str] = None


class CreateAddressInput(BaseModel):
    country: str
    city: str
    street: str
    zip_code: str = Field(alias="zipCode")


class CreateOwnPrivateAccountInput(BaseModel):
    phone_number: str = Field(alias="phoneNumber")
    address: "CreateAddressInput"
    locale: Optional[str] = None


class UpdateAccountInput(BaseModel):
    email: str
    first_name: Optional[str] = Field(alias="firstName", default=None)
    last_name: Optional[str] = Field(alias="lastName", default=None)
    disabled: Optional[bool] = None
    phone_number: Optional[str] = Field(alias="phoneNumber", default=None)
    locale: Optional[str] = None
    address: Optional["UpdateAddressInput"] = None
    company_id: Optional[int] = Field(alias="companyId", default=None)
    role: Optional[ROLE] = None


class UpdateAddressInput(BaseModel):
    country: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    zip_code: Optional[str] = Field(alias="zipCode", default=None)


class UpdateOwnAccountInput(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None
    locale: Optional[str] = None
    phone_number: Optional[str] = Field(alias="phoneNumber", default=None)
    street: Optional[str] = None
    zip_code: Optional[str] = Field(alias="zipCode", default=None)
    first_name: Optional[str] = Field(alias="firstName", default=None)
    last_name: Optional[str] = Field(alias="lastName", default=None)
    company: Optional["AccountCompanyUpdate"] = None


class AccountCompanyUpdate(BaseModel):
    country: Optional[str] = None
    id: Optional[int] = None
    address: Optional[str] = None
    m_3_number: Optional[str] = Field(alias="m3number", default=None)
    mailbox: Optional[str] = None
    name: Optional[str] = None
    parent_id: Optional[int] = Field(alias="parentId", default=None)
    phone_number: Optional[str] = Field(alias="phoneNumber", default=None)
    sales_reference_email: Optional[str] = Field(
        alias="salesReferenceEmail", default=None
    )
    sales_reference_name: Optional[str] = Field(
        alias="salesReferenceName", default=None
    )
    sales_reference_phone_number: Optional[str] = Field(
        alias="salesReferencePhoneNumber", default=None
    )
    street: Optional[str] = None
    city: Optional[str] = None
    zip_code: Optional[str] = Field(alias="zipCode", default=None)


class DeleteAccountInput(BaseModel):
    email: str


class CreateCompanyInput(BaseModel):
    name: str
    phone_number: str = Field(alias="phoneNumber")
    mailbox: str
    m_3_number: Optional[str] = Field(alias="m3Number", default=None)
    parent_id: Optional[int] = Field(alias="parentId", default=None)
    address: "CreateAddressInput"
    sales_reference: "CreateSalesReferenceInput" = Field(alias="salesReference")
    type: COMPANY_TYPE


class CreateSalesReferenceInput(BaseModel):
    name: str
    email: str
    phone_number: str = Field(alias="phoneNumber")


class UpdateCompanyInput(BaseModel):
    id: int
    name: Optional[str] = None
    phone_number: Optional[str] = Field(alias="phoneNumber", default=None)
    mailbox: Optional[str] = None
    m_3_number: Optional[str] = Field(alias="m3Number", default=None)
    parent_id: Optional[int] = Field(alias="parentId", default=None)
    address: Optional["UpdateAddressInput"] = None
    sales_reference: Optional["UpdateSalesReferenceInput"] = Field(
        alias="salesReference", default=None
    )
    type: Optional[COMPANY_TYPE] = None


class UpdateSalesReferenceInput(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = Field(alias="phoneNumber", default=None)


class DeleteCompanyInput(BaseModel):
    id: int


class AssignDeviceToAccountInput(BaseModel):
    device_id: str = Field(alias="deviceId")
    name: str


class RemoveDeviceFromAccountInput(BaseModel):
    device_id: str = Field(alias="deviceId")


class UpdateDeviceInfoInput(BaseModel):
    identifier: Optional[str] = None
    name: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    street: Optional[str] = None
    zipcode: Optional[str] = None


class OrderFilterInput(BaseModel):
    device_id: Optional[str] = Field(alias="deviceId", default=None)
    first_name: Optional[str] = Field(alias="firstName", default=None)
    last_name: Optional[str] = Field(alias="lastName", default=None)
    phone_number: Optional[str] = Field(alias="phoneNumber", default=None)
    address: Optional[str] = None
    postal_code: Optional[str] = Field(alias="postalCode", default=None)
    city: Optional[str] = None
    free_text: Optional[str] = Field(alias="freeText", default=None)
    country: Optional["OrderFilterCountry"] = None
    selected_filter_kits: Optional[List[Optional["OrderFilterKits"]]] = Field(
        alias="selectedFilterKits", default=None
    )
    subscription: Optional[bool] = None
    first_shipment_now: Optional[bool] = Field(alias="firstShipmentNow", default=None)
    shipment_once_per_year: Optional[bool] = Field(
        alias="shipmentOncePerYear", default=None
    )
    save_user_information: Optional[bool] = Field(
        alias="saveUserInformation", default=None
    )
    first_shipment_date: Optional[str] = Field(alias="firstShipmentDate", default=None)


class OrderFilterCountry(BaseModel):
    locale: Optional[str] = None
    english: Optional[str] = None


class OrderFilterKits(BaseModel):
    amount: Optional[int] = None
    kit_id: Optional[int] = Field(alias="kitId", default=None)


class MarkNotificationAsReadInput(BaseModel):
    notification_id: Optional[str] = Field(alias="notificationId", default=None)
    clean_all: Optional[bool] = Field(alias="cleanAll", default=None)


class HandleServicePartnerRequestInput(BaseModel):
    notification_id: Optional[str] = Field(alias="notificationId", default=None)
    access_period: Optional[int] = Field(alias="accessPeriod", default=None)
    accept: Optional[bool] = None


class UpdateRolePermissionsInput(BaseModel):
    role: Optional[str] = None
    permissions: Optional[List[Optional[str]]] = None


class CreateExternalDeviceAccessInput(BaseModel):
    device_identifier: str = Field(alias="deviceIdentifier")
    name: str
    own_unit: bool = Field(alias="ownUnit")
    project_id: Optional[int] = Field(alias="projectId", default=None)
    access_period: Optional[int] = Field(alias="accessPeriod", default=None)
    company_id: Optional[int] = Field(alias="companyId", default=None)


class UpdateTranslationsInput(BaseModel):
    locale: Optional[str] = None
    updates: Optional[List[Optional["TranslationUpdateType"]]] = None


class TranslationUpdateType(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None
    description: Optional[str] = None


class ImportExternalDeviceDataInput(BaseModel):
    device_ids: Optional[List[Optional[str]]] = Field(alias="deviceIds", default=None)
    configuration: Optional["GraphqlProxyImportInput"] = None


class GraphqlProxyImportInput(BaseModel):
    version: Optional[str] = None
    type: Optional[str] = None
    registers: Optional[List[Optional["DataItemImportInput"]]] = None


class DataItemImportInput(BaseModel):
    id: Optional[int] = None
    value: Optional[int] = None
