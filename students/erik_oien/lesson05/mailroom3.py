#!/usr/bin/env python3

import sys 
import os

donor_dict = {
    "Nathan Explosion": [39595, 35081, 93295], 
    "Skwisgaar Skwigelf": [37198], 
    "Toki Wartooth": [20037, 32892, 99788],
    "William Murderface": [87470, 86870, 4397],
    "Pickles": [87838, 60282, 26653],
}

# main menu for program 

def menu():
    while True:
        welcome_input = input(opening_promt)
        try:
            main_menu_switch[welcome_input]()
        except KeyError:
            print("Invalid option, please choose a number from the list below:")

# thank you menu
def thank_you():
    while True:
        donor_name = input(f"Please choose a donor or type list to see previous donors.\n{sub_menu_prompt}")
        past_donor = False
        if donor_name.lower() in ["menu", "quit"]:
            sub_menu_switch[donor_name.lower()]()
        elif donor_name.lower() == 'list':
            past_donor = False
            for donor in donor_dict.keys():
                print(donor)
        else:
            for donor in donor_dict:
                if donor_name.lower() == donor.lower():
                    past_donor = True
                    donation_amount = input("How much was the most recent donation from {}? >>> ".format(donor_name))
                    donor_dict[donor].append(int(donation_amount))
            if past_donor == False:
                print("Looks like this is a new donor, lets add them!")
                donation_amount = input("How much did {} donate? >>> ".format(donor_name))
                donor_dict[donor_name] = [int(donation_amount)]
        email = thank_you_email(donor_name, donation_amount)
        print(email)
        return False
   
# create report menu

def create_report():
    donor_info = sorted(donor_dict.items(), key=lambda x: sum(x[1]), reverse=True)
    table_header()
    for donor in donor_info:
        row = [donor[0], sum(donor[1]), len(donor[1]), sum(donor[1])/len(donor[1])]
        row_formatter(row)
    return_input = input(f"{sub_menu_prompt}")
    if return_input in ["menu", "quit"]:
            sub_menu_switch[return_input.lower()]()
        
# send letters to all donors

def thank_all_donors():
    while True:
        wd = os.getcwd()
        dir_name = input(f"What would you like to call the directory?\n{sub_menu_prompt}")
        if dir_name.lower() in ["menu", "quit"]:
            sub_menu_switch[dir_name.lower()]()
            return False
        else:
            try:
                dir_path = wd + "/" + dir_name
                os.mkdir(wd + "/" + dir_name)
                for donor in donor_dict.items():
                    donor_facts = [donor[0], len(donor[1]), sum(donor[1])]
                    donor_letter = thank_you_letter(donor_facts, dir_path)
                return False
            except FileExistsError:
                print("Please try a different file name")

# helper functions

# function to create email
def thank_you_email(donor, amount):
    email_text = "Dear {},\n\nThank you for your generous donation of ${}! As you certianly know, kittens\nand metal are awesome and your donation will insure that others will be able\nto enjoy kittens and metal.\n\nThank you,\n\nKitten and Metal Charity \m/\n\n"
    return email_text.format(donor, amount)

# function for table header
def table_header():
    print("{:25}|{:12}|{:10}|{:12}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-" * 62)

# function to format rows
def row_formatter(row):
    print("{:25}|${:11.2f}|{:10}|${:11.2f}".format(*row))

# function to quit program
def quit_program():
    print("Bye!")
    sys.exit()  

# thank you letter
def thank_you_letter(text, dir_path):
    letter_text = "Dear {},\n\n\tYou have made {} donations to the kittens and metal charity totaling ${}.\n\nThank you,\n\n\tKitten and Metal Charity \m/".format(*text)
    file_name = dir_path + "/" + text[0] + ".txt"
    with open(file_name, "w") as f:
        f.write(letter_text)

# using dictionary for switch

main_menu_switch = {
    "1": thank_you,
    "2": create_report,
    "3": thank_all_donors,
    "4": quit_program,
    "quit": quit_program,
}

sub_menu_switch = {
    "menu": menu,
    "quit": quit_program,
}

# prompts used in program

opening_promt = "\n".join(("Welcome to the mailroom!",
                "Please choose from the below options",
                "1 - Send a Thank You",
                "2 - Create a Report",
                "3 - Send letters to all donors",
                "4 - Quit",
                ">>> "))

sub_menu_prompt = "\n".join(("If you would like to return to the menu type menu.",
                    "If you would like to quit please type quit.",
                    ">>> "))

if __name__ == "__main__": 
    menu()
    