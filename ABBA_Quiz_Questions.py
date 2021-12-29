# Library ABBAQuiz
####YOU MUST DOWNLOAD BOTH THE QUIZ AND THE LIBRARY FILE FOR THE PROGRAM TO RUN####
# Functions Included in Library: 
#   question_1()
#   question_2()
#   question_3()
#   question_4()
#   question_5()
#   question_6()
# Author: Madeline Weber
# Date: 11/13/2021
# Revised: 
#   <revision date> 

# import library modules here

# Define global constants (name in ALL_CAPS)

# Function question_1()
# Description:
#   Asks the user the first question of the quiz
# Calls:
#   none
# Parameters:
#   points 
# Returns:
#   points

def question_1 ( points ):

    # Declare Local Variable types (NOT parameters)
    answer = str()

    print( '' )
    print('Question 1: What is your ideal way to spend a Saturday night?')
    print( '' )
    print('A. Watching your favorite movie with your BFF at home.')
    print('B. Dancing the night away at a nightclub')
    print('C. Playing in a high-stakes Poker match.')
    print('D. Travelling somewhere new and exploring the sights.')
    print( '' )

    answer = input('Type your answer here (A, B, etc...): ')

    while answer.upper() != 'A' and answer.upper() != 'B' and answer.upper() != 'C' and answer.upper() != 'D':
        print('Invalid user input. Please only enter letters A-D for your choice.')
        answer = input('Type your answer here: ')

        #while ends

    #if

    if answer.upper() == 'A':
        points = 1
    elif answer.upper() == 'B':
        points = 2
    elif answer.upper() == 'C':
        points = 3
    elif answer.upper() == 'D':
        points = 4

    # End if

    return points

    # Return the return variable, if any

#} Function question_1()

# Function question_2()
# Description:
#   Asks the user the second question of the quiz
# Calls:
#   none
# Parameters:
#   points 
# Returns:
#   points

def question_2 ( points ):

    # Declare Local Variable types (NOT parameters)
    answer = str()

    print( '' )
    print('Question 2: What is your ideal holiday like?')
    print( '' )
    print('A. Exploring London with your BFF')
    print('B. Dancing the night away in an Ibiza nightclub')
    print('C. All expenses paid shopping trip in Paris')
    print('D. Hiking Machu Picchu in Peru.')
    print( '' )

    answer = input('Type your answer here: ')

    while answer.upper() != 'A' and answer.upper() != 'B' and answer.upper() != 'C' and answer.upper() != 'D':
        print('Invalid user input. Please only enter letters A-D for your choice.')
        answer = input('Type your answer here: ')

        #while ends

    #if

    if answer.upper() == 'A':
        points = 1
    elif answer.upper() == 'B':
        points = 2
    elif answer.upper() == 'C':
        points = 3
    elif answer.upper() == 'D':
        points = 4

    # End if

    return points

    # Return the return variable, if any


#} Function question_2()
    
# Function question_3()
# Description:
#   Asks the user the third question of the quiz
# Calls:
#   none
# Parameters:
#   points 
# Returns:
#   points

def question_3 ( points ):

    # Declare Local Variable types (NOT parameters)
    answer = str()

    print( '' )
    print('Question 3: What do you look for in a romantic partner?')
    print( '' )
    print('A. Friendship')
    print('B. Killer dance moves')
    print('C. Confidence')
    print('D. Curiosity')
    print( '' )

    answer = input('Type your answer here: ')

    while answer.upper() != 'A' and answer.upper() != 'B' and answer.upper() != 'C' and answer.upper() != 'D':
        print('Invalid user input. Please only enter letters A-D for your choice.')
        answer = input('Type your answer here: ')

        #while ends

    #if

    if answer.upper() == 'A':
        points = 1
    elif answer.upper() == 'B':
        points = 2
    elif answer.upper() == 'C':
        points = 3
    elif answer.upper() == 'D':
        points = 4

    # End if

    return points

    # Return the return variable, if any


#} Function question_3()

# Function question_4()
# Description:
#   Asks the user the fourth question of the quiz
# Calls:
#   none
# Parameters:
#   points 
# Returns:
#   points


def question_4 ( points ):

    # Declare Local Variable types (NOT parameters)
    answer = str()

    print( '' )
    print('Question 4: How do you deal with a break-up?')
    print( '' )
    print('A. Crying and eating ice cream while watching sad movies')
    print('B. Getting your friends together and going out on the town')
    print('C. Blocking them on social media and re-installing a dating app')
    print('D. Going on a trip to find yourself')
    print( '' )

    answer = input('Type your answer here: ')

    while answer.upper() != 'A' and answer.upper() != 'B' and answer.upper() != 'C' and answer.upper() != 'D':
        print('Invalid user input. Please only enter letters A-D for your choice.')
        answer = input('Type your answer here: ')

        #while ends
        
    #if

    if answer.upper() == 'A':
        points = 1
    elif answer.upper() == 'B':
        points = 2
    elif answer.upper() == 'C':
        points = 3
    elif answer.upper() == 'D':
        points = 4

    # End if

    return points

    # Return the return variable, if any


#} Function question_4()

# Function question_5()
# Description:
#   Asks the user the fifth question of the quiz
# Calls:
#   none
# Parameters:
#   points 
# Returns:
#   points

def question_5 ( points ):

    # Declare Local Variable types (NOT parameters)
    answer = str()

    print( '' )
    print('Question 5: What is your favorite kind of book?')
    print( '' )
    print('A. A funny book you can share with your friends')
    print('B. None. You prefer more active hobbies')
    print('C. You\'ll read anything and everything')
    print('D. Travel books about exotic locations')
    print( '' )

    answer = input('Type your answer here: ')


    while answer.upper() != 'A' and answer.upper() != 'B' and answer.upper() != 'C' and answer.upper() != 'D':
        print('Invalid user input. Please only enter letters A-D for your choice.')
        answer = input('Type your answer here: ')

        #while ends

    #if

    if answer.upper() == 'A':
        points = 1
    elif answer.upper() == 'B':
        points = 2
    elif answer.upper() == 'C':
        points = 3
    elif answer.upper() == 'D':
        points = 4

    # End if

    return points

    # Return the return variable, if any


#} Function question_5()

# Function question_6()
# Description:
#   Asks the user the sixth question of the quiz
# Calls:
#   none
# Parameters:
#   points 
# Returns:
#   points

def question_6 ( points ):

    # Declare Local Variable types (NOT parameters)
    answer = str()

    print( '' )
    print('Question 6: What is your favorite hobby')
    print( '' )
    print('A. Any team sport, like soccer or baseball')
    print('B. Ballroom dancing')
    print('C. Watching TV')
    print('D. Rock climbing')
    print( '' )

    answer = input('Type your answer here: ')

    while answer.upper() != 'A' and answer.upper() != 'B' and answer.upper() != 'C' and answer.upper() != 'D':
        print('Invalid user input. Please only enter letters A-D for your choice.')
        answer = input('Type your answer here: ')

        #while ends
        
    #if

    if answer.upper() == 'A':
        points = 1
    elif answer.upper() == 'B':
        points = 2
    elif answer.upper() == 'C':
        points = 3
    elif answer.upper() == 'D':
        points = 4
    else:
        print('Invalid user input. Please only enter letters A-D for your choice.')
        answer = input('Type your answer here: ')

    # End if

    return points

    # Return the return variable, if any


#} Function question_6()


# End Module ABBAQuiz

