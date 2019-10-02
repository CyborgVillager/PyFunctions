#ask user to enter 5 scores
#display letter grade for each score adn avg test score
#must have calc_avg and return avg of the scores

#grade_total_count = 0

def main():
    grade_0 = float(input('Enter a grade number for student_0:'))


    grade_1 = float(input('Enter a grade number for student_1:'))


    grade_2 = float(input('Enter a grade number for student_2:'))


    grade_3 = float(input('Enter a grade number for student_3:'))



    grade_4 = float(input('Enter a grade number for student_4:'))



    grade_5 = float(input('Enter a grade number for student_5:'))

    grade_6 = float(input('Enter a grade number for student_6:'))

    sum_total = sum(grade_0,grade_1,grade_2,grade_3,grade_4,grade_5,grade_6)
    sum_avg = sum_total / 6

    print('The class total grade is ', sum_total, ' points' \
          'and the class avg is', sum_avg)



def sum(grade_0,grade_1,grade_2,grade_3,grade_4,grade_5,grade_6):
    result = grade_0 + grade_1 + grade_2 + grade_3 + grade_4 + grade_5 + grade_6
    return result

'''''''''
def total_avg(grade_0,grade_1,grade_2,grade_3,grade_4,grade_5,grade_6):
    combined_grade_total = sum(grade_0, grade_1 ,grade_2 ,grade_3 , grade_4 , grade_5 , grade_6)
    total_avg = combined_grade_total / grade_total_count
    print(total_avg)

total_avg(grade_0,grade_1,grade_2,grade_3,grade_4,grade_5,grade_6)
'''''''''
main()

