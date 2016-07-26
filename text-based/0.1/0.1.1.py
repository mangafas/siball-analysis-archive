pk_range = range(0, 1000)
pk_list = list(pk_range)

fk_range = range(0, 1000)
fk_list = list(fk_range)

ck_range = range(0, 1000)
ck_list = list(ck_range)

ti_range = range(0, 1000)
ti_list = list(ti_range)

v1_range = range(0, 1000)
v1_list = list(v1_range)

crosses_range = range(0, 1000)
crosses_list = list(crosses_range)

saves_range = range(0, 1000)
saves_list = list(saves_range)

shot_range = range(0, 1000)
shot_list = list(shot_range)

header_range = range(0, 1000)
header_list = list(header_range)



def body():
    print("Hello there, how are you? Thanks for using siball-analysis. If you anytime want to quit the program or the match has finished press the q button to get your results. Thank you!!!")
    # A big, big intro
    while True == True:
        choice = input("")
        if choice == "pk":
            first_number_pk = pk_list[0]
            pk_list.remove(first_number_pk)
            number_pk = pk_list[0]
            string_number_pk = str(number_pk)
            print(string_number_pk)
        elif choice == "fk":
            first_number_fk = fk_list[0]
            fk_list.remove(first_number_fk)
            number_fk = fk_list[0]
            string_number_fk = str(number_fk)
            print(string_number_fk)
        elif choice == "ck":
            first_number_ck = ck_list[0]
            ck_list.remove(first_number_ck)
            number_ck = ck_list[0]
            string_number_ck = str(number_ck)
            print(string_number_ck)
        elif choice == "ti":
            first_number_ti = ti_list[0]
            ti_list.remove(first_number_ti)
            number_ti = ti_list[0]
            string_number_ti = str(number_ti)
            print(string_number_ti)
        elif choice == "1v1":
            first_number_v1 = v1_list[0]
            v1_list.remove(first_number_v1)
            number_v1 = v1_list[0]
            string_number_v1 = str(number_v1)
            print(string_number_v1)
        elif choice == "crosses":
            first_number_crosses = crosses_list[0]
            crosses_list.remove(first_number_crosses)
            number_crosses = crosses_list[0]
            string_number_crosses = str(number_crosses)
            print(string_number_crosses)
        elif choice == "save":
            first_number_save = saves_list[0]
            saves_list.remove(first_number_save)
            number_save = saves_list[0]
            string_number_save = str(number_save)
            print(string_number_save)
        elif choice == "shot":
            first_number_shot = shot_list[0]
            shot_list.remove(first_number_shot)
            number_shot = shot_list[0]
            string_number_shot = str(number_shot)
            print(string_number_shot)
        elif choice == "header":
            first_number_header = header_list[0]
            header_list.remove(first_number_header)
            number_header = header_list[0]
            string_number_header = str(number_header)
            print(string_number_header)
        elif choice == "q":
            break
body()
