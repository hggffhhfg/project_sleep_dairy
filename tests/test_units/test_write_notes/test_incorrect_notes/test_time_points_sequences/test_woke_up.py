import pytest

from src.domain.note.model import Note
from src.domain.note.validators import SleepTimePointError


def test_woke_up_cannot_be_gt_got_up():
    with pytest.raises(SleepTimePointError) as error:
        Note(
            bedtime_date="2020-12-12",
            went_to_bed="01:00",
            fell_asleep="03:00",
            woke_up="14:00",
            got_up="13:00",
        )
    assert error.value.message == "При проверки поля с временем произошла ошибка."


def test_woke_up_cannot_be_gt_got_up_with_one_time_point_after_midnight_1():
    with pytest.raises(SleepTimePointError) as error:
        Note(
            bedtime_date="2020-12-12",
            went_to_bed="23:00",
            fell_asleep="01:00",
            woke_up="12:00",
            got_up="11:00",
        )
    assert error.value.message == "При проверки поля с временем произошла ошибка."


def test_woke_up_cannot_be_gt_got_up_with_one_time_point_after_midnight_2():
    with pytest.raises(SleepTimePointError) as error:
        Note(
            bedtime_date="2020-12-12",
            went_to_bed="13:00",
            fell_asleep="15:00",
            woke_up="02:00",
            got_up="01:00",
        )
    assert error.value.message == "При проверки поля с временем произошла ошибка."


def test_woke_up_cannot_be_gt_got_up_with_two_time_point_after_midnight_1():
    with pytest.raises(SleepTimePointError) as error:
        Note(
            bedtime_date="2020-12-12",
            went_to_bed="21:00",
            fell_asleep="23:00",
            woke_up="11:00",
            got_up="09:00",
        )
    assert error.value.message == "При проверки поля с временем произошла ошибка."


def test_woke_up_cannot_be_gt_got_up_with_two_time_point_after_midnight_2():
    with pytest.raises(SleepTimePointError) as error:
        Note(
            bedtime_date="2020-12-12",
            went_to_bed="15:00",
            fell_asleep="17:00",
            woke_up="04:00",
            got_up="03:00",
        )
    assert error.value.message == "При проверки поля с временем произошла ошибка."
