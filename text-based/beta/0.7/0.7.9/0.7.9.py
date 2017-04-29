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

# split the name of the .txt file so you can identify the home and away team
# this happens only if the user types the correct name according to howto.txt
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
    # global each variable to be able to be referenced later when you
    # print/write the total stat on each game at the end
    global pk_goal_2_h, pk_miss_2_h, pk_goal_2_a, pk_miss_2_a
    global fk_string_pd_2_h, string_number_fk_h, string_number_ck_pd_h
    global fk_string_pd_2_a, string_number_fk_a, string_number_ck_pd_a
    global cross_string_gd_2_h, cross_string_pd_2_h, cross_string_gd_2_a
    global header_oft_2_h, header_ont_2_h, cross_string_pd_2_a, header_oft_2_a
    global header_ont_2_a, string_number_v1_l_a, string_number_v1_a, string_number_v1_w_a
    global string_number_v1_l_h, string_number_v1_h, string_number_v1_w_h
    global string_number_lpi_tb_h, string_number_lpi_h, string_number_lpi_tb_a, string_number_lpi_a
    global ti_string_gd_2_h, string_number_ti_h, pl_23_2_h, ti_string_gd_2_a, string_number_ti_a, pl_23_2_a
    global lpi_attack_tb_2_h, lpi_attack_tb_2_a
    global lpi_attack_2_h, pl_23_13_2_h, lpi_attack_2_a, pl_23_13_2_a
    global lpi_attack_sb_2_h, ti_string_pd_2_h, lpi_attack_sb_2_a, ti_string_pd_2_a
    global pl_13_23_2_h, pl_13_2_h, midfield_input_h, pl_13_23_2_a, pl_13_2_a, midfield_input_a
    global pl_33_2_h, pl_23_33_2_h, pl_33_13_2_h, pl_33_2_a, pl_23_33_2_a, pl_33_13_2_a
    global pk_saved_2_h, pk_h, fk_string_gd_2_h, pk_saved_2_a, string_number_pk_a, fk_string_gd_2_a
    global string_number_offside_h, string_number_pw_23_33_away, string_number_offside_a
    global ck_string_gd_2_h, string_number_ck_h, end_away, start_home, team, ck_string_gd_2_a, string_number_ck_a
    global pw_33_home_2, shot_string_oft_2_h, shot_string_oft_2_a
    global string_number_crosses_h, string_number_shots_h, string_number_crosses_a, string_number_shots_a
    global elapsed_away, ball_away, string_number_ad_l_h, string_number_ad_h, string_number_ad_w_h
    global string_number_pl_h, string_number_transition_h, string_number_pl_a, string_number_transition_a
    global string_number_pw_13_23_away, shot_string_ont_2_h, shot_string_ont_2_a
    global pw_23_33_home_2, elapsed_home
    global string_number_pw_home, string_number_pw_33_away
    global string_number_lpi_sb_h, pl_13_33_2_h, string_number_lpi_sb_a, pl_13_33_2_a
    global string_number_pw_23_33, string_number_pw_13_33_away
    global string_number_save_h, start_away, string_number_headers_h, string_number_save_a, string_number_headers_a
    global lpi_defense_2_h, string_number_pw_23, lpi_defense_2_a0
    global string_number_pw_away, pw_13_33_home_2
    global lpi_attack_tb_2, string_number_kp_h, string_number_kp_a
    global string_number_pw_13_33, string_number_pw_13_away
    global lpi_attack_tb_2_h, string_number_gkto_h, lpi_attack_tb_2_a, string_number_gkto_a
    global pl_33_23_2_h, string_number_pw_13_h, pl_33_23_2_a, string_number_pw_13_a
    global string_number_pw_13_23, pw_13_23_home_2
    global pw_13_home_2, end_home, ball_home, string_number_ad_l_h, string_number_ad_h, string_number_ad_w_h

    # -----> * Introduction * <-----

    intro_part_one = '''
Welcome to Siball-Analysis v0.6.5-beta. If you do not know the commands '''

    intro_part_two = '''
type help to open the howto file.
I hope you enjoy the game between %s and %s.
Are you recording for %s or %s? You will be able to record for both teams

Notes on updates to come: Comparison between the two teams - Graphs on stats
'''

    intro_one = intro_part_one + intro_part_two
    # assigning the home and away teams to the intro
    # so the intro is game-specific
    print(intro_one % (home, away, home, away))
    home_or_away = input()

    stat_home_away = "%s/%s"
    home_away = (stat_home_away % (home, away))

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
    pk_range_h = range(0, 1000)
    # list the range to be accessible
    pk_list_h = list(pk_range_h)

    pk_range_goal_h = range(0, 1000)
    pk_list_goal_h = list(pk_range_goal_h)

    pk_range_saved_h = range(0, 1000)
    pk_list_saved_h = list(pk_range_saved_h)

    pk_range_missed_h = range(0, 1000)
    pk_list_missed_h = list(pk_range_missed_h)

    pk_input = '''goal/saved/missed
    '''

    pk_range_a = range(0, 1000)
    # list the range to be accessible
    pk_list_a = list(pk_range_a)

    pk_range_goal_a = range(0, 1000)
    pk_list_goal_a = list(pk_range_goal_a)

    pk_range_saved_a = range(0, 1000)
    pk_list_saved_a = list(pk_range_saved_a)

    pk_range_missed_a = range(0, 1000)
    pk_list_missed_a = list(pk_range_missed_a)

    # split to declare the good/bad stats, and to change colors later on
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

    fk_range_h = range(0, 1000)
    fk_list_h = list(fk_range_h)

    fk_range_gd_h = range(0, 1000)
    fk_list_gd_h = list(fk_range_gd_h)

    fk_range_pd_h = range(0, 1000)
    fk_list_pd_h = list(fk_range_pd_h)

    fk_range_a = range(0, 1000)
    fk_list_a = list(fk_range_a)

    fk_range_gd_a = range(0, 1000)
    fk_list_gd_a = list(fk_range_gd_a)

    fk_range_pd_a = range(0, 1000)
    fk_list_pd_a = list(fk_range_pd_a)

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

    ck_range_h = range(0, 1000)
    ck_list_h = list(ck_range_h)

    ck_range_gd_h = range(0, 1000)
    ck_list_gd_h = list(ck_range_gd_h)

    ck_range_pd_h = range(0, 1000)
    ck_list_pd_h = list(ck_range_pd_h)

    ck_range_a = range(0, 1000)
    ck_list_a = list(ck_range_a)

    ck_range_gd_a = range(0, 1000)
    ck_list_gd_a = list(ck_range_gd_a)

    ck_range_pd_a = range(0, 1000)
    ck_list_pd_a = list(ck_range_pd_a)

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

    ti_range_h = range(0, 1000)
    ti_list_h = list(ti_range_h)

    ti_range_gd_h = range(0, 1000)
    ti_list_gd_h = list(ti_range_gd_h)

    ti_range_pd_h = range(0, 1000)
    ti_list_pd_h = list(ti_range_pd_h)

    ti_range_a = range(0, 1000)
    ti_list_a = list(ti_range_a)

    ti_range_gd_a = range(0, 1000)
    ti_list_gd_a = list(ti_range_gd_a)

    ti_range_pd_a = range(0, 1000)
    ti_list_pd_a = list(ti_range_pd_a)

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

    cross_range_h = range(0, 1000)
    cross_list_h = list(cross_range_h)

    cross_range_gd_h = range(0, 1000)
    cross_list_gd_h = list(cross_range_gd_h)

    cross_range_pd_h = range(0, 1000)
    cross_list_pd_h = list(cross_range_pd_h)

    cross_range_a = range(0, 1000)
    cross_list_a = list(cross_range_a)

    cross_range_gd_a = range(0, 1000)
    cross_list_gd_a = list(cross_range_gd_a)

    cross_range_pd_a = range(0, 1000)
    cross_list_pd_a = list(cross_range_pd_a)

    cross_input = '''gd/pd
    '''
    gd_cross, pd_cross = cross_input.split("/")

    cross_words = ["cross", "Cross", "Cross ", "cross ", "crosses", "Crosses",
                   "Crosses ", "crosses "]

    cross_gd_words = ["gd", "GD", "gd ", "GD ", "051"]

    cross_pd_words = ["pd", "PD", "pd ", "PD ", "052"]

    # -----> * 1vs1 Variables * <-----

    v1_range_h = range(0, 1000)
    v1_list_h = list(v1_range_h)

    v1_range_w_h = range(0, 1000)
    v1_list_w_h = list(v1_range_w_h)

    v1_range_l_h = range(0, 1000)
    v1_list_l_h = list(v1_range_l_h)

    v1_input = '''w/l
    '''

    v1_range_a = range(0, 1000)
    v1_list_a = list(v1_range_a)

    v1_range_w_a = range(0, 1000)
    v1_list_w_a = list(v1_range_w_a)

    v1_range_l_a = range(0, 1000)
    v1_list_l_a = list(v1_range_l_a)

    w_v1, l_v1 = v1_input.split("/")

    v1_words = ["1v1", "1vs1", "1 versus 1", "1 Versus 1", "1VS1", "1v1 ",
                "1vs1 ", "1 versus 1 ", "1 Versus 1 ", "1VS1 "]

    # -----> * Shots Variables * <-----

    shot_range_h = range(0, 1000)
    shot_list_h = list(shot_range_h)

    shot_range_ont_h = range(0, 1000)
    shot_list_ont_h = list(shot_range_ont_h)

    shot_range_oft_h = range(0, 1000)
    shot_list_oft_h = list(shot_range_oft_h)

    shot_range_bs_h = range(0, 1000)
    shot_list_bs_h = list(shot_range_bs_h)

    shot_range_a = range(0, 1000)
    shot_list_a = list(shot_range_a)

    shot_range_ont_a = range(0, 1000)
    shot_list_ont_a = list(shot_range_ont_a)

    shot_range_oft_a = range(0, 1000)
    shot_list_oft_a = list(shot_range_oft_a)

    shot_range_bs_a = range(0, 1000)
    shot_list_bs_a = list(shot_range_bs_a)

    shot_input = '''on target/off target/blocked shots
    '''
    ont_shot, oft_shot, blocked_shot = shot_input.split("/")

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

    header_range_h = range(0, 1000)
    header_list_h = list(header_range_h)

    header_range_ont_h = range(0, 1000)
    header_list_ont_h = list(header_range_ont_h)

    header_range_oft_h = range(0, 1000)
    header_list_oft_h = list(header_range_oft_h)

    header_range_a = range(0, 1000)
    header_list_a = list(header_range_a)

    header_range_ont_a = range(0, 1000)
    header_list_ont_a = list(header_range_ont_a)

    header_range_oft_a = range(0, 1000)
    header_list_oft_a = list(header_range_oft_a)

    header_input = '''on target/off target
    '''
    ont_header, oft_header = header_input.split("/")

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

    save_range_h = range(0, 1000)
    save_list_h = list(save_range_h)

    save_range_a = range(0, 1000)
    save_list_a = list(save_range_a)

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

    lpi_input_defense = '''second ball/third ball
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

    attack_words = ["attack", "Attack", "ATTACK", "attack ", "Attack ",
                    "ATTACK ", "a", "33", "3/3", "33 ", "3/3 "]

    attack_midfield_words = ["midfield", "Midfield", "MIDFIELD", "midfield ",
                             "Midfield ", "MIDFIELD ", "m", "23",
                             "2/3", "23 ", "2/3 "]

    attack_defense_words = ["defense", "Defense", "DEFENSE", "defense ",
                            "Defense ", "DEFENSE ", "d", "13", "1/3",
                            "13 ", "1/3"]

    midfield_words = ["midfield", "Midfield", "MIDFIELD", "midfield ",
                      "Midfield ", "MIDFIELD ", "m", "23", "2/3",
                      "23 ", "2/3 "]

    midfield_attack_words = ["attack", "Attack", "ATTACK", "attack ",
                             "Attack ", "ATTACK ", "a", "33", "3/3", "33 ",
                             "3/3 "]

    midfield_defense_words = ["defense", "Defense", "DEFENSE", "defense ",
                              "Defense ", "DEFENSE ", "d", "13", "1/3",
                              "13 ", "1/3"]

    defense_words = ["defense", "Defense", "DEFENSE", "defense ",
                     "Defense ", "DEFENSE ", "d", "13", "1/3", "13 ",
                     "1/3"]

    defense_attack_words = ["attack", "Attack", "ATTACK", "attack ",
                            "Attack ", "ATTACK ", "a", "33", "3/3", "33 ",
                            "3/3 "]

    defense_midfield_words = ["midfield", "Midfield", "MIDFIELD", "midfield ",
                              "Midfield ", "MIDFIELD ", "m", "23",
                              "2/3", "23 ", "2/3 "]

    # -----> * Offside * <-----

    offside_range_h = range(0, 1000)
    offside_list_h = list(offside_range_h)

    offside_range_a = range(0, 1000)
    offside_list_a = list(offside_range_a)

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
                             # 500th line

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

    gkto_range_h = range(0, 1000)
    gkto_list_h = list(gkto_range_h)

    gkto_range_a = range(0, 1000)
    gkto_list_a = list(gkto_range_a)

    gkto_words = ["gkto", "Goalkeeper Turnover", "GOALKEEPER TURNOVER",
                  "gkto ", "Goalkeeper Turnover ", "GOALKEEPER TURNOVER "]

    kp_range_h = range(0, 1000)
    kp_list_h = list(kp_range_h)

    kp_range_a = range(0, 1000)
    kp_list_a = list(kp_range_a)

    kp_words = ["kp", "Key Pass", "KEY PASS",
                "kp ", "Key Pass ", "KEY PASS "]

    possession_range_h = range(0, 1000)
    possession_list_h = list(possession_range_h)

    possession_range_13_h = range(0, 1000)
    possession_list_13_h = list(possession_range_13_h)

    possession_range_23_h = range(0, 1000)
    possession_list_23_h = list(possession_range_23_h)

    possession_range_33_h = range(0, 1000)
    possession_list_33_h = list(possession_range_33_h)

    possession_input = '''13/23/33
        '''

    possession_range_a = range(0, 1000)
    possession_list_a = list(possession_range_a)

    possession_range_13_a = range(0, 1000)
    possession_list_13_a = list(possession_range_13_a)

    possession_range_23_a = range(0, 1000)
    possession_list_23_a = list(possession_range_23_a)

    possession_range_33_a = range(0, 1000)
    possession_list_33_a = list(possession_range_33_a)

    # split to declare the good/bad stats, and to change colors later on
    possession_13, possession_23, possession_33 = possession_input.split("/")

    # a list of possible words that the user may type in order to record stats
    possession_words = ["possession", "possession", "Possession", "PS",
                        "possessions", "ps", "Possessions", "possession "]

    cl_range_h = range(0, 1000)
    cl_list_h = list(cl_range_h)

    cl_range_gd_h = range(0, 1000)
    cl_list_gd_h = list(cl_range_gd_h)

    cl_range_pd_h = range(0, 1000)
    cl_list_pd_h = list(cl_range_pd_h)

    cl_range_a = range(0, 1000)
    cl_list_a = list(cl_range_a)

    cl_range_gd_a = range(0, 1000)
    cl_list_gd_a = list(cl_range_gd_a)

    cl_range_pd_a = range(0, 1000)
    cl_list_pd_a = list(cl_range_pd_a)

    cl_input = '''gd/pd
        '''
    gd_cl, pd_cl = cl_input.split("/")

    cl_words = ["cl", "clearance", "Clearance", "CL", "CLEARANCE"]

    cl_gd_words = ["gd", "GD", "gd ", "GD "]

    cl_pd_words = ["pd", "PD", "pd ", "PD "]

    # -----> * Aeriel Duels Variables * <-----

    ad_range_h = range(0, 1000)
    ad_list_h = list(ad_range_h)

    ad_range_w_h = range(0, 1000)
    ad_list_w_h = list(ad_range_w_h)

    ad_range_l_h = range(0, 1000)
    ad_list_l_h = list(ad_range_l_h)

    ad_input = '''w/l
        '''

    ad_range_a = range(0, 1000)
    ad_list_a = list(ad_range_a)

    ad_range_w_a = range(0, 1000)
    ad_list_w_a = list(ad_range_w_a)

    ad_range_l_a = range(0, 1000)
    ad_list_l_a = list(ad_range_l_a)

    w_ad, l_ad = ad_input.split("/")

    ad_words = ["ad", "aerial duel"]

    w_words = ["w", "W", "w ", "W ", "won", "Won", "WON", "won ", "Won ",
               "WON "]

    l_words = ["l", "L", "l ", "L ", "lost", "Lost", "LOST", "lost ", "Lost ",
               "LOST ", "062"]

    # false each variable to declare if a stat was called before or not
    int_number_pk_goal_h = False
    int_number_pk_saved_h = False
    int_number_pk_missed_h = False
    int_number_pk_h = False

    int_number_fk_gd_h = False
    int_number_fk_pd_h = False
    int_number_fk_h = False

    int_number_ck_gd_h = False
    int_number_ck_pd_h = False
    int_number_ck_h = False

    int_number_ti_gd_h = False
    int_number_ti_pd_h = False
    int_number_ti_h = False

    int_number_cross_gd_h = False
    int_number_cross_pd_h = False
    int_number_cross_h = False

    int_number_shot_ont_h = False
    int_number_shot_oft_h = False
    int_number_shot_bs_h = False
    int_number_shot_h = False

    int_number_header_ont_h = False
    int_number_header_oft_h = False
    int_number_header_h = False

    int_number_v1_w_h = False
    int_number_v1_l_h = False
    int_number_v1_h = False

    int_number_lpi_sb_attack = False
    int_number_lpi_tb_attack = False
    int_number_lpi_attack = False
    int_number_lpi_sb_defense = False
    int_number_lpi_tb_defense = False
    int_number_lpi_defense = False
    int_number_lpi = False

    int_number_saves_h = False

    int_number_saves_a = False

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

    int_number_offside_h = False

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

    int_number_gkto_h = False

    int_number_kp_h = False

    int_number_possession_13_h = False
    int_number_possession_23_h = False
    int_number_possession_33_h = False
    int_number_possession_h = False

    int_number_cl_gd_h = False
    int_number_cl_pd_h = False
    int_number_cl_h = False

    int_number_ad_w_h = False
    int_number_ad_l_h = False
    int_number_ad_h = False

    int_number_pk_goal_a = False
    int_number_pk_saved_a = False
    int_number_pk_missed_a = False
    int_number_pk_a = False

    int_number_fk_gd_a = False
    int_number_fk_pd_a = False
    int_number_fk_a = False

    int_number_ck_gd_a = False
    int_number_ck_pd_a = False
    int_number_ck_a = False

    int_number_ti_gd_a = False
    int_number_ti_pd_a = False
    int_number_ti_a = False

    int_number_cross_gd_a = False
    int_number_cross_pd_a = False
    int_number_cross_a = False

    int_number_shot_ont_a = False
    int_number_shot_oft_a = False
    int_number_shot_bs_a = False
    int_number_shot_a = False

    int_number_header_ont_a = False
    int_number_header_oft_a = False
    int_number_header_a = False

    int_number_v1_w_a = False
    int_number_v1_l_a = False
    int_number_v1_a = False

    int_number_offside_a = False

    int_number_gkto_a = False

    int_number_kp_a = False

    int_number_possession_13_a = False
    int_number_possession_23_a = False
    int_number_possession_33_a = False
    int_number_possession_a = False

    int_number_cl_gd_a = False
    int_number_cl_pd_a = False
    int_number_cl_a = False

    int_number_ad_w_a = False
    int_number_ad_l_a = False
    int_number_ad_a = False

    # it creates a while loop so the function will go on and on until
    # the user decides to quit the function

    while True:

        # the user decides which stat to record by calling it
        choice = input()

        # -----> * Penalty Kicks Function * <-----

        # user inserts one of the words in the list
        if choice in pk_words:

            print(home_away)
            team_input = input()

            if team_input == home:

                # the user decides whether a stat was successful or not
                print(blue % goal_pk, red % saved_pk, red % missed_pk)
                good_bad_input_pk = input()

                if good_bad_input_pk in goal_words:

                    # take the first number on the list
                    first_number_pk_goal_h = pk_list_goal_h[0]
                    # remove the first number on the lis
                    # the first time it is called it deletes 0
                    pk_list_goal_h.remove(first_number_pk_goal_h)
                    # takes the next number on a list which is the number
                    # that will be called
                    number_pk_goal_h = pk_list_goal_h[0]
                    # strings the number so it will be printable/writable
                    pk_goal_2_h = str(number_pk_goal_h)
                    # true the integer so it knows it was called
                    int_number_pk_goal_h = True
                    pk_goal_1_h = home + "'s Penalty Kick goal(s): "
                    pk_print_string_goal_h = pk_goal_1_h + pk_goal_2_h
                    # print a nice introduction and the time a stat was called
                    print(blue % pk_print_string_goal_h)

                elif good_bad_input_pk in saved_words:

                    first_number_pk_saved_h = pk_list_saved_h[0]
                    pk_list_saved_h.remove(first_number_pk_saved_h)
                    number_pk_saved_h = pk_list_saved_h[0]
                    pk_saved_2_h = str(number_pk_saved_h)
                    int_number_pk_saved_h = True
                    pk_saved_1_h = "Penalty Kick(s) saved: "
                    pk_print_string_saved_h = pk_saved_1_h + pk_saved_2_h
                    print(red % pk_print_string_saved_h)

                elif good_bad_input_pk in missed_words:

                    first_number_pk_missed_h = pk_list_missed_h[0]
                    pk_list_missed_h.remove(first_number_pk_missed_h)
                    number_pk_missed_h = pk_list_missed_h[0]
                    pk_miss_2_h = str(number_pk_missed_h)
                    int_number_pk_missed_h = True
                    pk_miss_1_h = home + "'s Penalty Kick(s) missed: "
                    pk_print_string_missed_h = pk_miss_1_h + pk_miss_2_h
                    print(red % pk_print_string_missed_h)

                first_number_pk_h = pk_list_h[0]
                pk_list_h.remove(first_number_pk_h)
                number_pk_h = pk_list_h[0]
                pk_h = str(number_pk_h)
                int_number_pk_h = True
                pk_print_string_h = home + "'s Penalty Kick(s): " + pk_h
                print(white % pk_print_string_h)

            elif team_input == away:

                # the user decides whether a stat was successful or not
                print(blue % goal_pk, red % saved_pk, red % missed_pk)
                good_bad_input_pk = input()

                if good_bad_input_pk in goal_words:

                    first_number_pk_goal_a = pk_list_goal_a[0]
                    pk_list_goal_a.remove(first_number_pk_goal_a)
                    number_pk_goal_a = pk_list_goal_a[0]
                    pk_goal_2_a = str(number_pk_goal_a)
                    int_number_pk_goal_a = True
                    pk_goal_1_a = away + "'s Penalty Kick goal(s): "
                    pk_print_string_goal_a = pk_goal_1_a + pk_goal_2_a
                    print(blue % pk_print_string_goal_a)

                elif good_bad_input_pk in saved_words:

                    first_number_pk_saved_a = pk_list_saved_a[0]
                    pk_list_saved_a.remove(first_number_pk_saved_a)
                    number_pk_saved_a = pk_list_saved_a[0]
                    pk_saved_2_a = str(number_pk_saved_a)
                    int_number_pk_saved_a = True
                    pk_saved_1_a = away + "'s Penalty Kick(s) saved: "
                    pk_print_string_saved_a = pk_saved_1_a + pk_saved_2_a
                    print(red % pk_print_string_saved_a)

                elif good_bad_input_pk in missed_words:

                    first_number_pk_missed_a = pk_list_missed_a[0]
                    pk_list_missed_a.remove(first_number_pk_missed_a)
                    number_pk_missed_a = pk_list_missed_a[0]
                    pk_miss_2_a = str(number_pk_missed_a)
                    int_number_pk_missed_a = True
                    pk_miss_1_a = away + "'s Penalty Kick(s) missed: "
                    pk_print_string_missed_a = pk_miss_1_a + pk_miss_2_a
                    print(red % pk_print_string_missed_a)

                first_number_pk_a = pk_list_a[0]
                pk_list_a.remove(first_number_pk_a)
                number_pk_a = pk_list_a[0]
                pk_a = str(number_pk_a)
                int_number_pk_a = True
                pk_print_string_a = away + "'s Penalty Kick(s): " + pk_a
                print(white % pk_print_string_a)

        # -----> * Free Kicks Function * <-----

        elif choice in fk_words:

            print(home_away)
            team_input = input()

            if team_input == home:

                print(blue % gd_fk, red % pd_fk)
                good_bad_input_fk = input()

                if good_bad_input_fk in fk_gd_words:

                    first_number_fk_gd_h = fk_list_gd_h[0]
                    fk_list_gd_h.remove(first_number_fk_gd_h)
                    number_fk_gd_h = fk_list_gd_h[0]
                    fk_gd_2_h = str(number_fk_gd_h)
                    int_number_fk_gd_h = True
                    fk_gd_1_h = home + "'s Free Kick(s) with Good Delivery: "
                    fk_print_string_gd_h = fk_gd_1_h + fk_gd_2_h
                    print(blue % fk_print_string_gd_h)

                elif good_bad_input_fk in fk_pd_words:

                    first_number_fk_pd_h = fk_list_pd_h[0]
                    fk_list_pd_h.remove(first_number_fk_pd_h)
                    number_fk_pd_h = fk_list_pd_h[0]
                    fk_pd_2_h = str(number_fk_pd_h)
                    int_number_fk_pd_h = True
                    fk_pd_1_h = home + "'s Free Kick(s) with Poor Delivery: "
                    fk_print_string_pd_h = fk_pd_1_h + fk_pd_2_h
                    print(red % fk_print_string_pd_h)

                first_number_fk_h = fk_list_h[0]
                fk_list_h.remove(first_number_fk_h)
                number_fk_h = fk_list_h[0]
                fk_h = str(number_fk_h)
                int_number_fk_h = True
                fk_print_string_h = home + "'s Free Kick(s): " + fk_h
                print(white % fk_print_string_h)

            elif team_input == away:

                print(blue % gd_fk, red % pd_fk)
                good_bad_input_fk = input()

                if good_bad_input_fk in fk_gd_words:

                    first_number_fk_gd_a = fk_list_gd_a[0]
                    fk_list_gd_a.remove(first_number_fk_gd_a)
                    number_fk_gd_a = fk_list_gd_a[0]
                    fk_gd_2_a = str(number_fk_gd_a)
                    int_number_fk_gd_a = True
                    fk_gd_1_a = away + "'s Free Kick(s) with Good Delivery: "
                    fk_print_string_gd_a = fk_gd_1_a + fk_gd_2_a
                    print(blue % fk_print_string_gd_a)

                elif good_bad_input_fk in fk_pd_words:

                    first_number_fk_pd_a = fk_list_pd_a[0]
                    fk_list_pd_a.remove(first_number_fk_pd_a)
                    number_fk_pd_a = fk_list_pd_a[0]
                    fk_pd_2_a = str(number_fk_pd_a)
                    int_number_fk_pd_a = True
                    fk_pd_1_a = away + "'s Free Kick(s) with Poor Delivery: "
                    fk_print_string_pd_a = fk_pd_1_a + fk_pd_2_a
                    print(red % fk_print_string_pd_a)

                first_number_fk_a = fk_list_a[0]
                fk_list_a.remove(first_number_fk_a)
                number_fk_a = fk_list_a[0]
                fk_a = str(number_fk_a)
                int_number_fk_a = True
                fk_print_string_a = away + "'s Free Kick(s): " + fk_a
                print(white % fk_print_string_a)

        # -----> * Corner Kick Variables * <-----

        elif choice in ck_words:

            print(home_away)
            team_input = input()

            if team_input == home:

                print(blue % gd_ck, red % pd_ck)
                good_bad_input_ck = input()

                if good_bad_input_ck in ck_gd_words:

                    first_number_ck_gd_h = ck_list_gd_h[0]
                    ck_list_gd_h.remove(first_number_ck_gd_h)
                    number_ck_gd_h = ck_list_gd_h[0]
                    ck_gd_2_h = str(number_ck_gd_h)
                    int_number_ck_gd_h = True
                    ck_gd_1_h = home + "'s Corner Kick(s) with Good Delivery: "
                    ck_print_string_gd_h = ck_gd_1_h + ck_gd_2_h
                    print(blue % ck_print_string_gd_h)

                elif good_bad_input_ck in ck_pd_words:

                    first_number_ck_pd_h = ck_list_pd_h[0]
                    ck_list_pd_h.remove(first_number_ck_pd_h)
                    number_ck_pd_h = ck_list_pd_h[0]
                    ck_pd_2_h = str(number_ck_pd_h)
                    int_number_ck_pd_h = True
                    ck_pd_1_h = home + "'s Corner Kick(s) with Poor Delivery: "
                    ck_print_string_pd_h = ck_pd_1_h + ck_pd_2_h
                    print(red % ck_print_string_pd_h)

                first_number_ck_h = ck_list_h[0]
                ck_list_h.remove(first_number_ck_h)
                number_ck_h = ck_list_h[0]
                ck_h = str(number_ck_h)
                int_number_ck_h = True
                ck_print_string_h = home + "'s Corner Kick(s): " + ck_h
                print(white % ck_print_string_h)

            elif team_input == away:

                print(blue % gd_ck, red % pd_ck)
                good_bad_input_ck = input()

                if good_bad_input_ck in ck_gd_words:

                    first_number_ck_gd_a = ck_list_gd_a[0]
                    ck_list_gd_a.remove(first_number_ck_gd_a)
                    number_ck_gd_a = ck_list_gd_a[0]
                    ck_gd_2_a = str(number_ck_gd_a)
                    int_number_ck_gd_a = True
                    ck_gd_1_a = away + "'s Corner Kick(s) with Good Delivery: "
                    ck_print_string_gd_a = ck_gd_1_a + ck_gd_2_a
                    print(blue % ck_print_string_gd_a)

                elif good_bad_input_ck in ck_pd_words:

                    first_number_ck_pd_a = ck_list_pd_a[0]
                    ck_list_pd_a.remove(first_number_ck_pd_a)
                    number_ck_pd_a = ck_list_pd_a[0]
                    ck_pd_2_a = str(number_ck_pd_a)
                    int_number_ck_pd_a = True
                    ck_pd_1_a = away + "'s Corner Kick(s) with Poor Delivery: "
                    ck_print_string_pd_a = ck_pd_1_a + ck_pd_2_a
                    print(red % ck_print_string_pd_a)

                first_number_ck_a = ck_list_a[0]
                ck_list_a.remove(first_number_ck_a)
                number_ck_a = ck_list_a[0]
                ck_a = str(number_ck_a)
                int_number_ck_a = True
                ck_print_string_a = away + "'s Corner Kick(s): " + ck_a
                print(white % ck_print_string_a)

        # -----> * Throw Ins Functions * <-----

        elif choice in ti_words:

            print(home_away)
            team_input = input()

            if team_input == home:

                print(blue % gd_ti, red % pd_ti)
                good_bad_input_ti = input()

                if good_bad_input_ti in ti_gd_words:

                    first_number_ti_gd_h = ti_list_gd_h[0]
                    ti_list_gd_h.remove(first_number_ti_gd_h)
                    number_ti_gd_h = ti_list_gd_h[0]
                    ti_gd_2_h = str(number_ti_gd_h)
                    int_number_ti_gd_h = True
                    ti_gd_1_h = home + "'s Throw In(s) with Good Delivery: "
                    ti_print_string_gd_h = ti_gd_1_h + ti_gd_2_h
                    print(blue % ti_print_string_gd_h)

                elif good_bad_input_ti in ti_pd_words:

                    first_number_ti_pd_h = ti_list_pd_h[0]
                    ti_list_pd_h.remove(first_number_ti_pd_h)
                    number_ti_pd_h = ti_list_pd_h[0]
                    ti_pd_2_h = str(number_ti_pd_h)
                    int_number_ti_pd_h = True
                    ti_pd_1_h = home + "'s Throw In(s) with Poor Delivery: "
                    ti_print_string_pd_h = ti_pd_1_h + ti_pd_2_h
                    print(red % ti_print_string_pd_h)

                first_number_ti_h = ti_list_h[0]
                ti_list_h.remove(first_number_ti_h)
                number_ti_h = ti_list_h[0]
                ti_h = str(number_ti_h)
                int_number_ti_h = True
                ti_print_string_h = home + "'s Throw In(s): " + ti_h
                print(white % ti_print_string_h)

            elif team_input == away:

                print(blue % gd_ti, red % pd_ti)
                good_bad_input_ti = input()

                if good_bad_input_ti in ti_gd_words:

                    first_number_ti_gd_a = ti_list_gd_a[0]
                    ti_list_gd_a.remove(first_number_ti_gd_a)
                    number_ti_gd_a = ti_list_gd_a[0]
                    ti_gd_2_a = str(number_ti_gd_a)
                    int_number_ti_gd_a = True
                    ti_gd_1_a = away + "'s Throw In(s) with Good Delivery: "
                    ti_print_string_gd_a = ti_gd_1_a + ti_gd_2_a
                    print(blue % ti_print_string_gd_a)

                elif good_bad_input_ti in ti_pd_words:

                    first_number_ti_pd_a = ti_list_pd_a[0]
                    ti_list_pd_a.remove(first_number_ti_pd_a)
                    number_ti_pd_a = ti_list_pd_a[0]
                    ti_pd_2_a = str(number_ti_pd_a)
                    int_number_ti_pd_a = True
                    ti_pd_1_a = away + "'s Throw In(s) with Poor Delivery: "
                    ti_print_string_pd_a = ti_pd_1_a + ti_pd_2_a
                    print(red % ti_print_string_pd_a)

                first_number_ti_a = ti_list_a[0]
                ti_list_a.remove(first_number_ti_a)
                number_ti_a = ti_list_a[0]
                ti_a = str(number_ti_a)
                int_number_ti_a = True
                ti_print_string_a = away + "'s Throw In(s): " + ti_a
                print(white % ti_print_string_a)

        # -----> * Crosses Function * <-----

        elif choice in cross_words:

            print(home_away)
            team_input = input()

            if team_input == home:

                print(blue % gd_cross, red % pd_cross)
                good_bad_input_cross = input()

                if good_bad_input_cross in cross_gd_words:

                    first_number_cross_gd_h = cross_list_gd_h[0]
                    cross_list_gd_h.remove(first_number_cross_gd_h)
                    number_cross_gd_h = cross_list_gd_h[0]
                    cross_gd_2_h = str(number_cross_gd_h)
                    int_number_cross_gd_h = True
                    cross_gd_1_h = home + "'s Cross(es) with Good Delivery: "
                    cross_print_string_gd_h = cross_gd_1_h + cross_gd_2_h
                    print(blue % cross_print_string_gd_h)

                elif good_bad_input_cross in cross_pd_words:

                    first_number_cross_pd_h = cross_list_pd_h[0]
                    cross_list_pd_h.remove(first_number_cross_pd_h)
                    number_cross_pd_h = cross_list_pd_h[0]
                    cross_pd_2_h = str(number_cross_pd_h)
                    int_number_cross_pd_h = True
                    cross_pd_1_h = home + "'s Cross(es) with Poor Delivery: "
                    cross_print_string_pd_h = cross_pd_1_h + cross_pd_2_h
                    print(red % cross_print_string_pd_h)

                first_number_cross_h = cross_list_h[0]
                cross_list_h.remove(first_number_cross_h)
                number_cross_h = cross_list_h[0]
                cross_h = str(number_cross_h)
                int_number_cross_h = True
                cross_print_string_h = home + "'s Cross(es): " + cross_h
                print(white % cross_print_string_h)

            elif team_input == away:

                print(blue % gd_cross, red % pd_cross)
                good_bad_input_cross = input()

                if good_bad_input_cross in cross_gd_words:

                    first_number_cross_gd_a = cross_list_gd_a[0]
                    cross_list_gd_a.remove(first_number_cross_gd_a)
                    number_cross_gd_a = cross_list_gd_a[0]
                    cross_gd_2_a = str(number_cross_gd_a)
                    int_number_cross_gd_a = True
                    cross_gd_1_a = away + "'s Cross(es) with Good Delivery: "
                    cross_print_string_gd_a = cross_gd_1_a + cross_gd_2_a
                    print(blue % cross_print_string_gd_a)

                elif good_bad_input_cross in cross_pd_words:

                    first_number_cross_pd_a = cross_list_pd_a[0]
                    cross_list_pd_a.remove(first_number_cross_pd_a)
                    number_cross_pd_a = cross_list_pd_a[0]
                    cross_pd_2_a = str(number_cross_pd_a)
                    int_number_cross_pd_a = True
                    cross_pd_1_a = away + "'s Cross(es) with Poor Delivery: "
                    cross_print_string_pd_a = cross_pd_1_a + cross_pd_2_a
                    print(red % cross_print_string_pd_a)

                first_number_cross_a = cross_list_a[0]
                cross_list_a.remove(first_number_cross_a)
                number_cross_a = cross_list_a[0]
                cross_a = str(number_cross_a)
                int_number_cross_a = True
                cross_print_string_a = away + "'s Cross(es): " + cross_a
                print(white % cross_print_string_a)

        # -----> * Shots Function * <-----

        elif choice in shot_words:

            print(home_away)
            team_input = input()

            if team_input == home:

                print(blue % ont_shot, red % oft_shot, red % blocked_shot)
                good_bad_input_shots = input()

                if good_bad_input_shots in shot_ont_words:

                    first_number_shot_ont_h = shot_list_ont_h[0]
                    shot_list_ont_h.remove(first_number_shot_ont_h)
                    number_shot_ont_h = shot_list_ont_h[0]
                    shot_string_ont_2_h = str(number_shot_ont_h)
                    int_number_shot_ont_h = True
                    shot_string_ont_1_h = home + "'s Shot(s) on target: "
                    shot_print_string_ont_h = shot_string_ont_1_h + shot_string_ont_2_h

                    print(blue % shot_print_string_ont_h)

                elif good_bad_input_shots in shot_oft_words:

                    first_number_shot_oft_h = shot_list_oft_h[0]
                    shot_list_oft_h.remove(first_number_shot_oft_h)
                    number_shot_oft_h = shot_list_oft_h[0]
                    shot_string_oft_2_h = str(number_shot_oft_h)
                    int_number_shot_oft_h = True
                    shot_string_oft_1_h = home + "'s Shot(s) off target: "
                    shot_print_string_oft_h = shot_string_oft_1_h + shot_string_oft_2_h
                    print(blue % shot_print_string_oft_h)

                elif good_bad_input_shots in blocked_shot_words:
                    first_number_shot_bs_h = shot_list_bs_h[0]
                    shot_list_bs_h.remove(first_number_shot_bs_h)
                    number_shot_bs_h = shot_list_bs_h[0]
                    shot_string_bs_2_h = str(number_shot_bs_h)
                    int_number_shot_bs_h = True
                    shot_string_bs_1_h = home + "'s Blocked Shot(s): "
                    shot_print_string_bs_h = shot_string_bs_1_h + shot_string_bs_2_h
                    print(red % shot_print_string_bs_h)

                first_number_shots_h = shot_list_h[0]
                shot_list_h.remove(first_number_shots_h)
                number_shots_h = shot_list_h[0]
                string_number_shots_h = str(number_shots_h)
                int_number_shot_h = True
                shot_print_string_h = home + "'s Shot(s): " + string_number_shots_h
                print(white % shot_print_string_h)

            elif team_input == away:

                print(blue % ont_shot, red % oft_shot, red % blocked_shot)
                good_bad_input_shots = input()

                if good_bad_input_shots in shot_ont_words:

                    first_number_shot_ont_a = shot_list_ont_a[0]
                    shot_list_ont_a.remove(first_number_shot_ont_a)
                    number_shot_ont_a = shot_list_ont_a[0]
                    shot_string_ont_2_a = str(number_shot_ont_a)
                    int_number_shot_ont_a = True
                    shot_string_ont_1_a = away + "'s Shot(s) on target: "
                    shot_print_string_ont_a = shot_string_ont_1_a + shot_string_ont_2_a

                    print(blue % shot_print_string_ont_a)

                elif good_bad_input_shots in shot_oft_words:

                    first_number_shot_oft_a = shot_list_oft_a[0]
                    shot_list_oft_a.remove(first_number_shot_oft_a)
                    number_shot_oft_a = shot_list_oft_a[0]
                    shot_string_oft_2_a = str(number_shot_oft_a)
                    int_number_shot_oft_a = True
                    shot_string_oft_1_a = away + "'s Shot(s) off target: "
                    shot_print_string_oft_a = shot_string_oft_1_a + shot_string_oft_2_a

                    print(blue % shot_print_string_oft_a)

                elif good_bad_input_shots in blocked_shot_words:
                    first_number_shot_bs_a = shot_list_bs_a[0]
                    shot_list_bs_a.remove(first_number_shot_bs_a)
                    number_shot_bs_a = shot_list_bs_a[0]
                    shot_string_bs_2_a = str(number_shot_bs_a)
                    int_number_shot_bs_a = True
                    shot_string_bs_1_a = away + "'s Blocked Shot(s): "
                    shot_print_string_bs_a = shot_string_bs_1_a + shot_string_bs_2_a
                    print(red % shot_print_string_bs_a)

                first_number_shots_a = shot_list_a[0]
                shot_list_a.remove(first_number_shots_a)
                number_shots_a = shot_list_a[0]
                string_number_shots_a = str(number_shots_a)
                int_number_shot_a = True
                shot_print_string_a = away + "'s Shot(s): " + string_number_shots_a
                print(white % shot_print_string_a)

        # -----> * Headers Function * <-----

        elif choice in header_words:

            print(home_away)
            team_input = input()

            if team_input == home:

                print(blue % ont_header, red % oft_header)
                good_bad_input_headers = input()

                if good_bad_input_headers in header_ont_words:

                    first_number_header_ont_h = header_list_ont_h[0]
                    header_list_ont_h.remove(first_number_header_ont_h)
                    number_header_ont_h = header_list_ont_h[0]
                    header_string_ont_2_h = str(number_header_ont_h)
                    int_number_header_ont_h = True
                    header_string_ont_1_h = home + "'s Header(s) on target: "
                    header_print_string_ont_h = header_string_ont_1_h + header_string_ont_2_h

                    print(blue % header_print_string_ont_h)

                elif good_bad_input_headers in header_oft_words:

                    first_number_header_oft_h = header_list_oft_h[0]
                    header_list_oft_h.remove(first_number_header_oft_h)
                    number_header_oft_h = header_list_oft_h[0]
                    header_string_oft_2_h = str(number_header_oft_h)
                    int_number_header_oft_h = True
                    header_string_oft_1_h = home + "'s Header(s) off target: "
                    header_print_string_oft_h = header_string_oft_1_h + header_string_oft_2_h
                    print(blue % header_print_string_oft_h)

                '''

                not sure if going to use or not

                elif good_bad_input_headers in blocked_header_words:
                    first_number_header_bs_h = header_list_bs_h[0]
                    header_list_bs_h.remove(first_number_header_bs_h)
                    number_header_bs_h = header_list_bs_h[0]
                    header_string_bs_2_h = str(number_header_bs_h)
                    int_number_header_bs_h = True
                    header_string_bs_1_h = home + "'s Blocked Header(s): "
                    header_print_string_bs_h = header_string_bs_1_h + header_string_bs_2_h
                    print(red % header_print_string_bs_h)

                '''

                first_number_headers_h = header_list_h[0]
                header_list_h.remove(first_number_headers_h)
                number_headers_h = header_list_h[0]
                string_number_headers_h = str(number_headers_h)
                int_number_header_h = True
                header_print_string_h = home + "'s Header(s): " + string_number_headers_h
                print(white % header_print_string_h)

            elif team_input == away:

                print(blue % ont_header, red % oft_header)
                good_bad_input_headers = input()

                if good_bad_input_headers in header_ont_words:

                    first_number_header_ont_a = header_list_ont_a[0]
                    header_list_ont_a.remove(first_number_header_ont_a)
                    number_header_ont_a = header_list_ont_a[0]
                    header_string_ont_2_a = str(number_header_ont_a)
                    int_number_header_ont_a = True
                    header_string_ont_1_a = away + "'s Header(s) on target: "
                    header_print_string_ont_a = header_string_ont_1_a + header_string_ont_2_a

                    print(blue % header_print_string_ont_a)

                elif good_bad_input_headers in header_oft_words:

                    first_number_header_oft_a = header_list_oft_a[0]
                    header_list_oft_a.remove(first_number_header_oft_a)
                    number_header_oft_a = header_list_oft_a[0]
                    header_string_oft_2_a = str(number_header_oft_a)
                    int_number_header_oft_a = True
                    header_string_oft_1_a = away + "'s Header(s) off target: "
                    header_print_string_oft_a = header_string_oft_1_a + header_string_oft_2_a
                    print(blue % header_print_string_oft_a)

                '''

                elif good_bad_input_headers in blocked_header_words:
                    first_number_header_bs_a = header_list_bs_a[0]
                    header_list_bs_a.remove(first_number_header_bs_a)
                    number_header_bs_a = header_list_bs_a[0]
                    header_string_bs_2_a = str(number_header_bs_a)
                    int_number_header_bs_a = True
                    header_string_bs_1_a = away + "'s Blocked Header(s): "
                    header_print_string_bs_a = header_string_bs_1_a + header_string_bs_2_a
                    print(red % header_print_string_bs_a)

                '''

                first_number_headers_a = header_list_a[0]
                header_list_a.remove(first_number_headers_a)
                number_headers_a = header_list_a[0]
                string_number_headers_a = str(number_headers_a)
                int_number_header_a = True
                header_print_string_a = away + "'s Header(s): " + string_number_headers_a
                print(white % header_print_string_a)

                # -----> * 1vs1 * <-----

        elif choice in v1_words:

            print(home_away)
            team_input = input()

            if team_input == home:

                print(blue % w_v1, red % l_v1)
                good_bad_input_v1 = input()

                if good_bad_input_v1 in w_words:

                    first_number_v1_w_h = v1_list_w_h[0]
                    v1_list_w_h.remove(first_number_v1_w_h)
                    number_v1_w_h = v1_list_w_h[0]
                    v1_w_2_h = str(number_v1_w_h)
                    int_number_v1_w_h = True
                    v1_w_1_h = home + "'s 1vs1 Won: "
                    v1_print_string_w_h = v1_w_1_h + v1_w_2_h
                    print(blue % v1_print_string_w_h)

                elif good_bad_input_v1 in l_words:

                    first_number_v1_l_h = v1_list_l_h[0]
                    v1_list_l_h.remove(first_number_v1_l_h)
                    number_v1_l_h = v1_list_l_h[0]
                    v1_l_2_h = str(number_v1_l_h)
                    int_number_v1_l_h = True
                    v1_l_1_h = home + "'s 1vs1 Lost: "
                    v1_print_string_l_h = v1_l_1_h + v1_l_2_h
                    print(red % v1_print_string_l_h)

                first_number_v1_h = v1_list_h[0]
                v1_list_h.remove(first_number_v1_h)
                number_v1_h = v1_list_h[0]
                v1_h = str(number_v1_h)
                int_number_v1_h = True
                v1_print_string_h = home + "'s 1vs1: " + v1_h
                print(white % v1_print_string_h)

            elif team_input == away:

                print(blue % w_v1, red % l_v1)
                good_bad_input_v1 = input()

                if good_bad_input_v1 in w_words:

                    first_number_v1_w_a = v1_list_w_a[0]
                    v1_list_w_a.remove(first_number_v1_w_a)
                    number_v1_w_a = v1_list_w_a[0]
                    v1_w_2_a = str(number_v1_w_a)
                    int_number_v1_w_a = True
                    v1_w_1_a = away + "'s 1vs1 Won: "
                    v1_print_string_w_a = v1_w_1_a + v1_w_2_a
                    print(blue % v1_print_string_w_a)

                elif good_bad_input_v1 in l_words:

                    first_number_v1_l_a = v1_list_l_a[0]
                    v1_list_l_a.remove(first_number_v1_l_a)
                    number_v1_l_a = v1_list_l_a[0]
                    v1_l_2_a = str(number_v1_l_a)
                    int_number_v1_l_a = True
                    v1_l_1_a = away + "'s 1vs1 Lost: "
                    v1_print_string_l_a = v1_l_1_a + v1_l_2_a
                    print(red % v1_print_string_l_a)

                first_number_v1_a = v1_list_a[0]
                v1_list_a.remove(first_number_v1_a)
                number_v1_a = v1_list_a[0]
                v1_a = str(number_v1_a)
                int_number_v1_a = True
                v1_print_string_a = away + "'s 1vs1: " + v1_a
                print(white % v1_print_string_a)

        # -----> * Long Passes * <-----
        # Home/Away availability is subject to change

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
                    lpi_attack_sb_2 = str(number_lpi_sb_attack)
                    lpi_attack_sb_1 = "Second Ball Long Pass Interceptions " \
                                      "on Attack: "
                    lpi_attack_sb_2 = lpi_attack_sb_2
                    lpi_print_attack_sb = lpi_attack_sb_1 + lpi_attack_sb_2
                    print(white % lpi_print_attack_sb)
                    int_number_lpi_sb_attack = True

                elif sec_third_input_long_pass_attack in attack_tb_words:
                    first_number_lpi_tb_attack = lpi_list_tb_attack[0]
                    lpi_list_tb_attack.remove(first_number_lpi_tb_attack)
                    number_lpi_tb_attack = lpi_list_tb_attack[0]
                    lpi_attack_tb_2 = str(number_lpi_tb_attack)
                    lpi_attack_tb_1 = "Third Ball Long Pass " \
                                      "Interceptions on Attack: "
                    lpi_attack_tb_2 = lpi_attack_tb_2
                    lpi_print_attack_tb = lpi_attack_tb_1 + lpi_attack_tb_2
                    print(white % lpi_print_attack_tb)
                    int_number_lpi_tb_attack = True

                first_number_lpi_attack = lpi_list_attack[0]
                lpi_list_attack.remove(first_number_lpi_attack)
                number_lpi_attack = lpi_list_attack[0]
                lpi_attack_2 = str(number_lpi_attack)
                lpi_attack_1 = "Long Pass Interceptions on Attack: "
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
                    lpi_defense_sb_2 = str(number_lpi_sb_defense)
                    lpi_defense_sb_1 = "Second Ball Long Pass " \
                                       "Interceptions on Defense: "
                    lpi_print_defense_sb = lpi_defense_sb_1 + lpi_defense_sb_2
                    print(white % lpi_print_defense_sb)
                    int_number_lpi_sb_defense = True

                elif sec_third_input_long_pass_defense in defense_tb_words:
                    first_number_lpi_tb_defense = lpi_list_tb_defense[0]
                    lpi_list_tb_defense.remove(first_number_lpi_tb_defense)
                    number_lpi_tb_defense = lpi_list_tb_defense[0]
                    lpi_defense_tb_2 = str(number_lpi_tb_defense)
                    lpi_defense_tb_1 = "Third Ball Long Pass " \
                                       "Interceptions on Defense: "
                    lpi_print_defense_tb = lpi_defense_tb_1 + lpi_defense_tb_2
                    print(white % lpi_print_defense_tb)
                    int_number_lpi_tb_defense = True

                first_number_lpi_defense = lpi_list_defense[0]
                lpi_list_defense.remove(first_number_lpi_defense)
                number_lpi_defense = lpi_list_defense[0]
                lpi_defense_2 = str(number_lpi_defense)
                lpi_defense_1 = "Long Pass Interceptions on Defense:"
                pk_print_string_goal = lpi_defense_1 + lpi_defense_2
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

            print(home_away)
            team_input = input()

            if team_input == home:

                first_number_save_h = save_list_h[0]
                save_list_h.remove(first_number_save_h)
                number_save_h = save_list_h[0]
                string_number_save_h = str(number_save_h)
                int_number_saves_h = True
                save_print_string_h = home + "'s Save(s): " + string_number_save_h

                print(white % save_print_string_h)

            elif team_input == away:

                first_number_save_a = save_list_a[0]
                save_list_a.remove(first_number_save_a)
                number_save_a = save_list_a[0]
                string_number_save_a = str(number_save_a)
                int_number_saves_a = True
                save_print_string_a = away + "'s Save(s): " + string_number_save_a
                print(white % save_print_string_a)

        # -----> * Possession Loss * <-----
        # Home/Away availability is subject to change

        elif choice in pl_words:

            good_bad_input_pl = input(pl_input)

            if good_bad_input_pl in attack_words:
                attack_input = input(attack_print)
                if attack_input in attack_midfield_words:
                    first_number_pl_33_23 = pl_list_33_23[0]
                    pl_list_33_23.remove(first_number_pl_33_23)
                    number_pl_33_23 = pl_list_33_23[0]
                    pl_33_23_2 = str(number_pl_33_23)
                    int_number_pl_33_23 = True
                    pl_33_23_1 = "Possession lost on offence " \
                                 "that came from Midfield: "
                    pl_print_string_33_23 = pl_33_23_1 + pl_33_23_2
                    print(white % pl_print_string_33_23)

                elif attack_input in attack_defense_words:
                    first_number_pl_33_13 = pl_list_33_13[0]
                    pl_list_33_13.remove(first_number_pl_33_13)
                    number_pl_33_13 = pl_list_33_13[0]
                    pl_33_13_2 = str(number_pl_33_13)
                    int_number_pl_33_13 = True
                    pl_33_13_1 = "Possession lost on offence" \
                                 " that came from Defense: "
                    pl_print_string_33_13 = pl_33_13_1 + pl_33_13_2
                    print(white % pl_print_string_33_13)

                first_number_pl_33 = pl_list_33[0]
                pl_list_33.remove(first_number_pl_33)
                number_pl_33 = pl_list_33[0]
                pl_33_2 = str(number_pl_33)
                int_number_pl_33 = True
                pl_33_1 = "Possession lost on offence: "
                pl_print_string_33 = pl_33_1 + pl_33_2
                print(white % pl_print_string_33)

            elif good_bad_input_pl in midfield_words:

                midfield_input = input(midfield_print)

                if midfield_input in midfield_attack_words:
                    first_number_pl_23_33 = pl_list_23_33[0]
                    pl_list_23_33.remove(first_number_pl_23_33)
                    number_pl_23_33 = pl_list_23_33[0]
                    pl_23_33_2 = str(number_pl_23_33)
                    int_number_pl_23_33 = True
                    pl_23_33_1 = "Possession lost on midfield that " \
                                 "came from Offense: "
                    pl_print_string_23_33 = pl_23_33_1 + pl_23_33_2
                    print(white % pl_print_string_23_33)

                elif midfield_input in midfield_defense_words:
                    first_number_pl_23_13 = pl_list_23_13[0]
                    pl_list_23_13.remove(first_number_pl_23_13)
                    number_pl_23_13 = pl_list_23_13[0]
                    pl_23_13_2 = str(number_pl_23_13)
                    int_number_pl_23_13 = True
                    pl_23_13_1 = "Possession lost on midfield " \
                                 "that came from Defense: "
                    pl_print_string_23_13 = pl_23_13_1 + pl_23_13_2
                    print(white % pl_print_string_23_13)

                first_number_pl_23 = pl_list_23[0]
                pl_list_23.remove(first_number_pl_23)
                number_pl_23 = pl_list_23[0]
                pl_23_2 = str(number_pl_23)
                int_number_pl_23 = True
                pl_23_1 = "Possession lost on midfield: "
                pl_print_string_23 = pl_23_1 + pl_23_2
                print(white % pl_print_string_23)

            elif good_bad_input_pl in defense_words:
                defense_input = input(defense_print)

                if defense_input in defense_attack_words:

                    first_number_pl_13_33 = pl_list_13_33[0]
                    pl_list_13_33.remove(first_number_pl_13_33)
                    number_pl_13_33 = pl_list_13_33[0]
                    pl_13_33_2 = str(number_pl_13_33)
                    int_number_pl_13_33 = True
                    pl_13_33_1 = "Possession lost on defense " \
                                 "that came from offense: "
                    pl_print_string_13_33 = pl_13_33_1 + pl_13_33_2
                    print(white % pl_print_string_13_33)

                elif defense_input in defense_midfield_words:

                    first_number_pl_13_23 = pl_list_13_23[0]
                    pl_list_13_23.remove(first_number_pl_13_23)
                    number_pl_13_23 = pl_list_13_23[0]
                    pl_13_23_2 = str(number_pl_13_23)
                    int_number_pl_13_23 = True
                    pl_13_23_1 = "Possession lost on defense that came " \
                                 "from midfield: "
                    pl_print_string_13_23 = pl_13_23_1 + pl_13_23_2
                    print(white % pl_print_string_13_23)

                first_number_pl_13 = pl_list_13[0]
                pl_list_13.remove(first_number_pl_13)
                number_pl_13 = pl_list_13[0]
                pl_13_2 = str(number_pl_13)
                int_number_pl_13 = True
                pl_13_1 = "Possession lost on defense: "
                pl_print_string_13 = pl_13_1 + pl_13_2
                print(white % pl_print_string_13)

            first_number_pl = pl_list[0]
            pl_list.remove(first_number_pl)
            number_pl = pl_list[0]
            string_number_pl = str(number_pl)
            int_number_pl = True
            pl_print_string = "Possession lost: " + string_number_pl
            print(white % pl_print_string)

        elif choice in offside_words:

            print(home_away)
            team_input = input()

            if team_input == home:

                first_number_offside_h = offside_list_h[0]
                offside_list_h.remove(first_number_offside_h)
                number_offside_h = offside_list_h[0]
                string_number_offside_h = str(number_offside_h)
                int_number_offside_h = True
                offside_print_string_h = home + "'s Offside(s): " + string_number_offside_h

                print(white % offside_print_string_h)

            elif team_input == away:

                first_number_offside_a = offside_list_a[0]
                offside_list_a.remove(first_number_offside_a)
                number_offside_a = offside_list_a[0]
                string_number_offside_a = str(number_offside_a)
                int_number_offside_a = True
                offside_print_string_a = away + "'s Offside(s): " + string_number_offside_a
                print(white % offside_print_string_a)

        elif choice in pw_words:

            attack_defense_input_transition = input(pw_input)

            if attack_defense_input_transition == home:

                home_input_pw_home = input(home_input_home)

                if home_input_pw_home in pw_attack_words_home:

                    first_number_pw_33_home = pw_list_33_home[0]
                    pw_list_33_home.remove(first_number_pw_33_home)
                    number_pw_33_home = pw_list_33_home[0]
                    pw_33_home_2 = str(number_pw_33_home)
                    int_number_pw_33_home = True
                    pw_33_home_1 = "Offensive Transitions: "
                    pw_print_string_33_home = pw_33_home_1 + pw_33_home_2
                    print(white % pw_print_string_33_home)

                elif home_input_pw_home in pw_midfield_words_home:

                    first_number_pw_23_33_home = pw_list_23_33_home[0]
                    pw_list_23_33_home.remove(first_number_pw_23_33_home)
                    int_number_pw_23_33_home = True
                    number_pw_23_33_home = pw_list_23_33_home[0]
                    pw_23_33_home_2 = str(number_pw_23_33_home)
                    pw_23_33_home_1 = "Offensive Transitions that came from " \
                                      "midfield: "
                    pw_print_23_33_home = pw_23_33_home_1 + pw_23_33_home_2
                    print(white % pw_print_23_33_home)

                elif home_input_pw_home in pw_defense_words_home:

                    defense_input_home = input(defense_pw_print_home)

                    if defense_input_home in defense_attack_pw_words_home:

                        first_number_pw_13_33_home = pw_list_13_33_home[0]
                        pw_list_13_33_home.remove(first_number_pw_13_33_home)
                        number_pw_13_33_home = pw_list_13_33_home[0]
                        pw_13_33_home_2 = str(number_pw_13_33_home)
                        int_number_pw_13_33_home = True
                        pw_13_33_home_1 = "Offensive Transitions that came " \
                                          "from defense: "
                        pw_print_13_33_home = pw_13_33_home_1 + pw_13_33_home_2
                        print(white % pw_print_13_33_home)

                    elif defense_input_home in defense_midfield_pw_words_home:

                        first_number_pw_13_23_home = pw_list_13_23_home[0]
                        pw_list_13_23_home.remove(first_number_pw_13_23_home)
                        number_pw_13_23_home = pw_list_13_23_home[0]
                        pw_13_23_home_2 = str(number_pw_13_23_home)
                        int_number_pw_13_23_home = True
                        pw_13_23_home_1 = "Midfield Transitions that came " \
                                          "from defense: "
                        pw_13_23_home_2 = pw_13_23_home_2
                        pw_print_13_23_home = pw_13_23_home_1 + pw_13_23_home_2
                        print(white % pw_print_13_23_home)

                    first_number_pw_13_home = pw_list_13_home[0]
                    pw_list_13_home.remove(first_number_pw_13_home)
                    number_pw_13_home = pw_list_13_home[0]
                    pw_13_home_2 = str(number_pw_13_home)
                    int_number_pw_13_home = True
                    pw_13_home_1 = "Transitions that came from defense: "
                    pw_13_home_2 = pw_13_home_2
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
                    pw_33_away_2 = str(number_pw_33_away)
                    int_number_pw_33_away = True
                    pw_33_away_1 = "Offensive Transitions: "
                    pw_print_string_33_away = pw_33_away_1 + pw_33_away_2
                    print(white % pw_print_string_33_away)

                elif away_input_pw_away in pw_midfield_words_away:

                    first_number_pw_23_33_away = pw_list_23_33_away[0]
                    pw_list_23_33_away.remove(first_number_pw_23_33_away)
                    int_number_pw_23_33_away = True
                    number_pw_23_33_away = pw_list_23_33_away[0]
                    pw_23_33_away_2 = str(number_pw_23_33_away)
                    pw_23_33_away_1 = "Offensive Transition that came from " \
                                      "midfield: "
                    pw_print_23_33_away = pw_23_33_away_1 + pw_23_33_away_2
                    print(white % pw_print_23_33_away)

                elif away_input_pw_away in pw_defense_words_away:

                    defense_input_away = input(defense_pw_print_away)

                    if defense_input_away in defense_attack_pw_words_away:

                        first_number_pw_13_33_away = pw_list_13_33_away[0]
                        pw_list_13_33_away.remove(first_number_pw_13_33_away)
                        number_pw_13_33_away = pw_list_13_33_away[0]
                        pw_13_33_away_2 = str(number_pw_13_33_away)
                        int_number_pw_13_33_away = True
                        pw_13_33_away_1 = "Offensive Transition that came " \
                                          "from defense: "
                        pw_print_13_33_away = pw_13_33_away_1 + pw_13_33_away_2
                        print(white % pw_print_13_33_away)

                    elif defense_input_away in defense_midfield_pw_words_away:

                        first_number_pw_13_23_away = pw_list_13_23_away[0]
                        pw_list_13_23_away.remove(first_number_pw_13_23_away)
                        number_pw_13_23_away = pw_list_13_23_away[0]
                        pw_13_23_away_2 = str(number_pw_13_23_away)
                        int_number_pw_13_23_away = True
                        pw_13_23_away_1 = "Midfield Transition that came " \
                                          "from defense: "
                        pw_13_23_away_2 = pw_13_23_away_2
                        pw_print_13_23_away = pw_13_23_away_1 + pw_13_23_away_2
                        print(white % pw_print_13_23_away)

                    first_number_pw_13_away = pw_list_13_away[0]
                    pw_list_13_away.remove(first_number_pw_13_away)
                    number_pw_13_away = pw_list_13_away[0]
                    pw_13_away_2 = str(number_pw_13_away)
                    int_number_pw_13_away = True
                    pw_13_away_1 = "Transition that came from defense: "
                    pw_13_away_2 = pw_13_away_2
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

            print(home_away)
            team_input = input()

            if team_input == home:

                first_number_gkto_h = gkto_list_h[0]
                gkto_list_h.remove(first_number_gkto_h)
                number_gkto_h = gkto_list_h[0]
                string_number_gkto_h = str(number_gkto_h)
                int_number_gkto_h = True
                gkto_print_string_h = home + "'s Goalkeeper Turnover(s): " + string_number_gkto_h

                print(white % gkto_print_string_h)

            elif team_input == away:

                first_number_gkto_a = gkto_list_a[0]
                gkto_list_a.remove(first_number_gkto_a)
                number_gkto_a = gkto_list_a[0]
                string_number_gkto_a = str(number_gkto_a)
                int_number_gkto_a = True
                gkto_print_string_a = away + "'s Goalkeeper Turnover(s): " + string_number_gkto_a
                print(white % gkto_print_string_a)

        elif choice in kp_words:

            print(home_away)
            team_input = input()

            if team_input == home:

                first_number_kp_h = kp_list_h[0]
                kp_list_h.remove(first_number_kp_h)
                number_kp_h = kp_list_h[0]
                string_number_kp_h = str(number_kp_h)
                int_number_kp_h = True
                kp_print_string_h = home + "'s Key Pass(es): " + string_number_kp_h

                print(white % kp_print_string_h)

            elif team_input == away:

                first_number_kp_a = kp_list_a[0]
                kp_list_a.remove(first_number_kp_a)
                number_kp_a = kp_list_a[0]
                string_number_kp_a = str(number_kp_a)
                int_number_kp_a = True
                kp_print_string_a = away + "'s Key Pass(es): " + string_number_kp_a
                print(white % kp_print_string_a)

        # counts the possession time of each team by typing the name
        # of each team. Provided that you named the file correctly according

        elif choice in possession_words:

            print(home_away)
            team_input = input()

            if team_input == home:

                print(blue % possession_13, red % possession_23,
                      red % possession_33)

                good_bad_input_possessions = input()

                if good_bad_input_possessions in defense_words:

                    first_number_possession_13_h = possession_list_13_h[0]
                    possession_list_13_h.remove(first_number_possession_13_h)
                    number_possession_13_h = possession_list_13_h[0]
                    possession_string_13_2_h = str(number_possession_13_h)
                    int_number_possession_13_h = True
                    possession_string_13_1_h = home + "'s Possession(s) on defense: "
                    possession_print_string_13_h = possession_string_13_1_h + possession_string_13_2_h

                    print(blue % possession_print_string_13_h)

                elif good_bad_input_possessions in midfield_words:

                    first_number_possession_23_h = possession_list_23_h[0]
                    possession_list_23_h.remove(first_number_possession_23_h)
                    number_possession_23_h = possession_list_23_h[0]
                    possession_string_23_2_h = str(number_possession_23_h)
                    int_number_possession_23_h = True
                    possession_string_23_1_h = home + "'s Possession(s) on midfield: "
                    possession_print_string_23_h = possession_string_23_1_h + possession_string_23_2_h
                    print(blue % possession_print_string_23_h)

                elif good_bad_input_possessions in attack_words:
                    first_number_possession_33_h = possession_list_33_h[0]
                    possession_list_33_h.remove(first_number_possession_33_h)
                    number_possession_33_h = possession_list_33_h[0]
                    possession_string_33_2_h = str(number_possession_33_h)
                    int_number_possession_33_h = True
                    possession_string_33_1_h = home + "'s Possession(s) on attack: "
                    possession_print_string_33_h = possession_string_33_1_h + possession_string_33_2_h
                    print(red % possession_print_string_33_h)

                first_number_possessions_h = possession_list_h[0]
                possession_list_h.remove(first_number_possessions_h)
                number_possessions_h = possession_list_h[0]
                string_number_possessions_h = str(number_possessions_h)
                int_number_possession_h = True
                possession_print_string_h = home + "'s Possession(s): " + string_number_possessions_h
                print(white % possession_print_string_h)

            elif team_input == away:

                print(blue % possession_13, red % possession_23,
                      red % possession_33)

                good_bad_input_possessions = input()

                if good_bad_input_possessions in defense_words:

                    first_number_possession_13_a = possession_list_13_a[0]
                    possession_list_13_a.remove(first_number_possession_13_a)
                    number_possession_13_a = possession_list_13_a[0]
                    possession_string_13_2_a = str(number_possession_13_a)
                    int_number_possession_13_a = True
                    possession_string_13_1_a = away + "'s Possession(s) on defense: "
                    possession_print_string_13_a = possession_string_13_1_a + possession_string_13_2_a

                    print(blue % possession_print_string_13_a)

                elif good_bad_input_possessions in midfield_words:

                    first_number_possession_23_a = possession_list_23_a[0]
                    possession_list_23_a.remove(first_number_possession_23_a)
                    number_possession_23_a = possession_list_23_a[0]
                    possession_string_23_2_a = str(number_possession_23_a)
                    int_number_possession_23_a = True
                    possession_string_23_1_a = away + "'s Possession(s) on midfield: "
                    possession_print_string_23_a = possession_string_23_1_a + possession_string_23_2_a

                    print(blue % possession_print_string_23_a)

                elif good_bad_input_possessions in attack_words:
                    first_number_possession_33_a = possession_list_33_a[0]
                    possession_list_33_a.remove(first_number_possession_33_a)
                    number_possession_33_a = possession_list_33_a[0]
                    possession_string_33_2_a = str(number_possession_33_a)
                    int_number_possession_33_a = True
                    possession_string_33_1_a = away + "'s Possession(s) on attack: "
                    possession_print_string_33_a = possession_string_33_1_a + possession_string_33_2_a
                    print(red % possession_print_string_33_a)

                first_number_possessions_a = possession_list_a[0]
                possession_list_a.remove(first_number_possessions_a)
                number_possessions_a = possession_list_a[0]
                string_number_possessions_a = str(number_possessions_a)
                int_number_possession_a = True
                possession_print_string_a = away + "'s Possession(s): " + string_number_possessions_a
                print(white % possession_print_string_a)

        # -----> * Clearance Function * <-----

        elif choice in cl_words:

            print(home_away)
            team_input = input()

            if team_input == home:

                print(blue % gd_cl, red % pd_cl)
                good_bad_input_cl = input()

                if good_bad_input_cl in cl_gd_words:

                    first_number_cl_gd_h = cl_list_gd_h[0]
                    cl_list_gd_h.remove(first_number_cl_gd_h)
                    number_cl_gd_h = cl_list_gd_h[0]
                    cl_gd_2_h = str(number_cl_gd_h)
                    int_number_cl_gd_h = True
                    cl_gd_1_h = home + "'s Clearance(s) to Teammates: "
                    cl_print_string_gd_h = cl_gd_1_h + cl_gd_2_h
                    print(blue % cl_print_string_gd_h)

                elif good_bad_input_cl in cl_pd_words:

                    first_number_cl_pd_h = cl_list_pd_h[0]
                    cl_list_pd_h.remove(first_number_cl_pd_h)
                    number_cl_pd_h = cl_list_pd_h[0]
                    cl_pd_2_h = str(number_cl_pd_h)
                    int_number_cl_pd_h = True
                    cl_pd_1_h = home + "'s Clearance(s) to Opponents: "
                    cl_print_string_pd_h = cl_pd_1_h + cl_pd_2_h
                    print(red % cl_print_string_pd_h)

                first_number_cl_h = cl_list_h[0]
                cl_list_h.remove(first_number_cl_h)
                number_cl_h = cl_list_h[0]
                cl_h = str(number_cl_h)
                int_number_cl_h = True
                cl_print_string_h = home + "'s Clearance(s): " + cl_h
                print(white % cl_print_string_h)

            elif team_input == away:

                print(blue % gd_cl, red % pd_cl)
                good_bad_input_cl = input()

                if good_bad_input_cl in cl_gd_words:

                    first_number_cl_gd_a = cl_list_gd_a[0]
                    cl_list_gd_a.remove(first_number_cl_gd_a)
                    number_cl_gd_a = cl_list_gd_a[0]
                    cl_gd_2_a = str(number_cl_gd_a)
                    int_number_cl_gd_a = True
                    cl_gd_1_a = away + "'s Clearance(s) to Teammates: "
                    cl_print_string_gd_a = cl_gd_1_a + cl_gd_2_a
                    print(blue % cl_print_string_gd_a)

                elif good_bad_input_cl in cl_pd_words:

                    first_number_cl_pd_a = cl_list_pd_a[0]
                    cl_list_pd_a.remove(first_number_cl_pd_a)
                    number_cl_pd_a = cl_list_pd_a[0]
                    cl_pd_2_a = str(number_cl_pd_a)
                    int_number_cl_pd_a = True
                    cl_pd_1_a = away + "'s Clearance(s) to Opponents: "
                    cl_print_string_pd_a = cl_pd_1_a + cl_pd_2_a
                    print(red % cl_print_string_pd_a)

                first_number_cl_a = cl_list_a[0]
                cl_list_a.remove(first_number_cl_a)
                number_cl_a = cl_list_a[0]
                cl_a = str(number_cl_a)
                int_number_cl_a = True
                cl_print_string_a = away + "'s Clearance(s): " + cl_a
                print(white % cl_print_string_a)

        elif choice in ad_words:

            print(home_away)
            team_input = input()

            if team_input == home:

                print(blue % w_ad, red % l_ad)
                good_bad_input_ad = input()

                if good_bad_input_ad in w_words:

                    first_number_ad_w_h = ad_list_w_h[0]
                    ad_list_w_h.remove(first_number_ad_w_h)
                    number_ad_w_h = ad_list_w_h[0]
                    ad_w_2_h = str(number_ad_w_h)
                    int_number_ad_w_h = True
                    ad_w_1_h = "Aerial Duels won from " + home + ": "
                    ad_print_string_w_h = ad_w_1_h + ad_w_2_h
                    print(blue % ad_print_string_w_h)

                elif good_bad_input_ad in l_words:

                    first_number_ad_l_h = ad_list_l_h[0]
                    ad_list_l_h.remove(first_number_ad_l_h)
                    number_ad_l_h = ad_list_l_h[0]
                    ad_l_2_h = str(number_ad_l_h)
                    int_number_ad_l_h = True
                    ad_l_1_h = "Aerial Duels lost from " + home + ": "
                    ad_print_string_l_h = ad_l_1_h + ad_l_2_h
                    print(red % ad_print_string_l_h)

                first_number_ad_h = ad_list_h[0]
                ad_list_h.remove(first_number_ad_h)
                number_ad_h = ad_list_h[0]
                ad_h = str(number_ad_h)
                int_number_ad_h = True
                ad_print_string_h = "Aerial Duels from " + home + ": " + ad_h
                print(white % ad_print_string_h)

            elif team_input == away:

                print(blue % w_ad, red % l_ad)
                good_bad_input_ad = input()

                if good_bad_input_ad in w_words:

                    first_number_ad_w_a = ad_list_w_a[0]
                    ad_list_w_a.remove(first_number_ad_w_a)
                    number_ad_w_a = ad_list_w_a[0]
                    ad_w_2_a = str(number_ad_w_a)
                    int_number_ad_w_a = True
                    ad_w_1_a = "Aerial Duels won from " + away + ": "
                    ad_print_string_w_a = ad_w_1_a + ad_w_2_a
                    print(blue % ad_print_string_w_a)

                elif good_bad_input_ad in l_words:

                    first_number_ad_l_a = ad_list_l_a[0]
                    ad_list_l_a.remove(first_number_ad_l_a)
                    number_ad_l_a = ad_list_l_a[0]
                    ad_l_2_a = str(number_ad_l_a)
                    int_number_ad_l_a = True
                    ad_l_1_a = "Aerial Duels lost from " + away + ": "
                    ad_print_string_l_a = ad_l_1_a + ad_l_2_a
                    print(red % ad_print_string_l_a)

                first_number_ad_a = ad_list_a[0]
                ad_list_a.remove(first_number_ad_a)
                number_ad_a = ad_list_a[0]
                ad_a = str(number_ad_a)
                int_number_ad_a = True
                ad_print_string_a = "Aerial Duels from " + away + ": " + ad_a
                print(white % ad_print_string_a)

        if choice == home:
            if ball_home:
                continue
            else:
                ball_away = False
                ball_home = True
                start_home = time.time()
                elapsed_away += time.time() - start_away
            print(home + " has possession")

        if choice == away:
            if ball_away:
                continue
            else:
                ball_away = True
                ball_home = False
                start_away = time.time()
                elapsed_home += time.time() - start_home
            print(away + " has ball")

        # when the user does not know the commands a howto.txt will pop up
        # to the howto.txt file. Tip: open it by typing help
        elif choice == "help":
            howto = "notepad.exe howto.txt"
            sub.Popen(howto)

        # -----> * Quit Function * <-----

        # if the user wants to quit he types q to begin the process

        elif choice == "q":

            # text to appear in the end of the program and the separate file
            draft_end_1 = '''The game between %s and %s finished.'''
            draft_end_2 = '''The following stats were recorded for both %s
            and %s:'''

            draft_ending_statement = draft_end_1 + draft_end_2
            ending_statement = draft_ending_statement % (home, away, home,
                                                         away)

            print(ending_statement)
            safile.write(ending_statement)

            # math function to calculate the percentage of each team in a match
            if elapsed_home + elapsed_away == 0:
                print("Possession has not been recorded")
                safile.write("Possession has not been recorded")

            elif elapsed_home + elapsed_away > 0:
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

            if int_number_pk_goal_h and \
                    int_number_pk_saved_h and \
                    int_number_pk_missed_h and \
                    int_number_pk_h and \
                            int_final_pk_h == all_pk_final_h:
                # makes the string to an int variable
                int_final_pk_goal_h = int(pk_goal_2_h)
                int_final_pk_missed_h = int(pk_miss_2_h)
                int_final_pk_saved_h = int(pk_saved_2_h)
                # adds all the "bad" stats to a general variable
                all_pk_bad_h = int_final_pk_missed_h + int_final_pk_saved_h
                all_pk_final_h = int_final_pk_goal_h + int_final_pk_missed_h
                all_pk_final_h += int_final_pk_saved_h
                # calculates the ratio between the good to bad
                perc_num_pk_h = 100 / all_pk_final_h
                perc_num_pk_good_h = perc_num_pk_h * int_final_pk_goal_h
                perc_num_pk_bad_h = perc_num_pk_h * all_pk_bad_h
                round_pk_good_h = round(perc_num_pk_good_h, 1)
                round_pk_bad_h = round(perc_num_pk_bad_h, 1)
                print_pk_good_h = str(round_pk_good_h)
                print_pk_bad_h = str(round_pk_bad_h)
                final_pk_good_h = print_pk_good_h + "% of the Penalty Kicks " \
                                                    "from " + home + \
                                  " were good"

                final_pk_bad_h = print_pk_bad_h + "% of the Penalty Kicks " \
                                                  "from " + home + \
                                 " were bad"
                print(blue % final_pk_good_h)
                print(red % final_pk_bad_h)

            # start print out/write on file each stat
            # if it was called
            if int_number_pk_goal_h:
                # print the number of the stat
                end_pk_goal_h = "Penalty Kick goal(s) from " + home + ": " + pk_goal_2_h
                print(white % end_pk_goal_h)
                # write on the file
                safile.write("Penalty Kick goal(s) from " + home + ": ")
                safile.write(pk_goal_2_h)
            # if it was not called
            elif not int_number_pk_goal_h:
                # print/write the time that the stat was called was None
                print("\nPenalty Kick goal(s) from " + home + ": 0")
                safile.write("\nPenalty Kick goal(s) from " + home + ": 0")

            if int_number_pk_missed_h:
                print("\nPenalty Kick(s) missed from " + home + ": ",
                      pk_miss_2)
                safile.write("\nPenalty Kick(s) missed from " + home + ": ")
                safile.write(pk_miss_2_h)
            elif not int_number_pk_missed_h:
                print("\nPenalty Kick(s) missed from " + home + ": 0 ")
                safile.write("\nPenalty Kick(s) missed from " + home + ": 0 ")

            if int_number_pk_saved_h:
                print("\nPenalty Kick(s) saved from " + home + ": ",
                      pk_saved_2_h)
                safile.write("\nPenalty Kick(s) saved from " + home + ": ")
                safile.write(pk_saved_2_h)
            elif not int_number_pk_saved_h:
                print("\nPenalty Kick(s) saved from " + home + ": 0")
                safile.write("\nPenalty Kick(s) saved from " + home + ": 0")

            if int_number_pk_h:
                print("\nPenalty Kick(s) from " + home + ": ", pk_h)
                safile.write("\nPenalty Kick(s) from " + home + ": ")
                safile.write(pk_h)
            elif not int_number_pk_h:
                print("\nPenalty Kick(s) from " + home + ": 0")
                safile.write("\nPenalty Kick(s) from " + home + ": 0")

            if int_number_pk_goal_a and \
                    int_number_pk_saved_a and \
                    int_number_pk_missed_a and \
                    int_number_pk_a and \
                            int_final_pk_a == all_pk_final_a:
                # makes the string to an int variable
                int_final_pk_goal_a = int(pk_goal_2_a)
                int_final_pk_missed_a = int(pk_miss_2_a)
                int_final_pk_saved_a = int(pk_saved_2_a)
                # adds all the "bad" stats to a general variable
                all_pk_bad_a = int_final_pk_missed_a + int_final_pk_saved_a
                all_pk_final_a = int_final_pk_goal_a + int_final_pk_missed_a
                all_pk_final_a += int_final_pk_saved_a
                # calculates the ratio between the good to bad
                perc_num_pk_a = 100 / all_pk_final_a
                perc_num_pk_good_a = perc_num_pk_a * int_final_pk_goal_a
                perc_num_pk_bad_a = perc_num_pk_a * all_pk_bad_a
                round_pk_good_a = round(perc_num_pk_good_a, 1)
                round_pk_bad_a = round(perc_num_pk_bad_a, 1)
                print_pk_good_a = str(round_pk_good_a)
                print_pk_bad_a = str(round_pk_bad_a)
                final_pk_good_a = print_pk_good_a + "% of the Penalty Kicks " \
                                                    "from " + away + \
                                  " were good"

                final_pk_bad_a = print_pk_bad_a + "% of the Penalty Kicks " \
                                                  "from " + away + \
                                 " were bad"
                print(blue % final_pk_good_a)
                print(red % final_pk_bad_a)

            # start print out/write on file each stat
            # if it was called
            if int_number_pk_goal_a:
                # print the number of the stat
                end_pk_goal_a = "Penalty Kick goal(s) from " + away + ": " + pk_goal_2_a
                print(white % end_pk_goal_a)
                # write on the file
                safile.write("Penalty Kick goal(s) from " + away + ": ")
                safile.write(pk_goal_2_a)
            # if it was not called
            elif not int_number_pk_goal_a:
                # print/write the time that the stat was called was None
                print("\nPenalty Kick goal(s) from " + away + ": 0")
                safile.write("\nPenalty Kick goal(s) from " + away + ": 0")

            if int_number_pk_missed_a:
                print("\nPenalty Kick(s) missed from " + away + ": ",
                      pk_miss_2)
                safile.write("\nPenalty Kick(s) missed from " + away + ": ")
                safile.write(pk_miss_2_a)
            elif not int_number_pk_missed_a:
                print("\nPenalty Kick(s) missed from " + away + ": 0 ")
                safile.write("\nPenalty Kick(s) missed from " + away + ": 0 ")

            if int_number_pk_saved_a:
                print("\nPenalty Kick(s) saved from " + away + ": ",
                      pk_saved_2_a)
                safile.write("\nPenalty Kick(s) saved from " + away + ": ")
                safile.write(pk_saved_2_a)
            elif not int_number_pk_saved_a:
                print("\nPenalty Kick(s) saved from " + away + ": 0")
                safile.write("\nPenalty Kick(s) saved from " + away + ": 0")

            if int_number_pk_a:
                print("\nPenalty Kick(s) from " + away + ": ")
                safile.write("\nPenalty Kick(s) from " + away + ": ")
                safile.write(pk_a)
            elif not int_number_pk_a:
                print("\nPenalty Kick(s) from " + away + ": 0")
                safile.write("\nPenalty Kick(s) from " + away + ": 0")

            if int_number_fk_gd_h and \
                    int_number_fk_pd_h and \
                    int_number_fk_h and \
                            int_final_fk_h == all_fk_final_h:
                int_final_fk_gd_h = int(fk_string_gd_2_h)
                int_final_fk_pd_h = int(fk_string_pd_2_h)
                all_fk_final_h = int_final_fk_gd_h + int_final_fk_pd_h
                perc_num_fk_h = 100 / all_fk_final_h
                perc_num_fk_good_h = perc_num_fk_h * int_final_fk_gd_h
                perc_num_fk_bad_h = perc_num_fk_h * int_final_fk_pd_h
                round_fk_good_h = round(perc_num_fk_good_h, 1)
                round_fk_bad_h = round(perc_num_fk_bad_h, 1)
                print_fk_good_h = str(round_fk_good_h)
                print_fk_bad_h = str(round_fk_bad_h)
                final_fk_good_h = print_fk_good_h + "% of the Free Kicks " \
                                                    "from " + home + \
                                  " were good"
                final_fk_bad_h = print_fk_bad_h + "% of the Free Kicks " \
                                                  "from " + home + \
                                 " were bad"
                print(blue % final_fk_good_h)
                print(red % final_fk_bad_h)

            if int_number_fk_gd_h:
                print("Free Kick(s) with Good Delivery from " + home + ": ",
                      fk_string_gd_2_h)
                safile.write("\nFree Kick(s) with Good Delivery from" + home +
                             ": ")
                safile.write(fk_string_gd_2_h)
            elif not int_number_fk_gd_h:
                print("Free Kick(s) with Good Delivery from " + home + ": 0")
                safile.write(
                    "\nFree Kick(s) with Good Delivery from " + home + ": 0")

            if int_number_fk_pd_h:
                print("Free Kick(s) with Good Delivery from " + home + ": ",
                      fk_string_pd_2_h)
                safile.write(
                    "\nFree Kick(s) with Poor Delivery from " + home + ": ")
                safile.write(fk_string_pd_2_h)
            elif not int_number_fk_pd_h:
                print("Free Kick(s) with Poor Delivery from " + home + ": 0")
                safile.write(
                    "\nFree Kick(s) with Poor Delivery from " + home + ": 0")

            if int_number_fk_h:
                print("Free Kick(s) from " + home + ": ", string_number_fk_h)
                safile.write("\nFree Kick(s) from " + home + ": ")
                safile.write(string_number_fk_h)
            elif not int_number_fk_h:
                print("Free Kick(s) from " + home + ": 0")
                safile.write("\nFree Kick(s) from " + home + ": 0")

            if int_number_fk_gd_a and \
                    int_number_fk_pd_a and \
                    int_number_fk_a and \
                            int_final_fk_a == all_fk_final_a:
                int_final_fk_gd_a = int(fk_string_gd_2_a)
                int_final_fk_pd_a = int(fk_string_pd_2_a)
                all_fk_final_a = int_final_fk_gd_a + int_final_fk_pd_a
                perc_num_fk_a = 100 / all_fk_final_a
                perc_num_fk_good_a = perc_num_fk_a * int_final_fk_gd_a
                perc_num_fk_bad_a = perc_num_fk_a * int_final_fk_pd_a
                round_fk_good_a = round(perc_num_fk_good_a, 1)
                round_fk_bad_a = round(perc_num_fk_bad_a, 1)
                print_fk_good_a = str(round_fk_good_a)
                print_fk_bad_a = str(round_fk_bad_a)
                final_fk_good_a = print_fk_good_a + "% of the Free Kicks " \
                                                    "from " + away + \
                                  " were good"
                final_fk_bad_a = print_fk_bad_a + "% of the Free Kicks " \
                                                  "from " + away + \
                                 " were bad"
                print(blue % final_fk_good_a)
                print(red % final_fk_bad_a)

            if int_number_fk_gd_a:
                print("Free Kick(s) with Good Delivery from " + away + ": ",
                      fk_string_gd_2_a)
                safile.write("\nFree Kick(s) with Good Delivery from" + away +
                             ": ")
                safile.write(fk_string_gd_2_a)
            elif not int_number_fk_gd_a:
                print("Free Kick(s) with Good Delivery from " + away + ": 0")
                safile.write(
                    "\nFree Kick(s) with Good Delivery from " + away + ": 0")

            if int_number_fk_pd_a:
                print("Free Kick(s) with Good Delivery from " + away + ": ",
                      fk_string_pd_2_a)
                safile.write(
                    "\nFree Kick(s) with Poor Delivery from " + away + ": ")
                safile.write(fk_string_pd_2_a)
            elif not int_number_fk_pd_a:
                print("Free Kick(s) with Poor Delivery from " + away + ": 0")
                safile.write(
                    "\nFree Kick(s) with Poor Delivery from " + away + ": 0")

            if int_number_fk_a:
                print("Free Kick(s) from " + away + ": ", string_number_fk_a)
                safile.write("\nFree Kick(s) from " + away + ": ")
                safile.write(string_number_fk_a)
            elif not int_number_fk_a:
                print("Free Kick(s) from " + away + ": 0")
                safile.write("\nFree Kick(s) from " + away + ": 0")

            if int_number_ck_gd_h and \
                    int_number_ck_pd_h and \
                    int_number_ck_h and \
                            int_final_ck_h == all_ck_final_h:
                int_final_ck_gd_h = int(ck_string_gd_2_h)
                int_final_ck_pd_h = int(ck_string_pd_2_h)
                all_ck_final_h = int_final_ck_gd_h + int_final_ck_pd_h
                perc_num_ck_h = 100 / all_ck_final_h
                perc_num_ck_good_h = perc_num_ck_h * int_final_ck_gd_h
                perc_num_ck_bad_h = perc_num_ck_h * int_final_ck_pd_h
                round_ck_good_h = round(perc_num_ck_good_h, 1)
                round_ck_bad_h = round(perc_num_ck_bad_h, 1)
                print_ck_good_h = str(round_ck_good_h)
                print_ck_bad_h = str(round_ck_bad_h)
                final_ck_good_h = print_ck_good_h + "% of the Corner Kicks " \
                                                    "from " + home + \
                                  " were good"
                final_ck_bad_h = print_ck_bad_h + "% of the Corner Kicks " \
                                                  "from " + home + \
                                 " were bad"
                print(blue % final_ck_good_h)
                print(red % final_ck_bad_h)

            if int_number_ck_gd_h:
                print("Corner Kick(s) with Good Delivery from " + home + ": ",
                      ck_string_gd_2_h)
                safile.write(
                    "\nCorner Kick(s) with Good Delivery from" + home +
                    ": ")
                safile.write(ck_string_gd_2_h)
            elif not int_number_ck_gd_h:
                print("Corner Kick(s) with Good Delivery from " + home + ": 0")
                safile.write(
                    "\nCorner Kick(s) with Good Delivery from " + home + ": 0")

            if int_number_ck_pd_h:
                print("Corner Kick(s) with Good Delivery from " + home + ": ",
                      ck_string_pd_2_h)
                safile.write(
                    "\nCorner Kick(s) with Poor Delivery from " + home + ": ")
                safile.write(ck_string_pd_2_h)
            elif not int_number_ck_pd_h:
                print("Corner Kick(s) with Poor Delivery from " + home + ": 0")
                safile.write(
                    "\nCorner Kick(s) with Poor Delivery from " + home + ": 0")

            if int_number_ck_h:
                print("Corner Kick(s) from " + home + ": ", string_number_ck_h)
                safile.write("\nCorner Kick(s) from " + home + ": ")
                safile.write(string_number_ck_h)
            elif not int_number_ck_h:
                print("Corner Kick(s) from " + home + ": 0")
                safile.write("\nCorner Kick(s) from " + home + ": 0")

            if int_number_ck_gd_a and \
                    int_number_ck_pd_a and \
                    int_number_ck_a and \
                            int_final_ck_a == all_ck_final_a:
                int_final_ck_gd_a = int(ck_string_gd_2_a)
                int_final_ck_pd_a = int(ck_string_pd_2_a)
                all_ck_final_a = int_final_ck_gd_a + int_final_ck_pd_a
                perc_num_ck_a = 100 / all_ck_final_a
                perc_num_ck_good_a = perc_num_ck_a * int_final_ck_gd_a
                perc_num_ck_bad_a = perc_num_ck_a * int_final_ck_pd_a
                round_ck_good_a = round(perc_num_ck_good_a, 1)
                round_ck_bad_a = round(perc_num_ck_bad_a, 1)
                print_ck_good_a = str(round_ck_good_a)
                print_ck_bad_a = str(round_ck_bad_a)
                final_ck_good_a = print_ck_good_a + "% of the Corner Kicks " \
                                                    "from " + away + \
                                  " were good"
                final_ck_bad_a = print_ck_bad_a + "% of the Corner Kicks " \
                                                  "from " + away + \
                                 " were bad"
                print(blue % final_ck_good_a)
                print(red % final_ck_bad_a)

            if int_number_ck_gd_a:
                print("Corner Kick(s) with Good Delivery from " + away + ": ",
                      ck_string_gd_2_a)
                safile.write(
                    "\nCorner Kick(s) with Good Delivery from" + away +
                    ": ")
                safile.write(ck_string_gd_2_a)
            elif not int_number_ck_gd_a:
                print("Corner Kick(s) with Good Delivery from " + away + ": 0")
                safile.write(
                    "\nCorner Kick(s) with Good Delivery from " + away + ": 0")

            if int_number_ck_pd_a:
                print("Corner Kick(s) with Good Delivery from " + away + ": ",
                      ck_string_pd_2_a)
                safile.write(
                    "\nCorner Kick(s) with Poor Delivery from " + away + ": ")
                safile.write(ck_string_pd_2_a)
            elif not int_number_ck_pd_a:
                print("Corner Kick(s) with Poor Delivery from " + away + ": 0")
                safile.write(
                    "\nCorner Kick(s) with Poor Delivery from " + away + ": 0")

            if int_number_ck_a:
                print("Corner Kick(s) from " + away + ": ", string_number_ck_a)
                safile.write("\nCorner Kick(s) from " + away + ": ")
                safile.write(string_number_ck_a)
            elif not int_number_ck_a:
                print("Corner Kick(s) from " + away + ": 0")
                safile.write("\nCorner Kick(s) from " + away + ": 0")

            if int_number_ti_gd_h and \
                    int_number_ti_pd_h and \
                    int_number_ti_h and \
                            int_final_ti_h == all_ti_final_h:
                int_final_ti_gd_h = int(ti_string_gd_2_h)
                int_final_ti_pd_h = int(ti_string_pd_2_h)
                all_ti_final_h = int_final_ti_gd_h + int_final_ti_pd_h
                perc_num_ti_h = 100 / all_ti_final_h
                perc_num_ti_good_h = perc_num_ti_h * int_final_ti_gd_h
                perc_num_ti_bad_h = perc_num_ti_h * int_final_ti_pd_h
                round_ti_good_h = round(perc_num_ti_good_h, 1)
                round_ti_bad_h = round(perc_num_ti_bad_h, 1)
                print_ti_good_h = str(round_ti_good_h)
                print_ti_bad_h = str(round_ti_bad_h)
                final_ti_good_h = print_ti_good_h + "% of the Throw Ins " \
                                                    "from " + home + \
                                  " were good"
                final_ti_bad_h = print_ti_bad_h + "% of the Throw Ins " \
                                                  "from " + home + \
                                 " were bad"
                print(blue % final_ti_good_h)
                print(red % final_ti_bad_h)

            if int_number_ti_gd_h:
                print("Throw In(s) with Good Delivery from " + home + ": ",
                      ti_string_gd_2_h)
                safile.write("\nThrow In(s) with Good Delivery from" + home +
                             ": ")
                safile.write(ti_string_gd_2_h)
            elif not int_number_ti_gd_h:
                print("Throw In(s) with Good Delivery from " + home + ": 0")
                safile.write(
                    "\nThrow In(s) with Good Delivery from " + home + ": 0")

            if int_number_ti_pd_h:
                print("Throw In(s) with Good Delivery from " + home + ": ",
                      ti_string_pd_2_h)
                safile.write(
                    "\nThrow In(s) with Poor Delivery from " + home + ": ")
                safile.write(ti_string_pd_2_h)
            elif not int_number_ti_pd_h:
                print("Throw In(s) with Poor Delivery from " + home + ": 0")
                safile.write(
                    "\nThrow In(s) with Poor Delivery from " + home + ": 0")

            if int_number_ti_h:
                print("Throw In(s) from " + home + ": ", string_number_ti_h)
                safile.write("\nThrow In(s) from " + home + ": ")
                safile.write(string_number_ti_h)
            elif not int_number_ti_h:
                print("Throw In(s) from " + home + ": 0")
                safile.write("\nThrow In(s) from " + home + ": 0")

            if int_number_ti_gd_a and \
                    int_number_ti_pd_a and \
                    int_number_ti_a and \
                            int_final_ti_a == all_ti_final_a:
                int_final_ti_gd_a = int(ti_string_gd_2_a)
                int_final_ti_pd_a = int(ti_string_pd_2_a)
                all_ti_final_a = int_final_ti_gd_a + int_final_ti_pd_a
                perc_num_ti_a = 100 / all_ti_final_a
                perc_num_ti_good_a = perc_num_ti_a * int_final_ti_gd_a
                perc_num_ti_bad_a = perc_num_ti_a * int_final_ti_pd_a
                round_ti_good_a = round(perc_num_ti_good_a, 1)
                round_ti_bad_a = round(perc_num_ti_bad_a, 1)
                print_ti_good_a = str(round_ti_good_a)
                print_ti_bad_a = str(round_ti_bad_a)
                final_ti_good_a = print_ti_good_a + "% of the Throw Ins " \
                                                    "from " + away + \
                                  " were good"
                final_ti_bad_a = print_ti_bad_a + "% of the Throw Ins " \
                                                  "from " + away + \
                                 " were bad"
                print(blue % final_ti_good_a)
                print(red % final_ti_bad_a)

            if int_number_ti_gd_a:
                print("Throw In(s) with Good Delivery from " + away + ": ",
                      ti_string_gd_2_a)
                safile.write("\nThrow In(s) with Good Delivery from" + away +
                             ": ")
                safile.write(ti_string_gd_2_a)
            elif not int_number_ti_gd_a:
                print("Throw In(s) with Good Delivery from " + away + ": 0")
                safile.write(
                    "\nThrow In(s) with Good Delivery from " + away + ": 0")

            if int_number_ti_pd_a:
                print("Throw In(s) with Good Delivery from " + away + ": ",
                      ti_string_pd_2_a)
                safile.write(
                    "\nThrow In(s) with Poor Delivery from " + away + ": ")
                safile.write(ti_string_pd_2_a)
            elif not int_number_ti_pd_a:
                print("Throw In(s) with Poor Delivery from " + away + ": 0")
                safile.write(
                    "\nThrow In(s) with Poor Delivery from " + away + ": 0")

            if int_number_ti_a:
                print("Throw In(s) from " + away + ": ", string_number_ti_a)
                safile.write("\nThrow In(s) from " + away + ": ")
                safile.write(string_number_ti_a)
            elif not int_number_ti_a:
                print("Throw In(s) from " + away + ": 0")
                safile.write("\nThrow In(s) from " + away + ": 0")

            if int_number_cross_gd_h and \
                    int_number_cross_pd_h and \
                    int_number_cross_h and \
                            int_final_cross_h == all_cross_final_h:
                int_final_cross_gd_h = int(cross_string_gd_2_h)
                int_final_cross_pd_h = int(cross_string_pd_2_h)
                all_cross_final_h = int_final_cross_gd_h + int_final_cross_pd_h
                perc_num_cross_h = 100 / all_cross_final_h
                perc_num_cross_good_h = perc_num_cross_h * int_final_cross_gd_h
                perc_num_cross_bad_h = perc_num_cross_h * int_final_cross_pd_h
                round_cross_good_h = round(perc_num_cross_good_h, 1)
                round_cross_bad_h = round(perc_num_cross_bad_h, 1)
                print_cross_good_h = str(round_cross_good_h)
                print_cross_bad_h = str(round_cross_bad_h)
                final_cross_good_h = print_cross_good_h + "% of the Crosses " \
                                                          "from " + home + \
                                     " were good"
                final_cross_bad_h = print_cross_bad_h + "% of the Crosses " \
                                                        "from " + home + \
                                    " were bad"
                print(blue % final_cross_good_h)
                print(red % final_cross_bad_h)

            if int_number_cross_gd_h:
                print("Cross(es) with Good Delivery from " + home + ": ",
                      cross_string_gd_2_h)
                safile.write("\nCross(es) with Good Delivery from" + home +
                             ": ")
                safile.write(cross_string_gd_2_h)
            elif not int_number_cross_gd_h:
                print("Cross(es) with Good Delivery from " + home + ": 0")
                safile.write(
                    "\nCross(es) with Good Delivery from " + home + ": 0")

            if int_number_cross_pd_h:
                print("Cross(es) with Good Delivery from " + home + ": ",
                      cross_string_pd_2_h)
                safile.write(
                    "\nCross(es) with Poor Delivery from " + home + ": ")
                safile.write(cross_string_pd_2_h)
            elif not int_number_cross_pd_h:
                print("Cross(es) with Poor Delivery from " + home + ": 0")
                safile.write(
                    "\nCross(es) with Poor Delivery from " + home + ": 0")

            if int_number_cross_h:
                print("Cross(es) from " + home + ": ", string_number_cross_h)
                safile.write("\nCross(es) from " + home + ": ")
                safile.write(string_number_cross_h)
            elif not int_number_cross_h:
                print("Cross(es) from " + home + ": 0")
                safile.write("\nCross(es) from " + home + ": 0")

            if int_number_cross_gd_a and \
                    int_number_cross_pd_a and \
                    int_number_cross_a and \
                            int_final_cross_a == all_cross_final_a:
                int_final_cross_gd_a = int(cross_string_gd_2_a)
                int_final_cross_pd_a = int(cross_string_pd_2_a)
                all_cross_final_a = int_final_cross_gd_a + int_final_cross_pd_a
                perc_num_cross_a = 100 / all_cross_final_a
                perc_num_cross_good_a = perc_num_cross_a * int_final_cross_gd_a
                perc_num_cross_bad_a = perc_num_cross_a * int_final_cross_pd_a
                round_cross_good_a = round(perc_num_cross_good_a, 1)
                round_cross_bad_a = round(perc_num_cross_bad_a, 1)
                print_cross_good_a = str(round_cross_good_a)
                print_cross_bad_a = str(round_cross_bad_a)
                final_cross_good_a = print_cross_good_a + "% of the Crosses " \
                                                          "from " + away + \
                                     " were good"
                final_cross_bad_a = print_cross_bad_a + "% of the Crosses " \
                                                        "from " + away + \
                                    " were bad"
                print(blue % final_cross_good_a)
                print(red % final_cross_bad_a)

            if int_number_cross_gd_a:
                print("Cross(es) with Good Delivery from " + away + ": ",
                      cross_string_gd_2_a)
                safile.write("\nCross(es) with Good Delivery from" + away +
                             ": ")
                safile.write(cross_string_gd_2_a)
            elif not int_number_cross_gd_a:
                print("Cross(es) with Good Delivery from " + away + ": 0")
                safile.write(
                    "\nCross(es) with Good Delivery from " + away + ": 0")

            if int_number_cross_pd_a:
                print("Cross(es) with Good Delivery from " + away + ": ",
                      cross_string_pd_2_a)
                safile.write(
                    "\nCross(es) with Poor Delivery from " + away + ": ")
                safile.write(cross_string_pd_2_a)
            elif not int_number_cross_pd_a:
                print("Cross(es) with Poor Delivery from " + away + ": 0")
                safile.write(
                    "\nCross(es) with Poor Delivery from " + away + ": 0")

            if int_number_cross_a:
                print("Cross(es) from " + away + ": ", string_number_cross_a)
                safile.write("\nCross(es) from " + away + ": ")
                safile.write(string_number_cross_a)
            elif not int_number_cross_a:
                print("Cross(es) from " + away + ": 0")
                safile.write("\nCross(es) from " + away + ": 0")

            # here bitches --490 lines left

            if int_number_shot_ont_h and \
                    int_number_shot_oft_h and \
                    int_number_shot_bs_h and \
                    int_number_shot_h and \
                            int_final_shot_h == all_shot_final_h:
                # makes the string to an int variable
                int_final_shot_ont_h = int(shot_ont_2_h)
                int_final_shot_bs_h = int(shot_bs_2_h)
                int_final_shot_oft_h = int(shot_oft_2_h)
                # adds all the "bad" stats to a general variable
                all_shot_bad_h = int_final_shot_bs_h + int_final_shot_oft_h
                all_shot_final_h = int_final_shot_ont_h + int_final_shot_bs_h
                all_shot_final_h += int_final_shot_oft_h
                # calculates the ratio between the good to bad
                perc_num_shot_h = 100 / all_shot_final_h
                perc_num_shot_good_h = perc_num_shot_h * int_final_shot_ont_h
                perc_num_shot_bad_h = perc_num_shot_h * all_shot_bad_h
                round_shot_good_h = round(perc_num_shot_good_h, 1)
                round_shot_bad_h = round(perc_num_shot_bad_h, 1)
                print_shot_good_h = str(round_shot_good_h)
                print_shot_bad_h = str(round_shot_bad_h)
                final_shot_good_h = print_shot_good_h + "% of the Shot " \
                                                        "from " + home + \
                                    " were good"

                final_shot_bad_h = print_shot_bad_h + "% of the Shot " \
                                                      "from " + home + \
                                   " were bad"
                print(blue % final_shot_good_h)
                print(red % final_shot_bad_h)

            if int_number_shot_ont_h:
                end_shot_ont_h = "Shot on target(s) from " + home + ": " + shot_ont_2_h
                print(white % end_shot_ont_h)
                # write on the file
                safile.write("Shot on target(s) from " + home + ": ")
                safile.write(shot_ont_2_h)
            elif not int_number_shot_ont_h:
                print("\nShot on target(s) from " + home + ": 0")
                safile.write("\nShot on target(s) from " + home + ": 0")

            if int_number_shot_bs_h:
                print("\nShot(s) blocked from " + home + ": ", shot_bs_2)
                safile.write("\nShot(s) blocked from " + home + ": ")
                safile.write(shot_bs_2_h)
            elif not int_number_shot_bs_h:
                print("\nShot(s) blocked from " + home + ": 0 ")
                safile.write("\nShot(s) blocked from " + home + ": 0 ")

            if int_number_shot_oft_h:
                print("\nShot(s) off target from " + home + ": ", shot_oft_2_h)
                safile.write("\nShot(s) off target from " + home + ": ")
                safile.write(shot_oft_2_h)
            elif not int_number_shot_oft_h:
                print("\nShot(s) off target from " + home + ": 0")
                safile.write("\nShot(s) off target from " + home + ": 0")

            if int_number_shot_h:
                print("Shot(s): ", string_number_shot_h)
                safile.write("\nShot(s) from " + home + ": ")
                safile.write(string_number_shot_h)
            elif not int_number_shot_h:
                print("\nShot(s) from " + home + ": 0")
                safile.write("\nShot(s) from " + home + ": 0")

            if int_number_shot_ont_a and \
                    int_number_shot_oft_a and \
                    int_number_shot_bs_a and \
                    int_number_shot_a and \
                            int_final_shot_a == all_shot_final_a:
                # makes the string to an int variable
                int_final_shot_ont_a = int(shot_ont_2_a)
                int_final_shot_bs_a = int(shot_bs_2_a)
                int_final_shot_oft_a = int(shot_oft_2_a)
                # adds all the "bad" stats to a general variable
                all_shot_bad_a = int_final_shot_bs_a + int_final_shot_oft_a
                all_shot_final_a = int_final_shot_ont_a + int_final_shot_bs_a
                all_shot_final_a += int_final_shot_oft_a
                # calculates the ratio between the good to bad
                perc_num_shot_a = 100 / all_shot_final_a
                perc_num_shot_good_a = perc_num_shot_a * int_final_shot_ont_a
                perc_num_shot_bad_a = perc_num_shot_a * all_shot_bad_a
                round_shot_good_a = round(perc_num_shot_good_a, 1)
                round_shot_bad_a = round(perc_num_shot_bad_a, 1)
                print_shot_good_a = str(round_shot_good_a)
                print_shot_bad_a = str(round_shot_bad_a)
                final_shot_good_a = print_shot_good_a + "% of the Shot " \
                                                        "from " + away + \
                                    " were good"

                final_shot_bad_a = print_shot_bad_a + "% of the Shot " \
                                                      "from " + away + \
                                   " were bad"
                print(blue % final_shot_good_a)
                print(red % final_shot_bad_a)

            if int_number_shot_ont_a:
                end_shot_ont_a = "Shot on target(s) from " + away + ": " + shot_ont_2_a
                print(white % end_shot_ont_a)
                safile.write("Shot on target(s) from " + away + ": ")
                safile.write(shot_ont_2_a)
            elif not int_number_shot_ont_a:
                print("\nShot on target(s) from " + away + ": 0")
                safile.write("\nShot on target(s) from " + away + ": 0")

            if int_number_shot_bs_a:
                print("\nShot(s) blocked from " + away + ": ", shot_bs_2)
                safile.write("\nShot(s) blocked from " + away + ": ")
                safile.write(shot_bs_2_a)
            elif not int_number_shot_bs_a:
                print("\nShot(s) blocked from " + away + ": 0 ")
                safile.write("\nShot(s) blocked from " + away + ": 0 ")

            if int_number_shot_oft_a:
                print("\nShot(s) off target from " + away + ": ", shot_oft_2_a)
                safile.write("\nShot(s) off target from " + away + ": ")
                safile.write(shot_oft_2_a)
            elif not int_number_shot_oft_a:
                print("\nShot(s) off target from " + away + ": 0")
                safile.write("\nShot(s) off target from " + away + ": 0")

            if int_number_shot_a:
                print("\nShot(s) from " + away + ": ", string_number_shot_a)
                safile.write("\nShot(s) from " + away + ": ")
                safile.write(string_number_shot_a)
            elif not int_number_shot_a:
                print("\nShot(s) from " + away + ": 0")
                safile.write("\nShot(s) from " + away + ": 0")

            if int_number_header_ont_h and \
                    int_number_header_oft_h and \
                    int_number_header_h and \
                            int_final_header_h == all_header_final_h:
                int_final_header_ont_h = int(header_string_gd_2_h)
                int_final_header_oft_h = int(header_string_pd_2_h)
                all_header_final_h = int_final_header_ont_h + int_final_header_oft_h
                perc_num_header_h = 100 / all_header_final_h
                perc_num_header_good_h = perc_num_header_h * int_final_header_ont_h
                perc_num_header_bad_h = perc_num_header_h * int_final_header_oft_h
                round_header_good_h = round(perc_num_header_good_h, 1)
                round_header_bad_h = round(perc_num_header_bad_h, 1)
                print_header_good_h = str(round_header_good_h)
                print_header_bad_h = str(round_header_bad_h)
                final_header_good_h = print_header_good_h + "% of the Headers " \
                                                            "from " + home + \
                                      " were good"
                final_header_bad_h = print_header_bad_h + "% of the Headers " \
                                                          "from " + home + \
                                     " were bad"
                print(blue % final_header_good_h)
                print(red % final_header_bad_h)

            if int_number_header_ont_h:
                print("Header(s) on target from " + home + ": ",
                      header_string_gd_2_h)
                safile.write("\nHeader(s) on target from" + home +
                             ": ")
                safile.write(header_string_gd_2_h)
            elif not int_number_header_ont_h:
                print("Header(s) on target from " + home + ": 0")
                safile.write(
                    "\nHeader(s) on target from " + home + ": 0")

            if int_number_header_oft_h:
                print("Header(s) on target from " + home + ": ",
                      header_string_pd_2_h)
                safile.write(
                    "\nHeader(s) off target from " + home + ": ")
                safile.write(header_string_pd_2_h)
            elif not int_number_header_oft_h:
                print("Header(s) off target from " + home + ": 0")
                safile.write(
                    "\nHeader(s) off target from " + home + ": 0")

            if int_number_header_h:
                print("Header(s) from " + home + ": ", string_number_header_h)
                safile.write("\nHeader(s) from " + home + ": ")
                safile.write(string_number_header_h)
            elif not int_number_header_h:
                print("Header(s) from " + home + ": 0")
                safile.write("\nHeader(s) from " + home + ": 0")

            if int_number_header_ont_a and \
                    int_number_header_oft_a and \
                    int_number_header_a and \
                            int_final_header_a == all_header_final_a:
                int_final_header_ont_a = int(header_string_gd_2_a)
                int_final_header_oft_a = int(header_string_pd_2_a)
                all_header_final_a = int_final_header_ont_a + int_final_header_oft_a
                perc_num_header_a = 100 / all_header_final_a
                perc_num_header_good_a = perc_num_header_a * int_final_header_ont_a
                perc_num_header_bad_a = perc_num_header_a * int_final_header_oft_a
                round_header_good_a = round(perc_num_header_good_a, 1)
                round_header_bad_a = round(perc_num_header_bad_a, 1)
                print_header_good_a = str(round_header_good_a)
                print_header_bad_a = str(round_header_bad_a)
                final_header_good_a = print_header_good_a + "% of the Headers " \
                                                            "from " + away + \
                                      " were good"
                final_header_bad_a = print_header_bad_a + "% of the Headers " \
                                                          "from " + away + \
                                     " were bad"
                print(blue % final_header_good_a)
                print(red % final_header_bad_a)

            if int_number_header_ont_a:
                print("Header(s) on target from " + away + ": ",
                      header_string_gd_2_a)
                safile.write("\nHeader(s) on target from" + away +
                             ": ")
                safile.write(header_string_gd_2_a)
            elif not int_number_header_ont_a:
                print("Header(s) on target from " + away + ": 0")
                safile.write("\nHeader(s) on target from " + away + ": 0")

            if int_number_header_oft_a:
                print("Header(s) on target from " + away + ": ",
                      header_string_pd_2_a)
                safile.write("\nHeader(s) off target from " + away + ":")

                safile.write(header_string_pd_2_a)
            elif not int_number_header_oft_a:
                print("Header(s) off target from " + away + ": 0")
                safile.write("\nHeader(s) off target from " + away + ": 0")

            if int_number_header_a:
                print("Header(s) from " + away + ": ", string_number_header_a)
                safile.write("\nHeader(s) from " + away + ": ")
                safile.write(string_number_header_a)
            elif not int_number_header_a:
                print("Header(s) from " + away + ": 0")
                safile.write("\nHeader(s) from " + away + ": 0")

            if int_number_v1_w_h and \
                    int_number_v1_l_h and \
                    int_number_v1_h and \
                            int_final_v1_h == all_v1_final_h:
                int_final_v1_w_h = int(v1_string_gd_2_h)
                int_final_v1_l_h = int(v1_string_pd_2_h)
                all_v1_final_h = int_final_v1_w_h + int_final_v1_l_h
                perc_num_v1_h = 100 / all_v1_final_h
                perc_num_v1_good_h = perc_num_v1_h * int_final_v1_w_h
                perc_num_v1_bad_h = perc_num_v1_h * int_final_v1_l_h
                round_v1_good_h = round(perc_num_v1_good_h, 1)
                round_v1_bad_h = round(perc_num_v1_bad_h, 1)
                print_v1_good_h = str(round_v1_good_h)
                print_v1_bad_h = str(round_v1_bad_h)
                final_v1_good_h = print_v1_good_h + "% of the 1v1 " \
                                                    "from " + home + \
                                  " were good"
                final_v1_bad_h = print_v1_bad_h + "% of the 1v1 " \
                                                  "from " + home + \
                                 " were bad"
                print(blue % final_v1_good_h)
                print(red % final_v1_bad_h)

            if int_number_v1_w_h:
                print("1v1 won from " + home + ": ",
                      v1_string_gd_2_h)
                safile.write("\n1v1 won from" + home +
                             ": ")
                safile.write(v1_string_gd_2_h)
            elif not int_number_v1_w_h:
                print("1v1 won from " + home + ": 0")
                safile.write(
                    "\n1v1 won from " + home + ": 0")

            if int_number_v1_l_h:
                print("1v1 won from " + home + ": ",
                      v1_string_pd_2_h)
                safile.write(
                    "\n1v1 lost from " + home + ": ")
                safile.write(v1_string_pd_2_h)
            elif not int_number_v1_l_h:
                print("1v1 lost from " + home + ": 0")
                safile.write(
                    "\n1v1 lost from " + home + ": 0")

            if int_number_v1_h:
                print("1v1 from " + home + ": ", string_number_v1_h)
                safile.write("\n1v1 from " + home + ": ")
                safile.write(string_number_v1_h)
            elif not int_number_v1_h:
                print("1v1 from " + home + ": 0")
                safile.write("\n1v1 from " + home + ": 0")

            if int_number_v1_w_a and \
                    int_number_v1_l_a and \
                    int_number_v1_a and \
                            int_final_v1_a == all_v1_final_a:
                int_final_v1_w_a = int(v1_string_gd_2_a)
                int_final_v1_l_a = int(v1_string_pd_2_a)
                all_v1_final_a = int_final_v1_w_a + int_final_v1_l_a
                perc_num_v1_a = 100 / all_v1_final_a
                perc_num_v1_good_a = perc_num_v1_a * int_final_v1_w_a
                perc_num_v1_bad_a = perc_num_v1_a * int_final_v1_l_a
                round_v1_good_a = round(perc_num_v1_good_a, 1)
                round_v1_bad_a = round(perc_num_v1_bad_a, 1)
                print_v1_good_a = str(round_v1_good_a)
                print_v1_bad_a = str(round_v1_bad_a)
                final_v1_good_a = print_v1_good_a + "% of the 1v1 " \
                                                    "from " + away + \
                                  " were good"
                final_v1_bad_a = print_v1_bad_a + "% of the 1v1 " \
                                                  "from " + away + \
                                 " were bad"
                print(blue % final_v1_good_a)
                print(red % final_v1_bad_a)

            if int_number_v1_w_a:
                print("1v1 won from " + away + ": ",
                      v1_string_gd_2_a)
                safile.write("\n1v1 won from" + away +
                             ": ")
                safile.write(v1_string_gd_2_a)
            elif not int_number_v1_w_a:
                print("1v1 won from " + away + ": 0")
                safile.write(
                    "\n1v1 won from " + away + ": 0")

            if int_number_v1_l_a:
                print("1v1 won from " + away + ": ",
                      v1_string_pd_2_a)
                safile.write(
                    "\n1v1 lost from " + away + ":")

                safile.write(v1_string_pd_2_a)
            elif not int_number_v1_l_a:
                print("1v1 lost from " + away + ": 0")
                safile.write(
                    "\n1v1 lost from " + away + ": 0")

            if int_number_v1_a:
                print("1v1 from " + away + ": ", string_number_v1_a)
                safile.write("\n1v1 from " + away + ": ")
                safile.write(string_number_v1_a)
            elif not int_number_v1_a:
                print("1v1 from " + away + ": 0")
                safile.write("\n1v1 from " + away + ": 0")

            if int_number_lpi_sb_attack:
                end_lpi_sb_attack = "Second Ball Long Pass Interceptions on " \
                                    "Attack: "
                print(end_lpi_sb_attack + lpi_attack_sb_2)
                lpisba_f = "\nSecond Ball Long Pass Interceptions on Attack: "
                safile.write(lpisba_f)
                safile.write(lpi_attack_sb_2)
            elif not int_number_lpi_sb_attack:
                lpisba_f0 = "Second Ball Long Pass Interceptions on Attack: 0"
                print(lpisba_f0)
                safile.write("\n" + lpisba_f0)

            if int_number_lpi_tb_attack:
                lpitba = "Third Ball Long Pass Interceptions on Attack: "
                print(lpitba + lpi_attack_tb_2)
                safile.write(lpitba)
                safile.write(lpi_attack_tb_2)
            elif not int_number_lpi_tb_attack:
                lpitba_f0 = "Third Ball Long Pass Interceptions on Attack: 0"
                print(lpitba_f0)
                safile.write("\n" + lpitba_f0)

            if int_number_lpi_attack:
                lpia = "Long Pass Interceptions on Attack: "
                print("\n" + lpia + lpi_attack_2)
                safile.write("\nLong Pass Interceptions on Attack: ")
                safile.write(lpi_attack_2)
            elif not int_number_lpi_attack:
                print("Long Pass Interceptions on Attack: 0")
                safile.write("\nLong Pass Interceptions on Attack: 0")

            if int_number_lpi_sb_defense:
                lpisbd = "Second Ball Long Pass Interceptions on Defense: "
                print(lpisbd + lpi_attack_tb_2)
                safile.write("\n" + lpisbd)
                safile.write(lpi_attack_tb_2)
            elif not int_number_lpi_sb_defense:
                lpisbb_f0 = "Second Ball Long Pass Interceptions on Defense: 0"
                print("Second Ball Long Pass Interceptions on Defense: 0")
                safile.write("\n" + lpisbb_f0)

            if int_number_lpi_tb_defense:
                lpitbd = "Third Ball Long Pass Interceptions on Defense: "
                print(lpitbd + lpi_attack_tb_2)
                safile.write("\n" + lpitbd)
                safile.write(lpi_attack_tb_2)
            elif not int_number_lpi_tb_defense:
                lpitbd_f0 = "Third Ball Long Pass Interceptions on Defense: 0"
                print(lpitbd_f0)
                safile.write("\n" + lpitbd_f0)

            if int_number_lpi_defense:
                lpid = "Long Pass Interceptions on Defense: "
                print(lpid + lpi_defense_2)
                safile.write("\nLong Pass Interceptions on Defense: ")
                safile.write(lpi_defense_2)
            elif not int_number_lpi_defense:
                print("Long Pass Interceptions on Defense: 0")
                safile.write("\nLong Pass Interceptions on Defense: 0")

            if int_number_lpi:
                print("Long Pass Interceptions: ", string_number_lpi)
                # 2000th line

                safile.write("\nLong Pass Interceptions: ")
                safile.write(string_number_lpi)
            elif not int_number_lpi:
                print("Long Pass Interceptions: 0")
                safile.write("\nLg Pass Interceptions: 0")

            if int_number_saves_h:
                print(home + "'s Saves: ", string_number_save_h)
                safile.write("\n" + home + "'s Saves: ")
                safile.write(string_number_save_h)
            elif not int_number_saves_h:
                print(home + "'s Saves: 0")
                safile.write("\n" + home + "'s Saves: 0")

            if int_number_saves_a:
                print(away + "'s Saves: ", string_number_save_a)
                safile.write("\n" + away + "'s Saves: ")
                safile.write(string_number_save_a)
            elif not int_number_saves_a:
                print(away + "'s Saves: 0")
                safile.write("\n" + away + "'s Saves: 0")

            if int_number_pl_33_23:
                pl233 = "Possession(s) lost on offence that came from " \
                        "midfield: "
                print(pl233 + pl_33_23_2)
                safile.write("\n" + pl233)
                safile.write(pl_33_23_2)
            elif not int_number_pl_33_23:
                pl233_f0 = "Possession lost on offence that came from " \
                           "midfield: 0"
                print(pl233_f0)
                safile.write("\n" + pl233_f0)

            if int_number_pl_33_13:
                pl3313 = "Possession(s) lost on offence that came " \
                         "from defense: "
                print(pl3313 + pl_33_13_2)
                safile.write("\n" + pl3313)
                safile.write(pl_33_13_2)
            elif not int_number_pl_33_13:
                pl3313 = "Possession lost on offence that came from defense: 0"
                print(pl3313)
                safile.write("\n" + pl3313)

            if int_number_pl_33:
                print("Possession(s) lost on offence: ", pl_33_2)
                safile.write("\nPossession(s) lost on offence: ")
                safile.write(pl_33_2)
            elif not int_number_pl_33:
                print("Possession lost on offence: 0")
                safile.write("\nPossession lost on offence: 0")

            if int_number_pl_23_33:
                pl2333 = "Possession(s) lost on midfield that came from " \
                         "offense: "
                print(pl2333 + pl_23_33_2)
                safile.write("\n" + pl2333)
                safile.write(pl_23_33_2)
            elif not int_number_pl_23_33:
                pl2333_f0 = "Possession lost on midfield that came from " \
                            "offense: 0"
                print(pl2333_f0)
                safile.write("\n" + pl2333_f0)

            if int_number_pl_23_13:
                pl2313 = "Possession(s) lost on midfield that came from " \
                         "defense: "
                print(pl2313 + pl_23_13_2)
                safile.write("\n" + pl2313)
                safile.write(pl_23_13_2)
            elif not int_number_pl_23_13:
                pl2313_f0 = "Possession lost on midfield that came from " \
                            "defense: 0"
                print(pl2313_f0)
                safile.write("\n" + pl2313_f0)

            if int_number_pl_23:
                print("Possession(s) lost on midfield: ", pl_23_2)
                safile.write("\nPossession(s) lost on midfield: ")
                safile.write(pl_23_2)
            elif not int_number_pl_23:
                print("Possession lost on midfield: 0")
                safile.write("\nPossession lost on midfield: 0")

            if int_number_pl_13_33:
                pl1333 = "Possession(s) lost on defense that came from " \
                         "offense: "
                print(pl1333 + pl_13_33_2)
                safile.write("\n" + pl1333)
                safile.write(pl_13_33_2)
            elif not int_number_pl_13_33:
                pl1333_f0 = "Possession lost on defense that came from " \
                            "offense: 0"
                print(pl1333_f0)
                safile.write("\n" + pl1333_f0)

            if int_number_pl_13_23:
                pl1323 = "Possession(s) lost on defense that came from " \
                         "offense: "
                print(pl1323 + pl_13_23_2)
                safile.write("\n" + pl1323)
                safile.write(pl_13_23_2)
            elif not int_number_pl_13_23:
                pl1323_f0 = "Possession lost on defense that came from " \
                            "offense: 0"
                print(pl1323_f0)
                safile.write("\n" + pl1323_f0)

            if int_number_pl_13:
                print("Possession(s) lost on defense: ", pl_13_2)
                safile.write("\nPossession(s) lost on defense: ")
                safile.write(pl_13_2)
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

            if int_number_offside_h:
                print(home + "'s Offsides: ", string_number_offside_h)
                safile.write("\n" + home + "'s Offsides: ")
                safile.write(string_number_offside_h)
            elif not int_number_offside_h:
                print(home + "'s Offsides: 0")
                safile.write("\n" + home + "'s Offsides: 0")

            if int_number_offside_a:
                print(away + "'s Offsides: ", string_number_offside_a)
                safile.write("\n" + away + "'s Offsides: ")
                safile.write(string_number_offside_a)
            elif not int_number_offside_a:
                print(away + "'s Offsides: 0")
                safile.write("\n" + away + "'s Offsides: 0")

            if int_number_pw_33_home:
                print("Offensive Transitions: ", pw_33_home_2)
                safile.write("\nOffensive Transitions: ")
                safile.write(pw_33_home_2)
            elif not int_number_pw_33_home:
                print("Offensive Transitions: 0")
                safile.write("\nOffensive Transitions: 0")

            if int_number_pw_23_33_home:
                pw2333h = "Offensive transitions that came from midfield: "
                print(pw2333h + pw_23_33_home_2)
                safile.write("\n" + pw2333h)
                safile.write(pw_23_33_home_2)
            elif not int_number_pw_23_33_home:
                pw2333h_f0 = "Offensive transitions that came from midfield: 0"
                print(pw2333h_f0)
                safile.write("\n" + pw2333h_f0)

            if int_number_pw_13_33_home:
                pw1333h = "Offensive transitions that came from defense: "
                print(pw1333h + pw_13_33_home_2)
                safile.write("\n" + pw1333h)
                safile.write(pw_13_33_home_2)
            elif not int_number_pw_13_33_home:
                pw1333h_f0 = "Offensive transitions that came from defense: 0"
                print(pw1333h_f0)
                safile.write("\n" + pw1333h_f0)

            if int_number_pw_13_23_home:
                pw1323h = "Midfield transitions that came from defense: "
                print(pw1323h + pw_13_23_home_2)
                safile.write("\nMidfield transitions that came from defense: ")
                safile.write(pw_13_23_home_2)
            elif not int_number_pw_13_23_home:
                pw1323h_f0 = "Midfield transitions that came from defense: 0"
                print(pw1323h_f0)
                safile.write("\n" + pw1323h_f0)

            if int_number_pw_13_home:
                pw13h = "Transitions that came from defense: "
                print(pw13h + pw_13_home_2)
                safile.write("\nTransitions that came from defense: ")
                safile.write(pw_13_home_2)
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

            if int_number_gkto_h:
                print(home + "'s Goalkeeper Turnovers: ", string_number_gkto_h)
                safile.write("\n" + home + "'s Goalkeeper Turnovers: ")
                safile.write(string_number_gkto_h)
            elif not int_number_gkto_h:
                print(home + "'s Goalkeeper Turnovers: 0")
                safile.write("\n" + home + "'s Goalkeeper Turnovers: 0")

            if int_number_gkto_a:
                print(away + "'s Goalkeeper Turnovers: ", string_number_gkto_a)
                safile.write("\n" + away + "'s Goalkeeper Turnovers: ")
                safile.write(string_number_gkto_a)
            elif not int_number_gkto_a:
                print(away + "'s Goalkeeper Turnovers: 0")
                safile.write("\n" + away + "'s Goalkeeper Turnovers: 0")

            if int_number_kp_h:
                print(home + "'s Key Passes: ", string_number_kp_h)
                safile.write("\n" + home + "'s Key Passes: ")
                safile.write(string_number_kp_h)
            elif not int_number_kp_h:
                print(home + "'s Key Passes: 0")
                safile.write("\n" + home + "'s Key Passes: 0")

            if int_number_kp_a:
                print(away + "'s Key Passes: ", string_number_kp_a)
                safile.write("\n" + away + "'s Key Passes: ")
                safile.write(string_number_kp_a)
            elif not int_number_kp_a:
                print(away + "'s Key Passes: 0")
                safile.write("\n" + away + "'s Key Passes: 0")

            if int_number_possession_13_h:
                end_possession_13_h = "Possession(s) on defense from " + home + ": " + possession_13_2_h
                print(white % end_possession_13_h)
                # write on the file
                safile.write("Possession(s) on defense from " + home + ": ")
                safile.write(possession_13_2_h)
            elif not int_number_possession_13_h:
                print("\nPossession(s) on defense from " + home + ": 0")
                safile.write("\nPossession(s) on defense from " + home + ": 0")

            if int_number_possession_23_h:
                print("\nPossession(s) on midfield from " + home + ": ",
                      possession_23_2)
                safile.write("\nPossession(s) on midfield from " + home + ": ")
                safile.write(possession_23_2_h)
            elif not int_number_possession_23_h:
                print("\nPossession(s) on midfield from " + home + ": 0 ")
                safile.write(
                    "\nPossession(s) on midfield from " + home + ": 0 ")

            if int_number_possession_33_h:
                print("\nPossession(s) on attack from " + home + ": ",
                      possession_33_2_h)
                safile.write("\nPossession(s) on attack from " + home + ": ")
                safile.write(possession_33_2_h)
            elif not int_number_possession_33_h:
                print("\nPossession(s) on attack from " + home + ": 0")
                safile.write("\nPossession(s) on attack from " + home + ": 0")

            if int_number_possession_h:
                print("Possession(s): ", string_number_possession_h)
                safile.write("\nPossession(s) from " + home + ": ")
                safile.write(string_number_possession_h)
            elif not int_number_possession_h:
                print("\nPossession(s) from " + home + ": 0")
                safile.write("\nPossession(s) from " + home + ": 0")

            if int_number_possession_13_a:
                end_possession_13_a = "Possession on defense from " + away + ": " + possession_13_2_a
                print(white % end_possession_13_a)
                # write on the file
                safile.write("Possession on defense from " + away + ": ")
                safile.write(possession_13_2_a)
            elif not int_number_possession_13_a:
                print("\nPossession on defense from " + away + ": 0")
                safile.write("\nPossession on defense from " + away + ": 0")

            if int_number_possession_23_a:
                print("\nPossession(s) on midfield from " + away + ": ",
                      possession_23_2)
                safile.write("\nPossession(s) on midfield from " + away + ": ")
                safile.write(possession_23_2_a)
            elif not int_number_possession_23_a:
                print("\nPossession(s) on midfield from " + away + ": 0 ")
                safile.write(
                    "\nPossession(s) on midfield from " + away + ": 0 ")

            if int_number_possession_33_a:
                print("\nPossession(s) on attack from " + away + ": ",
                      possession_33_2_a)
                safile.write("\nPossession(s) on attack from " + away + ": ")
                safile.write(possession_33_2_a)
            elif not int_number_possession_33_a:
                print("\nPossession(s) on attack from " + away + ": 0")
                safile.write("\nPossession(s) on attack from " + away + ": 0")

            if int_number_possession_a:
                print("Possession(s): ", string_number_possession_a)
                safile.write("\nPossession(s) from " + away + ": ")
                safile.write(string_number_possession_a)
            elif not int_number_possession_a:
                print("\nPossession(s) from " + away + ": 0")
                safile.write("\nPossession(s) from " + away + ": 0")

            if int_number_cl_gd_h and \
                    int_number_cl_pd_h and \
                    int_number_cl_h and \
                            int_final_cl_h == all_cl_final_h:
                int_final_cl_gd_h = int(cl_string_gd_2_h)
                int_final_cl_pd_h = int(cl_string_pd_2_h)
                all_cl_final_h = int_final_cl_gd_h + int_final_cl_pd_h
                perc_num_cl_h = 100 / all_cl_final_h
                perc_num_cl_good_h = perc_num_cl_h * int_final_cl_gd_h
                perc_num_cl_bad_h = perc_num_cl_h * int_final_cl_pd_h
                round_cl_good_h = round(perc_num_cl_good_h, 1)
                round_cl_bad_h = round(perc_num_cl_bad_h, 1)
                print_cl_good_h = str(round_cl_good_h)
                print_cl_bad_h = str(round_cl_bad_h)
                final_cl_good_h = print_cl_good_h + "% of the Clearances " \
                                                    "from " + home + \
                                  " were good"
                final_cl_bad_h = print_cl_bad_h + "% of the Clearances " \
                                                  "from " + home + \
                                 " were bad"
                print(blue % final_cl_good_h)
                print(red % final_cl_bad_h)

            if int_number_cl_gd_h:
                print("Clearance(s) to Teammates from " + home + ": ",
                      cl_string_gd_2_h)
                safile.write("\nClearance(s) to Teammates from" + home +
                             ": ")
                safile.write(cl_string_gd_2_h)
            elif not int_number_cl_gd_h:
                print("Clearance(s) to Teammates from " + home + ": 0")
                safile.write(
                    "\nClearance(s) to Teammates from " + home + ": 0")

            if int_number_cl_pd_h:
                print("Clearance(s) to Teammates from " + home + ": ",
                      cl_string_pd_2_h)
                safile.write(
                    "\nClearance(s) to Opponents from " + home + ": ")
                safile.write(cl_string_pd_2_h)
            elif not int_number_cl_pd_h:
                print("Clearance(s) to Opponents from " + home + ": 0")
                safile.write(
                    "\nClearance(s) to Opponents from " + home + ": 0")

            if int_number_cl_h:
                print("Clearance(s) from " + home + ": ", string_number_cl_h)
                safile.write("\nClearance(s) from " + home + ": ")
                safile.write(string_number_cl_h)
            elif not int_number_cl_h:
                print("Clearance(s) from " + home + ": 0")
                safile.write("\nClearance(s) from " + home + ": 0")

            if int_number_cl_gd_a and \
                    int_number_cl_pd_a and \
                    int_number_cl_a and \
                            int_final_cl_a == all_cl_final_a:
                int_final_cl_gd_a = int(cl_string_gd_2_a)
                int_final_cl_pd_a = int(cl_string_pd_2_a)
                all_cl_final_a = int_final_cl_gd_a + int_final_cl_pd_a
                perc_num_cl_a = 100 / all_cl_final_a
                perc_num_cl_good_a = perc_num_cl_a * int_final_cl_gd_a
                perc_num_cl_bad_a = perc_num_cl_a * int_final_cl_pd_a
                round_cl_good_a = round(perc_num_cl_good_a, 1)
                round_cl_bad_a = round(perc_num_cl_bad_a, 1)
                print_cl_good_a = str(round_cl_good_a)
                print_cl_bad_a = str(round_cl_bad_a)
                final_cl_good_a = print_cl_good_a + "% of the Clearances " \
                                                    "from " + away + \
                                  " were good"
                final_cl_bad_a = print_cl_bad_a + "% of the Clearances " \
                                                  "from " + away + \
                                 " were bad"
                print(blue % final_cl_good_a)
                print(red % final_cl_bad_a)

            if int_number_cl_gd_a:
                print("Clearance(s) to Teammates from " + away + ": ",
                      cl_string_gd_2_a)
                safile.write("\nClearance(s) to Teammates from" + away +
                             ": ")
                safile.write(cl_string_gd_2_a)
            elif not int_number_cl_gd_a:
                print("Clearance(s) to Teammates from " + away + ": 0")
                safile.write(
                    "\nClearance(s) to Teammates from " + away + ": 0")

            if int_number_cl_pd_a:
                print("Clearance(s) to Teammates from " + away + ": ",
                      cl_string_pd_2_a)
                safile.write(
                    "\nClearance(s) to Opponents from " + away + ": ")
                safile.write(cl_string_pd_2_a)
            elif not int_number_cl_pd_a:
                print("Clearance(s) to Opponents from " + away + ": 0")
                safile.write(
                    "\nClearance(s) to Opponents from " + away + ": 0")

            if int_number_cl_a:
                print("Clearance(s) from " + away + ": ", string_number_cl_a)
                safile.write("\nClearance(s) from " + away + ": ")
                safile.write(string_number_cl_a)
            elif not int_number_cl_a:
                print("Clearance(s) from " + away + ": 0")
                safile.write("\nClearance(s) from " + away + ": 0")

            if int_number_ad_w_h and \
                    int_number_ad_l_h and \
                    int_number_ad_h:
                int_final_ad_w_h = int(ad_string_gd_2_h)
                int_final_ad_l_h = int(ad_string_pd_2_h)
                all_ad_final_h = int_final_ad_w_h + int_final_ad_l_h
                perc_num_ad_h = 100 / all_ad_final_h
                perc_num_ad_good_h = perc_num_ad_h * int_final_ad_w_h
                perc_num_ad_bad_h = perc_num_ad_h * int_final_ad_l_h
                round_ad_good_h = round(perc_num_ad_good_h, 1)
                round_ad_bad_h = round(perc_num_ad_bad_h, 1)
                print_ad_good_h = str(round_ad_good_h)
                print_ad_bad_h = str(round_ad_bad_h)
                final_ad_good_h = print_ad_good_h + "% of the Aerial Duels " \
                                                    "from " + home + \
                                  " were good"
                final_ad_bad_h = print_ad_bad_h + "% of the Aerial Duels " \
                                                  "from " + home + \
                                 " were bad"
                print(blue % final_ad_good_h)
                print(red % final_ad_bad_h)

            if int_number_ad_w_h:
                print("Aerial Duels won from " + home + ": ",
                      ad_string_gd_2_h)
                safile.write("\nAerial Duels won from" + home +
                             ": ")
                safile.write(ad_string_gd_2_h)
            elif not int_number_ad_w_h:
                print("Aerial Duels won from " + home + ": 0")
                safile.write(
                    "\nAerial Duels won from " + home + ": 0")

            if int_number_ad_l_h:
                print("Aerial Duels won from " + home + ": ",
                      ad_string_pd_2_h)
                safile.write(
                    "\nAerial Duels lost from " + home + ": ")
                safile.write(ad_string_pd_2_h)
            elif not int_number_ad_l_h:
                print("Aerial Duels lost from " + home + ": 0")
                safile.write(
                    "\nAerial Duels lost from " + home + ": 0")

            if int_number_ad_h:
                print("Aerial Duels from " + home + ": ", string_number_ad_h)
                safile.write("\nAerial Duels from " + home + ": ")
                safile.write(string_number_ad_h)
            elif not int_number_ad_h:
                print("Aerial Duels from " + home + ": 0")
                safile.write("\nAerial Duels from " + home + ": 0")

            if int_number_ad_w_a and \
                    int_number_ad_l_a and \
                    int_number_ad_a and \
                            int_final_ad_a == all_ad_final_a:
                int_final_ad_w_a = int(ad_string_gd_2_a)
                int_final_ad_l_a = int(ad_string_pd_2_a)
                all_ad_final_a = int_final_ad_w_a + int_final_ad_l_a
                perc_num_ad_a = 100 / all_ad_final_a
                perc_num_ad_good_a = perc_num_ad_a * int_final_ad_w_a
                perc_num_ad_bad_a = perc_num_ad_a * int_final_ad_l_a
                round_ad_good_a = round(perc_num_ad_good_a, 1)
                round_ad_bad_a = round(perc_num_ad_bad_a, 1)
                print_ad_good_a = str(round_ad_good_a)
                print_ad_bad_a = str(round_ad_bad_a)
                final_ad_good_a = print_ad_good_a + "% of the Aerial Duels " \
                                                    "from " + away + \
                                  " were good"
                final_ad_bad_a = print_ad_bad_a + "% of the Aerial Duels " \
                                                  "from " + away + \
                                 " were bad"
                print(blue % final_ad_good_a)
                print(red % final_ad_bad_a)

            if int_number_ad_w_a:
                print("Aerial Duels won from " + away + ": ",
                      ad_string_gd_2_a)
                safile.write("\nAerial Duels won from" + away +
                             ": ")
                safile.write(ad_string_gd_2_a)
            elif not int_number_ad_w_a:
                print("Aerial Duels won from " + away + ": 0")
                safile.write(
                    "\nAerial Duels won from " + away + ": 0")

            if int_number_ad_l_a:
                print("Aerial Duels won from " + away + ": ",
                      ad_string_pd_2_a)
                safile.write(
                    "\nAerial Duels lost from " + away + ":")

                safile.write(ad_string_pd_2_a)
            elif not int_number_ad_l_a:
                print("Aerial Duels lost from " + away + ": 0")
                safile.write(
                    "\nAerial Duels lost from " + away + ": 0")

            if int_number_ad_a:
                print("Aerial Duels from " + away + ": ", string_number_ad_a)
                safile.write("\nAerial Duels from " + away + ": ")
                safile.write(string_number_ad_a)
            elif not int_number_ad_a:
                print("Aerial Duels from " + away + ": 0")
                safile.write("\nAerial Duels from " + away + ": 0")

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
