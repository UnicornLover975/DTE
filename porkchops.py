#functions go here
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes/no")

#main routine goes here

while True:
    want_instructions = yes_no("do you want to read the instructions??????? ")
    print(want_instructions)

    if want_instructions == "yes" or want_instructions == "y":
        print("instructions go here")
    elif want_instructions == "no" or want_instructions == "n":
        print("program continues")
    else:
        print("please answer yes/no")

print("We are done.")