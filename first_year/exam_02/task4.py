# Task 4. Bob is preparing to pass IQ test. The most frequent task in this test is to 
# find out which one of the given numbers differs from the others.
# Bob observed that one number usually differs from the others in evenness. 
# Help Bob — to check his answers, he needs a program that among the given numbers 
# finds one that is different in evenness, and return a position of this number.
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means 
# indexes of the elements start from 1 (not 0)

def find_dissimilar_number(numbers: list):
  # Getting indexes of all even and odd numbers
  even_numbers = list(
    filter(
      lambda x: x, 
      [index if int(numbers[index]) % 2 == 0 else None for index in range(0, len(numbers))]
    )
  )

  odd_numbers = list(
    filter(
      lambda x: x,
      [index if int(numbers[index]) % 2 != 0 else None for index in range(0, len(numbers))]
    )
  )

  # The correct numbers are those that are more in number
  incorrect_numbers = even_numbers if len(even_numbers) < len(odd_numbers) else odd_numbers
  return incorrect_numbers

# I don't want to make tests
if __name__ == "__main__":
  # Iq-test game
  problems = [
    "2 4 7 8 10",
    "1 2 1 1",
  ]

  for i in range(0, len(problems)):
    print('-------------------------------------------------')
    print(f'{i + 1}. Find INDEX of dissimilar number(s) among this numbers: {problems[i]}')
    print('(If there are more than one dissimilar number, they should be separated by comma)')
    user_answer = input('Your answer: ')

    # Checking user answer
    answers = find_dissimilar_number(problems[i].split(' '))
    
    # Reusable
    correct_answers = ', '.join(list(map(lambda answer: str(answer + 1), answers)))

    if any(int(number) - 1 in answers for number in user_answer.split(',')):
      if all(int(number) - 1 in answers for number in user_answer.split(',')):
        print('Correct answers!')
      else:
        print(f'Partly correct answer. Correct answers: { correct_answers }')
    else:
      print(f'Wrong! Correct answers: { correct_answers }')