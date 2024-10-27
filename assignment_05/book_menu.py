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
    
    elif menu_option =='b':
        print('We have fiction, nonfiction, poetry, graphic novels, and biographies. Please view our popular authors under each genre on our website.')