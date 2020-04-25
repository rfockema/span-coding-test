from app import app
import filecmp

league_table = app.LeagueTable(open('./tests/data/test_matches.txt', 'r'))


def test_print_ordered_table():
    import sys
    old_stdout = sys.stdout
    sys.stdout = open('./tests/data/test_result.txt', 'w')
    league_table.PrintOrderedTable()
    sys.stdout = old_stdout

    import difflib

    file1 = open('./tests/data/test_result.txt', 'r')
    file2 = open('./tests/data/correct_result.txt', 'r')
    diff = difflib.ndiff(file1.readlines(), file2.readlines())
    delta = ''.join(x[2:] for x in diff if x.startswith('- '))

    assert delta == ''


def test_get_points():
    assert (3, 0) == app.GetMatchPoints(1, 0)
    assert (1, 1) == app.GetMatchPoints(5, 5)
    assert (0, 3) == app.GetMatchPoints(1, 2)


def test_update_points():
    assert league_table.teams['Tarantulas'] == 6
    league_table.UpdatePoints('Tarantulas', 2)
    assert league_table.teams['Tarantulas'] == 8


def test_get_ordered_table_list():
    prev_row = [None, None]
    for row in league_table.GetOrderedTableList():
        if prev_row[0] != None:
            assert prev_row[1] > row[1] or (
                prev_row[1] == row[1] and prev_row[0] < row[0])
        prev_row = row