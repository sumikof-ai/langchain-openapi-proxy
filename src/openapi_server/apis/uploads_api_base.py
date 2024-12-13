# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBytes, StrictStr
from typing import Tuple, Union
from typing_extensions import Annotated
from openapi_server.models.complete_upload_request import CompleteUploadRequest
from openapi_server.models.create.create_upload_request import CreateUploadRequest
from openapi_server.models.upload import Upload
from openapi_server.models.upload_part import UploadPart


class BaseUploadsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUploadsApi.subclasses = BaseUploadsApi.subclasses + (cls,)
    async def add_upload_part(
        self,
        upload_id: Annotated[StrictStr, Field(description="The ID of the Upload. ")],
        data: Annotated[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]], Field(description="The chunk of bytes for this Part. ")],
    ) -> UploadPart:
        ...


    async def cancel_upload(
        self,
        upload_id: Annotated[StrictStr, Field(description="The ID of the Upload. ")],
    ) -> Upload:
        ...


    async def complete_upload(
        self,
        upload_id: Annotated[StrictStr, Field(description="The ID of the Upload. ")],
        complete_upload_request: CompleteUploadRequest,
    ) -> Upload:
        ...


    async def create_upload(
        self,
        create_upload_request: CreateUploadRequest,
    ) -> Upload:
        ...
