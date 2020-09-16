import master_mind_GUI as mmg
import random

row_index = 0
nr_of_guesses = 0

def solution_generator():
    solution = []
    while len(str(solution)) < 10:
        solution.append(random.randrange(0,6))
    print(solution)
    return solution


def correct_place_checker(player_guess, solution):
    print(player_guess, solution)
    for number in player_guess:
        if player_guess[number] == solution[number]:
            correct_place += 1
            return correct_place


def wrong_place_checker():
    return


solution = solution_generator()
window = mmg.create_GUI()


while nr_of_guesses < 6:
    player_guess = mmg.make_guess(row_index, window)
    correct_place = correct_place_checker(player_guess, solution)
    wrong_place = wrong_place_checker()
    mmg.peg_feedback(row_index, correct_place, wrong_place, window)
    row_index += 1
    nr_of_guesses += 1

mmg.gameover_screen(nr_of_guesses, "string")



"""
mmg.make_guess(row_index, window)

mmg.peg_feedback(row_index, correct_place, wrong_place, window)

mmg.gameover_screen(nr_of_guesses, string)
"""
