from app.app import LeagueTable, GetMatchPoints

TEST_INPUT_DATA_PATH = './tests/data/test_matches.txt'
TEST_OUTPUT_PATH = './tests/data/test_result.txt'
CORRECT_OUTPUT_DATA_PATH = './tests/data/correct_result.txt'


def test_get_points():
    assert (3, 0) == GetMatchPoints(1, 0)
    assert (1, 1) == GetMatchPoints(5, 5)
    assert (0, 3) == GetMatchPoints(1, 2)


def test_update_points():
    league_table = LeagueTable()
    league_table.UpdatePoints('Tarantulas', 2)
    assert league_table.teams['Tarantulas'] == 2


def test_add_match_results():
    league_table = LeagueTable()
    mock_match_data = [
        'Lions 3, Snakes 3\n',
        'Lions 3, Snakes 0\n',
        'Lions 0, Snakes 3\n',
    ]
    league_table.AddMatchResults(mock_match_data)
    assert league_table.teams['Lions'] == 4
    assert league_table.teams['Snakes'] == 4


def test_get_ordered_table_list():
    league_table = LeagueTable()
    league_table.AddMatchResults(open(TEST_INPUT_DATA_PATH, 'r'))
    prev_row = [None, None]
    for row in league_table.GetOrderedTableList():
        if prev_row[0] != None:
            assert prev_row[1] > row[1] or (
                prev_row[1] == row[1] and prev_row[0] < row[0])
        prev_row = row


def test_print_ordered_table():
    league_table = LeagueTable()
    league_table.AddMatchResults(open(TEST_INPUT_DATA_PATH, 'r'))

    import sys
    old_stdout = sys.stdout
    sys.stdout = open(TEST_OUTPUT_PATH, 'w')
    league_table.PrintOrderedTable()
    sys.stdout = old_stdout

    import difflib
    test_result = open(TEST_OUTPUT_PATH, 'r')
    correct_result = open(CORRECT_OUTPUT_DATA_PATH, 'r')
    diff = difflib.ndiff(test_result.readlines(), correct_result.readlines())
    delta = ''.join(x[2:] for x in diff if x.startswith('- '))

    assert delta == ''
