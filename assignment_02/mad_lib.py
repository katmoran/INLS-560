# Mad Lib example for functions. 

def madlib(verb_1, adjective_1, noun_1, adjective_2, noun_2, noun_3, adjective_3, noun_4, verb_2):
    '''Mad lib function''' # Docstring must be indented 
    story =f'''
Today, I decided to {verb_1} to the ice cream shop with my best friend. 
We were so excited because we had been craving {adjective_1} ice cream 
for weeks. As soon as we walked in, the smell of {noun_1} filled the air. 
The shop was full of colorful {adjective_2} tubs of ice cream. We quickly chose
 our favorite flavors: {noun_2} and {noun_3} After ordering, we sat down to 
 enjoy our {adjective_3} treats. Suddenly, we saw a huge {noun_4} walk in, 
 and we couldn't stop {verb_2} about it!
''' 
    
    return story 


def get_user_input(): 
    """Prompt the user for input for the mad lib"""
    verb_1 = input("Enter verb: ")
    adjective_1 = input("Enter adj: ")
    noun_1 = input("Enter noun: ")
    adjective_2 = input("Enter adj: ")
    noun_2 = input("Enter noun: ")
    noun_3 = input("Enter noun: ")
    adjective_3 = input("Enter adj: ")
    noun_4 = input("Enter noun: ")
    verb_2 = input("Enter verb: ")

    return verb_1, adjective_1, noun_1, adjective_2, noun_2, noun_3, adjective_3, noun_4, verb_2


