from datetime import timedelta

from src.domain.note.durations import NoteDurations

eight_hour_timedelta_of_sleep = timedelta(hours=8)
one_hour_timedelta_of_no_sleep = timedelta(hours=1)


def test_note_durations_all_time_point_is_sequences():
    note = NoteDurations(
        bedtime_date="2020-12-12",
        went_to_bed="01:00",
        fell_asleep="03:00",
        woke_up="11:00",
        got_up="13:00",
        no_sleep="01:00",
    )
    assert note._sleep_duration_without_the_no_sleep == eight_hour_timedelta_of_sleep
    assert note._no_sleep_duration == one_hour_timedelta_of_no_sleep


def test_note_durations_with_one_time_point_after_midnight():
    note = NoteDurations(
        bedtime_date="2020-12-12",
        went_to_bed="13:00",
        fell_asleep="15:00",
        woke_up="23:00",
        got_up="01:00",
        no_sleep="01:00",
    )
    assert note._sleep_duration_without_the_no_sleep == eight_hour_timedelta_of_sleep
    assert note._no_sleep_duration == one_hour_timedelta_of_no_sleep


def test_note_durations_with_two_time_point_after_midnight():
    note = NoteDurations(
        bedtime_date="2020-12-12",
        went_to_bed="15:00",
        fell_asleep="17:00",
        woke_up="01:00",
        got_up="03:00",
        no_sleep="01:00",
    )
    assert note._sleep_duration_without_the_no_sleep == eight_hour_timedelta_of_sleep
    assert note._no_sleep_duration == one_hour_timedelta_of_no_sleep


def test_note_durations_with_three_time_point_after_midnight():
    note = NoteDurations(
        bedtime_date="2020-12-12",
        went_to_bed="23:00",
        fell_asleep="01:00",
        woke_up="09:00",
        got_up="11:00",
        no_sleep="01:00",
    )
    assert note._sleep_duration_without_the_no_sleep == eight_hour_timedelta_of_sleep
    assert note._no_sleep_duration == one_hour_timedelta_of_no_sleep