# IPND Stage 2 Final Project - Resubmit 1
# Dale Millar 
#2 February 2016

#This project is a fill-in-the gaps quiz with three levels of difficulty.  
#The user is initially prompted for the level she wants to attempt
#and then how many goes she wants to have at each word.
#
#We start of by declaring paragraphs (a list of the 3 paragraphs with their 
#gaps) and answers ( a list of 3 lists each containing the 4 gap-fillers).

paragraphs=['''A ___1___, is created with the def keyword. You specify the 
inputs a ___1___ takes by adding ___2___ separated by commas between the 
parentheses. ___1___s by default return ___3___ if you don't specify the value 
to return. ___2___ can be standard data types such as string, number, 
dictionary, tuple, and ___4___ or can be more complicated such as objects and 
lambda functions.''','''An ___1___ object has a fixed value. ___1___ objects 
include numbers, strings and ___2___. Such an object cannot be ___3___. 
A new ___4___ has to be created if a different value has to be stored.''',
'''___1___ is an ___2___ language (like Perl), as opposed to a ___3___ one 
(like C). This means that the source files can be run directly without first 
creating an executable which is then run. ___2___ languages typicaly have a 
shorter development/debug cycle than ___3___ ones, though their programs 
generally also run more ___4___.''']

answers=[['function','arguments','None','list'],
        ['immutable','tuples','altered','object'],
        ['Python','interpreted','compiled','slowly']]

def transformer(paragraph,word,question):
        """
        transformer(paragraph,word,question) returns a paragraph with a blank 
        removed and a filler inserted.
        inputs: paragraph with blanks, a new filler word and the number of the 
        question being addressed (ie the number of the blank)
        """           
        new_paragraph=paragraph.replace("___"+str(question+1)+"___",word)
        return new_paragraph

def starter_level():
        """
        starter_level() takes user input on the level she wants to play and 
        returns an integer indicating the level.
        inputs: nil
        outputs: integer indicating level
        """
        choices=['easy','medium','hard']
        level_choice=raw_input('''Please select a level of difficulty 
                (easy, medium or hard): ''')
        level_choice=level_choice.lower().strip(' ')
        while level_choice not in choices:
                level_choice=raw_input('''Sorry you have to input easy, 
                        medium or hard: ''')
        print "You've chosen "+level_choice
        if level_choice=='easy':
                level=0
        elif level_choice=='medium':
                level=1
        elif level_choice=='hard':
                level=2
        return level        

def starter_attempts():
        """
        starter_attempts() takes user input on the attemts she wants to have and 
        returns an integer indicating the number.
        inputs: nil
        outputs: integer indicating number of attempts.
        """
        attempts=raw_input('''How many goes would you like at filling in each 
                gap? (Please enter a positive integer (eg 1): ''')
        attempts=int(attempts)
        while attempts<1:
                attempts=raw_input("Please type in a positive integer: ")
                attempts=int(attempts)
        return attempts

def questioner(level,attempts):
        """
        questioner(level,attempts) prompts the user for answers. If correct, 
        transformer is called to insert the answer into the paragraph, 
        if not, messages aredispayed indicating failure or prompting another 
        attempt.
        inputs: integers indicating level of play and number of attempts 
        requested.
        outputs: nil
        """
        print '''Here is an incomplete paragraph; check it out and get ready to 
                fill in the numbered gaps:'''
        print paragraphs[level]
        question_number,counter,paragraph=0,attempts,paragraphs[level]
        while question_number<=3 and counter>0:
                answer=raw_input("What's the required word in gap " 
                        + str(question_number+1)+" :")
                if answer==answers[level][question_number]:
                        print "That's right!"
                        paragraph =transformer(paragraph,answer,question_number)
                        question_number +=1
                        print paragraph
                        counter=attempts
                else: 
                        counter=counter-1
                        messenger(counter)
                          
def messenger(counter):
        """
        messenger(counter) provides a tailored messaging service to questioner 
        when the user inputs a incorrect answer.  
        The counter variable indicates how manyattempts the user has had.
        inputs: integer indicating how many attempts have been used.
        """        
        messages=['''Sorry, you failed - better luck next time!''',
        '''Incorrect.  You've only got 1 attempt left. Try again: ''',
        '''Sorry, incorrect. You've got '''+str(counter)+''' attempts left: ''']
        if counter>1:
                print messages[len(messages)-1]
        else:
                print messages[counter]        

questioner(starter_level(),starter_attempts())




