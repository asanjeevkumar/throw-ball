# Script finds the maximum number of players that can touch a single ball.
from os import path as osp
import click
import csv


def get_players_length(player, visibility_matrix, first_player=None):
    counter = 0

    for pass_to in visibility_matrix[player]:
        print(player, visibility_matrix[player])
        if first_player != pass_to:
            counter += get_players_length(
                pass_to, visibility_matrix, player)
            counter += 1
        else:
            break
    print(player, counter)

    return counter


def get_max_touches_by_single_ball(file_location):
    """Process the csv file and converts data into
    dictionary of containing list items.

    :param str file_location:
    :return : max players can touch single ball.
    """
    def clean_data():
        ball_mat = {}
        with open(file_location) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                ball_mat[row[0]] = [i.strip() for i in row[1:]]
        return ball_mat

    processed_data = clean_data()
    player_pass_length = 0
    for player, visibility in processed_data.items():
        i = get_players_length(player, processed_data)
        if player_pass_length < i:
            player_pass_length = i
    return player_pass_length


@click.command()
@click.argument('file_location',
                type=click.Path(exists=True, resolve_path=True))
def main(file_location):

    # Validating for csv file.
    if osp.basename(file_location).split('.')[1] != 'csv':
        raise ValueError("File does not exist or not csv"
                         " %s" % file_location)
    print(get_max_touches_by_single_ball(file_location))


if __name__ == "__main__":
    main()

