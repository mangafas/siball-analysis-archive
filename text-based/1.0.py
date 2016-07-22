pk_range = range(0,1000)
pk_list = list(pk_range)
fk_range = range(0,1000)
fk_list = list(fk_range)
#it creates a list through the range functions so the user will be able to interact with it


def body():
    print("Hello there, how are you? Thanks for using siball-analysis. If you anytime want to quit the program or the match has finished press the q button to get your results. Thank you!!!")
    # A big, big intro                                                                                               __
    while True == True:  # true=true will run forever as it will always be True                                        |
        choice = input("")  # in choice you right what you want ex. 'pk'                                               |
        if choice == "pk":                                                                                           # |
            first_number_pk = pk_list[0]  # it takes the first number. At start its 0 but then it will be 1, 2,3 and   |
            # so on                                                                                                    |
            pk_list.remove(first_number_pk)  # it deletes the first number. At start it will remove 0 from the list    |
            # but then it will remove the number that have been printed below the number                               |
            number_pk = pk_list[0]  # it re-takes the first number or the next number after the deleted one          __|
            string_number_pk = str(number_pk)                                                                      # |
            print(string_number_pk)                                                                                # |
        elif choice == "fk":                                                                                       # |
            first_number_fk = fk_list[0]           # this is the same as the above -----------------------------------
            fk_list.remove(first_number_fk)
            number_fk = fk_list[0]
            string_number_fk = str(number_fk)
            print(string_number_fk)
        elif choice == "q":
            total_pk = string_number_pk
            print("In this game there have been a total of", str(total_pk), "Penalty Kick")
            total_fk = string_number_pk
            print("In this game there have been a total of", str(total_fk), "Free Kick")
            break
            # here if the user wants to quit it will break the while loop, killing the program but meanwhile it will
            # display the total number of fk and pk in a match

body()

# NOTE: TOO MUCH COMMENTING AND TOO LONG VARIABLE NAMES... I KNOW... IT'S FUN THAT WAY :P
