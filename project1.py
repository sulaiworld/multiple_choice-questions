

def ask_question(question, options, correct_answer):
  """Asks a question and returns True if the answer is correct, False otherwise."""
  print(question)
  for idx, option in enumerate(options, 1):
    print(f"{idx}. {option}")
  while True:
    try:
      answer = int(input("Your answer (1-4): "))
      if 1 <= answer <= 4:
        break
      else:
        print("Invalid input. Please enter a number between 1 and 3.")
    except ValueError:
      print("Invalid input. Please enter a number.")
  return answer == correct_answer

def calculate_score(num_correct, num_questions):
  """Calculates and prints the score."""
  score = (num_correct / num_questions) * 100
  print(f"You got {num_correct} out of {num_questions} questions right.")
  print(f"Your score is {score:.2f}%.")

def play_quiz():
  """Plays a multi-choice quiz."""
  questions = [
      ("(Q1). What is the capital of France?", ["Rome", "Berlin", "Madrid", "Paris"], 4),
      ("(Q2). What planet is known as the red planet?", ["Earth", "Mars", "Jupiter", "Venus"], 2),
      ("(Q3). Who wrote 'To kill a Mockingbird'?", ["Harper Lee", "J.K Rowling", "George Orwell", "Ernest Hemingway"], 1),
      ("(Q4). What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], 4),
      ("(Q5). What is the chemical symbol for gold?", ["Au", "Ag", "Fe", "Hg"], 1),
      ("(Q6). Who painted the Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], 3),
      ("(Q7). Which element has the atomic number 1?", ["Oxygen", "Hydrogen", "Carbon", "Helium"], 2),
      ("(Q8). What is the smallest unit of life?", ["Organ", "Tissue", "Cell", "Molecule"], 3),
      ("(Q9). Who is known as the father of computer?", ["Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs"], 1),
      ("(Q10). Which country has the largest land mass?", ["Canada", "China", "United States of America", "Russia"], 4)
  ]
  num_correct = 0
  for question, options, correct_answer in questions:
    if ask_question(question, options, correct_answer):
      num_correct += 1
      print("Correct")
    else:
        print("incorrect")
  calculate_score(num_correct, len(questions))

play_quiz()

