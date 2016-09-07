import subprocess as sub
import time

elapsed_home = 0
elapsed_away = 0
start_home = 0
start_away = 0
ball_home = False
ball_away = True  # Assuming that away team has the starting kick

# -----> * Filing * <-----

# ask the user the name of the game to create a .txt file
print("Enter game's name:")
name_file = input("")
name_file_string = str(name_file)
file_name = name_file_string + ".txt"

# create a writable .txt file
safile = open(file_name, "w")
safile.write("This game's stats were:\n")

# -----> * Team Separator * <-----

home_team, away_team, date_of_game = name_file_string.split('-')
teams = [home_team, away_team]

# -----> * Penalty Kicks Variables * <-----

# create a range from 0 to 1000
pk_range = range(0, 1000)
# list the range to be accessible
pk_list = list(pk_range)
pk_range_goal = range(0, 1000)
pk_list_goal = list(pk_range_goal)
pk_range_saved = range(0, 1000)
pk_list_saved = list(pk_range_saved)
pk_range_missed = range(0, 1000)
pk_list_missed = list(pk_range_missed)
pk_input = '''goal/saved/missed
'''
# a list of possible words that the user may type in order to record a stat
pk_words = ["pk", "penalty kick", "Penalty kick", "Penalty Kick", "penalty Kick", "PK", "Pk", "pK", "a1ta", "penalty kicks", "Penalty kicks", "Penalty Kicks", "penalty Kicks",  "penalty kick ", "Penalty kick ", "Penalty Kick ", "penalty Kick ", "penalty kicks ", "Penalty kicks ", "Penalty Kicks ", "penalty Kicks ", "01"]
goal_words = ["goal", "Goal", "GOAL", "goal ", "Goal ", "GOAL ",  "011"]
missed_words = ["missed", "Missed", "MISSED", "missed ", "Missed ", "MISSED ", "miss", "Miss", "MISS", "miss ", "Miss ", "MISS ", "012"]
saved_words = ["saved", "Saved", "SAVED", "saved ", "Saved ", "SAVED ", "save", "Save", "SAVE", "save ", "Save ", "SAVE ", "013"]


# -----> * Free Kicks Variables <-----


fk_range = range(0, 1000)
fk_list = list(fk_range)
fk_range_gd = range(0, 1000)
fk_list_gd = list(fk_range_gd)
fk_range_pd = range(0, 1000)
fk_list_pd = list(fk_range_pd)
fk_input = '''gd/pd
'''
fk_words = ["fk", "free kick", "Free kick", "Free Kick", "free Kick", "FK", "Fk", "fK", "a1ta", "free kicks", "Free kicks", "Free Kicks", "free Kicks",  "free kick ", "Free kick ", "Free Kick ", "free Kick ", "free kicks ", "Free kicks ", "Free Kicks ", "free Kicks ", "02"]
fk_gd_words = ["gd", "GD", "gd ", "GD ", "021"]
fk_pd_words = ["pd", "PD", "pd ", "PD ", "022"]

# -----> * Corner Kicks Variables * <-----


ck_range = range(0, 1000)
ck_list = list(ck_range)
ck_range_gd = range(0, 1000)
ck_list_gd = list(ck_range_gd)
ck_range_pd = range(0, 1000)
ck_list_pd = list(ck_range_pd)
ck_input = '''gd/pd
'''
ck_words = ["ck", "corner kick", "Corner kick", "Corner Kick", "corner Kick", "CK", "Ck", "cK", "a1ta", "corner kicks", "Corner kicks", "Corner Kicks", "corner Kicks",  "corner kick ", "Corner kick ", "Corner Kick ", "corner Kick ", "corner kicks ", "Corner kicks ", "Corner Kicks ", "corner Kicks ", "03"]
ck_gd_words = ["gd", "GD", "gd ", "GD ", "031"]
ck_pd_words = ["pd", "PD", "pd ", "PD ", "032"]

# -----> * Throw Ins Variables * <-----


ti_range = range(0, 1000)
ti_list = list(ti_range)
ti_range_gd = range(0, 1000)
ti_list_gd = list(ti_range_gd)
ti_range_pd = range(0, 1000)
ti_list_pd = list(ti_range_pd)
ti_input = '''gd/pd
'''
ti_words = ["ti", "throw in", "Throw in", "Throw In", "throw In", "TI", "Ti", "tI", "a1ta", "throw ins", "Throw ins", "Throw Ins", "throw Ins",  "throw in ", "Throw in ", "Throw In ", "throw In ", "throw ins ", "Throw ins ", "Throw Ins ", "throw Ins ", "04"]
ti_gd_words = ["gd", "GD", "gd ", "GD ", "041"]
ti_pd_words = ["pd", "PD", "pd ", "PD ", "042"]

# -----> * Crosses Variables * <-----


crosses_range = range(0, 1000)
crosses_list = list(crosses_range)
crosses_range_gd = range(0, 1000)
crosses_list_gd = list(crosses_range_gd)
crosses_range_pd = range(0, 1000)
crosses_list_pd = list(crosses_range_pd)
crosses_input = '''gd/pd
'''
cross_words = ["cross", "Cross", "Cross ", "cross ", "crosses", "Crosses", "Crosses ", "crosses ", "a1ta", "05"]
cross_gd_words = ["gd", "GD", "gd ", "GD ", "051"]
cross_pd_words = ["pd", "PD", "pd ", "PD ", "052"]

# -----> * True vs True Variables * <-----


v1_range = range(0, 1000)
v1_list = list(v1_range)
v1_range_w = range(0, 1000)
v1_list_w = list(v1_range_w)
v1_range_l = range(0, 1000)
v1_list_l = list(v1_range_l)
v1_input = '''w/l
'''
v1_words = ["1v1", "1vs1", "1 versus 1", "1 Versus 1", "1VS1", "1v1 ", "1vs1 ", "1 versus 1 ", "1 Versus 1 ", "1VS1 ", "a1ta", "06"]
w_words = ["w", "W", "w ", "W ", "won", "Won", "WON", "won ", "Won ", "WON ", "061"]
l_words = ["l", "L", "l ", "L ", "lost", "Lost", "LOST", "lost ", "Lost ", "LOST ", "062"]


# -----> * Shots Variables * <-----


shots_range = range(0, 1000)
shots_list = list(shots_range)
shots_range_gd = range(0, 1000)
shots_list_gd = list(shots_range_gd)
shots_range_pd = range(0, 1000)
shots_list_pd = list(shots_range_pd)
shots_input = '''on target/off target
'''
shot_words = ["shot", "Shot", "SHOT", "shot ", "Shot ", "SHOT ", "shots", "Shots", "SHOTS", "shots ", "Shots ", "SHOTS ", "a1ta", "07"]
shot_ont_words = ["on target", "On target", "On Target", "ON TARGET", "on target ", "On target ", "On Target ", "ON TARGET ", "ont", "ONT", "ont ", "ONT ", "071"]
shot_oft_words = ["off target", "Off target", "Off Target", "OFF TARGET", "off target ", "Off target ", "Off Target ", "OFF TARGET ", "oft", "OFT", "oft ", "OFT ", "072"]

# -----> * Headers Variables * <-----

headers_range = range(0, 1000)
headers_list = list(headers_range)
headers_range_gd = range(0, 1000)
headers_list_gd = list(headers_range_gd)
headers_range_pd = range(0, 1000)
headers_list_pd = list(headers_range_pd)
headers_input = '''on target/off target
'''
header_words = ["header", "Header", "HEADER", "header ", "Header ", "HEADER ", "header", "Header", "HEADER", "headers ", "Headers ", "HEADERS ", "a1ta", "08"]
header_ont_words = ["on target", "On target", "On Target", "ON TARGET", "on target ", "On target ", "On Target ", "ON TARGET ", "ont", "ONT", "ont ", "ONT ", "081"]
header_oft_words = ["off target", "Off target", "Off Target", "OFF TARGET", "off target ", "Off target ", "Off Target ", "OFF TARGET ", "oft", "OFT", "oft ", "OFT ", "082"]


# -----> * Saves Variables * <-----

saves_range = range(0, 1000)
saves_list = list(saves_range)
save_words = ["save", "Save", "SAVE", "saves", "Saves", "SAVES", "save ", "Save ", "SAVE ", "saves ", "Saves ", "SAVES ", "a1ta", "09"]


# -----> * Long Pass Variables * <-----
long_passes_range = range(0, 1000)
long_passes_list = list(long_passes_range)
long_passes_range_second_ball_defense = range(0, 1000)
long_passes_list_second_ball_defense = list(long_passes_range_second_ball_defense)
long_passes_range_third_ball_defense = range(0, 1000)
long_passes_list_third_ball_defense = list(long_passes_range_third_ball_defense)
long_passes_range_attack = range(0, 1000)
long_passes_list_attack = list(long_passes_range_attack)
long_passes_range_second_ball_attack = range(0, 1000)
long_passes_list_second_ball_attack = list(long_passes_range_second_ball_attack)
long_passes_range_third_ball_attack = range(0, 1000)
long_passes_list_third_ball_attack = list(long_passes_range_third_ball_attack)
long_passes_range_defense = range(0, 1000)
long_passes_list_defense = list(long_passes_range_defense)
long_passes_input_defense = '''second_ball/third_ball
'''
long_passes_input = '''attack/defence
'''
long_passes_input_attack = '''second ball/third ball
'''
long_pass_words = ["long pass", "Long pass", "long pass ", "Long Pass ", "LP", "lp", "LP ", "lp ", "long pass interception", "Long pass interception", "long pass interception ", "Long Pass Interception ", "LPI", "lpi", "LPI ", "lpi ", "a1ta", "10"]
lpi_attack_words = ["attack", "Attack", "ATTACK", "attack ", "Attack ", "ATTACK ", "a", "33", "3/3", "33 ", "3/3 ", "101"]
attack_sb_words = ["second ball", "Second ball", "SECOND BALL ", "second ball ", "Second ball ", "SECOND BALL ", "SB", "sb", "SB ", "sb ", "1011"]
attack_tb_words = ["third ball", "Third ball", "THIRD BALL ", "third ball ", "Third ball ", "THIRD BALL ", "TB", "tb", "TB ", "tb ", "1012"]
defense_words = ["defense", "Defense", "DEFENSE", "defense ", "Defense ", "DEFENSE ", "d", "13", "1/3", "13 ", "1/3", "102"]
defense_sb_words = ["second ball", "Second ball", "SECOND BALL ", "second ball ", "Second ball ", "SECOND BALL ", "SB", "sb", "SB ", "sb ", "1021"]
defense_tb_words = ["third ball", "Third ball", "THIRD BALL ", "third ball ", "Third ball ", "THIRD BALL ", "TB", "tb", "TB ", "tb ", "1022"]

# -----> * Possession Loss Variables * <-----
pl_range = range(0, 1000)
pl_list = list(pl_range)
pl_range_33 = range(0, 1000)
pl_list_33 = list(pl_range_33)
pl_range_33_23 = range(0, 1000)
pl_list_33_23 = list(pl_range_33_23)
pl_range_33_13 = range(0, 1000)
pl_list_33_13 = list(pl_range_33_13)
pl_range_23 = range(0, 1000)
pl_list_23 = list(pl_range_23)
pl_range_23_33 = range(0, 1000)
pl_list_23_33 = list(pl_range_23_33)
pl_range_23_13 = range(0, 1000)
pl_list_23_13 = list(pl_range_23_13)
pl_range_13 = range(0, 1000)
pl_list_13 = list(pl_range_13)
pl_range_13_33 = range(0, 1000)
pl_list_13_33 = list(pl_range_13_33)
pl_range_13_23 = range(0, 1000)
pl_list_13_23 = list(pl_range_13_33)
pl_input = '''3/3
2/3
1/3
'''
attack_print = '''
2/3
1/3
'''
midfield_print = '''
3/3
1/3
'''
defense_print = '''
3/3
2/3
'''
pl_words = ["pl", "PL", "Possession Loss", "Possession loss", "possession loss", "pl ", "PL ", "Possession Loss ", "Possession loss ", "possession loss ", "a1ta", "11"]
pl_attack_words = ["attack", "Attack", "ATTACK", "attack ", "Attack ", "ATTACK ", "a", "33", "3/3", "33 ", "3/3 ", "111"]
attack_midfield_words = ["midfield", "Midfield", "MIDFIELD", "midfield ", "Midfield ", "MIDFIELD ", "m", "23", "2/3", "23 ", "2/3 ", "1111"]
attack_defense_words = ["defense", "Defense", "DEFENSE", "defense ", "Defense ", "DEFENSE ", "d", "13", "1/3", "13 ", "1/3", "1112"]
pl_midfield_words = ["midfield", "Midfield", "MIDFIELD", "midfield ", "Midfield ", "MIDFIELD ", "m", "23", "2/3", "23 ", "2/3 ", "112"]
midfield_attack_words = ["attack", "Attack", "ATTACK", "attack ", "Attack ", "ATTACK ", "a", "33", "3/3", "33 ", "3/3 ", "1121"]
midfield_defense_words = ["defense", "Defense", "DEFENSE", "defense ", "Defense ", "DEFENSE ", "d", "13", "1/3", "13 ", "1/3", "1122"]
pl_defense_words = ["defense", "Defense", "DEFENSE", "defense ", "Defense ", "DEFENSE ", "d", "13", "1/3", "13 ", "1/3", "113"]
defense_attack_words = ["attack", "Attack", "ATTACK", "attack ", "Attack ", "ATTACK ", "a", "33", "3/3", "33 ", "3/3 ", "1131"]
defense_midfield_words = ["midfield", "Midfield", "MIDFIELD", "midfield ", "Midfield ", "MIDFIELD ", "m", "23", "2/3", "23 ", "2/3 ", "1132"]

# -----> * Offside * <-----

offside_range = range(0, 1000)
offside_list = list(offside_range)
offside_words = ["offside", "Offside", "offside ", "Offside ", "a1ta", "12"]


# -----> * Main Function * <-----


def body():
    # global each variable to be able to be referenced later when you print/write the total stat on each game at the end
    global string_number_pk_goal, string_number_pk_missed, string_number_pk_saved, string_number_pk, string_number_fk_gd, string_number_offside
    global string_number_fk_pd, string_number_fk, string_number_ck_pd, string_number_ck_gd, string_number_ck, ball_home
    global string_number_crosses_gd, string_number_crosses_pd, string_number_crosses, string_number_shots, ball_away
    global string_number_headers_pd, string_number_headers_gd, string_number_shots_pd, string_number_shots_gd
    global string_number_v1_l, string_number_v1, string_number_long_passes_second_ball, string_number_v1_w, start_home
    global string_number_long_passes_third_ball, string_number_long_passes, string_number_save, string_number_headers
    global string_number_ti_gd, string_number_ti, string_number_long_passes_defense, string_number_pl_23, start_away
    global string_number_long_passes_second_ball_defense, string_number_long_passes_third_ball_defense, end_home
    global string_number_long_passes_attack, string_number_long_passes_third_ball_attack, string_number_pl_23_13
    global string_number_long_passes_second_ball_attack, string_number_ti_pd, string_number_pl_13_33, end_away
    global string_number_pl_13_23, string_number_pl_13, midfield_input, string_number_pl_33_23, elapsed_away
    global string_number_pl_33, string_number_pl_23_33, string_number_pl_33_13, string_number_pl, elapsed_home

    # false each variable to declare if a stat was called before or not
    int_number_pk_goal = False
    int_number_pk_saved = False
    int_number_pk_missed = False
    int_number_pk = False

    int_number_fk_gd = False
    int_number_fk_pd = False
    int_number_fk = False

    int_number_ck_gd = False
    int_number_ck_pd = False
    int_number_ck = False

    int_number_ti_gd = False
    int_number_ti_pd = False
    int_number_ti = False

    int_number_crosses_gd = False
    int_number_crosses_pd = False
    int_number_crosses = False

    int_number_shots_gd = False
    int_number_shots_pd = False
    int_number_shots = False

    int_number_headers_gd = False
    int_number_headers_pd = False
    int_number_headers = False

    int_number_v1_w = False
    int_number_v1_l = False
    int_number_v1 = False

    int_number_long_passes_second_ball_attack = False
    int_number_long_passes_third_ball_attack = False
    int_number_long_passes_attack = False
    int_number_long_passes_second_ball_defense = False
    int_number_long_passes_third_ball_defense = False
    int_number_long_passes_defense = False
    int_number_long_passes = False

    int_number_saves = False

    int_number_pl_33_23 = False
    int_number_pl_33_13 = False
    int_number_pl_23_33 = False
    int_number_pl_23_13 = False
    int_number_pl_23 = False
    int_number_pl_33 = False
    int_number_pl_13_33 = False
    int_number_pl_13_23 = False
    int_number_pl_13 = False
    int_number_pl = False

    int_number_offside = False

    # it creates a while loop so the function will go on and on until a the user decides to quit the function
    while True:
        # the user decides which stat to record by calling it
        choice = input("")

        # -----> * Penalty Kicks Function * <-----

        # user inserts one of the words in the list
        if choice in pk_words:

            # the user decides whether a stat was successful or not
            good_bad_input_pk = input(pk_input)

            if good_bad_input_pk in goal_words:
                # take the first number on the list
                first_number_pk_goal = pk_list_goal[0]
                # remove the first number on the list. The first time it is called it deletes 0
                pk_list_goal.remove(first_number_pk_goal)
                # takes the next number on a list which is the number that will be called
                number_pk_goal = pk_list_goal[0]
                # strings the number so it will be printable/writable
                string_number_pk_goal = str(number_pk_goal)
                # true the integer so it knows it was called
                int_number_pk_goal = True
                # print a nice introduction and the time a stat was called
                print("Penalty Kick goal(s): ", string_number_pk_goal)

            elif good_bad_input_pk in save_words:
                first_number_pk_saved = pk_list_saved[0]
                pk_list_saved.remove(first_number_pk_saved)
                number_pk_saved = pk_list_saved[0]
                string_number_pk_saved = str(number_pk_saved)
                int_number_pk_saved = True
                print("Penalty Kick(s) saved: ", string_number_pk_saved)

            elif good_bad_input_pk in missed_words:
                first_number_pk_missed = pk_list_missed[0]
                pk_list_missed.remove(first_number_pk_missed)
                number_pk_missed = pk_list_missed[0]
                string_number_pk_missed = str(number_pk_missed)
                int_number_pk_missed = True
                print("Penalty Kick(s) missed: ", string_number_pk_missed)

            first_number_pk = pk_list[0]
            pk_list.remove(first_number_pk)
            number_pk = pk_list[0]
            string_number_pk = str(number_pk)
            int_number_pk = True
            print("Penalty Kick(s) : ", string_number_pk)

        # -----> * Free Kicks Function * <-----

        elif choice in fk_words:

            good_bad_input_fk = input(fk_input)

            if good_bad_input_fk in fk_gd_words:
                first_number_fk_gd = fk_list_gd[0]
                fk_list_gd.remove(first_number_fk_gd)
                number_fk_gd = fk_list_gd[0]
                string_number_fk_gd = str(number_fk_gd)
                int_number_fk_gd = True
                print("Free Kick(s) with a Good Delivery: ", string_number_fk_gd)

            elif good_bad_input_fk in fk_pd_words:
                first_number_fk_pd = fk_list_pd[0]
                fk_list_pd.remove(first_number_fk_pd)
                number_fk_pd = fk_list_pd[0]
                string_number_fk_pd = str(number_fk_pd)
                int_number_fk_pd = True
                print("Free Kick(s) with a Poor Delivery: ", string_number_fk_pd)

            first_number_fk = fk_list[0]
            fk_list.remove(first_number_fk)
            number_fk = fk_list[0]
            string_number_fk = str(number_fk)
            int_number_fk = True
            print("Free Kick(s)", string_number_fk)

        # -----> * Corner Kick Variables * <-----

        elif choice in ck_words:

            good_bad_input_ck = input(ck_input)

            if good_bad_input_ck in ck_gd_words:
                first_number_ck_gd = ck_list_gd[0]
                ck_list_gd.remove(first_number_ck_gd)
                number_ck_gd = ck_list_gd[0]
                string_number_ck_gd = str(number_ck_gd)
                int_number_ck_gd = True
                print("Corner Kick(s) with a Good Delivery: ", string_number_ck_gd)

            elif good_bad_input_ck in ck_pd_words:
                first_number_ck_pd = ck_list_pd[0]
                ck_list_pd.remove(first_number_ck_pd)
                number_ck_pd = ck_list_pd[0]
                string_number_ck_pd = str(number_ck_pd)
                int_number_ck_pd = True
                print("Corner Kick(s) with a Poor Delivery: ", string_number_ck_pd)

            first_number_ck = ck_list[0]
            ck_list.remove(first_number_ck)
            number_ck = ck_list[0]
            string_number_ck = str(number_ck)
            int_number_ck = True
            print("Corner Kick(s): ", string_number_ck)

        # -----> * Throw Ins Functions * <-----

        elif choice in ti_words:

            good_bad_input_ti = input(ti_input)

            if good_bad_input_ti in ti_gd_words:
                first_number_ti_gd = ti_list_gd[0]
                ti_list_gd.remove(first_number_ti_gd)
                number_ti_gd = ti_list_gd[0]
                string_number_ti_gd = str(number_ti_gd)
                int_number_ti_gd = True
                print("Throw In(s) with a Good Delivery: ", string_number_ti_gd)

            elif good_bad_input_ti in ti_pd_words:
                first_number_ti_pd = ti_list_pd[0]
                ti_list_pd.remove(first_number_ti_pd)
                number_ti_pd = ti_list_pd[0]
                string_number_ti_pd = str(number_ti_pd)
                int_number_ti_pd = True
                print("Throw In(s) with a Poor Delivery: ", string_number_ti_pd)

            first_number_ti = ti_list[0]
            ti_list.remove(first_number_ti)
            number_ti = ti_list[0]
            string_number_ti = str(number_ti)
            int_number_ti = True
            print("Throw In(s): ", string_number_ti)

        # -----> * Crosses Function * <-----

        elif choice in cross_words:

            good_bad_input_crosses = input(crosses_input)

            if good_bad_input_crosses in cross_gd_words:
                first_number_crosses_gd = crosses_list_gd[0]
                crosses_list_gd.remove(first_number_crosses_gd)
                number_crosses_gd = crosses_list_gd[0]
                string_number_crosses_gd = str(number_crosses_gd)
                int_number_crosses_gd = True
                print("Cross(es) with a Good Delivery: ", string_number_crosses_gd)

            elif good_bad_input_crosses in cross_pd_words:
                first_number_crosses_pd = crosses_list_pd[0]
                crosses_list_pd.remove(first_number_crosses_pd)
                number_crosses_pd = crosses_list_pd[0]
                string_number_crosses_pd = str(number_crosses_pd)
                int_number_crosses_pd = True
                print("Cross(es) with a Poor Delivery: ", string_number_crosses_pd)

            first_number_crosses = crosses_list[0]
            crosses_list.remove(first_number_crosses)
            number_crosses = crosses_list[0]
            string_number_crosses = str(number_crosses)
            int_number_crosses = True
            print("Cross(es): ", string_number_crosses)

        # -----> * 1 versus 1 Function * <-----

        elif choice in v1_words:

            good_bad_input_v1 = input(v1_input)

            if good_bad_input_v1 in w_words:
                first_number_v1_w = v1_list_w[0]
                v1_list_w.remove(first_number_v1_w)
                number_v1_w = v1_list_w[0]
                string_number_v1_w = str(number_v1_w)
                int_number_v1_w = True
                print("Won 1vs1: ", string_number_v1_w)

            elif good_bad_input_v1 in l_words:
                first_number_v1_l = v1_list_l[0]
                v1_list_l.remove(first_number_v1_l)
                number_v1_l = v1_list_l[0]
                string_number_v1_l = str(number_v1_l)
                int_number_v1_l = True
                print("Lost 1vs1: ", string_number_v1_l)

            first_number_v1 = v1_list[0]
            v1_list.remove(first_number_v1)
            number_v1 = v1_list[0]
            string_number_v1 = str(number_v1)
            int_number_v1 = True
            print("1vs1: ", string_number_v1)

        # -----> * Shots Function * <-----

        elif choice in shot_words:

            good_bad_input_shots = input(shots_input)

            if good_bad_input_shots in shot_ont_words:
                first_number_shots_gd = shots_list_gd[0]
                shots_list_gd.remove(first_number_shots_gd)
                number_shots_gd = shots_list_gd[0]
                string_number_shots_gd = str(number_shots_gd)
                int_number_shots_gd = True
                print("Shot(s) on target: ", string_number_shots_gd)

            elif good_bad_input_shots in shot_oft_words:
                first_number_shots_pd = shots_list_pd[0]
                shots_list_pd.remove(first_number_shots_pd)
                number_shots_pd = shots_list_pd[0]
                string_number_shots_pd = str(number_shots_pd)
                int_number_shots_pd = True
                print("Shot(s) off target: ", string_number_shots_pd)

            first_number_shots = shots_list[0]
            shots_list.remove(first_number_shots)
            number_shots = shots_list[0]
            string_number_shots = str(number_shots)
            int_number_shots = True
            print("Shot(s): ", string_number_shots)

        # -----> * Headers Function * <-----

        elif choice in header_words:

            good_bad_input_headers = input(headers_input)

            if good_bad_input_headers in header_ont_words:
                first_number_headers_gd = headers_list_gd[0]
                headers_list_gd.remove(first_number_headers_gd)
                number_headers_gd = headers_list_gd[0]
                string_number_headers_gd = str(number_headers_gd)
                int_number_headers_gd = True
                print("Header(s) on target: ", string_number_headers_gd)

            elif good_bad_input_headers in header_oft_words:
                first_number_headers_pd = headers_list_pd[0]
                headers_list_pd.remove(first_number_headers_pd)
                number_headers_pd = headers_list_pd[0]
                string_number_headers_pd = str(number_headers_pd)
                int_number_headers_pd = True
                print("Header(s) off target: ", string_number_headers_pd)

            first_number_headers = headers_list[0]
            headers_list.remove(first_number_headers)
            number_headers = headers_list[0]
            string_number_headers = str(number_headers)
            int_number_crosses = True
            print("Header(s): ", string_number_headers)

        # -----> * Long Passes * <-----

        elif choice in long_pass_words:

            attack_defense_input_long_pass = input(long_passes_input)
            sec_third_input_long_pass_attack = input(long_passes_input_attack)

            if attack_defense_input_long_pass in pl_attack_words:

                if sec_third_input_long_pass_attack in attack_sb_words:
                    first_number_long_passes_second_ball_attack = long_passes_list_second_ball_attack[0]
                    long_passes_list_second_ball_attack.remove(first_number_long_passes_second_ball_attack)
                    number_long_passes_second_ball_attack = long_passes_list_second_ball_attack[0]
                    string_number_long_passes_second_ball_attack = str(number_long_passes_second_ball_attack)
                    print("Second Ball Long Pass Interceptions on Attack:", string_number_long_passes_second_ball_attack)
                    int_number_long_passes_second_ball_attack = True

                elif sec_third_input_long_pass_attack in attack_tb_words:
                    first_number_long_passes_third_ball_attack = long_passes_list_third_ball_attack[0]
                    long_passes_list_third_ball_attack.remove(first_number_long_passes_third_ball_attack)
                    number_long_passes_third_ball_attack = long_passes_list_third_ball_attack[0]
                    string_number_long_passes_third_ball_attack = str(number_long_passes_third_ball_attack)
                    print("Third Ball Long Pass Interceptions on Attack:", string_number_long_passes_third_ball_attack)
                    int_number_long_passes_third_ball_attack = True

                first_number_long_passes_attack = long_passes_list_attack[0]
                long_passes_list_attack.remove(first_number_long_passes_attack)
                number_long_passes_attack = long_passes_list_attack[0]
                string_number_long_passes_attack = str(number_long_passes_attack)
                print("Long Pass Interceptions on Attack:", string_number_long_passes_attack)
                int_number_long_passes_attack = True

            elif attack_defense_input_long_pass in pl_defense_words:

                if sec_third_input_long_pass_attack in defense_sb_words:
                    first_number_long_passes_second_ball_defense = long_passes_list_second_ball_defense[0]
                    long_passes_list_second_ball_defense.remove(first_number_long_passes_second_ball_defense)
                    number_long_passes_second_ball_defense = long_passes_list_second_ball_defense[0]
                    string_number_long_passes_second_ball_defense = str(number_long_passes_second_ball_defense)
                    print("Second Ball Long Pass Interceptions on Defense:", string_number_long_passes_second_ball_defense)
                    int_number_long_passes_second_ball_defense = True

                elif sec_third_input_long_pass_attack in defense_tb_words:
                    first_number_long_passes_third_ball_defense = long_passes_list_third_ball_defense[0]
                    long_passes_list_third_ball_defense.remove(first_number_long_passes_third_ball_defense)
                    number_long_passes_third_ball_defense = long_passes_list_third_ball_defense[0]
                    string_number_long_passes_third_ball_defense = str(number_long_passes_third_ball_defense)
                    print("Third Ball Long Pass Interceptions on Defense:", string_number_long_passes_third_ball_defense)
                    int_number_long_passes_third_ball_defense = True

                first_number_long_passes_defense = long_passes_list_defense[0]
                long_passes_list_defense.remove(first_number_long_passes_defense)
                number_long_passes_defense = long_passes_list_defense[0]
                string_number_long_passes_defense = str(number_long_passes_defense)
                print("Long Pass Interceptions on Defense:", string_number_long_passes_defense)
                int_number_long_passes_defense = True

            first_number_long_passes = long_passes_list[0]
            long_passes_list.remove(first_number_long_passes)
            number_long_passes = long_passes_list[0]
            string_number_long_passes = str(number_long_passes)
            print("Long Pass Interceptions: ", string_number_long_passes)
            int_number_long_passes = True

        # -----> * Saves * <-----

        elif choice in save_words:
            first_number_save = saves_list[0]
            saves_list.remove(first_number_save)
            number_save = saves_list[0]
            string_number_save = str(number_save)
            int_number_saves = True
            print("Save(s)", string_number_save)

        # -----> * Possession Loss * <-----

        elif choice in pl_words:

            good_bad_input_pl = input(pl_input)

            if good_bad_input_pl in pl_attack_words:
                attack_input = input(attack_print)
                if attack_input in attack_midfield_words:
                    first_number_pl_33_23 = pl_list_33_23[0]
                    pl_list_33_23.remove(first_number_pl_33_23)
                    number_pl_33_23 = pl_list_33_23[0]
                    string_number_pl_33_23 = str(number_pl_33_23)
                    int_number_pl_33_23 = True
                    print("Possession lost on offence that came from Midfield: ", string_number_pl_33_23)
                elif attack_input in attack_defense_words:
                    first_number_pl_33_13 = pl_list_33_13[0]
                    pl_list_33_13.remove(first_number_pl_33_13)
                    number_pl_33_13 = pl_list_33_13[0]
                    string_number_pl_33_13 = str(number_pl_33_13)
                    int_number_pl_33_13 = True
                    print("Possession lost on offence that came from Defense: ", string_number_pl_33_13)
                first_number_pl_33 = pl_list_33[0]
                pl_list_33.remove(first_number_pl_33)
                number_pl_33 = pl_list_33[0]
                string_number_pl_33 = str(number_pl_33)
                int_number_pl_33 = True
                print("Possession lost on offence: ", string_number_pl_33)

            elif good_bad_input_pl in pl_midfield_words:

                midfield_input = input(midfield_print)

                if midfield_input in midfield_attack_words:
                    first_number_pl_23_33 = pl_list_23_33[0]
                    pl_list_23_33.remove(first_number_pl_23_33)
                    number_pl_23_33 = pl_list_23_33[0]
                    string_number_pl_23_33 = str(number_pl_23_33)
                    int_number_pl_23_33 = True
                    print("Possession lost on midfield that came from Offense: ", string_number_pl_23_33)
                elif midfield_input in midfield_defense_words:
                    first_number_pl_23_13 = pl_list_23_13[0]
                    pl_list_23_13.remove(first_number_pl_23_13)
                    number_pl_23_13 = pl_list_23_13[0]
                    string_number_pl_23_13 = str(number_pl_23_13)
                    int_number_pl_23_13 = True
                    print("Possession lost on midfield that came from Defense: ", string_number_pl_23_13)
                first_number_pl_23 = pl_list_23[0]
                pl_list_23.remove(first_number_pl_23)
                number_pl_23 = pl_list_23[0]
                string_number_pl_23 = str(number_pl_23)
                int_number_pl_23 = True
                print("Possession lost on midfield: ", string_number_pl_23)

            elif good_bad_input_pl in pl_defense_words:
                defense_input = input(defense_print)

                if defense_input in attack_defense_words:
                    first_number_pl_13_33 = pl_list_13_33[0]
                    pl_list_13_33.remove(first_number_pl_13_33)
                    number_pl_13_33 = pl_list_13_33[0]
                    string_number_pl_13_33 = str(number_pl_13_33)
                    int_number_pl_13_33 = True
                    print("Possession lost on defense that came from offense: ", string_number_pl_13_33)
                elif defense_input in defense_midfield_words:
                    first_number_pl_13_23 = pl_list_13_23[0]
                    pl_list_13_23.remove(first_number_pl_13_23)
                    number_pl_13_23 = pl_list_13_23[0]
                    string_number_pl_13_23 = str(number_pl_13_23)
                    int_number_pl_13_23 = True
                    print("Possession lost on defense that came from midfield: ", string_number_pl_13_23)

                first_number_pl_13 = pl_list_13[0]
                pl_list_13.remove(first_number_pl_13)
                number_pl_13 = pl_list_13[0]
                string_number_pl_13 = str(number_pl_13)
                int_number_pl_13 = True
                print("Possession lost on defense: ", string_number_pl_13)

            first_number_pl = pl_list[0]
            pl_list.remove(first_number_pl)
            number_pl = pl_list[0]
            string_number_pl = str(number_pl)
            int_number_pl = True
            print("Possession lost:", string_number_pl)

        elif choice in offside_words:

            first_number_offside = offside_list[0]
            offside_list.remove(first_number_offside)
            number_offside = offside_list[0]
            string_number_offside = str(number_offside)
            int_number_offside = True
            print("Offside(s):", string_number_offside)

        # -----> Help Function <-----

        # when the user does not know the commands a howto.txt will be popped up

        elif choice == "h":
            howto = "notepad.exe HOW TO USE.txt"
            sub.Popen(howto)

        if choice == home_team:
            if ball_home:
                continue
            else:
                ball_away = False
                ball_home = True
                start_home = time.time()
                elapsed_away += time.time() - start_away

        if choice == away_team:
            if ball_away:
                continue
            else:
                ball_away = True
                ball_home = False
                start_away = time.time()
                elapsed_home += time.time() - start_home

        # -----> * Quit Function * <-----

        # if the user wants to quit he types q to begin the process

        elif choice == "q":

            total_num = elapsed_home + elapsed_away
            percentage_num = 100 / total_num
            final_home = elapsed_home * percentage_num
            final_away = elapsed_away * percentage_num
            round_home = round(final_home, 1)
            round_away = round(final_away, 1)
            string_home = str(round_home)
            string_away = str(round_away)
            print_home = string_home + "%"
            print_away = string_away + "%"
            print(print_home)
            print(print_away)

            # start print out/write on file each stat
            # if it was called
            if int_number_pk_goal:
                # print the number of the stat
                print("Penalty Kick goal(s): ", string_number_pk_goal)
                # write on the file
                safile.write("Penalty Kick goal(s): ")
                safile.write(string_number_pk_goal)
            # if it was not called
            elif not int_number_pk_goal:
                # print/write the time that the stat was called was None
                print("Penalty Kick goal(s): 0")
                safile.write("\nPenalty Kick goal(s): 0")

            if int_number_pk_missed:
                print("Penalty Kick(s) missed: ", string_number_pk_missed)
                safile.write("\nPenalty Kick(s) missed: ")
                safile.write(string_number_pk_missed)
            elif not int_number_pk_missed:
                print("Penalty Kick(s) missed: 0")
                safile.write("\nPenalty Kick(s) missed: 0 ")

            if int_number_pk_saved:
                print("Penalty Kick(s) saved: ", string_number_pk_saved)
                safile.write("\nPenalty Kick(s) saved: ")
                safile.write(string_number_pk_saved)
            elif not int_number_pk_saved:
                print("Penalty Kick(s) saved: 0")
                safile.write("\nPenalty Kick(s) saved: 0")

            if int_number_pk:
                print("Penalty Kick(s): ", string_number_pk)
                safile.write("\nPenalty Kick(s): ")
                safile.write(string_number_pk)
            elif not int_number_pk:
                print("Penalty Kick(s): 0")
                safile.write("\nPenalty Kick(s): 0")

            if int_number_fk_gd:
                print("Free Kick(s) with Good Delivery: ", string_number_fk_gd)
                safile.write("\nFree Kick(s) with Good Delivery: ")
                safile.write(string_number_fk_gd)
            elif not int_number_fk_gd:
                print("Free Kick(s) with Good Delivery: 0")
                safile.write("\nFree Kick(s) with Good Delivery: 0")

            if int_number_fk_pd:
                print("Free Kick(s) with Good Delivery: ", string_number_fk_pd)
                safile.write("\nFree Kick(s) with Poor Delivery: ")
                safile.write(string_number_fk_pd)
            elif not int_number_fk_pd:
                print("Free Kick(s) with Poor Delivery: 0")
                safile.write("\nFree Kick(s) with Poor Delivery: 0")

            if int_number_fk:
                print("Free Kick(s): ", string_number_fk)
                safile.write("\nFree Kick(s): ")
                safile.write(string_number_fk)
            elif not int_number_fk:
                print("Free Kick(s): 0")
                safile.write("\nFree Kick(s): 0")

            if int_number_ck_gd:
                print("Corner Kick(s) with Good Delivery: ", string_number_ck_gd)
                safile.write("\nCorner Kick(s) with Good Delivery: ")
                safile.write(string_number_ck_gd)
            elif not int_number_ck_gd:
                print("Corner Kick(s) with Good Delivery: 0")
                safile.write("\nCorner Kick(s) with Good Delivery: ")

            if int_number_ck_pd:
                print("Corner Kick(s) with Poor Delivery: ", string_number_ck_pd)
                safile.write("\nCorner Kick(s) with Good Delivery: ")
                safile.write(string_number_ck_pd)
            elif not int_number_ck_pd:
                print("Corner Kick(s) with Poor Delivery: 0")
                safile.write("\nCorner Kick(s) with Good Delivery: 0")

            if int_number_ck:
                print("Corner Kick(s): ", string_number_ck)
                safile.write("\nCorner Kick(s): ")
                safile.write(string_number_ck)
            elif not int_number_ck:
                print("Corner Kick(s): 0")
                safile.write("\nCorner Kick(s): 0")

            if int_number_ti_gd:
                print("Throw In(s) with Good Delivery: ", string_number_ti_gd)
                safile.write("\nThrow In(s) with Good Delivery: ")
                safile.write(string_number_ti_gd)
            elif not int_number_ti_gd:
                print("Throw In(s) with Good Delivery: 0")
                safile.write("\nThrow In(s) with Good Delivery: 0")

            if int_number_ti_pd:
                print("Throw In(s) with Poor Delivery: ", string_number_ti_pd)
                safile.write("\nThrow In(s) with Poor Delivery: ")
                safile.write(string_number_ti_pd)
            elif not int_number_ti_pd:
                print("Throw In(s) with Poor Delivery: 0")
                safile.write("\nThrow In(s) with Poor Delivery: 0")

            if int_number_ti:
                print("Throw In(s): ", string_number_ti)
                safile.write("\nThrow In(s): ")
                safile.write(string_number_ti)
            elif not int_number_ti:
                print("Throw In(s): 0")
                safile.write("\nThrow In(s): 0")

            if int_number_crosses_gd:
                print("Cross(es) with Good Delivery: ", string_number_crosses_gd)
                safile.write("\nCross(es) with Good Delivery: ")
                safile.write(string_number_crosses_gd)
            elif not int_number_crosses_gd:
                print("Cross(es) with Good Delivery: 0")
                safile.write("\nCross(es) with Good Delivery: ")

            if int_number_crosses_pd:
                print("Cross(es) with Poor Delivery: ", string_number_crosses_pd)
                safile.write("\nCross(es) with Poor Delivery: ")
                safile.write(string_number_crosses_pd)
            elif not int_number_crosses_pd:
                print("Cross(es) with Poor Delivery: 0")
                safile.write("\nCross(es) with Poor Delivery: 0")

            if int_number_crosses:
                print("Cross(es): ", string_number_crosses)
                safile.write("\nCross(es): ")
                safile.write(string_number_crosses)
            elif not int_number_crosses:
                print("Cross(es): 0")
                safile.write("\nCross(es): 0")

            if int_number_shots_gd:
                print("Shot(s) on Target: ", string_number_shots_gd)
                safile.write("\nShot(s) on Target: ")
                safile.write(string_number_shots_gd)
            elif not int_number_shots_gd:
                print("Shot(s) on Target: 0")
                safile.write("\nShot(s) on Target: 0")

            if int_number_shots_pd:
                print("Shot(s) off Target: ", string_number_shots_pd)
                safile.write("\nShot(s) off Target: ")
                safile.write(string_number_shots_pd)
            elif not int_number_shots_pd:
                print("Shot(s) off Target: 0")
                safile.write("\nShot(s) off Target: 0")

            if int_number_shots:
                print("Shot(s): ", string_number_shots)
                safile.write("\nShot(s): ")
                safile.write(string_number_shots)
            elif not int_number_shots:
                print("Shot(s): 0")
                safile.write("\nShot(s): 0")

            if int_number_headers_gd:
                print("Header(s) on Target: ", string_number_headers_gd)
                safile.write("\nHeader(s) on Target: ")
                safile.write(string_number_headers_gd)
            elif not int_number_headers_gd:
                print("Header(s) on Target: 0")
                safile.write("\nHeader(s) on Target: 0")

            if int_number_headers_pd:
                print("Header(s) off Target: ", string_number_headers_pd)
                safile.write("\nHeader(s) off Target: ")
                safile.write(string_number_headers_pd)
            elif not int_number_headers_pd:
                print("Header(s) off Target: 0")
                safile.write("\nHeader(s) off Target: 0")

            if int_number_headers:
                print("Header(s): ", string_number_headers)
                safile.write("\nHeader(s): ")
                safile.write(string_number_headers)
            elif not int_number_headers:
                print("Header(s): 0")
                safile.write("\nHeader(s): 0")

            if int_number_v1_w:
                print("1vs1 Won: ", string_number_v1_w)
                safile.write("\n1vs1 Won: ")
                safile.write(string_number_v1_w)
            elif not int_number_v1_w:
                print("1vs1 Won: 0")
                safile.write("\n1vs1 Won: 0")

            if int_number_v1_l:
                print("1vs1 Lost: ", string_number_v1_l)
                safile.write("\n1vs1 Lost: ")
                safile.write(string_number_v1_l)
            elif not int_number_v1_l:
                print("1vs1 Lost: 0")
                safile.write("\n1vs1 Lost: 0")

            if int_number_v1:
                print("1vs1: ", string_number_v1)
                safile.write("\n1vs1: ")
                safile.write(string_number_v1)
            elif not int_number_v1:
                print("1vs1: 0")
                safile.write("\n1vs1: 0")

            if int_number_long_passes_second_ball_attack:
                print("Second Ball Long Pass Interceptions on Attack: ", string_number_long_passes_second_ball_attack)
                safile.write("\nSecond Ball Long Pass Interceptions on Attack: ")
                safile.write(string_number_long_passes_second_ball_attack)
            elif not int_number_long_passes_second_ball_attack:
                print("Second Ball Long Pass Interceptions on Attack: 0")
                safile.write("\nSecond Ball Long Pass Interceptions on Attack: 0")

            if int_number_long_passes_third_ball_attack:
                print("Third Ball Long Pass Interceptions on Attack: ", string_number_long_passes_third_ball_attack)
                safile.write("\nThird Ball Long Pass Interceptions on Attack: ")
                safile.write(string_number_long_passes_third_ball_attack)
            elif not int_number_long_passes_third_ball_attack:
                print("Third Ball Long Pass Interceptions on Attack: 0")
                safile.write("\nThird Ball Long Pass Interceptions on Attack: 0")

            if int_number_long_passes_attack:
                print("Long Pass Interceptions on Attack: ", string_number_long_passes_attack)
                safile.write("\nLong Pass Interceptions on Attack: ")
                safile.write(string_number_long_passes_attack)
            elif not int_number_long_passes_attack:
                print("Long Pass Interceptions on Attack: 0")
                safile.write("\nLong Pass Interceptions on Attack: 0")

            if int_number_long_passes_second_ball_defense:
                print("Second Ball Long Pass Interceptions on Defense: ", string_number_long_passes_second_ball_defense)
                safile.write("\nSecond Ball Long Pass Interceptions on Defense: ")
                safile.write(string_number_long_passes_second_ball_defense)
            elif not int_number_long_passes_second_ball_defense:
                print("Second Ball Long Pass Interceptions on Defense: 0")
                safile.write("\nSecond Ball Long Pass Interceptions on Defense: 0")

            if int_number_long_passes_third_ball_defense:
                print("Third Ball Long Pass Interceptions on Defense: ", string_number_long_passes_third_ball_defense)
                safile.write("\nThird Ball Long Pass Interceptions on Defense: ")
                safile.write(string_number_long_passes_third_ball_defense)
            elif not int_number_long_passes_third_ball_defense:
                print("Third Ball Long Pass Interceptions on Defense: 0")
                safile.write("\nThird Ball Long Pass Interceptions on Defense: 0")

            if int_number_long_passes_defense:
                print("Long Pass Interceptions on Defense: ", string_number_long_passes_defense)
                safile.write("\nLong Pass Interceptions on Defense: ")
                safile.write(string_number_long_passes_defense)
            elif not int_number_long_passes_defense:
                print("Long Pass Interceptions on Defense: 0")
                safile.write("\nLong Pass Interceptions on Defense: 0")

            if int_number_long_passes:
                print("Long Pass Interceptions: ", string_number_long_passes)
                safile.write("\nLong Pass Interceptions: ")
                safile.write(string_number_long_passes)
            elif not int_number_long_passes:
                print("Long Pass Interceptions: 0")
                safile.write("\nLong Pass Interceptions: 0")

            if int_number_saves:
                print("Saves: ", string_number_save)
                safile.write("\nSaves: ")
                safile.write(string_number_save)
            elif not int_number_saves:
                print("\nSaves: 0")
                safile.write("\nSaves: 0")

            if int_number_pl_33_23:
                print("Possession(s) lost on offence that came from midfield: ", string_number_pl_33_23)
                safile.write("\nPossession(s) lost on offence that came from midfield: ")
                safile.write(string_number_pl_33_23)
            elif not int_number_pl_33_23:
                print("Possession lost on offence that came from midfield: 0")
                safile.write("\nPossession lost on offence that came from midfield: 0")

            if int_number_pl_33_13:
                print("Possession(s) lost on offence that came from defense: ", string_number_pl_33_13)
                safile.write("\nPossession(s) lost on offence that came from defense: ")
                safile.write(string_number_pl_33_13)
            elif not int_number_pl_33_13:
                print("Possession lost on offence that came from defense: 0")
                safile.write("\nPossession lost on offence that came from defense: 0")

            if int_number_pl_33:
                print("Possession(s) lost on offence: ", string_number_pl_33)
                safile.write("\nPossession(s) lost on offence: ")
                safile.write(string_number_pl_33)
            elif not int_number_pl_33:
                print("Possession lost on offence: 0")
                safile.write("\nPossession lost on offence: 0")

            if int_number_pl_23_33:
                print("Possession(s) lost on midfield that came from offense: ", string_number_pl_23_33)
                safile.write("\nPossession(s) lost on midfield that came from offense: ")
                safile.write(string_number_pl_23_33)
            elif not int_number_pl_23_33:
                print("Possession lost on midfield that came from offense: 0")
                safile.write("\nPossession lost on midfield that came from offense: 0")

            if int_number_pl_23_13:
                print("Possession(s) lost on midfield that came from defense: ", string_number_pl_23_13)
                safile.write("\nPossession(s) lost on midfield that came from defense: ")
                safile.write(string_number_pl_23_13)
            elif not int_number_pl_23_13:
                print("Possession lost on midfield that came from defense: 0")
                safile.write("\nPossession lost on midfield that came from defense: 0")

            if int_number_pl_23:
                print("Possession(s) lost on midfield: ", string_number_pl_23)
                safile.write("\nPossession(s) lost on midfield: ")
                safile.write(string_number_pl_23)
            elif not int_number_pl_23:
                print("Possession lost on midfield: 0")
                safile.write("\nPossession lost on midfield: 0")

            if int_number_pl_13_33:
                print("Possession(s) lost on defense that came from offense: ", string_number_pl_13_33)
                safile.write("\nPossession(s) lost on defense that came from offense: ")
                safile.write(string_number_pl_13_33)
            elif not int_number_pl_13_33:
                print("Possession lost on defense that came from offense: 0")
                safile.write("\nPossession lost on defense that came from offense: 0")

            if int_number_pl_13_23:
                print("Possession(s) lost on defense that came from offense: ", string_number_pl_13_23)
                safile.write("\nPossession(s) lost on defense that came from offense: ")
                safile.write(string_number_pl_13_23)
            elif not int_number_pl_13_23:
                print("Possession lost on defense that came from offense: 0")
                safile.write("\nPossession lost on defense that came from offense: 0")

            if int_number_pl_13:
                print("Possession(s) lost on defense: ", string_number_pl_13)
                safile.write("\nPossession(s) lost on defense: ")
                safile.write(string_number_pl_13)
            elif not int_number_pl_13:
                print("Possession lost on defense: 0")
                safile.write("\nPossession lost on defense: 0")

            if int_number_pl:
                print("Possession(s) lost: ", string_number_pl)
                safile.write("\nPossession(s) lost: ")
                safile.write(string_number_pl)
            elif not int_number_pl:
                print("Possessions lost: 0")
                safile.write("\nPossession lost: 0")

            if int_number_offside:
                print("Offside(s): ", string_number_offside)
                safile.write("\nOffside(s): ")
                safile.write(string_number_offside)
            elif not int_number_offside:
                print("Offside(s) h2: 0")
                safile.write("\nOffside(s): 0 ")

            # close the file
            safile.close()

            # break the while loop, quiting the function
            break


if ball_away:
    start_away = time.time()
else:
    start_home = time.time()

body()
