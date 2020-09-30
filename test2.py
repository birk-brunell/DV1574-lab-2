player_guess = [3, 4, 5, 6]
solution = [2, 3, 4, 5]

one_pg = player_guess.count(1)
one_sl = solution.count(1)
two_pg = player_guess.count(2)
two_sl = solution.count(2)
three_pg = player_guess.count(3)
three_sl = solution.count(3)
four_pg = player_guess.count(4)
four_sl = solution.count(4)
five_pg = player_guess.count(5)
five_sl = solution.count(5)

ones = one_pg + one_sl
twos = one_pg + one_sl
threes = one_pg + one_sl
fours = one_pg + one_sl
fives = one_pg + one_sl

print(ones, twos, threes, fours, fives)