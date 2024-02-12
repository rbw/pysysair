from typing import Any, Dict

from .async_base_client import AsyncBaseClient
from .get_all_devices import GetAllDevices


def gql(q: str) -> str:
    return q


class Client(AsyncBaseClient):
    async def get_all_devices(self, **kwargs: Any) -> GetAllDevices:
        query = gql(
            """
            query GetAllDevices {
              GetAccountDevices {
                identifier
                name
                street
                zipcode
                city
                country
                deviceType {
                  entry
                  module
                  scope
                  type
                }
                status {
                  connectionStatus
                  serialNumber
                  model
                  startupWizardRequired
                  updateInProgress
                  filterLocked
                  weekScheduleLocked
                  serviceLocked
                  hasAlarms
                }
              }
            }
            """
        )
        variables: Dict[str, object] = {}
        response = await self.execute(
            query=query, operation_name="GetAllDevices", variables=variables, **kwargs
        )
        data = self.get_data(response)
        return GetAllDevices.model_validate(data)
