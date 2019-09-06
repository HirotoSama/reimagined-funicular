# requirements
# TODO update with OS module
import os

print('This program is meant to generate a wordlist from 2 text files and allow the use to append digits')
print(' - Developped by Sote\n')


# global functions


def x():
    input('Press Enter to Continue')


def detect_input():  # detects user input
    return input('\n' + os.getlogin() + ': ')

# menus layout


def print_main_menu():
    print(40 * '_')
    print('{:^40}'.format('-Main Menu-'))
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
    print('4 > Set digits to append')
    print('5 > Set working directory')
    print('99 > back to Main Menu')


print('\nHello ' + os.getlogin() + '!')
x()

main_menu = True
print_main_menu()
while main_menu:
    user_input = detect_input()

    if user_input == '0':  # about sub menu
        about_sub = True
        while about_sub:
            print_about_sub()
            x()
            about_sub = False
            print_main_menu()

    elif user_input == '1':  # settings sub menu
        settings_sub = True
        print_settings_sub()
        while settings_sub:
            user_input = detect_input()
            if user_input == 0:
                current_settings = True
                while current_settings:
                    x()
                    print_settings_sub()
                    current_settings = False
            if user_input == '1':
                file1 = True
                while file1:
                    print('{:^40}'.format('- Importing 1st file -'))
                    print("Enter the file name with it's extension")
                    user_input = detect_input()
                    try:
                        os.open(user_input, os.O_RDONLY)
                        print('{:^40}'.format('! File access granted !'))
                        file1 = False
                    except Exception as e:
                        print(e)
                        file1 = False
            if user_input == '99':
                print_main_menu()
                settings_sub = False
            elif user_input == '?':  # help
                print_settings_sub()
            else:  # handles bad inputs
                print('Invalid input. Try again or type ? to display the main menu again')

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
