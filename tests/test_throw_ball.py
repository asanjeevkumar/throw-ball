import pytest
from scripts import max_touches

TEST_DATA = {
    'George': ['Beth', 'Sue'],
    'Rick': ['Anne'],
    'Anne': ['Beth'],
    'Beth': ['Anne', 'George'],
    'Sue': ['Beth']
}


def test_get_max_touches_by_single_ball_pass():
    assert max_touches.get_max_touches_by_single_ball('tests/test_file.csv') == 3


def test_file_not_found_exception():
    with pytest.raises(FileNotFoundError):
        max_touches.get_max_touches_by_single_ball('tests/test_file_no_found.csv')


@pytest.mark.parametrize('player, ret_val', [
    ("George", 1),
    ("Rick", 0),
    ("Anne", 1),
    ("Beth", 1),
    ("Sue", 0),

])
def test_get_players_length(player, ret_val):
    assert max_touches.get_players_length(player, TEST_DATA) == ret_val
