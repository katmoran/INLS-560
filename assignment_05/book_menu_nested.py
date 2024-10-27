# prime the while loop 
menu_option = ''

# Outer loop, continues looping until user inputs 'q'
while menu_option != 'q':
    # Prints menu opions
    print(f'''
    Menu:
    a: view authors
    b: browse book genres
    q: exit
    ''')
    # Allows user to input a menu option, sets menu_option variable equal to user input 
    menu_option = input('Enter a letter to learn more about what books we have:')
    # If menu_option is 'a', prints this statement
    if menu_option == 'a':
        print('We have a wide range of authors including: Jane Austen, Brandon Sanderson, RF Kuang, Sally Rooney, and Sabaa Tahir.')
    # Else, if menu_option is 'b', prints this statement 
    elif menu_option =='b':
        genre_preference = input('Are you searching for a fiction book? enter (y or n):  ')
        # Response if user's answer is 'y'
        if genre_preference =='y':
            print("Great! We can help find a fiction book that interests you!")
            # Response if user's answer is 'n'
        else:
            print("Great! You can navigate our other genres such as nonfiction to find a book that interests you!")
