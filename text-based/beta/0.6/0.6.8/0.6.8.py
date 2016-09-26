import subprocess as sub
import time

# -----> * Filing * <-----

# ask the user the name of the game to create a .txt file
print("Enter game's name:")
name_file = input("")
name_file_string = str(name_file)
file_name = name_file_string + ".txt"

# create a writable .txt file
safile = open(file_name, "w")

# -----> * Team Separator * <-----

home, away, date = name_file_string.split('-')

# -----> * Timing * <-----

# Referencing variables so the are available to use in function
elapsed_home = 0
elapsed_away = 0
start_home = 0
start_away = 0
ball_home = False
ball_away = True  # Assuming that away team has the starting kick


def body():
    # -----> * Introduction * <-----

    intro_part_one = '''
Welcome to Siball-Analysis v0.6.5-beta. If you do not know the commands '''

    intro_part_two = '''
type help to open the howto file.
I hope you enjoy the game between %s and %s.
Are you recording for %s or %s?'''

    intro_one = intro_part_one + intro_part_two
    # assigning the home and away teams to the intro so the intro is user friendly
    print(intro_one % (home, away, home, away))
    home_or_away = input()

    # asking the user which team are they recording stats for

    if True:
        if home_or_away == home:
            team = home
            intro_two = '''
Great! I hope %s has a good game!
                '''
            print(intro_two % team)

        elif home_or_away == away:
            team = away
            intro_two = '''
Great! I hope %s has a good game!
            '''
            print(intro_two % team)

    # -----> * Colors Variables * <-----

    # adding color to the output
    # red is if something did not go well ex. missed penalty kick
    red = "\033[1;31;50m%s"

    # blue if something went well ex. goal from penalty kick
    blue = "\033[1;34;50m%s"

    # white for general things like the total of penalty kicks
    white = "\033[1;38;50m%s"

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
    goal_pk, saved_pk, missed_pk = pk_input.split("/")
    # a list of possible words that the user may type in order to record stats

    pk_words = ["pk", "penalty kick", "Penalty kick", "Penalty Kick",
                "penalty Kick", "PK", "Pk", "pK", "penalty kicks",
                "Penalty kicks", "Penalty Kicks", "penalty Kicks",
                "penalty kick "]

    goal_words = ["goal", "Goal", "GOAL", "goal ", "Goal ", "GOAL "]

    missed_words = ["missed", "Missed", "MISSED", "missed ", "Missed ",
                    "MISSED ", "miss", "Miss", "MISS", "miss ",
                    "Miss ", "MISS "]

    saved_words = ["saved", "Saved", "SAVED", "saved ", "Saved ", "SAVED ",
                   "save", "Save", "SAVE", "save ", "Save ", "SAVE "]

    # -----> * Free Kicks Variables <-----

    fk_range = range(0, 1000)
    fk_list = list(fk_range)

    fk_range_gd = range(0, 1000)
    fk_list_gd = list(fk_range_gd)

    fk_range_pd = range(0, 1000)
    fk_list_pd = list(fk_range_pd)

    fk_input = '''gd/pd
    '''
    gd_fk, pd_fk = fk_input.split("/")

    fk_words = ["fk", "free kick", "Free kick", "Free Kick", "free Kick",
                "Free kicks", "Free Kicks", "free Kicks", "free kick ", "FK",
                "free kicks ", "Free kicks ", "Free Kicks ", "free Kicks ",
                "Fk", "free kicks", "Free kick ", "Free Kick ", "free Kick "]

    fk_gd_words = ["gd", "GD", "gd ", "GD "]

    fk_pd_words = ["pd", "PD", "pd ", "PD "]

    # -----> * Corner Kicks Variables * <-----

    ck_range = range(0, 1000)
    ck_list = list(ck_range)
    ck_range_gd = range(0, 1000)
    ck_list_gd = list(ck_range_gd)
    ck_range_pd = range(0, 1000)
    ck_list_pd = list(ck_range_pd)

    ck_input = '''gd/pd
    '''
    gd_ck, pd_ck = ck_input.split("/")

    ck_words = ["ck", "corner kick", "Corner kick", "Corner Kick",
                "corner kicks", "Corner kicks", "Corner Kicks",
                "Corner Kick ", "corner Kick ", "corner kicks ",
                "corner Kick", "CK", "Ck", "cK", "Corner kicks ",
                "Corner Kicks ", "corner Kicks ""Corner kicks ",
                "Corner Kicks ", "corner Kicks ", "Corner kick ",
                "corner Kicks", "corner kick "]

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
    gd_ti, pd_ti = ti_input.split("/")

    ti_words = ["ti", "throw in", "Throw in", "Throw In", "throw In", "TI",
                "Throw ins", "Throw Ins", "throw Ins", "throw in ",
                "Throw ins ", "Throw Ins ", "throw Ins ", "throw In ",
                "Ti", "tI", "throw ins", "Throw in ", "Throw In ",
                "throw ins "]

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
    gd_cross, pd_cross = crosses_input.split("/")

    cross_words = ["cross", "Cross", "Cross ", "cross ", "crosses", "Crosses",
                   "Crosses ", "crosses "]

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
    w_v1, l_v1 = v1_input.split("/")

    v1_words = ["1v1", "1vs1", "1 versus 1", "1 Versus 1", "1VS1", "1v1 ",
                "1vs1 ", "1 versus 1 ", "1 Versus 1 ", "1VS1 "]

    w_words = ["w", "W", "w ", "W ", "won", "Won", "WON", "won ", "Won ",
               "WON "]

    l_words = ["l", "L", "l ", "L ", "lost", "Lost", "LOST", "lost ", "Lost ",
               "LOST ", "062"]

    # -----> * Shots Variables * <-----

    shots_range = range(0, 1000)
    shots_list = list(shots_range)

    shots_range_gd = range(0, 1000)
    shots_list_gd = list(shots_range_gd)

    shots_range_pd = range(0, 1000)
    shots_list_pd = list(shots_range_pd)

    shots_range_bs = range(0, 1000)
    shots_list_bs = list(shots_range_bs)

    shots_input = '''on target/off target/blocked shots
    '''
    ont_shot, oft_shot, blocked_shot = shots_input.split("/")

    shot_words = ["shot", "Shot", "SHOT", "shot ", "Shot ", "SHOT ", "shots",
                  "SHOTS ", "Shots", "SHOTS", "shots ", "Shots "]

    shot_ont_words = ["on target", "On target", "On Target", "ON TARGET",
                      "ON TARGET ", "ont", "ONT", "ont ", "ONT ",
                      "on target ", "On target ", "On Target "]

    shot_oft_words = ["off target", "Off target", "Off Target", "OFF TARGET",
                      "Off Target ", "OFF TARGET ", "oft", "OFT", "oft ",
                      "OFT ", "off target ", "Off target "]
    blocked_shot_words = ["blocked shot", "Blocked Shot", "BLOCKED SHOT",
                          "blocked shot ", "Blocked Shot ", "BLOCKED SHOT ",
                          "BS", "bs", "BS ", "bs "]

    # -----> * Headers Variables * <-----

    headers_range = range(0, 1000)
    headers_list = list(headers_range)

    headers_range_gd = range(0, 1000)
    headers_list_gd = list(headers_range_gd)

    headers_range_pd = range(0, 1000)
    headers_list_pd = list(headers_range_pd)

    headers_input = '''on target/off target
    '''
    ont_header, oft_header = headers_input.split("/")

    header_words = ["header", "Header", "HEADER", "header ", "Header ",
                    "headers ", "Headers ", "HEADERS ", "a1ta", "HEADER ",
                    "header", "Header", "HEADER"]

    header_ont_words = ["on target", "On target", "On Target", "ON TARGET",
                        "ON TARGET ", "ont", "ONT", "ont ", "ONT ",
                        "on target ", "On target ", "On Target "]

    header_oft_words = ["off target", "Off target", "Off Target",
                        "Off Target ", "OFF TARGET ", "oft", "OFT", "oft ",
                        "OFT ", "OFF TARGET", "off target ", "Off target "]

    # -----> * Saves Variables * <-----

    saves_range = range(0, 1000)
    saves_list = list(saves_range)

    save_words = ["save", "Save", "SAVE", "saves", "Saves", "SAVES", "save ",
                  "SAVES "]

    # -----> * Long Pass Variables * <-----
    lpi_range = range(0, 1000)
    lpi_list = list(lpi_range)

    lpi_range_sb_defense = range(0, 1000)
    lpi_list_sb_defense = list(lpi_range_sb_defense)

    lpi_range_tb_defense = range(0, 1000)
    lpi_list_tb_defense = list(lpi_range_tb_defense)

    lpi_range_attack = range(0, 1000)
    lpi_list_attack = list(lpi_range_attack)

    lpi_range_sb_attack = range(0, 1000)
    lpi_list_sb_attack = list(lpi_range_sb_attack)

    lpi_range_tb_attack = range(0, 1000)
    lpi_list_tb_attack = list(lpi_range_tb_attack)

    lpi_range_defense = range(0, 1000)
    lpi_list_defense = list(lpi_range_defense)

    lpi_input_defense = '''sb/tb
'''
    lpi_input = '''attack/defence
'''
    lpi_input_attack = '''second ball/third ball
'''

    attack_lpi, defense_lpi = lpi_input.split("/")

    long_pass_words = ["long pass", "Long pass", "long pass ", "Long Pass ",
                       "long pass interception", "Long pass interception",
                       "Long Pass Interception ", "LPI", "lpi", "LPI ", "LP",
                       "lp", "LP ", "lp ", "long pass interception ", "lpi "]

    lpi_attack_words = ["attack", "Attack", "ATTACK", "attack ", "Attack ",
                        "ATTACK ", "a", "33", "3/3", "33 ", "3/3 "]

    attack_sb_words = ["second ball", "Second ball", "SECOND BALL ",
                       "SB", "sb", "SB ", "sb ", "second ball ",
                       "Second ball ", "SECOND BALL "]

    attack_tb_words = ["third ball", "Third ball", "THIRD BALL ",
                       "tb", "TB ", "tb ", "third ball ", "Third ball ",
                       "THIRD BALL ", "TB"]

    lpi_defense_words = ["defense", "Defense", "DEFENSE", "defense ", "1/3",
                         "Defense ", "DEFENSE ", "d", "13", "1/3", "13 "]

    defense_sb_words = ["second ball", "Second ball", "SECOND BALL ", "SB",
                        "second ball ", "Second ball ", "SECOND BALL ",
                        "sb", "SB ", "sb "]

    defense_tb_words = ["third ball", "Third ball", "THIRD BALL ",
                        "third ball ", "Third ball ", "THIRD BALL ", "TB",
                        "tb", "TB ", "tb "]

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
    pl_list_13_23 = list(pl_range_13_23)

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
    pl_words = ["pl", "PL", "Possession Loss", "Possession loss",
                "possession loss", "pl ", "PL ", "Possession Loss ",
                "Possession loss ", "possession loss "]

    pl_attack_words = ["attack", "Attack", "ATTACK", "attack ", "Attack ",
                       "ATTACK ", "a", "33", "3/3", "33 ", "3/3 "]

    attack_midfield_words = ["midfield", "Midfield", "MIDFIELD", "midfield ",
                             "Midfield ", "MIDFIELD ", "m", "23",
                             "2/3", "23 ", "2/3 "]

    attack_defense_words = ["defense", "Defense", "DEFENSE", "defense ",
                            "Defense ", "DEFENSE ", "d", "13", "1/3",
                            "13 ", "1/3"]

    pl_midfield_words = ["midfield", "Midfield", "MIDFIELD", "midfield ",
                         "Midfield ", "MIDFIELD ", "m", "23", "2/3",
                         "23 ", "2/3 "]

    midfield_attack_words = ["attack", "Attack", "ATTACK", "attack ",
                             "Attack ", "ATTACK ", "a", "33", "3/3", "33 ",
                             "3/3 "]

    midfield_defense_words = ["defense", "Defense", "DEFENSE", "defense ",
                              "Defense ", "DEFENSE ", "d", "13", "1/3",
                              "13 ", "1/3"]

    pl_defense_words = ["defense", "Defense", "DEFENSE", "defense ",
                        "Defense ", "DEFENSE ", "d", "13", "1/3", "13 ",
                        "1/3"]

    defense_attack_words = ["attack", "Attack", "ATTACK", "attack ",
                            "Attack ", "ATTACK ", "a", "33", "3/3", "33 ",
                            "3/3 "]

    defense_midfield_words = ["midfield", "Midfield", "MIDFIELD", "midfield ",
                              "Midfield ", "MIDFIELD ", "m", "23",
                              "2/3", "23 ", "2/3 "]

    # -----> * Offside * <-----

    offside_range = range(0, 1000)
    offside_list = list(offside_range)

    offside_words = ["offside", "Offside", "offside ", "Offside "]

    # -----> * Transition * <-----

    pw_range_33_home = range(0, 1000)
    pw_list_33_home = list(pw_range_33_home)

    pw_range_home = range(0, 1000)
    pw_list_home = list(pw_range_home)

    pw_range_23_33_home = range(0, 1000)
    pw_list_23_33_home = list(pw_range_23_33_home)

    pw_range_13_home = range(0, 1000)
    pw_list_13_home = list(pw_range_13_home)

    pw_range_13_33_home = range(0, 1000)
    pw_list_13_33_home = list(pw_range_13_33_home)

    pw_range_13_23_home = range(0, 1000)
    pw_list_13_23_home = list(pw_range_13_23_home)

    pw_input = home + "/" + away + '''
'''

    home_input_home = '''3/3
2/3
1/3
'''

    defense_pw_print_home = '''3/3
2/3
'''

    pw_words = ["transition", "Transition", "Transition ",
                "transition"]

    pw_midfield_words_home = ["midfield", "Midfield", "MIDFIELD",
                              "midfield ", "Midfield ", "MIDFIELD ",
                              "m", "23", "2/3", "23 ", "2/3 "]

    pw_defense_words_home = ["defense", "Defense", "DEFENSE",
                             "defense ", "Defense ", "DEFENSE ", "d",
                             "13", "1/3", "13 ", "1/3", "113"]

    defense_attack_pw_words_home = ["attack", "Attack", "ATTACK",
                                    "attack ", "Attack ", "ATTACK ",
                                    "3/3", "a", "33", "33 ", "3/3 "]

    defense_midfield_pw_words_home = ["midfield", "Midfield",
                                      "MIDFIELD", "midfield ",
                                      "Midfield ", "MIDFIELD ",
                                      "23", "2/3", "23 ", "2/3 ", "m"]

    pw_attack_words_home = ["attack", "Attack", "ATTACK", "attack ",
                            "Attack ", "ATTACK ", "a", "33", "3/3",
                            "33 ", "3/3"]

    pw_range_33_away = range(0, 1000)
    pw_list_33_away = list(pw_range_33_away)
    # ---------------------------------500th line---------------------------------

    pw_range_away = range(0, 1000)
    pw_list_away = list(pw_range_away)

    pw_range_23_33_away = range(0, 1000)
    pw_list_23_33_away = list(pw_range_23_33_away)

    pw_range_13_away = range(0, 1000)
    pw_list_13_away = list(pw_range_13_away)

    pw_range_13_33_away = range(0, 1000)
    pw_list_13_33_away = list(pw_range_13_33_away)

    pw_range_13_23_away = range(0, 1000)
    pw_list_13_23_away = list(pw_range_13_23_away)

    away_input_away = '''3/3
2/3
1/3
'''

    defense_pw_print_away = '''3/3
2/3
'''

    pw_midfield_words_away = ["midfield", "Midfield", "MIDFIELD",
                              "midfield ", "Midfield ", "MIDFIELD ",
                              "23", "m", "2/3", "23 ", "2/3 "]

    pw_defense_words_away = ["defense", "Defense", "DEFENSE",
                             "defense ", "Defense ", "DEFENSE ", "d",
                             "1/3", "13", "13 ", "1/3"]

    defense_attack_pw_words_away = ["attack", "Attack", "ATTACK",
                                    "attack ", "Attack ", "ATTACK ",
                                    "33 ", "3/3 ", "a", "33", "3/3"]

    defense_midfield_pw_words_away = ["midfield", "Midfield",
                                      "MIDFIELD", "midfield ",
                                      "Midfield ", "MIDFIELD ",
                                      "m", "23", "2/3", "23 ", "2/3 "]

    pw_attack_words_away = ["attack", "Attack", "ATTACK", "attack ",
                            "Attack ", "ATTACK ", "a", "33", "3/3",
                            "33 ", "3/3"]

    # -----> * Goalkeeper Turnover * <-----

    gkto_range = range(0, 1000)
    gkto_list = list(gkto_range)
    gkto_words = ["gkto", "Goalkeeper Turnover", "GOALKEEPER TURNOVER",
                  "gkto ", "Goalkeeper Turnover ", "GOALKEEPER TURNOVER "]

    kp_range = range(0, 1000)
    kp_list = list(kp_range)
    kp_words = ["kp", "Key Pass", "KEY PASS",
                "kp ", "Key Pass ", "KEY PASS "]

    # global each variable to be able to be referenced later when you
    # print/write the total stat on each game at the end
    global string_number_pk_goal, string_number_pk_missed
    global string_number_fk_pd, string_number_fk, string_number_ck_pd
    global string_number_crosses_gd, string_number_crosses_pd
    global string_number_headers_pd, string_number_headers_gd
    global string_number_v1_l, string_number_v1, string_number_v1_w
    global string_number_lpi_tb, string_number_lpi
    global string_number_ti_gd, string_number_ti, string_number_pl_23
    global string_number_lpi_sb_defense
    global string_number_lpi_attack, string_number_pl_23_13
    global string_number_lpi_sb_attack, string_number_ti_pd
    global string_number_pl_13_23, string_number_pl_13, midfield_input
    global string_number_pl_33, string_number_pl_23_33, string_number_pl_33_13
    global string_number_pk_saved, string_number_pk, string_number_fk_gd
    global string_number_offside, string_number_pw_23_33_away
    global string_number_ck_gd, string_number_ck, end_away, start_home, team
    global string_number_pw_33_home, string_number_shots_pd
    global string_number_crosses, string_number_shots, elapsed_away, ball_away
    global string_number_pl, string_number_transition
    global string_number_pw_13_23_away, string_number_shots_gd
    global string_number_pw_23_33_home, elapsed_home
    global string_number_pw_home, string_number_pw_33_away
    global string_number_lpi_sb, string_number_pl_13_33
    global string_number_pw_23_33, string_number_pw_13_33_away
    global string_number_save, start_away, string_number_headers
    global string_number_lpi_defense, string_number_pw_23
    global string_number_pw_away, string_number_pw_13_33_home
    global string_number_lpi_tb_defense, string_number_kp
    global string_number_pw_13_33, string_number_pw_13_away
    global string_number_lpi_tb_attack, string_number_gkto
    global string_number_pl_33_23, string_number_pw_13
    global string_number_pw_13_23, string_number_pw_13_23_home
    global string_number_pw_13_home, end_home, ball_home

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
    int_number_shots_bs = False
    int_number_shots = False

    int_number_headers_gd = False
    int_number_headers_pd = False
    int_number_headers = False

    int_number_v1_w = False
    int_number_v1_l = False
    int_number_v1 = False

    int_number_lpi_sb_attack = False
    int_number_lpi_tb_attack = False
    int_number_lpi_attack = False
    int_number_lpi_sb_defense = False
    int_number_lpi_tb_defense = False
    int_number_lpi_defense = False
    int_number_lpi = False

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

    int_number_transition = False
    int_number_pw_13_home = False
    int_number_pw_13_23_home = False
    int_number_pw_13_33_home = False
    int_number_pw_23_33_home = False
    int_number_pw_33_home = False
    int_number_pw_home = False

    int_number_pw_13_away = False
    int_number_pw_13_23_away = False
    int_number_pw_13_33_away = False
    int_number_pw_23_33_away = False

    int_number_pw_33_away = False
    int_number_pw_away = False

    int_number_gkto = False

    # it creates a while loop so the function will go on and on until
    # the user decides to quit the function
    while True:
        # the user decides which stat to record by calling it
        choice = input()

        # -----> * Penalty Kicks Function * <-----

        # user inserts one of the words in the list
        if choice in pk_words:
            # the user decides whether a stat was successful or not
            print(blue % goal_pk, red % saved_pk, red % missed_pk)
            good_bad_input_pk = input()

            if good_bad_input_pk in goal_words:

                # take the first number on the list
                first_number_pk_goal = pk_list_goal[0]
                # remove the first number on the lis
                # the first time it is called it deletes 0
                pk_list_goal.remove(first_number_pk_goal)
                # takes the next number on a list which is the number
                # that will be called
                number_pk_goal = pk_list_goal[0]
                # strings the number so it will be printable/writable
                string_number_pk_goal = str(number_pk_goal)
                # true the integer so it knows it was called
                int_number_pk_goal = True
                pk_goal_1 = "Penalty Kick goal(s): "
                pk_goal_2 = string_number_pk_goal
                pk_print_string_goal = pk_goal_1 + pk_goal_2
                # print a nice introduction and the time a stat was called
                print(blue % pk_print_string_goal)

            elif good_bad_input_pk in saved_words:

                first_number_pk_saved = pk_list_saved[0]
                pk_list_saved.remove(first_number_pk_saved)
                number_pk_saved = pk_list_saved[0]
                string_number_pk_saved = str(number_pk_saved)
                int_number_pk_saved = True
                pk_saved_1 = "Penalty Kick(s) saved: "
                pk_saved_2 = string_number_pk_saved
                pk_print_string_saved = pk_saved_1 + pk_saved_2
                print(red % pk_print_string_saved)

            elif good_bad_input_pk in missed_words:

                first_number_pk_missed = pk_list_missed[0]
                pk_list_missed.remove(first_number_pk_missed)
                number_pk_missed = pk_list_missed[0]
                string_number_pk_missed = str(number_pk_missed)
                int_number_pk_missed = True
                pk_miss_1 = "Penalty Kick(s) missed: "
                pk_miss_2 = string_number_pk_missed
                pk_print_string_missed = pk_miss_1 + pk_miss_2
                print(red % pk_print_string_missed)

            first_number_pk = pk_list[0]
            pk_list.remove(first_number_pk)
            number_pk = pk_list[0]
            string_number_pk = str(number_pk)
            int_number_pk = True
            pk_print_string = "Penalty Kick(s) : " + string_number_pk
            print(white % pk_print_string)

        # -----> * Free Kicks Function * <-----

        elif choice in fk_words:
            print(blue % gd_fk, red % pd_fk)
            good_bad_input_fk = input()

            if good_bad_input_fk in fk_gd_words:

                first_number_fk_gd = fk_list_gd[0]
                fk_list_gd.remove(first_number_fk_gd)
                number_fk_gd = fk_list_gd[0]
                string_number_fk_gd = str(number_fk_gd)
                int_number_fk_gd = True
                fk_string_gd_1 = "Free Kick(s) with a Good Delivery: "
                fk_string_gd_2 = string_number_fk_gd
                fk_print_string_gd = fk_string_gd_1 + fk_string_gd_2
                print(blue % fk_print_string_gd)

            elif good_bad_input_fk in fk_pd_words:

                first_number_fk_pd = fk_list_pd[0]
                fk_list_pd.remove(first_number_fk_pd)
                number_fk_pd = fk_list_pd[0]
                string_number_fk_pd = str(number_fk_pd)
                int_number_fk_pd = True
                fk_string_pd_1 = "Free Kick(s) with a Poor Delivery: "
                fk_string_pd_2 = string_number_fk_pd
                fk_print_string_pd = fk_string_pd_1 + fk_string_pd_2
                print(red % fk_print_string_pd)

            first_number_fk = fk_list[0]
            fk_list.remove(first_number_fk)
            number_fk = fk_list[0]
            string_number_fk = str(number_fk)
            int_number_fk = True
            fk_print_string = "Free Kick(s)" + string_number_fk
            print(white % fk_print_string)

        # -----> * Corner Kick Variables * <-----

        elif choice in ck_words:

            print(blue % gd_ck, red % pd_ck)
            good_bad_input_ck = input()

            if good_bad_input_ck in ck_gd_words:

                first_number_ck_gd = ck_list_gd[0]
                ck_list_gd.remove(first_number_ck_gd)
                number_ck_gd = ck_list_gd[0]
                string_number_ck_gd = str(number_ck_gd)
                int_number_ck_gd = True
                ck_string_gd_1 = "Corner Kick(s) with a Good Delivery: "
                ck_string_gd_2 = string_number_ck_gd
                ck_print_string_gd = ck_string_gd_1 + ck_string_gd_2
                print(blue % ck_print_string_gd)

            elif good_bad_input_ck in ck_pd_words:

                first_number_ck_pd = ck_list_pd[0]
                ck_list_pd.remove(first_number_ck_pd)
                number_ck_pd = ck_list_pd[0]
                string_number_ck_pd = str(number_ck_pd)
                int_number_ck_pd = True
                ck_string_pd_1 = "Corner Kick(s) with a Poor Delivery: "
                ck_string_pd_2 = string_number_ck_pd
                ck_print_string_pd = ck_string_pd_1 + ck_string_pd_2
                print(red % ck_print_string_pd)

            first_number_ck = ck_list[0]
            ck_list.remove(first_number_ck)
            number_ck = ck_list[0]
            string_number_ck = str(number_ck)
            int_number_ck = True
            ck_print_string = "Corner Kick(s): " + string_number_ck
            print(white % ck_print_string)

        # -----> * Throw Ins Functions * <-----

        elif choice in ti_words:

            print(blue % gd_ti, red % pd_ti)
            good_bad_input_ti = input()

            if good_bad_input_ti in ti_gd_words:

                first_number_ti_gd = ti_list_gd[0]
                ti_list_gd.remove(first_number_ti_gd)
                number_ti_gd = ti_list_gd[0]
                string_number_ti_gd = str(number_ti_gd)
                int_number_ti_gd = True
                ti_string_gd_1 = "Throw In(s) with a Good Delivery: "
                ti_string_gd_2 = string_number_ti_gd
                ti_print_string_gd = ti_string_gd_1 + ti_string_gd_2
                print(blue % ti_print_string_gd)

            elif good_bad_input_ti in ti_pd_words:

                first_number_ti_pd = ti_list_pd[0]
                ti_list_pd.remove(first_number_ti_pd)
                number_ti_pd = ti_list_pd[0]
                string_number_ti_pd = str(number_ti_pd)
                int_number_ti_pd = True
                ti_string_pd_1 = "Throw In(s) with a Poor Delivery: "
                ti_string_pd_2 = string_number_ti_pd
                ti_print_string_pd = ti_string_pd_1 + ti_string_pd_2
                print(red % ti_print_string_pd)

            first_number_ti = ti_list[0]
            ti_list.remove(first_number_ti)
            number_ti = ti_list[0]
            string_number_ti = str(number_ti)
            int_number_ti = True
            ti_print_string = "Throw In(s): " + string_number_ti
            print(white % ti_print_string)

        # -----> * Crosses Function * <-----

        elif choice in cross_words:

            print(blue % gd_cross, red % pd_cross)
            good_bad_input_crosses = input()

            if good_bad_input_crosses in cross_gd_words:

                first_number_crosses_gd = crosses_list_gd[0]
                crosses_list_gd.remove(first_number_crosses_gd)
                number_crosses_gd = crosses_list_gd[0]
                string_number_crosses_gd = str(number_crosses_gd)
                int_number_crosses_gd = True
                cross_string_gd_1 = "Cross(es) with a Good Delivery: "
                cross_string_gd_2 = string_number_crosses_gd
                cross_print_string_gd = cross_string_gd_1 + cross_string_gd_2
                print(blue % cross_print_string_gd)

            elif good_bad_input_crosses in cross_pd_words:

                first_number_crosses_pd = crosses_list_pd[0]
                crosses_list_pd.remove(first_number_crosses_pd)
                number_crosses_pd = crosses_list_pd[0]
                string_number_crosses_pd = str(number_crosses_pd)
                int_number_crosses_pd = True
                cross_string_pd_1 = "Cross(es) with a Poor Delivery: "
                cross_string_pd_2 = string_number_crosses_pd
                cross_print_string_pd = cross_string_pd_1 + cross_string_pd_2
                print(red % cross_print_string_pd)

            first_number_crosses = crosses_list[0]
            crosses_list.remove(first_number_crosses)
            number_crosses = crosses_list[0]
            string_number_crosses = str(number_crosses)
            int_number_crosses = True
            cross_print_string = "Cross(es): " + string_number_crosses
            print(white % cross_print_string)

        # -----> * 1 versus 1 Function * <-----

        elif choice in v1_words:

            print(blue % w_v1, red % l_v1)
            good_bad_input_v1 = input()

            if good_bad_input_v1 in w_words:

                first_number_v1_w = v1_list_w[0]
                v1_list_w.remove(first_number_v1_w)
                number_v1_w = v1_list_w[0]
                string_number_v1_w = str(number_v1_w)
                int_number_v1_w = True
                v1_print_string_w = "Won 1vs1: " + string_number_v1_w
                print(blue % v1_print_string_w)

            elif good_bad_input_v1 in l_words:

                first_number_v1_l = v1_list_l[0]
                v1_list_l.remove(first_number_v1_l)
                number_v1_l = v1_list_l[0]
                string_number_v1_l = str(number_v1_l)
                int_number_v1_l = True
                v1_print_string_l = "Lost 1vs1: " + string_number_v1_l
                print(red % v1_print_string_l)

            first_number_v1 = v1_list[0]
            v1_list.remove(first_number_v1)
            number_v1 = v1_list[0]
            string_number_v1 = str(number_v1)
            int_number_v1 = True
            v1_print_string = "1vs1: " + string_number_v1
            print(white % v1_print_string)

        # -----> * Shots Function * <-----

        elif choice in shot_words:

            print(blue % ont_shot, red % oft_shot, red % blocked_shot)
            good_bad_input_shots = input()

            if good_bad_input_shots in shot_ont_words:

                first_number_shots_gd = shots_list_gd[0]
                shots_list_gd.remove(first_number_shots_gd)
                number_shots_gd = shots_list_gd[0]
                string_number_shots_gd = str(number_shots_gd)
                int_number_shots_gd = True
                shot_string_ont_1 = "Shot(s) on target: "
                shot_string_ont_2 = string_number_shots_gd
                shot_print_string_ont = shot_string_ont_1 + shot_string_ont_2
                print(blue % shot_print_string_ont)

            elif good_bad_input_shots in shot_oft_words:

                first_number_shots_pd = shots_list_pd[0]
                shots_list_pd.remove(first_number_shots_pd)
                number_shots_pd = shots_list_pd[0]
                string_number_shots_pd = str(number_shots_pd)
                int_number_shots_pd = True
                shot_string_oft_1 = "Shot(s) off target: "
                shot_string_oft_2 = string_number_shots_pd
                shot_print_string_oft = shot_string_oft_1 + shot_string_oft_2
                print(red % shot_print_string_oft)

            elif good_bad_input_shots in blocked_shot_words:
                first_number_shots_bs = shots_list_bs[0]
                shots_list_bs.remove(first_number_shots_bs)
                number_shots_bs = shots_list_bs[0]
                string_number_shots_bs = str(number_shots_bs)
                int_number_shots_bs = True
                shot_string_bs_1 = "Blocked Shot(s): "
                shot_string_bs_2 = string_number_shots_bs
                shot_print_string_bs = shot_string_bs_1 + shot_string_bs_2
                print(red % shot_print_string_bs)

            first_number_shots = shots_list[0]
            shots_list.remove(first_number_shots)
            number_shots = shots_list[0]
            string_number_shots = str(number_shots)
            int_number_shots = True
            shot_print_string = "Shot(s): " + string_number_shots
            print(white % shot_print_string)

        # -----> * Headers Function * <-----

        elif choice in header_words:

            print(blue % ont_header, red % oft_header)
            good_bad_input_headers = input()

            if good_bad_input_headers in header_ont_words:

                first_number_headers_gd = headers_list_gd[0]
                headers_list_gd.remove(first_number_headers_gd)
                number_headers_gd = headers_list_gd[0]
                string_number_headers_gd = str(number_headers_gd)
                int_number_headers_gd = True
                header_ont_1 = "Header(s) on target: "
                header_ont_2 = string_number_headers_gd
                header_print_string_ont = header_ont_1 + header_ont_2
                print(blue % header_print_string_ont)

            elif good_bad_input_headers in header_oft_words:

                first_number_headers_pd = headers_list_pd[0]
                headers_list_pd.remove(first_number_headers_pd)
                number_headers_pd = headers_list_pd[0]
                string_number_headers_pd = str(number_headers_pd)
                int_number_headers_pd = True
                header_oft_1 = "Header(s) off target: "
                header_oft_2 = string_number_headers_pd
                header_print_string_oft = header_oft_1 + header_oft_2
                print(red % header_print_string_oft)

            first_number_headers = headers_list[0]
            headers_list.remove(first_number_headers)
            number_headers = headers_list[0]
            string_number_headers = str(number_headers)
            int_number_crosses = True
            header_print_string = "Header(s): ", white % string_number_headers
            print(white % header_print_string)

        # -----> * Long Passes * <-----

        # -----------------------------1000th line-----------------------------

        elif choice in long_pass_words:

            print(blue % attack_lpi, red % defense_lpi)
            attack_defense_input_long_pass = input()

            if attack_defense_input_long_pass in lpi_attack_words:

                print(blue % lpi_input_attack)
                sec_third_input_long_pass_attack = input()

                if sec_third_input_long_pass_attack in attack_sb_words:
                    first_number_lpi_sb_attack = lpi_list_sb_attack[0]
                    lpi_list_sb_attack.remove(first_number_lpi_sb_attack)
                    number_lpi_sb_attack = lpi_list_sb_attack[0]
                    string_number_lpi_sb_attack = str(number_lpi_sb_attack)
                    lpi_attack_sb_1 = "Second Ball Long Pass Interceptions " \
                                      "on Attack: "
                    lpi_attack_sb_2 = string_number_lpi_sb_attack
                    lpi_print_attack_sb = lpi_attack_sb_1 + lpi_attack_sb_2
                    print(white % lpi_print_attack_sb)
                    int_number_lpi_sb_attack = True

                elif sec_third_input_long_pass_attack in attack_tb_words:
                    first_number_lpi_tb_attack = lpi_list_tb_attack[0]
                    lpi_list_tb_attack.remove(first_number_lpi_tb_attack)
                    number_lpi_tb_attack = lpi_list_tb_attack[0]
                    string_number_lpi_tb_attack = str(number_lpi_tb_attack)
                    lpi_attack_tb_1 = "Third Ball Long Pass " \
                                      "Interceptions on Attack: "
                    lpi_attack_tb_2 = string_number_lpi_tb_attack
                    lpi_print_attack_tb = lpi_attack_tb_1 + lpi_attack_tb_2
                    print(white % lpi_print_attack_tb)
                    int_number_lpi_tb_attack = True

                first_number_lpi_attack = lpi_list_attack[0]
                lpi_list_attack.remove(first_number_lpi_attack)
                number_lpi_attack = lpi_list_attack[0]
                string_number_lpi_attack = str(number_lpi_attack)
                lpi_attack_1 = "Long Pass Interceptions on Attack: "
                lpi_attack_2 = string_number_lpi_attack
                lpi_print_string_attack = lpi_attack_1 + lpi_attack_2
                print(white % lpi_print_string_attack)
                int_number_lpi_attack = True

            elif attack_defense_input_long_pass in lpi_defense_words:

                print(red % lpi_input_defense)
                sec_third_input_long_pass_defense = input()

                if sec_third_input_long_pass_defense in defense_sb_words:
                    first_number_lpi_sb_defense = lpi_list_sb_defense[0]
                    lpi_list_sb_defense.remove(first_number_lpi_sb_defense)
                    number_lpi_sb_defense = lpi_list_sb_defense[0]
                    string_number_lpi_sb_defense = str(number_lpi_sb_defense)
                    lpi_defense_sb_1 = "Second Ball Long Pass " \
                                       "Interceptions on Defense: "
                    lpi_defense_sb_2 = string_number_lpi_sb_defense
                    lpi_print_defense_sb = lpi_defense_sb_1 + lpi_defense_sb_2
                    print(white % lpi_print_defense_sb)
                    int_number_lpi_sb_defense = True

                elif sec_third_input_long_pass_defense in defense_tb_words:
                    first_number_lpi_tb_defense = lpi_list_tb_defense[0]
                    lpi_list_tb_defense.remove(first_number_lpi_tb_defense)
                    number_lpi_tb_defense = lpi_list_tb_defense[0]
                    string_number_lpi_tb_defense = str(number_lpi_tb_defense)
                    lpi_defense_tb_1 = "Third Ball Long Pass " \
                                       "Interceptions on Defense: "
                    lpi_defense_tb_2 = string_number_lpi_tb_defense
                    lpi_print_defense_tb = lpi_defense_tb_1 + lpi_defense_tb_2
                    print(white % lpi_print_defense_tb)
                    int_number_lpi_tb_defense = True

                first_number_lpi_defense = lpi_list_defense[0]
                lpi_list_defense.remove(first_number_lpi_defense)
                number_lpi_defense = lpi_list_defense[0]
                string_number_lpi_defense = str(number_lpi_defense)
                pk_goal_1 = "Long Pass Interceptions on Defense:"
                pk_goal_2 = string_number_lpi_defense
                pk_print_string_goal = pk_goal_1 + pk_goal_2
                print(white % pk_print_string_goal)
                int_number_lpi_defense = True

            first_number_lpi = lpi_list[0]
            lpi_list.remove(first_number_lpi)
            number_lpi = lpi_list[0]
            string_number_lpi = str(number_lpi)
            lpi_print_string = "Long Pass Interceptions: " + string_number_lpi
            print(white % lpi_print_string)
            int_number_lpi = True

        # -----> * Saves * <-----

        elif choice in save_words:
            first_number_save = saves_list[0]
            saves_list.remove(first_number_save)
            number_save = saves_list[0]
            string_number_save = str(number_save)
            int_number_saves = True
            saves_print_string = "Save(s)" + string_number_save
            print(white % saves_print_string)

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
                    pl_33_23_1 = "Possession lost on offence " \
                                 "that came from Midfield: "
                    pl_33_23_2 = string_number_pl_33_23
                    pl_print_string_33_23 = pl_33_23_1 + pl_33_23_2
                    print(white % pl_print_string_33_23)

                elif attack_input in attack_defense_words:
                    first_number_pl_33_13 = pl_list_33_13[0]
                    pl_list_33_13.remove(first_number_pl_33_13)
                    number_pl_33_13 = pl_list_33_13[0]
                    string_number_pl_33_13 = str(number_pl_33_13)
                    int_number_pl_33_13 = True
                    pl_33_13_1 = "Possession lost on offence" \
                                 " that came from Defense: "
                    pl_33_13_2 = string_number_pl_33_13
                    pl_print_string_33_13 = pl_33_13_1 + pl_33_13_2
                    print(white % pl_print_string_33_13)

                first_number_pl_33 = pl_list_33[0]
                pl_list_33.remove(first_number_pl_33)
                number_pl_33 = pl_list_33[0]
                string_number_pl_33 = str(number_pl_33)
                int_number_pl_33 = True
                pl_33_1 = "Possession lost on offence: "
                pl_33_2 = string_number_pl_33
                pl_print_string_33 = pl_33_1 + pl_33_2
                print(white % pl_print_string_33)

            elif good_bad_input_pl in pl_midfield_words:

                midfield_input = input(midfield_print)

                if midfield_input in midfield_attack_words:
                    first_number_pl_23_33 = pl_list_23_33[0]
                    pl_list_23_33.remove(first_number_pl_23_33)
                    number_pl_23_33 = pl_list_23_33[0]
                    string_number_pl_23_33 = str(number_pl_23_33)
                    int_number_pl_23_33 = True
                    pl_23_33_1 = "Possession lost on midfield that " \
                                 "came from Offense: "
                    pl_23_33_2 = string_number_pl_23_33
                    pl_print_string_23_33 = pl_23_33_1 + pl_23_33_2
                    print(white % pl_print_string_23_33)

                elif midfield_input in midfield_defense_words:
                    first_number_pl_23_13 = pl_list_23_13[0]
                    pl_list_23_13.remove(first_number_pl_23_13)
                    number_pl_23_13 = pl_list_23_13[0]
                    string_number_pl_23_13 = str(number_pl_23_13)
                    int_number_pl_23_13 = True
                    pl_23_13_1 = "Possession lost on midfield " \
                                 "that came from Defense: "
                    pl_23_13_2 = string_number_pl_23_13
                    pl_print_string_23_13 = pl_23_13_1 + pl_23_13_2
                    print(white % pl_print_string_23_13)

                first_number_pl_23 = pl_list_23[0]
                pl_list_23.remove(first_number_pl_23)
                number_pl_23 = pl_list_23[0]
                string_number_pl_23 = str(number_pl_23)
                int_number_pl_23 = True
                pl_23_1 = "Possession lost on midfield: "
                pl_23_2 = string_number_pl_23
                pl_print_string_23 = pl_23_1 + pl_23_2
                print(white % pl_print_string_23)

            elif good_bad_input_pl in pl_defense_words:
                defense_input = input(defense_print)

                if defense_input in defense_attack_words:

                    first_number_pl_13_33 = pl_list_13_33[0]
                    pl_list_13_33.remove(first_number_pl_13_33)
                    number_pl_13_33 = pl_list_13_33[0]
                    string_number_pl_13_33 = str(number_pl_13_33)
                    int_number_pl_13_33 = True
                    pl_13_33_1 = "Possession lost on defense " \
                                 "that came from offense: "
                    pl_13_33_2 = string_number_pl_13_33
                    pl_print_string_13_33 = pl_13_33_1 + pl_13_33_2
                    print(white % pl_print_string_13_33)

                elif defense_input in defense_midfield_words:

                    first_number_pl_13_23 = pl_list_13_23[0]
                    pl_list_13_23.remove(first_number_pl_13_23)
                    number_pl_13_23 = pl_list_13_23[0]
                    string_number_pl_13_23 = str(number_pl_13_23)
                    int_number_pl_13_23 = True
                    pl_13_23_1 = "Possession lost on defense that came " \
                                 "from midfield: "
                    pl_13_23_2 = string_number_pl_13_23
                    pl_print_string_13_23 = pl_13_23_1 + pl_13_23_2
                    print(white % pl_print_string_13_23)

                first_number_pl_13 = pl_list_13[0]
                pl_list_13.remove(first_number_pl_13)
                number_pl_13 = pl_list_13[0]
                string_number_pl_13 = str(number_pl_13)
                int_number_pl_13 = True
                pl_13_1 = "Possession lost on defense: "
                pl_13_2 = string_number_pl_13
                pl_print_string_13 = pl_13_1 + pl_13_2
                print(white % pl_print_string_13)

            first_number_pl = pl_list[0]
            pl_list.remove(first_number_pl)
            number_pl = pl_list[0]
            string_number_pl = str(number_pl)
            int_number_pl = True
            pl_print_string = "Possession lost:" + string_number_pl
            print(white % pl_print_string)

        elif choice in offside_words:

            first_number_offside = offside_list[0]
            offside_list.remove(first_number_offside)
            number_offside = offside_list[0]
            string_number_offside = str(number_offside)
            int_number_offside = True
            offside_print_string = "Offside(s):" + string_number_offside
            print(white % offside_print_string)

        elif choice in pw_words:

            attack_defense_input_transition = input(pw_input)

            if attack_defense_input_transition == home:

                home_input_pw_home = input(home_input_home)

                if home_input_pw_home in pw_attack_words_home:

                    first_number_pw_33_home = pw_list_33_home[0]
                    pw_list_33_home.remove(first_number_pw_33_home)
                    number_pw_33_home = pw_list_33_home[0]
                    string_number_pw_33_home = str(number_pw_33_home)
                    int_number_pw_33_home = True
                    pw_33_home_1 = "Offensive Transitions: "
                    pw_33_home_2 = string_number_pw_33_home
                    pw_print_string_33_home = pw_33_home_1 + pw_33_home_2
                    print(white % pw_print_string_33_home)

                elif home_input_pw_home in pw_midfield_words_home:

                    first_number_pw_23_33_home = pw_list_23_33_home[0]
                    pw_list_23_33_home.remove(first_number_pw_23_33_home)
                    int_number_pw_23_33_home = True
                    number_pw_23_33_home = pw_list_23_33_home[0]
                    string_number_pw_23_33_home = str(number_pw_23_33_home)
                    pw_23_33_home_1 = "Offensive Transition that came from " \
                                      "midfield: "
                    pw_23_33_home_2 = string_number_pw_23_33_home
                    pw_print_23_33_home = pw_23_33_home_1 + pw_23_33_home_2
                    print(white % pw_print_23_33_home)

                elif home_input_pw_home in pw_defense_words_home:

                    defense_input_home = input(defense_pw_print_home)

                    if defense_input_home in defense_attack_pw_words_home:

                        first_number_pw_13_33_home = pw_list_13_33_home[0]
                        pw_list_13_33_home.remove(first_number_pw_13_33_home)
                        number_pw_13_33_home = pw_list_13_33_home[0]
                        string_number_pw_13_33_home = str(number_pw_13_33_home)
                        int_number_pw_13_33_home = True
                        pw_13_33_home_1 = "Offensive Transition that came " \
                                          "from defense: "
                        pw_13_33_home_2 = string_number_pw_13_33_home
                        pw_print_13_33_home = pw_13_33_home_1 + pw_13_33_home_2
                        print(white % pw_print_13_33_home)

                    elif defense_input_home in defense_midfield_pw_words_home:

                        first_number_pw_13_23_home = pw_list_13_23_home[0]
                        pw_list_13_23_home.remove(first_number_pw_13_23_home)
                        number_pw_13_23_home = pw_list_13_23_home[0]
                        string_number_pw_13_23_home = str(number_pw_13_23_home)
                        int_number_pw_13_23_home = True
                        pw_13_23_home_1 = "Midfield Transition that came " \
                                          "from defense: "
                        pw_13_23_home_2 = string_number_pw_13_23_home
                        pw_print_13_23_home = pw_13_23_home_1 + pw_13_23_home_2
                        print(white % pw_print_13_23_home)

                    first_number_pw_13_home = pw_list_13_home[0]
                    pw_list_13_home.remove(first_number_pw_13_home)
                    number_pw_13_home = pw_list_13_home[0]
                    string_number_pw_13_home = str(number_pw_13_home)
                    int_number_pw_13_home = True
                    pw_13_home_1 = "Transition that came from defense: "
                    pw_13_home_2 = string_number_pw_13_home
                    pw_print_string_13_home = pw_13_home_1 + pw_13_home_2
                    print(white % pw_print_string_13_home)

                first_number_pw_home = pw_list_home[0]
                pw_list_home.remove(first_number_pw_home)
                number_pw_home = pw_list_home[0]
                string_number_pw_home = str(number_pw_home)
                int_number_pw_home = True
                pw_print_string_home = "Transitions from " + home + ": " \
                                       + string_number_pw_home
                print(white % pw_print_string_home)

            elif attack_defense_input_transition == away:

                away_input_pw_away = input(away_input_away)

                if away_input_pw_away in pw_attack_words_away:

                    first_number_pw_33_away = pw_list_33_away[0]
                    pw_list_33_away.remove(first_number_pw_33_away)
                    number_pw_33_away = pw_list_33_away[0]
                    string_number_pw_33_away = str(number_pw_33_away)
                    int_number_pw_33_away = True
                    pw_33_away_1 = "Offensive Transitions: "
                    pw_33_away_2 = string_number_pw_33_away
                    pw_print_string_33_away = pw_33_away_1 + pw_33_away_2
                    print(white % pw_print_string_33_away)

                elif away_input_pw_away in pw_midfield_words_away:

                    first_number_pw_23_33_away = pw_list_23_33_away[0]
                    pw_list_23_33_away.remove(first_number_pw_23_33_away)
                    int_number_pw_23_33_away = True
                    number_pw_23_33_away = pw_list_23_33_away[0]
                    string_number_pw_23_33_away = str(number_pw_23_33_away)
                    pw_23_33_away_1 = "Offensive Transition that came from " \
                                      "midfield: "
                    pw_23_33_away_2 = string_number_pw_23_33_away
                    pw_print_23_33_away = pw_23_33_away_1 + pw_23_33_away_2
                    print(white % pw_print_23_33_away)

                elif away_input_pw_away in pw_defense_words_away:

                    defense_input_away = input(defense_pw_print_away)

                    if defense_input_away in defense_attack_pw_words_away:

                        first_number_pw_13_33_away = pw_list_13_33_away[0]
                        pw_list_13_33_away.remove(first_number_pw_13_33_away)
                        number_pw_13_33_away = pw_list_13_33_away[0]
                        string_number_pw_13_33_away = str(number_pw_13_33_away)
                        int_number_pw_13_33_away = True
                        pw_13_33_away_1 = "Offensive Transition that came " \
                                          "from defense: "
                        pw_13_33_away_2 = string_number_pw_13_33_away
                        pw_print_13_33_away = pw_13_33_away_1 + pw_13_33_away_2
                        print(white % pw_print_13_33_away)

                    elif defense_input_away in defense_midfield_pw_words_away:

                        first_number_pw_13_23_away = pw_list_13_23_away[0]
                        pw_list_13_23_away.remove(first_number_pw_13_23_away)
                        number_pw_13_23_away = pw_list_13_23_away[0]
                        string_number_pw_13_23_away = str(number_pw_13_23_away)
                        int_number_pw_13_23_away = True
                        pw_13_23_away_1 = "Midfield Transition that came " \
                                          "from defense: "
                        pw_13_23_away_2 = string_number_pw_13_23_away
                        pw_print_13_23_away = pw_13_23_away_1 + pw_13_23_away_2
                        print(white % pw_print_13_23_away)

                    first_number_pw_13_away = pw_list_13_away[0]
                    pw_list_13_away.remove(first_number_pw_13_away)
                    number_pw_13_away = pw_list_13_away[0]
                    string_number_pw_13_away = str(number_pw_13_away)
                    int_number_pw_13_away = True
                    pw_13_away_1 = "Transition that came from defense: "
                    pw_13_away_2 = string_number_pw_13_away
                    pw_print_string_13_away = pw_13_away_1 + pw_13_away_2
                    print(white % pw_print_string_13_away)

                first_number_pw_away = pw_list_away[0]
                pw_list_away.remove(first_number_pw_away)
                number_pw_away = pw_list_away[0]
                string_number_pw_away = str(number_pw_away)
                int_number_pw_away = True
                pw_print_string_away = "Transitions from " + away + ": " \
                                       + string_number_pw_away
                print(white % pw_print_string_away)

        elif choice in gkto_words:

            first_number_gkto = gkto_list[0]
            gkto_list.remove(first_number_gkto)
            number_gkto = gkto_list[0]
            string_number_gkto = str(number_gkto)
            int_number_gkto = True
            gkto_print_string = "Free Kick(s)" + string_number_gkto
            print(red % gkto_print_string)
            
        elif choice in kp_words:

            first_number_kp = kp_list[0]
            kp_list.remove(first_number_kp)
            number_kp = kp_list[0]
            string_number_kp = str(number_kp)
            int_number_kp = True
            kp_print_string = "Key Passes" + string_number_kp
            print(red % kp_print_string)

        if choice == home:
            if ball_home:
                continue
            else:
                ball_away = False
                ball_home = True
                start_home = time.time()
                elapsed_away += time.time() - start_away

        if choice == away:
            if ball_away:
                continue
            else:
                ball_away = True
                ball_home = False
                start_away = time.time()
                elapsed_home += time.time() - start_home

        # when the user does not know the commands a howto.txt will pop up
        elif choice == "help":
            howto = "notepad.exe howto.txt"
            sub.Popen(howto)

        # -----> * Quit Function * <-----

        # if the user wants to quit he types q to begin the process

        elif choice == "q":

            # text to appear in the end of the program and the separate file
            draft_end_1 = '''The game between %s and %s finished.'''
            draft_end_2 = '''The following stats were recorded for %s:'''

            draft_ending_statement = draft_end_1 + draft_end_2
            ending_statement = draft_ending_statement % (home, away, team)

            print(ending_statement)
            safile.write(ending_statement)

            # math function to calculate the percentage of each team in a match
            total_num = elapsed_home + elapsed_away
            percentage_num_possession = 100 / total_num
            final_home = elapsed_home * percentage_num_possession
            final_away = elapsed_away * percentage_num_possession
            round_home = round(final_home, 1)
            round_away = round(final_away, 1)
            string_home = str(round_home)
            string_away = str(round_away)
            print_home = home + " had " + string_home + "% possession"
            print_away = away + " had " + string_away + "% possession"

            # blues and reds are the percentage of possession depending on
            # team you have selected above
            if home_or_away == home:
                print(blue % print_home)
                print(red % print_away)
            elif home_or_away == away:
                print(blue % print_away)
                print(red % print_home)
            safile.write(print_home)
            safile.write(print_away)

            int_final_pk_goal = int(string_number_pk_goal)
            int_final_pk_missed = int(string_number_pk_missed)
            int_final_pk_saved = int(string_number_pk_saved)
            all_pk_bad = int_final_pk_missed + int_final_pk_saved
            all_pk_final = int_final_pk_goal + int_final_pk_missed
            all_pk_final += int_final_pk_saved
            int_final_pk = int(string_number_pk)
            if int_number_pk_goal and \
                    int_number_pk_saved and \
                    int_number_pk_missed and \
                    int_number_pk and \
                            int_final_pk == all_pk_final:
                perc_num_pk = 100 / all_pk_final
                perc_num_pk_good = perc_num_pk * int_final_pk_goal
                perc_num_pk_bad = perc_num_pk * all_pk_bad
                round_pk_good = round(perc_num_pk_good, 1)
                round_pk_bad = round(perc_num_pk_bad, 1)
                print_pk_good = str(round_pk_good)
                print_pk_bad = str(round_pk_bad)
                final_pk_good = print_pk_good + "% of the Penalty Kicks " \
                                                "were good"
                final_pk_bad = print_pk_bad + "% of the Penalty Kicks were " \
                                              "bad"
                print(blue % final_pk_good)
                print(red % final_pk_bad)

            # start print out/write on file each stat
            # if it was called
            if int_number_pk_goal:
                # print the number of the stat
                end_pk_goal = "Penalty Kick goal(s): " + string_number_pk_goal
                print(white % end_pk_goal)
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

            int_final_fk_gd = int(string_number_fk_gd)
            int_final_fk_pd = int(string_number_fk_pd)
            all_fk_final = int_final_fk_gd + int_final_fk_pd
            int_final_fk = int(string_number_fk)
            if int_number_fk_gd and \
                    int_number_fk_pd and \
                    int_number_fk and \
                            int_final_fk == all_fk_final:
                perc_num_fk = 100 / all_fk_final
                perc_num_fk_good = perc_num_fk * int_final_fk_gd
                perc_num_fk_bad = perc_num_fk * int_final_fk_pd
                round_fk_good = round(perc_num_fk_good, 1)
                round_fk_bad = round(perc_num_fk_bad, 1)
                print_fk_good = str(round_fk_good)
                print_fk_bad = str(round_fk_bad)
                final_fk_good = print_fk_good + "% of the Free Kicks were " \
                                                "good"
                final_fk_bad = print_fk_bad + "% of the Free Kicks were " \
                                              "bad"
                print(blue % final_fk_good)
                print(red % final_fk_bad)

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

            int_final_ck_gd = int(string_number_ck_gd)
            int_final_ck_pd = int(string_number_ck_pd)
            all_ck_final = int_final_ck_gd + int_final_ck_pd
            int_final_ck = int(string_number_ck)
            if int_number_ck_gd and \
                    int_number_ck_pd and \
                    int_number_ck and \
                            int_final_ck == all_ck_final:
                perc_num_ck = 100 / all_ck_final
                perc_num_ck_good = perc_num_ck * int_final_ck_gd
                perc_num_ck_bad = perc_num_ck * int_final_ck_pd
                round_ck_good = round(perc_num_ck_good, 1)
                round_ck_bad = round(perc_num_ck_bad, 1)
                print_ck_good = str(round_ck_good)
                print_ck_bad = str(round_ck_bad)
                final_ck_good = print_ck_good + "% of the Corner Kicks were " \
                                                "good"
                final_ck_bad = print_ck_bad + "% of the Corner Kicks were " \
                                              "bad"
                print(blue % final_ck_good)
                print(red % final_ck_bad)

            if int_number_ck_gd:
                end_ck_gd = "Corner Kick(s) with Good Delivery: "
                print(end_ck_gd + string_number_ck_gd)
                safile.write("\nCorner Kick(s) with Good Delivery: ")
                safile.write(string_number_ck_gd)
            elif not int_number_ck_gd:
                print("Corner Kick(s) with Good Delivery: 0")
                safile.write("\nCorner Kick(s) with Good Delivery: ")

            if int_number_ck_pd:
                end_ck_pd = "Corner Kick(s) with Poor Delivery: "
                print(end_ck_pd + string_number_ck_pd)
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

            int_final_ti_gd = int(string_number_ti_gd)
            int_final_ti_pd = int(string_number_ti_pd)
            all_ti_final = int_final_ti_gd + int_final_ti_pd
            int_final_ti = int(string_number_ti)
            if int_number_ti_gd and \
                    int_number_ti_pd and \
                    int_number_ti and \
                            int_final_ti == all_ti_final:
                perc_num_ti = 100 / all_ti_final
                perc_num_ti_good = perc_num_ti * int_final_ti_gd
                perc_num_ti_bad = perc_num_ti * int_final_ti_pd
                round_ti_good = round(perc_num_ti_good, 1)
                round_ti_bad = round(perc_num_ti_bad, 1)
                print_ti_good = str(round_ti_good)
                print_ti_bad = str(round_ti_bad)
                final_ti_good = print_ti_good + "% of the Corner Kicks were " \
                                                "good"
                final_ti_bad = print_ti_bad + "% of the Corner Kicks were " \
                                              "bad"
                print(blue % final_ti_good)
                print(red % final_ti_bad)

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

            int_final_crosses_gd = int(string_number_crosses_gd)
            int_final_crosses_pd = int(string_number_crosses_pd)
            all_crosses_final = int_final_crosses_gd + int_final_crosses_pd
            int_final_crosses = int(string_number_crosses)
            if int_number_crosses_gd and \
                    int_number_crosses_pd and \
                    int_number_crosses and \
                            int_final_crosses == all_crosses_final:
                perc_num_crosses = 100 / all_crosses_final
                perc_num_crosses_good = perc_num_crosses * int_final_crosses_gd
                perc_num_crosses_bad = perc_num_crosses * int_final_crosses_pd
                round_crosses_good = round(perc_num_crosses_good, 1)
                round_crosses_bad = round(perc_num_crosses_bad, 1)
                print_crosses_good = str(round_crosses_good)
                print_crosses_bad = str(round_crosses_bad)
                final_crosses_good = print_crosses_good + "% of the Crosses " \
                                                          "were good "
                final_crosses_bad = print_crosses_bad + "% of the Crosses " \
                                                        " were bad"

                print(blue % final_crosses_good)
                print(red % final_crosses_bad)

            if int_number_crosses_gd:
                end_cross_gd = "Cross(es) with Good Delivery: "
                print(end_cross_gd + string_number_crosses_gd)
                safile.write("\nCross(es) with Good Delivery: ")
                safile.write(string_number_crosses_gd)
            elif not int_number_crosses_gd:
                print("Cross(es) with Good Delivery: 0")
                safile.write("\nCross(es) with Good Delivery: ")

            if int_number_crosses_pd:
                end_cross_pd = "Cross(es) with Poor Delivery: "
                print(end_cross_pd + string_number_crosses_pd)
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

            int_final_shot_gd = int(string_number_shots_gd)
            int_final_shot_pd = int(string_number_shots_pd)
            int_final_shot_bs = int(string_number_shots_bs)
            all_shot_bad = int_final_shot_bs + int_final_shot_pd
            all_shot_final = int_final_shot_gd + int_final_shot_pd
            all_shot_final += int_final_shot_bs
            int_final_shot = int(string_number_shots)
            if int_number_shots_gd and \
                    int_number_shots_pd and \
                    int_number_shots and \
                            int_final_shot == all_shot_final:
                perc_num_shot = 100 / all_shot_final
                perc_num_shot_good = perc_num_shot * int_final_shot_gd
                perc_num_shot_bad = perc_num_shot * all_shot_bad
                round_shot_good = round(perc_num_shot_good, 1)
                round_shot_bad = round(perc_num_shot_bad, 1)
                print_shot_good = str(round_shot_good)
                print_shot_bad = str(round_shot_bad)
                final_shot_good = print_shot_good + "% of the Shots " \
                                                    "were good "
                final_shot_bad = print_shot_bad + "% of the Shots " \
                                                  " were bad"

                print(blue % final_shot_good)
                print(red % final_shot_bad)

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

            if int_number_shots_bs:
                print("Blocked Shot(s): ", string_number_shots_bs)
                safile.write("\nBlocked Shot(s): ")
                safile.write(string_number_shots_bs)
            elif not int_number_shots_bs:
                print("Blocked Shot(s): 0")
                safile.write("\nBlocked Shot(s): 0")

            if int_number_shots:
                print("Shot(s): ", string_number_shots)
                safile.write("\nShot(s): ")
                safile.write(string_number_shots)
            elif not int_number_shots:
                print("Shot(s): 0")
                safile.write("\nShot(s): 0")

            int_final_header_gd = int(string_number_headers_gd)
            int_final_header_pd = int(string_number_headers_pd)
            all_header_final = int_final_header_gd + int_final_header_pd
            int_final_header = int(string_number_headers)
            if int_number_headers_gd and \
                    int_number_headers_pd and \
                    int_number_headers and \
                            int_final_header == all_header_final:
                perc_num_header = 100 / all_header_final
                perc_num_header_good = perc_num_header * int_final_header_gd
                perc_num_header_bad = perc_num_header * int_final_header_pd
                round_header_good = round(perc_num_header_good, 1)
                round_header_bad = round(perc_num_header_bad, 1)
                print_header_good = str(round_header_good)
                print_header_bad = str(round_header_bad)
                final_header_good = print_header_good + "% of the Headers " \
                                                        "were good "
                final_header_bad = print_header_bad + "% of the Headers " \
                                                      " were bad"

                print(blue % final_header_good)
                print(red % final_header_bad)

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

            int_final_v1_w = int(string_number_v1_w)
            int_final_v1_l = int(string_number_v1_l)
            all_v1_final = int_final_v1_w + int_final_v1_l
            int_final_v1 = int(string_number_v1)
            if int_number_v1_w and \
                    int_number_v1_l and \
                    int_number_v1 and \
                            int_final_v1 == all_v1_final:
                perc_num_v1 = 100 / all_v1_final
                perc_num_v1_good = perc_num_v1 * int_final_v1_w
                perc_num_v1_bad = perc_num_v1 * int_final_v1_l
                round_v1_good = round(perc_num_v1_good, 1)
                round_v1_bad = round(perc_num_v1_bad, 1)
                print_v1_good = str(round_v1_good)
                print_v1_bad = str(round_v1_bad)
                final_v1_good = print_v1_good + "% of the 1vs1 " \
                                                "were good "
                final_v1_bad = print_v1_bad + "% of the 1vs1 " \
                                              " were bad"

                print(blue % final_v1_good)
                print(red % final_v1_bad)

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

            if int_number_lpi_sb_attack:
                end_lpi_sb_attack = "Second Ball Long Pass Interceptions on " \
                                    "Attack: "
                print(end_lpi_sb_attack + string_number_lpi_sb_attack)
                lpisba_f = "\nSecond Ball Long Pass Interceptions on Attack: "
                safile.write(lpisba_f)
                safile.write(string_number_lpi_sb_attack)
            elif not int_number_lpi_sb_attack:
                lpisba_f0 = "Second Ball Long Pass Interceptions on Attack: 0"
                print(lpisba_f0)
                safile.write("\n" + lpisba_f0)

            if int_number_lpi_tb_attack:
                lpitba = "Third Ball Long Pass Interceptions on Attack: "
                print(lpitba + string_number_lpi_tb_attack)
                safile.write(lpitba)
                safile.write(string_number_lpi_tb_attack)
            elif not int_number_lpi_tb_attack:
                lpitba_f0 = "Third Ball Long Pass Interceptions on Attack: 0"
                print(lpitba_f0)
                safile.write("\n" + lpitba_f0)

            if int_number_lpi_attack:
                lpia = "Long Pass Interceptions on Attack: "
                print("\n" + lpia + string_number_lpi_attack)
                safile.write("\nLong Pass Interceptions on Attack: ")
                safile.write(string_number_lpi_attack)
            elif not int_number_lpi_attack:
                print("Long Pass Interceptions on Attack: 0")
                safile.write("\nLong Pass Interceptions on Attack: 0")

            if int_number_lpi_sb_defense:
                lpisbd = "Second Ball Long Pass Interceptions on Defense: "
                print(lpisbd + string_number_lpi_sb_defense)
                safile.write("\n" + lpisbd)
                safile.write(string_number_lpi_sb_defense)
            elif not int_number_lpi_sb_defense:
                lpisbb_f0 = "Second Ball Long Pass Interceptions on Defense: 0"
                print("Second Ball Long Pass Interceptions on Defense: 0")
                safile.write("\n" + lpisbb_f0)

            if int_number_lpi_tb_defense:
                lpitbd = "Third Ball Long Pass Interceptions on Defense: "
                print(lpitbd + string_number_lpi_tb_defense)
                safile.write("\n" + lpitbd)
                safile.write(string_number_lpi_tb_defense)
            elif not int_number_lpi_tb_defense:
                lpitbd_f0 = "Third Ball Long Pass Interceptions on Defense: 0"
                print(lpitbd_f0)
                safile.write("\n" + lpitbd_f0)

            if int_number_lpi_defense:
                lpid = "Long Pass Interceptions on Defense: "
                print(lpid + string_number_lpi_defense)
                safile.write("\nLong Pass Interceptions on Defense: ")
                safile.write(string_number_lpi_defense)
            elif not int_number_lpi_defense:
                print("Long Pass Interceptions on Defense: 0")
                safile.write("\nLong Pass Interceptions on Defense: 0")

            if int_number_lpi:
                print("Long Pass Interceptions: ", string_number_lpi)
                safile.write("\nLong Pass Interceptions: ")
                safile.write(string_number_lpi)
            elif not int_number_lpi:
                print("Long Pass Interceptions: 0")
                safile.write("\nLg Pass Interceptions: 0")

            if int_number_saves:
                print("Saves: ", string_number_save)
                safile.write("\nSaves: ")
                safile.write(string_number_save)
            elif not int_number_saves:
                print("\nSaves: 0")
                safile.write("\nSaves: 0")

            if int_number_pl_33_23:
                pl233 = "Possession(s) lost on offence that came from " \
                        "midfield: "
                print(pl233 + string_number_pl_33_23)
                safile.write("\n" + pl233)
                safile.write(string_number_pl_33_23)
            elif not int_number_pl_33_23:
                pl233_f0 = "Possession lost on offence that came from " \
                           "midfield: 0"
                print(pl233_f0)
                safile.write("\n" + pl233_f0)

            if int_number_pl_33_13:
                pl3313 = "Possession(s) lost on offence that came " \
                         "from defense: "
                print(pl3313 + string_number_pl_33_13)
                safile.write("\n" + pl3313)
                safile.write(string_number_pl_33_13)
            elif not int_number_pl_33_13:
                pl3313 = "Possession lost on offence that came from defense: 0"
                print(pl3313)
                safile.write("\n" + pl3313)

            if int_number_pl_33:
                print("Possession(s) lost on offence: ", string_number_pl_33)
                safile.write("\nPossession(s) lost on offence: ")
                safile.write(string_number_pl_33)
            elif not int_number_pl_33:
                print("Possession lost on offence: 0")
                safile.write("\nPossession lost on offence: 0")

            if int_number_pl_23_33:
                pl2333 = "Possession(s) lost on midfield that came from " \
                         "offense: "
                print(pl2333 + string_number_pl_23_33)
                safile.write("\n" + pl2333)
                safile.write(string_number_pl_23_33)
            elif not int_number_pl_23_33:
                pl2333_f0 = "Possession lost on midfield that came from " \
                            "offense: 0"
                print(pl2333_f0)
                safile.write("\n" + pl2333_f0)

            if int_number_pl_23_13:
                pl2313 = "Possession(s) lost on midfield that came from " \
                         "defense: "
                print(pl2313 + string_number_pl_23_13)
                safile.write("\n" + pl2313)
                safile.write(string_number_pl_23_13)
            elif not int_number_pl_23_13:
                pl2313_f0 = "Possession lost on midfield that came from " \
                            "defense: 0"
                print(pl2313_f0)
                safile.write("\n" + pl2313_f0)

            if int_number_pl_23:
                print("Possession(s) lost on midfield: ", string_number_pl_23)
                safile.write("\nPossession(s) lost on midfield: ")
                safile.write(string_number_pl_23)
            elif not int_number_pl_23:
                print("Possession lost on midfield: 0")
                safile.write("\nPossession lost on midfield: 0")

            if int_number_pl_13_33:
                pl1333 = "Possession(s) lost on defense that came from " \
                         "offense: "
                print(pl1333 + string_number_pl_13_33)
                safile.write("\n" + pl1333)
                safile.write(string_number_pl_13_33)
            elif not int_number_pl_13_33:
                pl1333_f0 = "Possession lost on defense that came from " \
                            "offense: 0"
                print(pl1333_f0)
                safile.write("\n" + pl1333_f0)

            if int_number_pl_13_23:
                pl1323 = "Possession(s) lost on defense that came from " \
                         "offense: "
                print(pl1323 + string_number_pl_13_23)
                safile.write("\n" + pl1323)
                safile.write(string_number_pl_13_23)
            elif not int_number_pl_13_23:
                pl1323_f0 = "Possession lost on defense that came from " \
                            "offense: 0"
                print(pl1323_f0)
                safile.write("\n" + pl1323_f0)

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

            if int_number_pw_33_home:
                print("Offensive Transitions: ", string_number_pw_33_home)
                safile.write("\nOffensive Transitions: ")
                safile.write(string_number_pw_33_home)
            elif not int_number_pw_33_home:
                print("Offensive Transitions: 0")
                safile.write("\nOffensive Transitions: 0")

            if int_number_pw_23_33_home:
                pw2333h = "Offensive transitions that came from midfield: "
                print(pw2333h + string_number_pw_23_33_home)
                safile.write("\n" + pw2333h)
                safile.write(string_number_pw_23_33_home)
            elif not int_number_pw_23_33_home:
                pw2333h_f0 = "Offensive transitions that came from midfield: 0"
                print(pw2333h_f0)
                safile.write("\n" + pw2333h_f0)

            if int_number_pw_13_33_home:
                pw1333h = "Offensive transitions that came from defense: "
                print(pw1333h + string_number_pw_13_33_home)
                safile.write("\n" + pw1333h)
                safile.write(string_number_pw_13_33_home)
            elif not int_number_pw_13_33_home:
                pw1333h_f0 = "Offensive transitions that came from defense: 0"
                print(pw1333h_f0)
                safile.write("\n" + pw1333h_f0)

            if int_number_pw_13_23_home:
                pw1323h = "Midfield transitions that came from defense: "
                print(pw1323h + string_number_pw_13_23_home)
                safile.write("\nMidfield transitions that came from defense: ")
                safile.write(string_number_pw_13_23_home)
            elif not int_number_pw_13_23_home:
                pw1323h_f0 = "Midfield transitions that came from defense: 0"
                print(pw1323h_f0)
                safile.write("\n" + pw1323h_f0)

            if int_number_pw_13_home:
                pw13h = "Transitions that came from defense: "
                print(pw13h + string_number_pw_13_home)
                safile.write("\nTransitions that came from defense: ")
                safile.write(string_number_pw_13_home)
            elif not int_number_pw_13_home:
                print("Transitions that came from defense: 0")
                safile.write("\nTransitions that came from defense: 0")

            if int_number_pw_home:
                print("Transitions from " + home + ": ", string_number_pw_home)
                safile.write("\nTransitions from " + home + ": ")
                safile.write(string_number_pw_home)
            elif not int_number_pw_home:
                print("Transitions from " + home + ": 0")
                safile.write("\nTransitions from " + home + ": 0")

            if int_number_pw_33_away:
                print("Offensive Transitions: ", string_number_pw_33_away)
                safile.write("\nOffensive Transitions: ")
                safile.write(string_number_pw_33_away)
            elif not int_number_pw_33_away:
                print("Offensive Transitions: 0")
                safile.write("\nOffensive Transitions: 0")

            if int_number_pw_23_33_away:
                pw2333a = "Offensive transitions that came from midfield: "
                print(pw2333a + string_number_pw_23_33_away)
                safile.write("\n" + pw2333a)
                safile.write(string_number_pw_23_33_away)
            elif not int_number_pw_23_33_away:
                pw2333a_f0 = "Offensive transitions that came from midfield: 0"
                print("Offensive transitions that came from midfield: 0")
                safile.write("\n" + pw2333a_f0)

            if int_number_pw_13_33_away:
                pw1333a = "Offensive transitions that came from defense: "
                print(pw1333a + string_number_pw_13_33_away)
                safile.write("\n" + pw1333a)
                safile.write(string_number_pw_13_33_away)
            elif not int_number_pw_13_33_away:
                pw1333a_f0 = "Offensive transitions that came from defense: 0"
                print("Offensive transitions that came from defense: 0")
                safile.write("\n" + pw1333a_f0)

            if int_number_pw_13_23_away:
                pw1323a = "Midfield transitions that came from defense: "
                print(pw1323a + string_number_pw_13_23_away)
                safile.write("\nMidfield transitions that came from defense: ")
                safile.write(string_number_pw_13_23_away)
            elif not int_number_pw_13_23_away:
                pw1323a_f0 = "Midfield transitions that came from defense: 0"
                print("Midfield transitions that came from defense: 0")
                safile.write("\n" + pw1323a_f0)

            if int_number_pw_13_away:
                pw13a = "Transitions that came from defense: "
                print(pw13a + string_number_pw_13_away)
                safile.write("\nTransitions that came from defense: ")
                safile.write(string_number_pw_13_away)
            elif not int_number_pw_13_away:
                print("Transitions that came from defense: 0")
                safile.write("\nTransitions that came from defense: 0")

            if int_number_pw_away:
                print("Transitions from " + away + ": ", string_number_pw_away)
                safile.write("\nTransitions from " + away + ": ")
                safile.write(string_number_pw_away)
            elif not int_number_pw_away:
                print("Transitions from " + away + ": 0")
                safile.write("\nTransitions from " + away + ": 0")

            if int_number_transition:
                print("Transitions: ", string_number_transition)
                safile.write("\nTransitions: ")
                safile.write(string_number_transition)
            elif not int_number_transition:
                print("Transitions: 0")
                safile.write("\nTransitions: 0")

            if int_number_gkto:
                # print the number of the stat
                print("Goalkeeper Turnovers: ", string_number_gkto)
                # write on the file
                safile.write("Goalkeeper Turnovers: ")
                safile.write(string_number_gkto)
            # if it was not called
            elif not int_number_gkto:
                # print/write the time that the stat was called was None
                print("Goalkeeper Turnovers: 0")
                safile.write("\nGoalkeeper Turnover: 0")
                
            if int_number_kp:
                # print the number of the stat
                print("Goalkeeper Turnovers: ", string_number_kp)
                # write on the file
                safile.write("Goalkeeper Turnovers: ")
                safile.write(string_number_kp)
            # if it was not called
            elif not int_number_kp:
                # print/write the time that the stat was called was None
                print("Goalkeeper Turnovers: 0")
                safile.write("\nGoalkeeper Turnover: 0")

            # close the file
            safile.close()

            # break the while loop, quiting the function
            break


# i have no idea why this is necessary but it is
if ball_away:
    start_away = time.time()
else:
    start_home = time.time()

body()
