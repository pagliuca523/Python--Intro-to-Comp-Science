# Program used to generates usernames ; Rule First letter + up to 7 chars Last Name


def main():

    print("Program used to generates usernames\n")
    usr_first_name = str(input("Please enter your first name: "))
    while len(usr_first_name) <=1:
        usr_first_name = str(input("Please enter your first name: "))
    
    usr_last_name = str(input("Please enter your last name: "))
    while len(usr_last_name) <=1:
          usr_last_name = str(input("Please enter your last name: "))

    final_username = usr_first_name[0]+usr_last_name[0:7]
    print ("Your username is: {}".format(final_username))
    
   
       


main()