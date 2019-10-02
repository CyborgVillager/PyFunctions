a = float(input('Enter a score for test A: '))
b = float(input('Enter a score for test B: '))
c = float(input('Enter a score for test C: '))
d = float(input('Enter a score for test D: '))
f = float(input('Enter a score for test F: '))

def calc_class_average(a, b, c, d, f):
    average = (a + b + c + d + f) / 5

    return average

def get_grade_from_class(a, b, c, d, f):
    for grade in a, b, c, d, f:
        if 90 <= grade:
            print('The grade of', grade, 'is A')
        elif 80 <= grade and grade <= 89:
            print('The grade of', grade, 'is B')
        elif 70 <= grade and grade <= 79:
            print('The grade of', grade, 'is C')
        elif 60 <= grade and grade <= 69:
            print('The grade of', grade, 'is D')
        elif grade < 60:
            print('The grade of', grade, 'is F')
average = calc_class_average(a, b, c, d, f)
print('The average of your class scores is', average)

get_grade_from_class(a, b, c, d, f)