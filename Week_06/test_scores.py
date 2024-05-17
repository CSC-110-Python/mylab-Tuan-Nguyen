print('Welcome to the test scores page. Enter 999 at any time to quit.')

total_score = 0
num_score = 0
counter = 0
score = input('Enter your score(or 999 to exit): ')
while score != '999':
    if score.isdigit():
        score = int(input(score))
        if 0<=score<=100:
            total_score += score
            num_score += 1
        else:
            print('Invalid score. Please enter number between 0-100')
    else:
        print('Invalid score')

    score = input('Enter another your score(or 999 to exit): ')

if num_score > 0:
    average = total_score / num_score
print('Your total score is {total_score}, your average score is {average}')