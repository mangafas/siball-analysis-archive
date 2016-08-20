# -----> * Filing * <-----

# ask the user the name of the game to create a .txt file
print("Enter game's name:")
name_file = input("")
name_file_string = str(name_file)
file_name = name_file_string + ".txt"

# create a writable .txt file
safile = open(file_name, "w")
safile.write("This game's stats were:\n")


# -----> * INTRODUCTION * <-----


Commands = '''      STAT ------------> COMMAND

      Penalty Kick -----> pk
      -> Goal ----------> goal
      -> Saved ---------> saved
      -> Missed --------> missed

      Free Kick --------> fk
      Corner Kick ------> ck
      Throw In ---------> ti
      Cross ------------> cross
      -> Good Delivery -> gd
      -> Good Delivery -> pd

      1 versus 1 ------> 1v1
      -> Won ----------> w
      -> Lost ---------> l

      Shot ------------> shot
      Header ----------> header
      -> On Target ----> on target
      -> Off Target ---> off target

      Save ------------> save

      Long Pass Interception
      -> On Attack
      --> Second Ball
      --> Third Ball
      -> On Defence
      --> Second Ball
      --> Third Ball

      To quit press q
       '''

print(Commands)

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

# -----> * Free Kicks Variables <-----


fk_range = range(0, 1000)
fk_list = list(fk_range)
fk_range_gd = range(0, 1000)
fk_list_gd = list(fk_range_gd)
fk_range_pd = range(0, 1000)
fk_list_pd = list(fk_range_pd)
fk_input = '''gd/pd
'''

# -----> * Corner Kicks Variables * <-----


ck_range = range(0, 1000)
ck_list = list(ck_range)
ck_range_gd = range(0, 1000)
ck_list_gd = list(ck_range_gd)
ck_range_pd = range(0, 1000)
ck_list_pd = list(ck_range_pd)
ck_input = '''gd/pd
'''

# -----> * Throw Ins Variables * <-----


ti_range = range(0, 1000)
ti_list = list(ti_range)
ti_range_gd = range(0, 1000)
ti_list_gd = list(ti_range_gd)
ti_range_pd = range(0, 1000)
ti_list_pd = list(ti_range_pd)
ti_input = '''gd/pd
'''

# -----> * Crosses Variables * <-----


crosses_range = range(0, 1000)
crosses_list = list(crosses_range)
crosses_range_gd = range(0, 1000)
crosses_list_gd = list(crosses_range_gd)
crosses_range_pd = range(0, 1000)
crosses_list_pd = list(crosses_range_pd)
crosses_input = '''gd/pd
'''

# -----> * True vs True Variables * <-----


v1_range = range(0, 1000)
v1_list = list(v1_range)
v1_range_w = range(0, 1000)
v1_list_w = list(v1_range_w)
v1_range_l = range(0, 1000)
v1_list_l = list(v1_range_l)
v1_input = '''w/l
'''

# -----> * Shots Variables * <-----


shots_range = range(0, 1000)
shots_list = list(shots_range)
shots_range_gd = range(0, 1000)
shots_list_gd = list(shots_range_gd)
shots_range_pd = range(0, 1000)
shots_list_pd = list(shots_range_pd)
shots_input = '''on target/off target
'''

# -----> * Headers Variables * <-----

headers_range = range(0, 1000)
headers_list = list(headers_range)
headers_range_gd = range(0, 1000)
headers_list_gd = list(headers_range_gd)
headers_range_pd = range(0, 1000)
headers_list_pd = list(headers_range_pd)
headers_input = '''on target/off target
'''

# -----> * Saves Variables * <-----

saves_range = range(0, 1000)
saves_list = list(saves_range)

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


# -----> * Main Function * <-----


def body():
    # global each variable to be able to be referenced later when you print/write the total stat on each game at the end
    global string_number_pk_goal, string_number_pk_missed, string_number_pk_saved, string_number_pk, string_number_fk_gd
    global string_number_fk_pd, string_number_fk, string_number_ck_pd, string_number_ck_gd, string_number_ck
    global string_number_crosses_gd, string_number_crosses_pd, string_number_crosses, string_number_shots
    global string_number_headers_pd, string_number_headers_gd, string_number_shots_pd, string_number_shots_gd
    global string_number_v1_l, string_number_v1, string_number_long_passes_second_ball, string_number_v1_w
    global string_number_long_passes_third_ball, string_number_long_passes, string_number_save, string_number_headers
    global string_number_ti_gd, string_number_ti, string_number_long_passes_defense
    global string_number_long_passes_second_ball_defense, string_number_long_passes_third_ball_defense
    global string_number_long_passes_attack, string_number_long_passes_third_ball_attack
    global string_number_long_passes_second_ball_attack, string_number_ti_pd

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

    # it creates a while loop so the function will go on and on until a the user decides to quit the function
    while True:
        # the user decides which stat to record by calling it
        choice = input("")

        # -----> * Penalty Kicks Function * <-----

        # user inserts each stat's codename/name so it records it
        if choice == "pk":

            # the user decides whether a stat was successful or not
            good_bad_input_pk = input(pk_input)

            # the user inserts each stat's codename/name on its success or its failure
            if good_bad_input_pk == "goal":
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
                # print a nice introduction/explainer and the time a stat was called
                print("Penalty Kick goal(s): ", string_number_pk_goal)

            elif good_bad_input_pk == "saved":
                first_number_pk_saved = pk_list_saved[0]
                pk_list_saved.remove(first_number_pk_saved)
                number_pk_saved = pk_list_saved[0]
                string_number_pk_saved = str(number_pk_saved)
                int_number_pk_saved = True
                print("Penalty Kick(s) saved: ", string_number_pk_saved)

            elif good_bad_input_pk == "missed":
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

        elif choice == "fk":

            good_bad_input_fk = input(fk_input)

            if good_bad_input_fk == "gd":
                first_number_fk_gd = fk_list_gd[0]
                fk_list_gd.remove(first_number_fk_gd)
                number_fk_gd = fk_list_gd[0]
                string_number_fk_gd = str(number_fk_gd)
                int_number_fk_gd = True
                print("Free Kick(s) with a Good Delivery: ", string_number_fk_gd)

            elif good_bad_input_fk == "pd":
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

        elif choice == "ck":

            good_bad_input_ck = input(ck_input)

            if good_bad_input_ck == "gd":
                first_number_ck_gd = ck_list_gd[0]
                ck_list_gd.remove(first_number_ck_gd)
                number_ck_gd = ck_list_gd[0]
                string_number_ck_gd = str(number_ck_gd)
                int_number_ck_gd = True
                print("Corner Kick(s) with a Good Delivery: ", string_number_ck_gd)

            elif good_bad_input_ck == "pd":
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

        elif choice == "ti":

            good_bad_input_ti = input(ti_input)

            if good_bad_input_ti == "gd":
                first_number_ti_gd = ti_list_gd[0]
                ti_list_gd.remove(first_number_ti_gd)
                number_ti_gd = ti_list_gd[0]
                string_number_ti_gd = str(number_ti_gd)
                int_number_ti_gd = True
                print("Throw In(s) with a Good Delivery: ", string_number_ti_gd)

            elif good_bad_input_ti == "pd":
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

        elif choice == "cross":

            good_bad_input_crosses = input(crosses_input)

            if good_bad_input_crosses == "gd":
                first_number_crosses_gd = crosses_list_gd[0]
                crosses_list_gd.remove(first_number_crosses_gd)
                number_crosses_gd = crosses_list_gd[0]
                string_number_crosses_gd = str(number_crosses_gd)
                int_number_crosses_gd = True
                print("Cross(es) with a Good Delivery: ", string_number_crosses_gd)

            elif good_bad_input_crosses == "pd":
                first_number_crosses_pd = crosses_list_pd[0]
                crosses_list_pd.remove(first_number_crosses_pd)
                number_crosses_pd = crosses_list_pd[0]
                string_number_crosses_pd = str(number_crosses_pd)
                int_number_crosses_pd = True
                print("Cross(es) with a Good Delivery: ", string_number_crosses_pd)

            first_number_crosses = crosses_list[0]
            crosses_list.remove(first_number_crosses)
            number_crosses = crosses_list[0]
            string_number_crosses = str(number_crosses)
            int_number_crosses = True
            print("Cross(es): ", string_number_crosses)

        # -----> * 1 versus 1 Function * <-----

        elif choice == "1v1":

            good_bad_input_v1 = input(v1_input)

            if good_bad_input_v1 == "w":
                first_number_v1_w = v1_list_w[0]
                v1_list_w.remove(first_number_v1_w)
                number_v1_w = v1_list_w[0]
                string_number_v1_w = str(number_v1_w)
                int_number_v1_w = True
                print("Won 1vs1: ", string_number_v1_w)

            elif good_bad_input_v1 == "l":
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

        elif choice == "shot":

            good_bad_input_shots = input(shots_input)

            if good_bad_input_shots == "on target":
                first_number_shots_gd = shots_list_gd[0]
                shots_list_gd.remove(first_number_shots_gd)
                number_shots_gd = shots_list_gd[0]
                string_number_shots_gd = str(number_shots_gd)
                int_number_shots_gd = True
                print("Shot(s) on target: ", string_number_shots_gd)

            elif good_bad_input_shots == "off target":
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

        elif choice == "header":

            good_bad_input_headers = input(headers_input)

            if good_bad_input_headers == "on target":
                first_number_headers_gd = headers_list_gd[0]
                headers_list_gd.remove(first_number_headers_gd)
                number_headers_gd = headers_list_gd[0]
                string_number_headers_gd = str(number_headers_gd)
                int_number_headers_gd = True
                print("Header(s) on target: ", string_number_headers_gd)

            elif good_bad_input_headers == "off target":
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

        elif choice == "long pass":

            # NOTE: long pass has more 'complexity'

            attack_defense_input_long_pass = input(long_passes_input)
            sec_third_input_long_pass_attack = input(long_passes_input_attack)

            if attack_defense_input_long_pass == "attack":

                if sec_third_input_long_pass_attack == "second ball":
                    first_number_long_passes_second_ball_attack = long_passes_list_second_ball_attack[0]
                    long_passes_list_second_ball_attack.remove(first_number_long_passes_second_ball_attack)
                    number_long_passes_second_ball_attack = long_passes_list_second_ball_attack[0]
                    string_number_long_passes_second_ball_attack = str(number_long_passes_second_ball_attack)
                    print("Second Ball Long Pass Interceptions on Attack:",
                          string_number_long_passes_second_ball_attack)
                    int_number_long_passes_second_ball_attack = True

                elif sec_third_input_long_pass_attack == "third ball":
                    first_number_long_passes_third_ball_attack = long_passes_list_third_ball_attack[0]
                    long_passes_list_third_ball_attack.remove(first_number_long_passes_third_ball_attack)
                    number_long_passes_third_ball_attack = long_passes_list_third_ball_attack[0]
                    string_number_long_passes_third_ball_attack = str(number_long_passes_third_ball_attack)
                    int_number_long_passes_third_ball_attack = True

                first_number_long_passes_attack = long_passes_list_attack[0]
                long_passes_list_attack.remove(first_number_long_passes_attack)
                number_long_passes_attack = long_passes_list_attack[0]
                string_number_long_passes_attack = str(number_long_passes_attack)
                int_number_long_passes_attack = True

            elif attack_defense_input_long_pass == "defense":

                if sec_third_input_long_pass_attack == "second ball":
                    first_number_long_passes_second_ball_defense = long_passes_list_second_ball_defense[0]
                    long_passes_list_second_ball_defense.remove(first_number_long_passes_second_ball_defense)
                    number_long_passes_second_ball_defense = long_passes_list_second_ball_defense[0]
                    string_number_long_passes_second_ball_defense = str(number_long_passes_second_ball_defense)
                    int_number_long_passes_second_ball_defense = True

                elif sec_third_input_long_pass_attack == "third ball":
                    first_number_long_passes_third_ball_defense = long_passes_list_third_ball_defense[0]
                    long_passes_list_third_ball_defense.remove(first_number_long_passes_third_ball_defense)
                    number_long_passes_third_ball_defense = long_passes_list_third_ball_defense[0]
                    string_number_long_passes_third_ball_defense = str(number_long_passes_third_ball_defense)
                    int_number_long_passes_third_ball_defense = True

                first_number_long_passes_defense = long_passes_list_defense[0]
                long_passes_list_defense.remove(first_number_long_passes_defense)
                number_long_passes_defense = long_passes_list_defense[0]
                string_number_long_passes_defense = str(number_long_passes_defense)
                int_number_long_passes_defense = True

            first_number_long_passes = long_passes_list[0]
            long_passes_list.remove(first_number_long_passes)
            number_long_passes = long_passes_list[0]
            string_number_long_passes = str(number_long_passes)
            print("Long Pass Interceptions: ", string_number_long_passes)
            int_number_long_passes = True

        # -----> * Saves * <-----

        elif choice == "save":
            first_number_save = saves_list[0]
            saves_list.remove(first_number_save)
            number_save = saves_list[0]
            string_number_save = str(number_save)
            int_number_saves = True
            print("Save(s)", string_number_save)

        # -----> * Quit Function * <-----

        # if the user wants to quit he types q to begin the process
        elif choice == "q":

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
                print("Saves: 0")
                safile.write("\nSaves: 0")

            # close the file
            safile.close()

            # break the while loop, quiting the function
            break


body()
