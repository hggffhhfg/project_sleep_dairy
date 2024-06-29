from src.pydantic_schemas.sleep.notes import SleepNote
from src.routes.notes import ns_notes
from src.utils.restx_schema import response_schema
from src.utils.status_codes import HTTP

response_model_200: dict = response_schema(
    code=HTTP.OK_200,
    ns=ns_notes,
    model=SleepNote,
)
response_not_found_404 = "Note with that id not found"
response_model_404: dict = response_schema(
    code=HTTP.NOT_FOUND_404,
    ns=ns_notes,
    description=response_not_found_404,
)

path_params: dict = {
    "id": {
        "in": "path",
        "description": "Идентификатор записи",
        "required": True,
        "type": "integer",
        "format": "int32",
        "example": "42",
    },
}