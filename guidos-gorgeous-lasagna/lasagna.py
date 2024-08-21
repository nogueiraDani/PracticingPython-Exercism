"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from
    'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Calculo do tempo de preparação

    :param number_of_layers: int - quantidade de camadas
    :return: int - tempo total de preparação
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_lauers, elapsed_bake_time):
    """
    Calculo do tempo total de cozimento

    :param number_of_lauers: int - numero de camadas
    :param elapsed_bake_time: int - minutos que a lasanha ja esta assando
    :return: int - tempo total de cozimento
    """
    return (number_of_lauers * PREPARATION_TIME) + elapsed_bake_time
