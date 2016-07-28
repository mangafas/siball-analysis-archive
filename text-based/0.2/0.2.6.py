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


# -----> * Main Function * <-----

def body():
    global string_number_ck_pd, string_number_save, string_number_headers, string_number_headers_pd, string_number_headers_gd, string_number_shots, string_number_shots_pd, string_number_shots_gd, string_number_v1, string_number_v1_l, string_number_v1_w, string_number_crosses, string_number_crosses_pd, string_number_crosses_gd, string_number_ti, string_number_ti_pd, string_number_ti_gd, string_number_ck, string_number_ck_gd, string_number_fk, string_number_fk_pd, string_number_fk_gd, string_number_pk, string_number_pk_missed, string_number_pk_goal
    while True:
        choice = input("")

        # -----> * Penalty Kicks Function * <-----

        if choice == "pk":

            good_bad_input_pk = input(pk_input)

            if good_bad_input_pk == "goal":
                first_number_pk_goal = pk_list_goal[0]
                pk_list_goal.remove(first_number_pk_goal)
                number_pk_goal = pk_list_goal[0]
                string_number_pk_goal = str(number_pk_goal)
                print("Penalty Kick goal(s): ", string_number_pk_goal)

            elif good_bad_input_pk == "saved":
                first_number_pk_saved = pk_list_saved[0]
                pk_list_saved.remove(first_number_pk_saved)
                number_pk_saved = pk_list_saved[0]
                string_number_pk_saved = str(number_pk_saved)
                print("Penalty Kick(s) saved: ", string_number_pk_saved)

            elif good_bad_input_pk == "missed":
                first_number_pk_missed = pk_list_missed[0]
                pk_list_missed.remove(first_number_pk_missed)
                number_pk_missed = pk_list_missed[0]
                string_number_pk_missed = str(number_pk_missed)
                print("Penalty Kick(s) missed: ", string_number_pk_missed)

            else:
                pass

            first_number_pk = pk_list[0]
            pk_list.remove(first_number_pk)
            number_pk = pk_list[0]
            string_number_pk = str(number_pk)
            print("Penalty Kick(s) : ", string_number_pk)

        # -----> * Free Kicks Function * <-----

        elif choice == "fk":

            good_bad_input_fk = input(fk_input)

            if good_bad_input_fk == "gd":
                first_number_fk_gd = fk_list_gd[0]
                fk_list_gd.remove(first_number_fk_gd)
                number_fk_gd = fk_list_gd[0]
                string_number_fk_gd = str(number_fk_gd)
                print("Free Kick(s) with a Good Delivery: ", string_number_fk_gd)

            elif good_bad_input_fk == "pd":
                first_number_fk_pd = fk_list_pd[0]
                fk_list_pd.remove(first_number_fk_pd)
                number_fk_pd = fk_list_pd[0]
                string_number_fk_pd = str(number_fk_pd)
                print("Free Kick(s) with a Poor Delivery: ", string_number_fk_pd)

            else:
                pass

            first_number_fk = fk_list[0]
            fk_list.remove(first_number_fk)
            number_fk = fk_list[0]
            string_number_fk = str(number_fk)
            print("Free Kick(s)", string_number_fk)

        # -----> * Corner Kick Variables * <-----

        elif choice == "ck":

            good_bad_input_ck = input(ck_input)

            if good_bad_input_ck == "gd":
                first_number_ck_gd = ck_list_gd[0]
                ck_list_gd.remove(first_number_ck_gd)
                number_ck_gd = ck_list_gd[0]
                string_number_ck_gd = str(number_ck_gd)
                print("Corner Kick(s) with a Good Delivery: ", string_number_ck_gd)

            elif good_bad_input_ck == "pd":
                first_number_ck_pd = ck_list_pd[0]
                ck_list_pd.remove(first_number_ck_pd)
                number_ck_pd = ck_list_pd[0]
                string_number_ck_pd = str(number_ck_pd)
                print("Corner Kick(s) with a Poor Delivery: ", string_number_ck_pd)

            else:
                pass

            first_number_ck = ck_list[0]
            ck_list.remove(first_number_ck)
            number_ck = ck_list[0]
            string_number_ck = str(number_ck)
            print("Corner Kick(s): ", string_number_ck)

        # -----> * Throw Ins Functions * <-----

        elif choice == "ti":

            good_bad_input_ti = input(ti_input)

            if good_bad_input_ti == "gd":
                first_number_ti_gd = ti_list_gd[0]
                ti_list_gd.remove(first_number_ti_gd)
                number_ti_gd = ti_list_gd[0]
                string_number_ti_gd = str(number_ti_gd)
                print("Throw In(s) with a Good Delivery: ", string_number_ti_gd)

            elif good_bad_input_ti == "pd":
                first_number_ti_pd = ti_list_pd[0]
                ti_list_pd.remove(first_number_ti_pd)
                number_ti_pd = ti_list_pd[0]
                string_number_ti_pd = str(number_ti_pd)
                print("Throw In(s) with a Poor Delivery: ", string_number_ti_pd)

            else:
                pass

            first_number_ti = ti_list[0]
            ti_list.remove(first_number_ti)
            number_ti = ti_list[0]
            string_number_ti = str(number_ti)
            print("Throw In(s): ", string_number_ti)

        # -----> * Crosses Function * <-----

        elif choice == "cross":

            good_bad_input_crosses = input(crosses_input)

            if good_bad_input_crosses == "gd":
                first_number_crosses_gd = crosses_list_gd[0]
                crosses_list_gd.remove(first_number_crosses_gd)
                number_crosses_gd = crosses_list_gd[0]
                string_number_crosses_gd = str(number_crosses_gd)
                print("Cross(es) with a Good Delivery: ", string_number_crosses_gd)

            elif good_bad_input_crosses == "pd":
                first_number_crosses_pd = crosses_list_pd[0]
                crosses_list_pd.remove(first_number_crosses_pd)
                number_crosses_pd = crosses_list_pd[0]
                string_number_crosses_pd = str(number_crosses_pd)
                print("Cross(es) with a Good Delivery: ", string_number_crosses_pd)

            else:
                pass

            first_number_crosses = crosses_list[0]
            crosses_list.remove(first_number_crosses)
            number_crosses = crosses_list[0]
            string_number_crosses = str(number_crosses)
            print("Cross(es): ", string_number_crosses)

        # -----> * 1 versus 1 Function * <-----

        elif choice == "1v1":

            good_bad_input_v1 = input(v1_input)

            if good_bad_input_v1 == "w":
                first_number_v1_w = v1_list_w[0]
                v1_list_w.remove(first_number_v1_w)
                number_v1_w = v1_list_w[0]
                string_number_v1_w = str(number_v1_w)
                print("Won 1vs1: ", string_number_v1_w)

            elif good_bad_input_v1 == "l":
                first_number_v1_l = v1_list_l[0]
                v1_list_l.remove(first_number_v1_l)
                number_v1_l = v1_list_l[0]
                string_number_v1_l = str(number_v1_l)
                print("Lost 1vs1: ", string_number_v1_l)

            else:
                pass

            first_number_v1 = v1_list[0]
            v1_list.remove(first_number_v1)
            number_v1 = v1_list[0]
            string_number_v1 = str(number_v1)
            print("1vs1: ", string_number_v1)

        # -----> * Shots Function * <-----

        elif choice == "shot":

            good_bad_input_shots = input(shots_input)

            if good_bad_input_shots == "on target":
                first_number_shots_gd = shots_list_gd[0]
                shots_list_gd.remove(first_number_shots_gd)
                number_shots_gd = shots_list_gd[0]
                string_number_shots_gd = str(number_shots_gd)
                print("Shot(s) on target: ", string_number_shots_gd)

            elif good_bad_input_shots == "off target":
                first_number_shots_pd = shots_list_pd[0]
                shots_list_pd.remove(first_number_shots_pd)
                number_shots_pd = shots_list_pd[0]
                string_number_shots_pd = str(number_shots_pd)
                print("Shot(s) off target: ", string_number_shots_pd)

            else:
                pass

            first_number_shots = shots_list[0]
            shots_list.remove(first_number_shots)
            number_shots = shots_list[0]
            string_number_shots = str(number_shots)
            print("Shot(s): ", string_number_shots)

        # -----> * Headers Function * <-----

        elif choice == "header":

            good_bad_input_headers = input(headers_input)

            if good_bad_input_headers == "on target":
                first_number_headers_gd = headers_list_gd[0]
                headers_list_gd.remove(first_number_headers_gd)
                number_headers_gd = headers_list_gd[0]
                string_number_headers_gd = str(number_headers_gd)
                print("Header(s) on target: ", string_number_headers_gd)

            elif good_bad_input_headers == "off target":
                first_number_headers_pd = headers_list_pd[0]
                headers_list_pd.remove(first_number_headers_pd)
                number_headers_pd = headers_list_pd[0]
                string_number_headers_pd = str(number_headers_pd)
                print("Header(s) off target: ", string_number_headers_pd)

            else:
                pass

            first_number_headers = headers_list[0]
            headers_list.remove(first_number_headers)
            number_headers = headers_list[0]
            string_number_headers = str(number_headers)
            print("Header(s): ", string_number_headers)

        # -----> * Saves * <-----

        elif choice == "save":
            first_number_save = saves_list[0]
            saves_list.remove(first_number_save)
            number_save = saves_list[0]
            string_number_save = str(number_save)
            print("Save(s)", string_number_save)

        elif choice == "q":
            print("Are you sure that you want to finish the stat counting? (yes/no)")
            quit_choice = input()
            if quit_choice == "yes":
                print("Penalty Kick goal(s): ", string_number_pk_goal)
                print("Penalty Kick(s) saved: ", string_number_pk_goal)
                print("Penalty Kick(s) missed: ", string_number_pk_missed)
                print("Total Penalty Kick(s): ", string_number_pk)
                print("Free Kick(s) with  Good Delivery: ", string_number_fk_gd)
                print("Free Kick(s) with  Poor Delivery: ", string_number_fk_pd)
                print("Free Kick(s): ", string_number_fk)
                print("Corner Kick(s) with Good Delivery: ", string_number_ck_gd)
                print("Corner Kick(s) with Poor Delivery: ", string_number_ck_pd)
                print('Corner Kick(s): ', string_number_ck)
                print("Throw In(s) with Good Delivery: ", string_number_ti_gd)
                print("Throw In(s) with Poor Delivery: ", string_number_ti_pd)
                print("Throw In(s): ", string_number_ti)
                print("Cross(es) with Good Delivery: ", string_number_crosses_gd)
                print("Cross(es) with Poor Delivery: ", string_number_crosses_pd)
                print("Cross(es): ", string_number_crosses)
                print("Won 1vs1: ", string_number_v1_w)
                print("Lost 1vs1: ", string_number_v1_l)
                print("1vs1: ", string_number_v1)
                print("Shot(s) on target: ", string_number_shots_gd)
                print("Shot(s) off target: ", string_number_shots_pd)
                print("Shot(s): ", string_number_shots)
                print("Header(s) on target: ", string_number_headers_gd)
                print("Header(s) off target: ", string_number_headers_pd)
                print("Header(s) : ", string_number_headers)
                print("Save(s)", string_number_save)
                break
            elif quit_choice == "no":
                pass

            else:
                pass


body()
