from flask import Response
from flask_restx import Resource

from sleep_diary_api.Routes.sleep import (
    ns_sleep,
    get_all_notes_response_model_200,
    post_new_note_response_model_201,
    new_note_expect_payload_model,
    get_all_notes_param, get_all_notes_response_model_404,
)
from sleep_diary_api.Utils.manage_notes import convert_notes, slice_on_week
from src.pydantic_schemas.notes.sleep_diary import SleepDiaryModel, SleepDiaryCompute
from src.pydantic_schemas.notes.sleep_notes import SleepNoteModel
from sleep_diary_api.CRUD.notation_queries import get_all_notations_of_user


class SleepRoute(Resource):
    @ns_sleep.doc(description='Получение всех записей дневника сна по id пользователя')
    @ns_sleep.expect(get_all_notes_param)
    @ns_sleep.response(**get_all_notes_response_model_200)
    @ns_sleep.response(**get_all_notes_response_model_404)
    def get(self):
        args = get_all_notes_param.parse_args()
        user_id = args['user_id']
        db_notes = get_all_notations_of_user(user_id)
        pd_notes = convert_notes(db_notes)
        pd_weeks = slice_on_week(pd_notes)
        sleep_diary = SleepDiaryCompute(weeks=pd_weeks)
        response = SleepDiaryModel.model_validate(sleep_diary)

        status = 400
        if db_notes:
            status = 200
        elif not db_notes:
            status = 404
        return Response(response.model_dump_json(), status, content_type='application/json')

    @ns_sleep.doc(description='Добавление новой записи в дневник сна')
    @ns_sleep.param('payload', 'Новая запись в дневник сна', _in='body')
    @ns_sleep.expect(new_note_expect_payload_model)
    @ns_sleep.response(**post_new_note_response_model_201)
    def post(self):
        user_id = 1
        new_sleep_note = SleepNoteModel(
            id=0,
            user_id=user_id,
            **ns_sleep.payload
        )
        response = new_sleep_note.model_dump_json(indent=4, by_alias=True)
        return Response(response)
