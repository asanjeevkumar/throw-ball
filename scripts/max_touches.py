"""Script prints the maximum number of players that can touch a single ball.

This script takes csv file location as argument and process csv file to
identify the maximum count of players touch a single ball.

`python throw_ball/scripts/max_touches.py [file_location]`
"""
from os import path as osp
import csv
import click


def get_players_length(player, visibility_matrix):
    """Gets number of players who have visibility between each other.

    :param str player: Name of player who has ball
    :param visibility_matrix: Array of player matrix.
    :return int: number of players visibility is both ways
    """
    counter = 0

    for pass_to in visibility_matrix[player]:

        # Checking if player is in others visibility list
        if player in visibility_matrix[pass_to]:
            counter = +1

    return counter


def clean_data(file_location):
    """Returns array of data by processing csv file.

    :param file_location:
    :return: dictionary with items as list
    """
    ball_mat = {}
    with open(file_location) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ball_mat[row[0]] = [i.strip() for i in row[1:]]
    return ball_mat


def get_max_touches_by_single_ball(file_location):
    """Process the csv file and converts data into
    dictionary of containing list items.

    :param str file_location:
    :return : max players can touch single ball.
    """
    processed_data = clean_data(file_location)
    print(processed_data)
    player_pass_length = 0
    for player, _ in processed_data.items():
        player_pass_length += get_players_length(player, processed_data)

    return player_pass_length


@click.command()
@click.argument('file_location',
                type=click.Path(exists=True, resolve_path=True))
def main(file_location):
    """main function is trigger point

    :param file_location: location of file
    :return:
    """
    # Validating for csv file.
    if osp.basename(file_location).split('.')[1] != 'csv':
        raise ValueError("File does not exist or not csv"
                         " %s" % file_location)
    print(get_max_touches_by_single_ball(file_location))


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
