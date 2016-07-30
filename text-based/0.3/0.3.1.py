

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

      To quit press q
       '''

print(Commands)

# -----> * Penalty Kicks Variables * <-----


pk_range = range(0, 1000)
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


fk_range = range(-1, 1000)
fk_list = list(fk_range)
fk_range_gd = range(-1, 1000)
fk_list_gd = list(fk_range_gd)
fk_range_pd = range(-1, 1000)
fk_list_pd = list(fk_range_pd)
fk_input = '''gd/pd
'''

# -----> * Corner Kicks Variables * <-----


ck_range = range(-1, 1000)
ck_list = list(ck_range)
ck_range_gd = range(-1, 1000)
ck_list_gd = list(ck_range_gd)
ck_range_pd = range(-1, 1000)
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

# -----> * 1 vs 1 Variables * <-----


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
long_passes_range_first_touch = range(0, 1000)
long_passes_list_first_touch = list(long_passes_range_first_touch)
long_passes_range_second_touch = range(0, 1000)
long_passes_list_second_touch = list(long_passes_range_second_touch)
long_passes_input = '''first touch/second touch
'''


# -----> * Main Function * <-----

def body():
    global string_number_pk, string_number_pk_goal, string_number_pk_missed, string_number_pk_saved, string_number_fk, string_number_fk_gd, string_number_fk_pd, string_number_ck, string_number_ck_gd, string_number_ck_pd, string_number_ti, string_number_ti_gd, string_number_ti_gd, string_number_ti_pd, string_number_crosses, string_number_crosses_gd, string_number_crosses_pd, string_number_shots, string_number_shots_gd, string_number_shots_pd, string_number_headers, string_number_headers_gd, string_number_v1, string_number_v1_w, string_number_v1_l, string_number_saves, string_number_long_passes, string_number_long_passes_first_touch, string_number_long_passes_second_touch
    while True:
        choice = input("")

        # -----> * Penalty_Kicks_total Variables * <-----

        first_number_pk = pk_list[0]
        first_number_pk_string = string_number_pk(first_number_pk)
        if first_number_pk_string == "-1":
            pk_list.remove(first_number_pk)

        # -----> * Penalty_Kicks_goal Variables * <-----

        first_number_pk_goal = pk_list_goal[0]
        first_number_pk_goal_string = string_number_pk_goal(first_number_pk_goal)
        if first_number_pk_goal_string == "-1":
            pk_list_goal.remove(first_number_pk_goal)

        # -----> * Penalty_Kicks_missed Variables * <-----

        first_number_pk_missed = pk_list_missed[0]
        first_number_pk_missed_string = string_number_pk_missed(first_number_pk_missed)
        if first_number_pk_missed_string == "-1":
            pk_list_missed.remove(first_number_pk_missed)

        # -----> * Penalty_Kicks_saved Variables * <-----

        first_number_pk_saved = pk_list_saved[0]
        first_number_pk_saved_string = string_number_headers_pd(first_number_pk_saved)
        if first_number_pk_saved_string == "-1":
            pk_list_saved.remove(first_number_pk_saved)

        # -----> * Free_Kicks_total Variables * <-----

        first_number_fk = fk_list[0]
        first_number_fk_string = string_number_headers_pd(first_number_fk)
        if first_number_fk_string == "-1":
            fk_list.remove(first_number_fk)

        # -----> * Free_Kicks_gd Variables * <-----

        first_number_fk_gd = fk_list_gd[0]
        first_number_fk_gd_string = string_number_headers_pd(first_number_fk_gd)
        if first_number_fk_gd_string == "-1":
            fk_list_gd.remove(first_number_fk_gd)

        # -----> * Free_Kicks_pd Variables * <-----

        first_number_fk_pd = fk_list_pd[0]
        first_number_fk_pd_string = string_number_headers_pd(first_number_fk_pd)
        if first_number_fk_pd_string == "-1":
            fk_list_pd.remove(first_number_fk_pd)

        # -----> * Corner_Kicks_total Variables * <-----

        first_number_ck = ck_list[0]
        first_number_ck_string = string_number_headers_pd(first_number_ck)
        if first_number_ck_string == "-1":
            ck_list.remove(first_number_ck)

        # -----> * Corner_Kicks_gd Variables * <-----

        first_number_ck_gd = ck_list_gd[0]
        first_number_ck_gd_string = string_number_headers_pd(first_number_ck_gd)
        if first_number_ck_gd_string == "-1":
            ck_list_gd.remove(first_number_ck_gd)

        # -----> * Corner_Kicks_pd Variables * <-----

        first_number_ck_pd = ck_list_pd[0]
        first_number_ck_pd_string = string_number_headers_pd(first_number_ck_pd)
        if first_number_ck_pd_string == "-1":
            ck_list_pd.remove(first_number_ck_pd)

        # -----> * Throw_Ins_total Variables * <-----

        first_number_ti = ti_list[0]
        first_number_ti_string = string_number_headers_pd(first_number_ti)
        if first_number_ti_string == "-1":
            ti_list.remove(first_number_ti)

        # -----> * Throw_Ins_gd Variables * <-----

        first_number_ti_gd = ti_list_gd[0]
        first_number_ti_gd_string = string_number_headers_pd(first_number_ti_gd)
        if first_number_ti_gd_string == "-1":
            ti_list_gd.remove(first_number_ti_gd)

        # -----> * Throw_Ins_pd Variables * <-----

        first_number_ti_pd = ti_list_pd[0]
        first_number_ti_pd_string = string_number_headers_pd(first_number_ti_pd)
        if first_number_ti_pd_string == "-1":
            ti_list_pd.remove(first_number_ti_pd)

        # -----> * crosses_total Variables * <-----

        first_number_crosses = crosses_list[0]
        first_number_crosses_string = string_number_headers_pd(first_number_crosses)
        if first_number_crosses_string == "-1":
            crosses_list.remove(first_number_crosses)

        # -----> * crosses_gd Variables * <-----

        first_number_crosses_gd = crosses_list_gd[0]
        first_number_crosses_gd_string = string_number_headers_pd(first_number_crosses_gd)
        if first_number_crosses_gd_string == "-1":
            crosses_list_gd.remove(first_number_crosses_gd)

        # -----> * crosses_pd Variables * <-----

        first_number_crosses_pd = crosses_list_pd[0]
        first_number_crosses_pd_string = string_number_headers_pd(first_number_crosses_pd)
        if first_number_crosses_pd_string == "-1":
            crosses_list_pd.remove(first_number_crosses_pd)

        # -----> * shot_total Variables * <-----

        first_number_shots = shots_list[0]
        first_number_shots_string = string_number_headers_pd(first_number_shots)
        if first_number_shots_string == "-1":
            shots_list.remove(first_number_shots)

        # -----> * shot_gd Variables * <-----

        first_number_shots_gd = shots_list_gd[0]
        first_number_shots_gd_string = string_number_headers_pd(first_number_shots_gd)
        if first_number_shots_gd_string == "-1":
            shots_list_gd.remove(first_number_shots_gd)

        # -----> * shot_pd Variables * <-----

        first_number_shots_pd = shots_list_pd[0]
        first_number_shots_pd_string = string_number_headers_pd(first_number_shots_pd)
        if first_number_shots_pd_string == "-1":
            shots_list_pd.remove(first_number_shots_pd)

        # -----> * headers_total Variables * <-----

        first_number_headers = headers_list[0]
        first_number_headers_string = string_number_headers_pd(first_number_headers)
        if first_number_headers_string == "-1":
            headers_list.remove(first_number_headers)

        # -----> * headers_gd Variables * <-----

        first_number_headers_gd = headers_list_gd[0]
        first_number_headers_gd_string = string_number_headers_pd(first_number_headers_gd)
        if first_number_headers_gd_string == "-1":
            headers_list_gd.remove(first_number_headers_gd)

        # -----> * headers_pd Variables * <-----

        first_number_headers_pd = headers_list_pd[0]
        first_number_headers_pd_string = string_number_headers_pd(first_number_headers_pd)
        if first_number_headers_pd_string == "-1":
            headers_list_pd.remove(first_number_headers_pd)

        # -----> * 1vs1_total Variables * <-----

        first_number_v1 = v1_list[0]
        first_number_v1_string = string_number_headers_pd(first_number_v1)
        if first_number_v1_string == "-1":
            v1_list.remove(first_number_v1)

        # -----> * 1vs1_won Variables * <-----

        first_number_v1_w = v1_list_w[0]
        first_number_v1_w_string = string_number_headers_pd(first_number_v1_w)
        if first_number_v1_w_string == "-1":
            v1_list_w.remove(first_number_v1_w)

        # -----> * 1vs1_lost Variables * <-----

        first_number_v1_l = v1_list_l[0]
        first_number_v1_l_string = string_number_headers_pd(first_number_v1_l)
        if first_number_v1_l_string == "-1":
            v1_list_l.remove(first_number_v1_l)

        # -----> * long_passes_total Variables * <-----

        first_number_long_passes = long_passes_list[0]
        first_number_long_passes_string = string_number_headers_pd(first_number_long_passes)
        if first_number_long_passes_string == "-1":
            long_passes_list.remove(first_number_long_passes)

        # -----> * long_passes_first_touch Variables * <-----

        first_number_long_passes_first_touch = long_passes_list_first_touch[0]
        first_number_long_passes_first_touch_string = string_number_headers_pd(first_number_long_passes_first_touch)
        if first_number_long_passes_first_touch_string == "-1":
            long_passes_list_first_touch.remove(first_number_long_passes_first_touch)

        # -----> * long_passes_second_touch Variables * <-----

        first_number_long_passes_second_touch = long_passes_list_second_touch[0]
        first_number_long_passes_second_touch_string = string_number_headers_pd(first_number_long_passes_second_touch)
        if first_number_long_passes_second_touch_string == "-1":
            long_passes_list_second_touch.remove(first_number_long_passes_second_touch)
        
        # -----> * saves_total Variables * <-----

        first_number_saves = saves_list[0]
        first_number_saves_string = string_number_headers_pd(first_number_saves)
        if first_number_saves_string == "-1":
            saves_list.remove(first_number_saves)

        # -----> * Penalty Kicks Function * <-----

        if choice == "pk":

            good_bad_input_pk = input(pk_input)

            if good_bad_input_pk == "goal":
                first_number_pk_goal = pk_list_goal[0]
                pk_list_goal.remove(first_number_pk_goal)
                number_pk_goal = pk_list_goal[0]
                string_number_pk_goal = string_number_headers_pd(number_pk_goal)
                print("Penalty Kick goal(s): ", string_number_pk_goal)

            elif good_bad_input_pk == "saved":
                first_number_pk_saved = pk_list_saved[0]
                pk_list_saved.remove(first_number_pk_saved)
                number_pk_saved = pk_list_saved[0]
                string_number_pk_saved = string_number_headers_pd(number_pk_saved)
                print("Penalty Kick(s) saved: ", string_number_pk_saved)

            elif good_bad_input_pk == "missed":
                first_number_pk_missed = pk_list_missed[0]
                pk_list_missed.remove(first_number_pk_missed)
                number_pk_missed = pk_list_missed[0]
                string_number_pk_missed = string_number_headers_pd(number_pk_missed)
                print("Penalty Kick(s) missed: ", string_number_pk_missed)

            else:
                pass

            first_number_pk = pk_list[0]
            pk_list.remove(first_number_pk)
            number_pk = pk_list[0]
            string_number_pk = string_number_headers_pd(number_pk)
            print("Penalty Kick(s) : ", string_number_pk)

        # -----> * Free Kicks Function * <-----

        elif choice == "fk":

            good_bad_input_fk = input(fk_input)

            if good_bad_input_fk == "gd":
                first_number_fk_gd = fk_list_gd[0]
                fk_list_gd.remove(first_number_fk_gd)
                number_fk_gd = fk_list_gd[0]
                string_number_fk_gd = string_number_headers_pd(number_fk_gd)
                print("Free Kick(s) with a Good Delivery: ", string_number_fk_gd)

            elif good_bad_input_fk == "pd":
                first_number_fk_pd = fk_list_pd[0]
                fk_list_pd.remove(first_number_fk_pd)
                number_fk_pd = fk_list_pd[0]
                string_number_fk_pd = string_number_headers_pd(number_fk_pd)
                print("Free Kick(s) with a Poor Delivery: ", string_number_fk_pd)

            else:
                pass

            first_number_fk = fk_list[0]
            fk_list.remove(first_number_fk)
            number_fk = fk_list[0]
            string_number_fk = string_number_headers_pd(number_fk)
            print("Free Kick(s)", string_number_fk)

        # -----> * Corner Kick Variables * <-----

        elif choice == "ck":

            good_bad_input_ck = input(ck_input)

            if good_bad_input_ck == "gd":
                first_number_ck_gd = ck_list_gd[0]
                ck_list_gd.remove(first_number_ck_gd)
                number_ck_gd = ck_list_gd[0]
                string_number_ck_gd = string_number_headers_pd(number_ck_gd)
                print("Corner Kick(s) with a Good Delivery: ", string_number_ck_gd)

            elif good_bad_input_ck == "pd":
                first_number_ck_pd = ck_list_pd[0]
                ck_list_pd.remove(first_number_ck_pd)
                number_ck_pd = ck_list_pd[0]
                string_number_ck_pd = string_number_headers_pd(number_ck_pd)
                print("Corner Kick(s) with a Poor Delivery: ", string_number_ck_pd)

            else:
                pass

            first_number_ck = ck_list[0]
            ck_list.remove(first_number_ck)
            number_ck = ck_list[0]
            string_number_ck = string_number_headers_pd(number_ck)
            print("Corner Kick(s): ", string_number_ck)

        # -----> * Throw Ins Functions * <-----

        elif choice == "ti":

            good_bad_input_ti = input(ti_input)

            if good_bad_input_ti == "gd":
                first_number_ti_gd = ti_list_gd[0]
                ti_list_gd.remove(first_number_ti_gd)
                number_ti_gd = ti_list_gd[0]
                string_number_ti_gd = string_number_headers_pd(number_ti_gd)
                print("Throw In(s) with a Good Delivery: ", string_number_ti_gd)

            elif good_bad_input_ti == "pd":
                first_number_ti_pd = ti_list_pd[0]
                ti_list_pd.remove(first_number_ti_pd)
                number_ti_pd = ti_list_pd[0]
                string_number_ti_pd = string_number_headers_pd(number_ti_pd)
                print("Throw In(s) with a Poor Delivery: ", string_number_ti_pd)

            else:
                pass

            first_number_ti = ti_list[0]
            ti_list.remove(first_number_ti)
            number_ti = ti_list[0]
            string_number_ti = string_number_headers_pd(number_ti)
            print("Throw In(s): ", string_number_ti)

        # -----> * Crosses Function * <-----

        elif choice == "cross":

            good_bad_input_crosses = input(crosses_input)

            if good_bad_input_crosses == "gd":
                first_number_crosses_gd = crosses_list_gd[0]
                crosses_list_gd.remove(first_number_crosses_gd)
                number_crosses_gd = crosses_list_gd[0]
                string_number_crosses_gd = string_number_headers_pd(number_crosses_gd)
                print("Cross(es) with a Good Delivery: ", string_number_crosses_gd)

            elif good_bad_input_crosses == "pd":
                first_number_crosses_pd = crosses_list_pd[0]
                crosses_list_pd.remove(first_number_crosses_pd)
                number_crosses_pd = crosses_list_pd[0]
                string_number_crosses_pd = string_number_headers_pd(number_crosses_pd)
                print("Cross(es) with a Good Delivery: ", string_number_crosses_pd)

            else:
                pass

            first_number_crosses = crosses_list[0]
            crosses_list.remove(first_number_crosses)
            number_crosses = crosses_list[0]
            string_number_crosses = string_number_headers_pd(number_crosses)
            print("Cross(es): ", string_number_crosses)

        # -----> * 1 versus 1 Function * <-----

        elif choice == "1v1":

            good_bad_input_v1 = input(v1_input)

            if good_bad_input_v1 == "w":
                first_number_v1_w = v1_list_w[0]
                v1_list_w.remove(first_number_v1_w)
                number_v1_w = v1_list_w[0]
                string_number_v1_w = string_number_headers_pd(number_v1_w)
                print("Won 1vs1: ", string_number_v1_w)

            elif good_bad_input_v1 == "l":
                first_number_v1_l = v1_list_l[0]
                v1_list_l.remove(first_number_v1_l)
                number_v1_l = v1_list_l[0]
                string_number_v1_l = string_number_headers_pd(number_v1_l)
                print("Lost 1vs1: ", string_number_v1_l)

            else:
                pass

            first_number_v1 = v1_list[0]
            v1_list.remove(first_number_v1)
            number_v1 = v1_list[0]
            string_number_v1 = string_number_headers_pd(number_v1)
            print("1vs1: ", string_number_v1)

        # -----> * Shots Function * <-----

        elif choice == "shot":

            good_bad_input_shots = input(shots_input)

            if good_bad_input_shots == "on target":
                first_number_shots_gd = shots_list_gd[0]
                shots_list_gd.remove(first_number_shots_gd)
                number_shots_gd = shots_list_gd[0]
                string_number_shots_gd = string_number_headers_pd(number_shots_gd)
                print("Shot(s) on target: ", string_number_shots_gd)

            elif good_bad_input_shots == "off target":
                first_number_shots_pd = shots_list_pd[0]
                shots_list_pd.remove(first_number_shots_pd)
                number_shots_pd = shots_list_pd[0]
                string_number_shots_pd = string_number_headers_pd(number_shots_pd)
                print("Shot(s) off target: ", string_number_shots_pd)

            else:
                pass

            first_number_shots = shots_list[0]
            shots_list.remove(first_number_shots)
            number_shots = shots_list[0]
            string_number_shots = string_number_headers_pd(number_shots)
            print("Shot(s): ", string_number_shots)

        # -----> * Headers Function * <-----

        elif choice == "header":

            good_bad_input_headers = input(headers_input)

            if good_bad_input_headers == "on target":
                first_number_headers_gd = headers_list_gd[0]
                headers_list_gd.remove(first_number_headers_gd)
                number_headers_gd = headers_list_gd[0]
                string_number_headers_gd = string_number_headers_pd(number_headers_gd)
                print("Header(s) on target: ", string_number_headers_gd)

            elif good_bad_input_headers == "off target":
                first_number_headers_pd = headers_list_pd[0]
                headers_list_pd.remove(first_number_headers_pd)
                number_headers_pd = headers_list_pd[0]
                string_number_headers_pd = string_number_headers_pd(number_headers_pd)
                print("Header(s) off target: ", string_number_headers_pd)

            else:
                pass

            first_number_headers = headers_list[0]
            headers_list.remove(first_number_headers)
            number_headers = headers_list[0]
            string_number_headers = string_number_headers_pd(number_headers)
            print("Header(s): ", string_number_headers)

        # -----> * Long Passes * <-----

        elif choice == "long pass":
            good_bad_input_long_passes = input(long_passes_input)
            first_number_long_passes = long_passes_list[0]
            long_passes_list.remove(first_number_long_passes)
            number_long_passes = long_passes_list[0]
            string_number_long_passes = string_number_headers_pd(number_long_passes)
            print("Long Pass(es): ", string_number_long_passes)

            if good_bad_input_long_passes == "first touch":
                first_number_long_passes_first_touch = long_passes_list_first_touch[0]
                long_passes_list_first_touch.remove(first_number_long_passes_first_touch)
                number_long_passes_first_touch = long_passes_list_first_touch[0]
                string_number_long_passes_first_touch = string_number_headers_pd(number_long_passes_first_touch)
                print("Long Pass(es) first touch: ", string_number_long_passes_first_touch)

            elif good_bad_input_long_passes == "second touch":
                first_number_long_passes_second_touch = long_passes_list_second_touch[0]
                long_passes_list_second_touch.remove(first_number_long_passes_second_touch)
                number_long_passes_second_touch = long_passes_list_second_touch[0]
                string_number_long_passes_second_touch = string_number_headers_pd(number_long_passes_second_touch)
                print("Long Pass(es) second touch: ", string_number_long_passes_second_touch)

            else:
                pass

        # -----> * Saves * <-----

        elif choice == "save":
            first_number_saves = saves_list[0]
            saves_list.remove(first_number_saves)
            number_saves = saves_list[0]
            string_number_saves = first_number_saves_string(number_saves)
            print("Save(s)", string_number_saves)

        # -----> * Quit * <-----

        elif choice == "q":

            print("Are you sure that you want to finish the stat counting? (yes/no)")
            quit_choice = input()

            if quit_choice == "yes":

                # -----> * Penalty_Kicks_total_quit_function * <-----

                if first_number_pk_string == "0":
                    print("Penalty Kick(s): ", string_number_pk)
                else:
                    print("Penalty Kicks: 0 ")

                # -----> * Penalty_Kicks_goal_quit_function * <-----
                
                if first_number_pk_goal_string == "0":
                    print("Goals from Penalty Kicks:  ", string_number_pk_goal)
                else:
                    print("Goals from Penalty Kicks: 0 ")

                # -----> * Penalty_Kicks_missed_quit_function * <-----
                
                if first_number_pk_missed_string == "0":
                    print("Missed Penalty Kicks: ", string_number_pk_missed)
                else:
                    print("Missed Penalty Kicks: 0 ")

                # -----> * Penalty_Kicks_saved_quit_function * <-----

                if first_number_pk_saved_string == "0":
                    print("Penalty Kick(s) with Good Delivery: ", string_number_pk_saved)
                else:
                    print("Saved Penalty Kicks: 0 ")

                # -----> * Free_Kicks_total_quit_function * <-----

                if first_number_fk_string == "0":
                    print("Free Kick(s): ", string_number_fk)
                else:
                    print("Free Kicks: 0 ")

                # -----> * Free_Kicks_gd_quit_function * <-----

                if first_number_fk_gd_string == "0":
                    print("Free Kick(s) with Good Delivery: ", string_number_fk_gd)
                else:
                    print("Free Kicks with Good Delivery: 0 ")

                # -----> * Free_Kick_pd_quit_function * <-----

                if first_number_fk_pd_string == "0":
                    print("Free Kick(s) with  Poor Delivery: ", string_number_fk_pd)
                else:
                    print("Free Kicks with Poor Delivery: 0 ")

                # -----> * Corner_Kick_total_quit_function * <-----

                if first_number_ck_string == "0":
                    print("Cross(es): ", string_number_ck)
                else:
                    print("Crosses: 0 ")

                # -----> * Corner_Kick_gd_quit_function * <-----
                
                if first_number_ck_gd_string == "0":
                    print("Cross(es) with Good Delivery: ", string_number_ck_gd)
                else:
                    print("Crosses with Good Delivery: 0 ")

                # -----> * Corner_Kick_pd_quit_function * <-----
                
                if first_number_ck_pd_string == "0":
                    print("Cross(es) with  Poor Delivery: ", string_number_ck_pd)
                else:
                    print("Crosses with Poor Delivery: 0 ")
                
                # -----> * Throw_Ins_total_quit_function * <-----

                if first_number_ti_string == "0":
                    print("Throw In(s): ", string_number_ti)
                else:
                    print("Throw Ins: 0 ")

                # -----> * Throw_Ins_gd_quit_function * <-----
                
                if first_number_ti_gd_string == "0":
                    print("Throw In(s) with Good Delivery: ", string_number_ti_gd)
                else:
                    print("Throw Ins with Good Delivery: 0 ")

                # -----> * Throw_Ins_pd_quit_function * <-----
                
                if first_number_ti_pd_string == "0":
                    print("Throw In(s) with  Poor Delivery: ", string_number_ti_pd)
                else:
                    print("Throw Ins with Poor Delivery: 0 ")
                
                # -----> * Crosses_total_quit_function * <-----

                if first_number_crosses_string == "0":
                    print("Cross(es): ", string_number_crosses)
                else:
                    print("Crosses: 0 ")

                # -----> * Crosses_gd_quit_function * <-----
                
                if first_number_crosses_gd_string == "0":
                    print("Cross(s) with Good Delivery: ", string_number_crosses_gd)
                else:
                    print("Crosses with Good Delivery: 0 ")

                # -----> * Crosses_pd_quit_function * <-----
                
                if first_number_crosses_pd_string == "0":
                    print("Cross(s) with  Poor Delivery: ", string_number_crosses_pd)
                else:
                    print("Crosses with Poor Delivery: 0 ")

                # -----> * Shots_total_quit_function * <-----

                if first_number_shots_string == "0":
                    print("Shot(s): ", string_number_shots)
                else:
                    print("Shots: 0 ")

                # -----> * Shots_gd_quit_function * <-----

                if first_number_shots_gd_string == "0":
                    print("Shot(s) on target: ", string_number_shots_gd)
                else:
                    print("Shots on target: 0 ")

                # -----> * Shots_pd_quit_function * <-----
                
                if first_number_shots_pd_string == "0":
                    print("Shot(s) off target: ", string_number_shots_pd)
                else:
                    print("Shots off target: 0 ")

                # -----> * Headers_total_quit_function * <-----

                if first_number_headers_string == "0":
                    print("Free Kick(s): ", string_number_headers)
                else:
                    print("Free Kicks: 0 ")

                # -----> * Headers_gd_quit_function * <-----
                
                if first_number_headers_gd_string == "0":
                    print("Header(s) on target: ", string_number_headers_gd)
                else:
                    print("Headers on target: 0 ")

                # -----> * Headers_pd_quit_function * <-----
                
                if first_number_headers_pd_string == "0":
                    print("Header(s) off target: ", string_number_headers_pd)
                else:
                    print("Headers off target: 0 ")

                # -----> * 1vs1_total_quit_function * <-----

                if first_number_v1_string == "0":
                    print("Free Kick(s): ", string_number_v1)
                else:
                    print("Free Kicks: 0 ")

                # -----> * 1vs1_won_quit_function * <-----

                if first_number_v1_w_string == "0":
                    print("1vs1 won: ", string_number_v1_w)
                else:
                    print("1vs1 won: 0 ")

                # -----> * 1vs1_pd_quit_function * <-----

                if first_number_v1_l_string == "0":
                    print("1vs1 Lost: ", string_number_v1_l)
                else:
                    print("1vs1 Lost: 0 ")

                # -----> * saves_total_quit_function * <-----

                if first_number_saves_string == "0":
                    print("Save(s): ", string_number_saves)
                else:
                    print("Saves: 0 ")

                # -----> * Long_Pass_total_quit_function * <-----

                if first_number_long_passes_string == "0":
                    print("Work In Progress... but: ", string_number_long_passes)
                else:
                    print("Work In Progress... but: 0 ")

                # -----> * Long_Pass_second_ball_quit_function * <-----

                if first_number_long_passes_string == "0":
                    print("Work In Progress... but: ", string_number_long_passes_first_touch)
                else:
                    print("Work In Progress... but: 0 ")

                # -----> * Long_Pass_Third_Ball_quit_function * <-----

                if first_number_long_passes_string == "0":
                    print("Work In Progress... but: ", string_number_long_passes_second_touch)
                else:
                    print("Work In Progress")

                break
            elif quit_choice == "no":
                pass

            else:
                pass


body()
