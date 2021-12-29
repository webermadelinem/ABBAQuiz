# Program ABBA Quiz
# Description: 
#   This program asks the user to answer questions in order to determine which
#   ABBA song they are most similar to. It relies on conventions of personality
#   quizzes in order to determine what song they are similar to and why.
#### YOU MUST DOWNLOAD BOTH THE QUIZ AND THE LIBRARY FILE FOR THE PROGRAM TO RUN ####
#### The library file is under ABBA Quiz Questions ####
# Author: Madeline Weber 
# Date: 11/05/21
# Revised: 
#   <revision date>

# import library modules here
import ABBA_Quiz_Questions
import os

# Define global constants (name in ALL_CAPS)


def main():

    # Declare Variable types (EVERY variable used in this main program)
    total = int()
    history_question = str()
    start_quiz = str()
    points_1 = int()
    points_2 = int()
    points_3 = int()
    points_4 = int()
    points_5 = int()
    points_6 = int()

    intro_screen()

    history_question = input('Would you like some background history on ABBA before we start? Y/N: ')

    while history_question.upper() != 'Y' and history_question.upper() != 'N':
        print( 'Invalid user input. Please only enter Y/N to proceed.' )
        print( 'Please try again. ')
        history_question = input('Would you like some background history on ABBA before we start? Y/N: ')

    # if
    if history_question.upper() == 'Y':
        history()
    else:
        pass
    # End if

    points_1 = 0
    points_2 = 0
    points_3 = 0
    points_4 = 0
    points_5 = 0
    points_6 = 0

    start_quiz = input('Shall we begin the quiz? Y/N: ')
    os.system('cls')

    while start_quiz.upper() != 'Y' and start_quiz.upper() != 'N':
        print( ' Invalid user input. Please try again, using only Y/N.')
        start_quiz = input('Shall we begin the quiz? Y/N: ')

       #while
        
    # if
    
    if start_quiz.upper() == 'Y':
        points_1 = ABBA_Quiz_Questions.question_1( points_1 )
        points_2 = ABBA_Quiz_Questions.question_2( points_2 )
        points_3 = ABBA_Quiz_Questions.question_3( points_3 )
        points_4 = ABBA_Quiz_Questions.question_4( points_4 )
        points_5 = ABBA_Quiz_Questions.question_5( points_5 )
        points_6 = ABBA_Quiz_Questions.question_6( points_6 )
        total = ( points_1 ) + ( points_2 ) + ( points_3 ) + ( points_4 ) + ( points_5 ) + ( points_6 )
        
        # if
        if total <= 8:
            chiquitita()
        elif total <= 15 and total >= 9:
            dancing_queen()
        elif total <= 20 and total >= 16:
            gimmie_gimmie_gimmie()
        elif total >= 21:
            fernando()
            
        # End if
        outro_screen()

    elif start_quiz.upper() == 'N':
        print('No worries. In the meantime, I suggest listening to ABBA\'s greatest hits!')

    # End if
        
# Function intro_screen()
# Description:
#   Gives the user basic information about the quiz
# Calls:
#   none
# Parameters:
#  none
# Returns:
#   none

def intro_screen():
    # Declare Variable types (EVERY variable used in this main function)

    print('Welcome to the \'Which ABBA Song Are You?\' Quiz!' )
    print('')
    print( 'There is an ABBA song for every occasion, but which one says the most about you?' )
    print( '' )
    print( 'Answer these questions to discover which ABBA song you really are!' )
    print( 'Don\'t worry, you don\'t need to have ABBA knowledge,')
    print( 'or be familiar with their music to take the quiz.' )
    print( '' )
    print( 'There will be a total of 6 questions,' )
    print( 'and you can retake the quiz as many times as you like!' )
    print( '' )
    
#} Function intro_screen()

# Function history()
# Description:
#   Gives the user basic history about ABBA
# Calls:
#   none
# Parameters:
#  none
# Returns:
#   none

def history():
    # Declare Variable types (EVERY variable used in this main function)
    more = str()

    print( '' )
    print( 'Thank you for wanting to learn more about ABBA!')
    print( '' )
    print( 'The ABBA story began in Stockholm, Sweden, and includes members Benny Andersson,' )
    print( 'Björn Ulvaeus, Agnetha Fältskog, and Anni-Frid “Frida” Lyngstad.')
    print( 'The group\'s name is actually an acronym of the first letters of their first names')
    print( ' arranged as a palindrome.' )
    print( '' )
    print( 'ABBA is widely considered one of the greatest musical groups of all time,')
    print( 'topping the charts worldwide from 1974 to 1983, and in 2021.' )
    print( 'ABBA have achieved 48 hit singles throughout the course of their career.' )
    print( '' )

    more = input('Would you like to learn even more? Y/N: ')

    #if
    
    if more.upper() == 'Y':
        more_history()

    elif more.upper() != 'Y' and more.upper() != 'N':
        print('Error message - invalid user input. Please try again, only answering with Y or N')
        more = input('Would you like to learn even more? Y/N: ')

    elif more.upper() == 'N':
        pass

    #if ends

#} Function history()

# Function more_history()
# Description:
#   Gives the user more history about ABBA
# Calls:
#   none
# Parameters:
#  none
# Returns:
#   none

def more_history():
    # Declare Variable types (EVERY variable used in this main function)
    
    print( '' )
    print( 'In 1974, ABBA were Sweden\'s first winner of the Eurovision Song Contest')
    print( 'with the song "Waterloo", which shot the group to fame.' )
    print( 'During the band\'s prime years, the group consisted of two married couples: ')
    print( 'Fältskog and Ulvaeus, and Lyngstad and Andersson.' )
    print( 'However, as the band\'s fame grew, the strain on the couples\' marriages grew worse,')
    print( 'until both couples broke up.' )
    print( '' )
    print( 'The band eventually seperated in December of 1982.')
    print( '' )
    print( 'Ten years after the group broke up, a compilation, \'ABBA Gold\', was released,' )
    print( 'becoming a worldwide hit.' )
    print( 'In 1999, ABBA\'s music was adapted into \'Mamma Mia!\', a widely successful musical ' )
    print( 'that toured worldwide and became one of the longest running musicals in both Broadway' )
    print( 'and the West End.' )
    print( 'A film of the same name became the highest-grossing film in the United Kingdom in 2008.' )
    print( 'A sequel, \'Mamma Mia! Here We Go Again\', was released in 2018.' )
    print( '' )
    print( 'In 2016, the group reunited and started working on a digital avatar concert tour!' )
    print( '\'Voyage\', their first new album in 40 years, was released on November 5, 2021.' )
    print( 'Today, ABBA are regarded as one of the classic pop acts of all time, acknowledged' )
    print( 'by their 2010 induction into the Rock And Roll Hall Of Fame.' )
    print( ' ' )

#} Function more_history()

# Function outro_screen()
# Description:
#   Thanks the user for playing and asks if they want to play again
# Calls:
#   none
# Parameters:
#  none
# Returns:
#   none
           
def outro_screen():
    # Declare Variable types (EVERY variable used in this main function)
    play_again = str()

    print( ' ')
    print( 'Thank you for taking the \'Which ABBA Song Are You?\' Quiz!' )
    
    play_again = input('Would you like to take the quiz again? Y/N: ' )

    while play_again.upper() != 'Y' and play_again.upper() != 'N':
        print( 'Invalid user input. Please try again.' )
        play_again = input( 'Would you like to take the quiz again? Y/N: ' )

        #while ends
        
    if play_again.upper() == 'Y':
        os.system('cls')
        main()
    elif play_again.upper() == 'N':
        print( 'Goodbye!' )

    #if

#} Function outro_screen()

# Function chiquitita()
# Description:
#   Gives the user their answer
# Calls:
#   none
# Parameters:
#  none
# Returns:
#   none
def chiquitita():
    # Declare Variable types (EVERY variable used in this main function)

    print( '' )
    print( 'You are....' )
    print( '' )
    print( '\'Chiquitita\'!' )
    print( '' )
    print( 'You care so much about friendship and the feelings of others.' )
    print( 'Just like in the song, you always go out of your way to make sure' )
    print( 'your friends are feeling good and taken care of.' )
    print( '' )
    
#} Function chiquitita()

# Function dancing_queen()
# Description:
#   Gives the user their answer
# Calls:
#   none
# Parameters:
#  none
# Returns:
#   none

def dancing_queen():
    
    # Declare Variable types (EVERY variable used in this main function)

    print( '' )
    print( 'You are...' )
    print( '' )
    print( '\'Dancing Queen\'!' )
    print( '' )
    print( 'You are high energy and love to dance.' )
    print( 'You always know how to have a good time and exude fun.' )
    print( '' )
    
#} Function dancing_queen()

# Function gimmie_gimmie_gimmie()
# Description:
#   Gives the user their answer
# Calls:
#   none
# Parameters:
#  none
# Returns:
#   none

def gimmie_gimmie_gimmie():
    
    # Declare Variable types (EVERY variable used in this main function)

    print( '' )
    print( 'You are...' )
    print( '' )
    print( '\'Gimmie! Gimmie! Gimmie! (A Man After Midnight\)!' )
    print( '' )
    print( 'You are confident and go after what you want in life.' )
    print( 'You are ambitious and hardworking, but love to have fun too.' )
    print( '' )

#} Function gimmie_gimmie_gimmie()

# Function fernando()
# Description:
#   Gives the user their answer
# Calls:
#   none
# Parameters:
#  none
# Returns:
#   none

def fernando():

    # Declare Variable types (EVERY variable used in this main function)

    print( '' )
    print( 'You are...' )
    print( '' )
    print( '\'Fernando\'!' )
    print( '' )
    print( 'You love to travel and are extremely curious.' )
    print( 'You enjoy being in nature and don\'t mind being alone.' )
    print( '' )

#} Function fernando()

# End program

main()    
