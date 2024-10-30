<pre>
<h1>Super Quiz </h1>
Super Quiz is a Python-based quiz application that allows users to take interactive quizzes with various question types, 
such as multiple-choice and true/false questions. The quizzes are stored as XML files in a designated Quizzes folder. 
The program offers a smooth user experience with the ability to retry incorrect questions and save quiz results to text files.

<h2>Features </h2>
<h3>Multiple Question Types: </h3>
Multiple Choice (MC)
True/False (TF)

<h3>Quiz Management: </h3>
List available quizzes dynamically from the Quizzes folder.
Automatically parse quizzes from XML files.

<h3>Interactive Experience: </h3>
Tracks and displays score and completion time.
Option to retry incorrect questions.

<h3>Results Management: </h3>
View quiz results at the end.
Option to save results as a text file for future reference.

<h2>Project Structure </h2>

SuperQuiz/
│
├── main.py                 # Entry point to run the application
├── quiz.py                 # Contains quiz logic, question classes, and scoring
├── quizparser.py           # Handles parsing of quiz data from XML files
├── quizmanager.py          # Manages quizzes, results, and interaction with the user
├── Quizzes/                # Folder containing XML quizzes with questions and answers
│   └── MyQuiz.xml          # Example quiz file (replace or add your own)
└── README.md               # Project documentation (this file)

<h2>XML Quiz File Format </h2>
Each quiz is represented by an XML file within the Quizzes/ folder. Below is a sample structure of a quiz XML file:

QuizML: Root tag for a quiz. name attribute defines the quiz title.
Description: Brief summary of the quiz.
Question: Contains a question of type "tf" (True/False) or "multichoice".
QuestionText: Defines the question text and the correct answer.
Answer: Contains possible answers for multiple-choice questions.

<h2>Installation and Setup </h2>
Clone the repository:
git clone https://github.com/your-username/SuperQuiz.git
cd SuperQuiz
Install Dependencies: This project requires Python 3.x and the colorama library for colored text in the terminal.
pip install colorama

<h2>Add Your Quizzes: </h2>
Place XML quiz files inside the Quizzes/ folder.
Follow the sample XML format to create your own quizzes.

<h2>How to Run </h2>
Open a terminal and navigate to the SuperQuiz project directory.

Run the application using:
python main.py
Follow the on-screen instructions to:
List available quizzes.
Take a quiz.
Save results.

<h2>Example Usage </h2>
Startup: Enter your name to begin.

Menu Options:

(L): List available quizzes.
(T): Take a quiz by entering its number.
(M): Display the menu again.
(E): Exit the program.
During the Quiz:

True/False questions: Answer with T or F.
Multiple-choice questions: Enter the corresponding letter (e.g., A, B).

<h2>Saving Results </h2>
After completing a quiz, you can choose to save your results.
The results will be saved as a QuizResults_YYYY_MM_DD.txt file in the current directory.

<h2>Example Output </h2>
**************************************
QUIZ NAME: General Knowledge Quiz
DESCRIPTION: A quiz to test your general knowledge.
QUESTIONS: 2
TOTAL POINTS: 15
**************************************

The Earth is round.
(T)rue or (F)alse ? T

--------------------------------------

What is the capital of France?
(a) Paris
(b) Berlin
(c) Madrid
(d) Rome
-> a

--------------------------------------

**************************************
RESULTS For 'John Doe'
DATE: 2024-10-30 12:34:56.789123
QUIZ NAME: General Knowledge Quiz
ELAPSED TIME: 0:00:15
QUESTIONS: 2 out of 2 correct
SCORE: 15 points out of 15 points
**************************************
</pre>
