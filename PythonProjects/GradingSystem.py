#Programmed by: Malachi McCloud
#Compute Grades with a weighted average.

def main():#Establish the main
    
    #4 Students, 3 Grades, Weights for Grades Loop to ask for grades once completed print the student with the highest graddes

    #Establish students starting points
    Mark = 0
    Sally = 0
    Tim = 0
    Betty = 0

    #Establish loop variable assignment
    assignment = 0
    #============================Prompt for info================================================
    while assignment == 0:
        MarkDiscussion = float(input("Enter Mark's score on the discussion board."))
        SallyDiscussion = float(input("Enter Sally's score on the discussion board."))
        TimDiscussion = float(input("Enter Tim's score on the discussion board."))
        BettyDiscussion = float(input("Enter Betty's score on the discussion board."))
        assignment = (assignment + 1)
        break
    
    while assignment == 1:
        MarkQuiz = float(input("Enter Mark's score on the quiz."))
        SallyQuiz = float(input("Enter Sally's score on the quiz."))
        TimQuiz = float(input("Enter Tim's score on the quiz."))
        BettyQuiz = float(input("Enter Betty's score on the quiz."))
        assignment = (assignment + 1)
        break

    while assignment == 2:
        MarkProgrammingAsg = float(input("Enter Mark's score on the Programming Assignment."))
        SallyProgrammingAsg = float(input("Enter Sally's score on the Programming Assignment."))
        TimProgrammingAsg = float(input("Enter Tim's score on the Programming Assignment."))
        BettyProgrammingAsg = float(input("Enter Betty's score on the Programming Assignment."))
        assignment = (assignment + 1)
        break

    #=============================End Prompts====================================================
    while assignment == 3:
        #Create totals
        #Grades are weighted at .2 Discussion .3 Quiz and .5 ProgrammingAsg
        Mark = ((MarkDiscussion * .2)+(MarkQuiz * .3)+(MarkProgrammingAsg * .5))
        Sally = ((SallyDiscussion * .2)+(SallyQuiz * .3)+(SallyProgrammingAsg * .5))
        Tim = ((TimDiscussion * .2)+(TimQuiz * .3)+(TimProgrammingAsg * .5))
        Betty = ((BettyDiscussion * .2)+(BettyQuiz * .3)+(BettyProgrammingAsg * .5))
        grades = [Mark, Sally, Tim, Betty]
        max_grade = max(grades)#Find the max grade
        #======================If statements to check for who has the highest grade to print their name and grade==========
        if Mark == max_grade:
            print("Mark had the highest grade at", max_grade)
        if Sally == max_grade:
            print("Sally had the highest grade at", max_grade)
        if Tim == max_grade:
            print("Tim had the highest grade at", max_grade)
        if Betty == max_grade:
            print("Betty had the highest grade at", max_grade)
        #=====================End if statements===========================================================
        assignment = (assignment + 1) #Dont allow for an endless loop
main()#Run the main
