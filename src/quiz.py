import datetime
import sys
import random
from colorama import Fore, Back

class Quiz:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.questions = []
        self.scores = 0
        self.correct_count = 0
        self.total_points = 0
        self.completion_time = 0

    def print_header(self):
        print("\n\n**************************************")
        print(f"QUIZ NAME: {self.name}")
        print(f"DESCRIPTION: {self.description}")
        print(f"QUESTIONS: {len(self.questions)}")
        print(f"TOTAL POINTS: {self.total_points}")
        print("**************************************\n")

    def print_results(self, quiztaker, thefile = sys.stdout):
        print("\n\n**************************************", file = thefile, flush = True)
        print(f"RESULTS For '{quiztaker}' ", file = thefile, flush = True)
        print(f"DATE: {datetime.datetime.today()}", file = thefile, flush = True)
        print(f"QUIZ NAME: {self.name}", file = thefile, flush = True)
        print(f"ELAPSED TIME: {self.completion_time}", file = thefile, flush = True)
        print(f"QUESTIONS: {self.correct_count} out of {len(self.questions)} correct", file = thefile, flush = True)
        print(f"SCORE: {self.score} points out of {self.total_points} points", file = thefile, flush = True)
        print("**************************************\n", file = thefile, flush = True)

    def take_quiz(self):
        self.score = 0
        self.correct_count = 0
        self.completion_time = 0

        for q in self.questions:
            q.is_correct = False
        self.print_header()

        random.shuffle(self.questions)
        starttime = datetime.datetime.now()

        # Execute each questions and record the results
        for q in self.questions:
            q.ask()
            if(q.is_correct):
                self.correct_count += 1
                self.score += q.points
            print("\n--------------------------------------\n")

        endtime = datetime.datetime.now()

        if self.correct_count != len(self.questions):
            response = input("\nIt looks like you missed some questions. Re-do the wrong ones? (y/n) ").lower()
            print("\n")
            if response[0] == "y":
                wrong_qs = [q for q in self.questions if q.is_correct == False]
                for q in wrong_qs:
                    q.ask()
                    if(q.is_correct):
                        self.correct_count += 1
                        self.score += q.points
                    print("\n--------------------------------------\n")
                endtime = datetime.datetime.now()


        self.completion_time = endtime - starttime
        self.completion_time = datetime.timedelta(seconds = round(self.completion_time.total_seconds()))
        return (self.score, self.correct_count, self.total_points)


class Question:
    def __init__(self):
        self.points = 0
        self.correct_answer = ""
        self.text = ""
        self.is_correct = False

class QuestionTF(Question):
    def __init__(self):
        super().__init__()

    def ask(self):
        while(True):
            print(f"{self.text}")
            response = input("(T)rue or (F)alse ? ")
            if len(response) == 0:
                print(Fore.RED + "Sorry That's Not A Valid Answer. Please Try Again")
                continue
            response = response.lower()
            if response != "t" and response != "f":
                print(Fore.RED + "Sorry That's Not A Valid Answer. Please Try Again")
                continue
            if response[0] == self.correct_answer:
                self.is_correct = True
            break

class QuestionMC(Question):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while(True):
            print(self.text)
            for a in self.answers:
                print(f"({a.name}) {a.text}")
            response = input("-> ")
            if len(response) == 0:
                print(Fore.RED + "Sorry That's Not A Valid Answer. Please Try Again")
                continue
            response = response.lower()
            if response[0] == self.correct_answer:
                self.is_correct = True
            break

class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""
