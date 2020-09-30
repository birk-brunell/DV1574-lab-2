# Kod skriven av Birk Brunell
# Mastermind labb 2
# Estimerad tid: 4h
# Faktisk tid: 5h
# Antal möjliga kombinationer = 6^4 = 1296

import master_mind_GUI as mmg
import random

def solution_generator():
    """Returns a list of four randomly generated numbers"""

    solution = []
    while len(solution) < 4:
        solution.append(random.randrange(0,6))

    return solution

    # skapar en dictionary för att hålla koll på redan matchade index
def correct_checker(player_guess, solution):
    """Checks how many direct matches that can be found 'correct_place'
    and how many indirect matches 'correct_amount' that can be found.
    Then returns a tuple: (correct_place, correct_amount)"""

    correct_place = 0
    wrong_place = 0
    matches_index = {}

    # Debugg
    print(player_guess)
    print(solution)

    # Kollar rätt tal på rätt plats
    for index_pg in range(len(player_guess)):
        if player_guess[index_pg] == solution[index_pg]:
            correct_place += 1
            matches_index[index_pg] = index_pg
 
    # Kollar rätt tal fel plats
    for index_pg in range(len(player_guess)):
        for index_sl in range(len(player_guess)):
            if player_guess[index_pg] == solution[index_sl] and index_pg != index_sl:
                if index_pg not in matches_index.keys() and index_sl not in matches_index.values():
                    wrong_place += 1
                    matches_index[index_pg] = index_sl

    return correct_place, wrong_place

# Definerar några variablar och startar det grafiska interfacet
row_index = 0
nr_of_guesses = 0
win = "Looser"

solution = solution_generator()
window = mmg.create_GUI()

# Main loopen
while nr_of_guesses < 6 and win == "Looser":

    player_guess = mmg.make_guess(row_index, window)
    nr_of_guesses += 1

    correct_place_wrong_place = correct_checker(player_guess, solution)
    correct_place = correct_place_wrong_place[0]
    wrong_place = correct_place_wrong_place[1]

    # Debugg
    print(correct_place, wrong_place)

    mmg.peg_feedback(row_index, correct_place, wrong_place, window)
    row_index += 1

    if correct_place == 4:
        win = "Winner"

mmg.gameover_screen(nr_of_guesses, win)