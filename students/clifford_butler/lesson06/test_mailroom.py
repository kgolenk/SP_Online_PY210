#!/usr/bin/env python3

'''
Mailroom Part 4
Add a full suite of unit tests.
'''

import mailroom4
import sys 
from mock import patch

def test_thank_you_text():
    '''
    test thank you text function
    '''
    full_name = 'Clifford Butler'
    amount = 5000
    thank_you_text = ("\nHi {}:\n\nThank you for the generous donation of ${:2d}, Sincerely, \n\nClifford Butler".format(full_name,amount))
    text = "\nHi Clifford Butler:\n\nThank you for the generous donation of $5000, Sincerely, \n\nClifford Butler"
    assert thank_you_text == text

def test_add_name():
    '''
    test add name function
    '''
    full_name = 'Clifford Butler'
    add_name(full_name)
    assert full_name in donor_list.keys()

def test_prompt_amount():
    '''
    test prompt amount function
    '''
    full_name = "Clifford Butler"
    amount = 5000
    prompt_amount(full_name,amount)
    assert donor_list[fullname][-1] == amount

def test_exit_program():
    '''
    test exit function 
    '''
    with patch('sys.exit') as exit_mock:
        mr.exit_program()
        assert exit_mock.called == True

if __name__== "__main__":
    test_thank_you_text()
    test_add_name()
    test_exit_program()
    print('All test passed')
    


  

