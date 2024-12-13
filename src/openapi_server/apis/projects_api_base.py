# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.project.project import Project
from openapi_server.models.project.project_api_key import ProjectApiKey
from openapi_server.models.project.project_api_key_delete_response import ProjectApiKeyDeleteResponse
from openapi_server.models.project.project_api_key_list_response import ProjectApiKeyListResponse
from openapi_server.models.project.project_create_request import ProjectCreateRequest
from openapi_server.models.project.project_list_response import ProjectListResponse
from openapi_server.models.project.project_service_account import ProjectServiceAccount
from openapi_server.models.project.project_service_account_create_request import ProjectServiceAccountCreateRequest
from openapi_server.models.project.project_service_account_create_response import ProjectServiceAccountCreateResponse
from openapi_server.models.project.project_service_account_delete_response import ProjectServiceAccountDeleteResponse
from openapi_server.models.project.project_service_account_list_response import ProjectServiceAccountListResponse
from openapi_server.models.project.project_update_request import ProjectUpdateRequest
from openapi_server.models.project.project_user import ProjectUser
from openapi_server.models.project.project_user_create_request import ProjectUserCreateRequest
from openapi_server.models.project.project_user_delete_response import ProjectUserDeleteResponse
from openapi_server.models.project.project_user_list_response import ProjectUserListResponse
from openapi_server.models.project.project_user_update_request import ProjectUserUpdateRequest


class BaseProjectsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseProjectsApi.subclasses = BaseProjectsApi.subclasses + (cls,)
    async def archive_project(
        self,
        project_id: Annotated[StrictStr, Field(description="The ID of the project.")],
    ) -> Project:
        ...


    async def create_project(
        self,
        project_create_request: Annotated[ProjectCreateRequest, Field(description="The project create request payload.")],
    ) -> Project:
        ...


    async def create_project_service_account(
        self,
        project_id: Annotated[StrictStr, Field(description="The ID of the project.")],
        project_service_account_create_request: Annotated[ProjectServiceAccountCreateRequest, Field(description="The project service account create request payload.")],
    ) -> ProjectServiceAccountCreateResponse:
        ...


    async def create_project_user(
        self,
        project_id: Annotated[StrictStr, Field(description="The ID of the project.")],
        project_user_create_request: Annotated[ProjectUserCreateRequest, Field(description="The project user create request payload.")],
    ) -> ProjectUser:
        ...


    async def delete_project_api_key(
        self,
        project_id: Annotated[StrictStr, Field(description="The ID of the project.")],
        key_id: Annotated[StrictStr, Field(description="The ID of the API key.")],
    ) -> ProjectApiKeyDeleteResponse:
        ...


    async def delete_project_service_account(
        self,
        project_id: Annotated[StrictStr, Field(description="The ID of the project.")],
        service_account_id: Annotated[StrictStr, Field(description="The ID of the service account.")],
    ) -> ProjectServiceAccountDeleteResponse:
        ...


    async def delete_project_user(
        self,
        project_id: Annotated[StrictStr, Field(description="The ID of the project.")],
        user_id: Annotated[StrictStr, Field(description="The ID of the user.")],
    ) -> ProjectUserDeleteResponse:
        ...


    async def list_project_api_keys(
        self,
        project_id: Annotated[StrictStr, Field(description="The ID of the project.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20. ")],
        after: Annotated[Optional[StrictStr], Field(description="A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list. ")],
    ) -> ProjectApiKeyListResponse:
        ...


    async def list_project_service_accounts(
        self,
        project_id: Annotated[StrictStr, Field(description="The ID of the project.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20. ")],
        after: Annotated[Optional[StrictStr], Field(description="A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list. ")],
    ) -> ProjectServiceAccountListResponse:
        ...


    async def list_project_users(
        self,
        project_id: Annotated[StrictStr, Field(description="The ID of the project.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20. ")],
        after: Annotated[Optional[StrictStr], Field(description="A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list. ")],
    ) -> ProjectUserListResponse:
        ...


    async def list_projects(
        self,
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20. ")],
        after: Annotated[Optional[StrictStr], Field(description="A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list. ")],
        include_archived: Annotated[Optional[StrictBool], Field(description="If `true` returns all projects including those that have been `archived`. Archived projects are not included by default.")],
    ) -> ProjectListResponse:
        ...


    async def modify_project(
        self,
        project_id: Annotated[StrictStr, Field(description="The ID of the project.")],
        project_update_request: Annotated[ProjectUpdateRequest, Field(description="The project update request payload.")],
    ) -> Project:
        ...


    async def modify_project_user(
        self,
        project_id: Annotated[StrictStr, Field(description="The ID of the project.")],
        user_id: Annotated[StrictStr, Field(description="The ID of the user.")],
        project_user_update_request: Annotated[ProjectUserUpdateRequest, Field(description="The project user update request payload.")],
    ) -> ProjectUser:
        ...


    async def retrieve_project(
        self,
        project_id: Annotated[StrictStr, Field(description="The ID of the project.")],
    ) -> Project:
        ...


    async def retrieve_project_api_key(
        self,
        project_id: Annotated[StrictStr, Field(description="The ID of the project.")],
        key_id: Annotated[StrictStr, Field(description="The ID of the API key.")],
    ) -> ProjectApiKey:
        ...


    async def retrieve_project_service_account(
        self,
        project_id: Annotated[StrictStr, Field(description="The ID of the project.")],
        service_account_id: Annotated[StrictStr, Field(description="The ID of the service account.")],
    ) -> ProjectServiceAccount:
        ...


    async def retrieve_project_user(
        self,
        project_id: Annotated[StrictStr, Field(description="The ID of the project.")],
        user_id: Annotated[StrictStr, Field(description="The ID of the user.")],
    ) -> ProjectUser:
        ...
