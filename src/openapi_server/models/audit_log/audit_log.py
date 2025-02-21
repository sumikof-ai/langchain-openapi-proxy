# coding: utf-8

"""
    OpenAI API

    The OpenAI REST API. Please see https://platform.openai.com/docs/api-reference for more details.

    The version of the OpenAPI document: 2.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_server.models.audit_log.audit_log_actor import AuditLogActor
from openapi_server.models.audit_log.audit_log_api_key_created import AuditLogApiKeyCreated
from openapi_server.models.audit_log.audit_log_api_key_deleted import AuditLogApiKeyDeleted
from openapi_server.models.audit_log.audit_log_api_key_updated import AuditLogApiKeyUpdated
from openapi_server.models.audit_log.audit_log_event_type import AuditLogEventType
from openapi_server.models.audit_log.audit_log_invite_accepted import AuditLogInviteAccepted
from openapi_server.models.audit_log.audit_log_invite_sent import AuditLogInviteSent
from openapi_server.models.audit_log.audit_log_login_failed import AuditLogLoginFailed
from openapi_server.models.audit_log.audit_log_organization_updated import AuditLogOrganizationUpdated
from openapi_server.models.audit_log.audit_log_project import AuditLogProject
from openapi_server.models.audit_log.audit_log_project_archived import AuditLogProjectArchived
from openapi_server.models.audit_log.audit_log_project_created import AuditLogProjectCreated
from openapi_server.models.audit_log.audit_log_project_updated import AuditLogProjectUpdated
from openapi_server.models.audit_log.audit_log_service_account_created import AuditLogServiceAccountCreated
from openapi_server.models.audit_log.audit_log_service_account_deleted import AuditLogServiceAccountDeleted
from openapi_server.models.audit_log.audit_log_service_account_updated import AuditLogServiceAccountUpdated
from openapi_server.models.audit_log.audit_log_user_added import AuditLogUserAdded
from openapi_server.models.audit_log.audit_log_user_deleted import AuditLogUserDeleted
from openapi_server.models.audit_log.audit_log_user_updated import AuditLogUserUpdated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AuditLog(BaseModel):
    """
    A log of a user action or configuration change within this organization.
    """ # noqa: E501
    id: StrictStr = Field(description="The ID of this log.")
    type: AuditLogEventType
    effective_at: StrictInt = Field(description="The Unix timestamp (in seconds) of the event.")
    project: Optional[AuditLogProject] = None
    actor: AuditLogActor
    api_key_created: Optional[AuditLogApiKeyCreated] = Field(default=None, alias="api_key.created")
    api_key_updated: Optional[AuditLogApiKeyUpdated] = Field(default=None, alias="api_key.updated")
    api_key_deleted: Optional[AuditLogApiKeyDeleted] = Field(default=None, alias="api_key.deleted")
    invite_sent: Optional[AuditLogInviteSent] = Field(default=None, alias="invite.sent")
    invite_accepted: Optional[AuditLogInviteAccepted] = Field(default=None, alias="invite.accepted")
    invite_deleted: Optional[AuditLogInviteAccepted] = Field(default=None, alias="invite.deleted")
    login_failed: Optional[AuditLogLoginFailed] = Field(default=None, alias="login.failed")
    logout_failed: Optional[AuditLogLoginFailed] = Field(default=None, alias="logout.failed")
    organization_updated: Optional[AuditLogOrganizationUpdated] = Field(default=None, alias="organization.updated")
    project_created: Optional[AuditLogProjectCreated] = Field(default=None, alias="project.created")
    project_updated: Optional[AuditLogProjectUpdated] = Field(default=None, alias="project.updated")
    project_archived: Optional[AuditLogProjectArchived] = Field(default=None, alias="project.archived")
    service_account_created: Optional[AuditLogServiceAccountCreated] = Field(default=None, alias="service_account.created")
    service_account_updated: Optional[AuditLogServiceAccountUpdated] = Field(default=None, alias="service_account.updated")
    service_account_deleted: Optional[AuditLogServiceAccountDeleted] = Field(default=None, alias="service_account.deleted")
    user_added: Optional[AuditLogUserAdded] = Field(default=None, alias="user.added")
    user_updated: Optional[AuditLogUserUpdated] = Field(default=None, alias="user.updated")
    user_deleted: Optional[AuditLogUserDeleted] = Field(default=None, alias="user.deleted")
    __properties: ClassVar[List[str]] = ["id", "type", "effective_at", "project", "actor", "api_key.created", "api_key.updated", "api_key.deleted", "invite.sent", "invite.accepted", "invite.deleted", "login.failed", "logout.failed", "organization.updated", "project.created", "project.updated", "project.archived", "service_account.created", "service_account.updated", "service_account.deleted", "user.added", "user.updated", "user.deleted"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AuditLog from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of actor
        if self.actor:
            _dict['actor'] = self.actor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of api_key_created
        if self.api_key_created:
            _dict['api_key.created'] = self.api_key_created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of api_key_updated
        if self.api_key_updated:
            _dict['api_key.updated'] = self.api_key_updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of api_key_deleted
        if self.api_key_deleted:
            _dict['api_key.deleted'] = self.api_key_deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of invite_sent
        if self.invite_sent:
            _dict['invite.sent'] = self.invite_sent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of invite_accepted
        if self.invite_accepted:
            _dict['invite.accepted'] = self.invite_accepted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of invite_deleted
        if self.invite_deleted:
            _dict['invite.deleted'] = self.invite_deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of login_failed
        if self.login_failed:
            _dict['login.failed'] = self.login_failed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of logout_failed
        if self.logout_failed:
            _dict['logout.failed'] = self.logout_failed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of organization_updated
        if self.organization_updated:
            _dict['organization.updated'] = self.organization_updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project_created
        if self.project_created:
            _dict['project.created'] = self.project_created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project_updated
        if self.project_updated:
            _dict['project.updated'] = self.project_updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project_archived
        if self.project_archived:
            _dict['project.archived'] = self.project_archived.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_account_created
        if self.service_account_created:
            _dict['service_account.created'] = self.service_account_created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_account_updated
        if self.service_account_updated:
            _dict['service_account.updated'] = self.service_account_updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_account_deleted
        if self.service_account_deleted:
            _dict['service_account.deleted'] = self.service_account_deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_added
        if self.user_added:
            _dict['user.added'] = self.user_added.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_updated
        if self.user_updated:
            _dict['user.updated'] = self.user_updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_deleted
        if self.user_deleted:
            _dict['user.deleted'] = self.user_deleted.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AuditLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "effective_at": obj.get("effective_at"),
            "project": AuditLogProject.from_dict(obj.get("project")) if obj.get("project") is not None else None,
            "actor": AuditLogActor.from_dict(obj.get("actor")) if obj.get("actor") is not None else None,
            "api_key.created": AuditLogApiKeyCreated.from_dict(obj.get("api_key.created")) if obj.get("api_key.created") is not None else None,
            "api_key.updated": AuditLogApiKeyUpdated.from_dict(obj.get("api_key.updated")) if obj.get("api_key.updated") is not None else None,
            "api_key.deleted": AuditLogApiKeyDeleted.from_dict(obj.get("api_key.deleted")) if obj.get("api_key.deleted") is not None else None,
            "invite.sent": AuditLogInviteSent.from_dict(obj.get("invite.sent")) if obj.get("invite.sent") is not None else None,
            "invite.accepted": AuditLogInviteAccepted.from_dict(obj.get("invite.accepted")) if obj.get("invite.accepted") is not None else None,
            "invite.deleted": AuditLogInviteAccepted.from_dict(obj.get("invite.deleted")) if obj.get("invite.deleted") is not None else None,
            "login.failed": AuditLogLoginFailed.from_dict(obj.get("login.failed")) if obj.get("login.failed") is not None else None,
            "logout.failed": AuditLogLoginFailed.from_dict(obj.get("logout.failed")) if obj.get("logout.failed") is not None else None,
            "organization.updated": AuditLogOrganizationUpdated.from_dict(obj.get("organization.updated")) if obj.get("organization.updated") is not None else None,
            "project.created": AuditLogProjectCreated.from_dict(obj.get("project.created")) if obj.get("project.created") is not None else None,
            "project.updated": AuditLogProjectUpdated.from_dict(obj.get("project.updated")) if obj.get("project.updated") is not None else None,
            "project.archived": AuditLogProjectArchived.from_dict(obj.get("project.archived")) if obj.get("project.archived") is not None else None,
            "service_account.created": AuditLogServiceAccountCreated.from_dict(obj.get("service_account.created")) if obj.get("service_account.created") is not None else None,
            "service_account.updated": AuditLogServiceAccountUpdated.from_dict(obj.get("service_account.updated")) if obj.get("service_account.updated") is not None else None,
            "service_account.deleted": AuditLogServiceAccountDeleted.from_dict(obj.get("service_account.deleted")) if obj.get("service_account.deleted") is not None else None,
            "user.added": AuditLogUserAdded.from_dict(obj.get("user.added")) if obj.get("user.added") is not None else None,
            "user.updated": AuditLogUserUpdated.from_dict(obj.get("user.updated")) if obj.get("user.updated") is not None else None,
            "user.deleted": AuditLogUserDeleted.from_dict(obj.get("user.deleted")) if obj.get("user.deleted") is not None else None
        })
        return _obj


