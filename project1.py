def ask_question(question, options, correct_answer):
  """Asks a multiple-choice question and returns True if the answer is correct."""
  print(question)
  for idx, option in enumerate(options, 1):
   print(f"{idx}. {option}")
  user_answer = int(input("Your answer (enter the correct number): "))

  return user_answer == correct_answer
def keep_score(questions, pass_mark):
  """Runs the quiz and keeps track of the score."""
  score = 0
  for question, options, correct_answer in questions:
    if ask_question(question, options, correct_answer):
      score += 1
      print("Correct!\n")
    else:
      print(f"Incorrect. The answer was: {options[correct_answer]}\n")

  print(f"You got {score} out of {len(questions)} questions right.")
  if (score / len(questions)) * 100 >= pass_mark:
    print("Congratulations, you passed!")
  else:
    print("You did not reach the pass mark. You failed kindly retake course in 24hrs.")

def main():
  """Defines the quiz questions and starts the quiz."""
  questions = [
      ("Which programming language are we working on ?", ["C++", "Python", "Javascript"], 2),
      ("How do make a python directory?", ["mkdir", "mkdr", "makedirs"], 1),
      ("How do you create multiple directories in python?", ["mkdir", "mkdr", "makedirs"], 3),

  ]
  pass_mark = 60  # Set the pass mark percentage

  keep_score(questions, pass_mark)

if __name__ == "__main__":
  main()
