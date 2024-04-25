from api.routes import ns_edit

from common.baseclasses.status_codes import HTTPStatusCodes

delete_success_response = "Все записи из дневника сна удалены"
delete_response_model_200 = {
    "code": HTTPStatusCodes.STATUS_OK_200,
    "description": delete_success_response,
}
from api.routes.edit.delete_diary.edit_delete import EditRouteDelete

ns_edit.add_resource(EditRouteDelete, '/delete')