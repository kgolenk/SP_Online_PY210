#!/usr/bin/env python3

"""
User interaction functions and main program flow
"""

from donor_models import Donor, DonorCollection
import sys

'''
def donor_list4():
    # dictionary with donor names and donation amounts
    dc = DonorCollection()
    donors = ["William Gates, III", "Jeff Bezos", "Paul Allen", "Mark Zuckerberg", "Alexandra Butler"]
    amounts = [[653772.32, 12.17], [877.33], [663.23, 43.87, 1.32], [1663.23, 4300.87, 10432.0], [777.77, 44.44]]
    for donor, amount in zip(donors,amounts):
        for donation in amount:
            dc.update_donor(donor, donation)
            
    print(donors.values())        
'''
def donor_list():
    # generate initial donor dict
    d = Donor('William Gates, III')
    z = [653772.32, 12.1]
    for amount in z:
        d.add_amount(amount)
          
    d1 = Donor('Jeff Bezos')
    z = [877.33]
    for amount in z:
        d1.add_amount(amount) 
        
    d2 = Donor('Paul Allen')
    z = [663.23, 43.87, 1.32]
    for amount in z:
        d2.add_amount(amount)

    d3 = Donor('Mark Zuckerberg')
    z = [1663.23, 4300.87, 10432.0]
    for amount in z:
        d3.add_amount(amount)

    d4 = Donor('Clifford Butler')
    z = [777.77, 44.44]
    for amount in z:
        d4.add_amount(amount)
        
def main_menu():
    # display the main menu
    print("\n".join(("Welcome to the MailRoom!",
        "Please choose from below options:",
        "1 - Send a Thank You",
        "2 - Create a Report",
        "3 - Send letters to all donors",
        "4 - Quit",
        ">>> ")))
    return input()

def prompt_amount(full_name):
    # request user input for donation amount
    try:    
        amount = input("What's the donation amount? \n >>")
        amount = int(amount)
        Donor(full_name).add_amount(full_name,amount) 
    except ValueError:
        print("Input must be a number. Donor information not entered. Try again! ")
    return amount

def prompt_name():
    # request user to input a full name
    try:
        full_name = input("Type the donors full name or type list to display donor names.")
        if full_name == 'list':
            for key in donor_list:
                print(key)
            prompt_name()
        elif full_name == "":
            raise TypeError
        else:
            Donor(full_name).update_donor(full_name)
    except TypeError:
            print("\nNot a valid answer. Please enter a name.\n>>>")
    return full_name

def thank_you_text(full_name,amount):
    # get user input to send thank you
    dc = DonorCollection()
    while True:
        donor_name = input("Enter the donor name, 'list' to get list of donors, or 'exit' to exit.) ")
        if donor_name.lower() == 'exit':
            exit_program()
        elif donor_name.lower() == "list":
            print('\nCurrent list of donors:\n')
            print('\n'.join(dc.donor_names))
            continue
        else:
            if donor_name not in dc.donor_names:
                answer = input("The donor name is not in the list of donors. "
                               "Do you want to add the donor? Yes or No ")
                if answer.lower() == "yes":
                    name = donor_name
                else:
                    exit_program()

        donation_amount = input("Enter the donation amount (or q to quit) ")
        if donation_amount.lower() == 'q':
            exit_program()
        elif float(donation_amount) > 0:
            amount = float(donation_amount)
            dc.update_donor(name,amount)
        else:
            print("The number you enter must be greater than 0.")

        dc.update_donor(name,amount)
        email = dc.get_donor(name).generate_email()
        print(email)
        return

def send_thank_you():
    # send thank you email based on user input information
    full_name = prompt_name()
    amount = prompt_amount(full_name)
    thank_you_text(full_name,amount)
    main()

def report_format(report):
    formatted_report = ['',
    'Donor Name                    | Total Donation | Num Donations | Avg Donation |',
    '-------------------------------------------------------------------------------']
    for donor in report:
        donor_name, total, number, average = donor
        formatted_report.append(f'{donor_name:<30} ${total:>14.2f}  {number:14d}  ${average:>12.2f}')
    formatted_report.append('')
    print('\n'.join(formatted_report))
    
def create_report():
    # Generate, format, and print report data
    dc = DonorCollection()
    report = dc.report_data()
    report_format(report)    
    
def letter_to_all():
    # send thank you letter to all donors
    dc = DonorCollection()
    for full_name in dc.get_donor:
        with open(f"{full_name}.txt","w+") as donor_letter:
            donor_letter.write(f"Hi {full_name},\n\nThank you for the generous donation of ${sum(donor_list[full_name]):.2f}.\n\nSincerely,\nClifford Butler")
    print("Thank you letters sent!")

def exit_program():
    # exit the interactive script
    print("Bye!")
    sys.exit() 

def main():
    #dict with the user options and the functions
    switch_dict = {
        '1': send_thank_you,
        '2': create_report,
        '3': letter_to_all,
        '4': exit_program
    }
    
    while True:
        try:
            response = main_menu()
            switch_dict[response]()
        except KeyError:
            print("\n'{}'  is not a valid option, please enter 1, 2, 3, or 4!. \n >> ".format(response))

if __name__ == "__main__":
   donor_list()
   main()