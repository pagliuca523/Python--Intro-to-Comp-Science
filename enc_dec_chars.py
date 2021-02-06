## Software used for enconde letter aka chars and/or decode them

def main():

    message_user = str(input('Please enter your message: '))

    for i in message_user:
        char_to_num = ord(i)
        num_to_char = chr(char_to_num)
        print("Char to NUM: {} -> Num to CHAR: {}".format(char_to_num,num_to_char) )

main()