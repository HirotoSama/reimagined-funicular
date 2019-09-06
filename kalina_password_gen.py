# requirements
import os

print('This program is meant to generate a wordlist from 2 text files and allow the user to append digits')
print(' - Developped by Sote\n')


# global functions


def x():
    input('Press Enter to Continue')


def detect_input():  # detects user input
    return input('\n' + os.getlogin() + ': ')

# menus layout


def print_main_menu():
    print(40 * '_')
    print('{:^40}'.format('- Main Menu -'))
    print(40 * '\u203e')
    print('0 > About')
    print('1 > Settings')
    print('2 > Generate')
    print('3 > Graphical output')
    print('4 > Exit')


def print_about_sub():
    print(40 * '_')
    print('{:^40}'.format('About'))
    print(40 * '\u203e')
    print('# TODO')
    # TODO open and print about.txt


def print_settings_sub():
    print(40 * '_')
    print('{:^40}'.format('Settings'))
    print(40 * '\u203e')
    print('0 > Print current Settings')
    print('1 > Import 1st file')
    print('2 > Import 2nd file')
    print('3 > Set file to generate')
    print('4 > Set min/max length')
    print('5 > Set digits to append')
    print('6 > Set working directory')
    print('99 > back to Main Menu')

# Settings
file1 = 'Text file 1'
file2 = 'Text file 2'
file_to_generate = 'File to generate'
minlength = 'Min length of words to generate'
maxlength = 'Max length of words to generate'
digits = 'Digits to append'
lstsettings = [file1, file2, file_to_generate, minlength, maxlength, digits, ]
settingsvalues = ['no file selected', 'no file selected', 'no file to generate', 'false', 'false', 'false', ]

print('\nHello ' + os.getlogin() + '!')
x()

main_menu = True
print_main_menu()
while main_menu:
    user_input = detect_input()

# about sub menu

    if user_input == '0':
        about_sub = True
        while about_sub:
            print_about_sub()
            x()
            print_main_menu()
            about_sub = False

# settings sub menu

    elif user_input == '1':
        settings_sub = True
        print_settings_sub()
        while settings_sub:
            user_input = detect_input()
            if user_input == '0':  # print current settings
                current_settings = True
                while current_settings:
                    index = 0
                    last_index = len(lstsettings)
                    while index < last_index:
                        print(lstsettings[index] + ' ----> ' + settingsvalues[index])
                        index += 1
                    else:
                        x()
                        print_settings_sub()
                        current_settings = False
            elif user_input == '1':  # select 1st file to use and save in settings
                file1_sub = True
                while file1_sub:
                    print('{:^40}'.format('- Importing 1st file -'))
                    print("Enter the file name")
                    user_input = detect_input()
                    try:
                        os.open(user_input + '.txt', os.O_RDONLY)
                        print('{:^40}'.format('! File access granted !'))
                        option = lstsettings.index(file1)
                        settingsvalues[option] = user_input + '.txt'
                        file1_sub = False
                    except Exception as e:
                        print(e)
                        print_settings_sub()
                        file1_sub = False
            elif user_input == '2':  # select 2nd file to use and save in settings
                file2_sub = True
                while file2_sub:
                    print('{:^40}'.format('- Importing 2nd file -'))
                    print("Enter the file name")
                    user_input = detect_input()
                    try:
                        os.open(user_input + '.txt', os.O_RDONLY)
                        print('{:^40}'.format('! File access granted !'))
                        option = lstsettings.index(file2)
                        settingsvalues[option] = user_input + '.txt'
                        file2_sub = False
                    except Exception as e:
                        print(e)
                        print_settings_sub()
                        file2_sub = False
            elif user_input == '3':  # set file to generate and save in settings
                generate_sub = True
                while generate_sub:
                    print('{:^40}'.format('- Setting up file to generate -'))
                    print("Enter the file name")
                    user_input = detect_input()
                    try:
                        os.open(user_input + '.txt', os.O_RDONLY)
                        print('{:^40}'.format('? This file already exists. Do you wish to use it: y or n ?'))
                        user_input2 = detect_input()
                        if user_input2 == 'y' or user_input == 'yes':
                            option = lstsettings.index(file_to_generate)
                            settingsvalues[option] = user_input + '.txt'
                            print('{:^40}'.format('! File already existing used !'))
                            generate_sub = False
                        if user_input2 == 'n' or user_input == 'no':
                            print('{:^40}'.format('! File creation aborted !'))
                            generate_sub = False
                    except:
                        os.open(user_input + '.txt', os.O_WRONLY | os.O_CREAT)
                        option = lstsettings.index(file_to_generate)
                        settingsvalues[option] = user_input + '.txt'
                        print('{:^40}'.format('! File successfully created !'))
                        print_settings_sub()
                        generate_sub = False
            elif user_input == '99':  # back to main menu
                print_main_menu()
                settings_sub = False
            elif user_input == '?':  # help
                print_settings_sub()
            else:  # handles bad inputs
                print('Invalid input. Try again or type ? to display the menu again')

    elif user_input == '2':  # run the program with the defined settings
        generate_sub = True
        while generate_sub:
            print('# TODO')
            x()
            generate_sub = False
            print_main_menu()

    elif user_input == '3':  # open the outputs generated into 6 different consoles for the memes
        graphic_sub = True
        while graphic_sub:
            print('# TODO')
            print('# Print Color coded wordlists')
            x()
            graphic_sub = False
            print_main_menu()

    elif user_input == '4':  # exit the loop
        Exit = True

    elif user_input == '?':  # help
        print_main_menu()

    else:  # handles bad inputs
        print('Invalid input. Try again or type ? to display the main menu again')
