from flask_restx import Namespace, Resource

from api.exceptions.handlers import handler_unprocessable_entity_422
from api.utils.restx_schema import response_schema
from common.baseclasses.status_codes import HTTP
from common.pydantic_schemas.errors.message import ErrorResponse

ns_notes = Namespace(
    name="Sleep diary notes",
    description="Записи из дневника сна",
    path="/note",
    decorators=[
        # validate_auth_token,
    ],
)
ns_notes.errorhandler(handler_unprocessable_entity_422)

response_model_400 = response_schema(
    code=HTTP.BAD_REQUEST_400,
    ns=ns_notes,
    model=ErrorResponse,
)
response_model_422 = response_schema(
    code=HTTP.UNPROCESSABLE_ENTITY_422,
    ns=ns_notes,
    model=ErrorResponse,
)

from api.routes.notes.note_add.note_add import AddNote  # noqa
from api.routes.notes.note_delete.note_delete import DeleteNote  # noqa
from api.routes.notes.note_update.note_update import UpdateNote  # noqa
from api.routes.notes.note_read_by_id.note_read_by_id import (
    NoteFindById,
    # noqa
)


class NotesRoute(
    Resource,
    AddNote,
    UpdateNote,
    DeleteNote,
): ...  # noqa


note_endpoint = "note"

ns_notes.add_resource(
    NotesRoute,
    "",
    endpoint=note_endpoint,
)

note_find_by_id_endpoint = "note_id"

from api.routes.notes.note_read_by_id.note_read_by_id import NoteFindById  # noqa

ns_notes.add_resource(
    NoteFindById,
    "/<int:note_id>",
    endpoint=note_find_by_id_endpoint,
)

note_find_by_date_endpoint = "note_date"

from api.routes.notes.note_read_by_date.note_read_by_date import (
    NoteFindByDate,
    # noqa
)

ns_notes.add_resource(
    NoteFindByDate,
    "/<string:calendar_date>",
    endpoint=note_find_by_date_endpoint,
)
