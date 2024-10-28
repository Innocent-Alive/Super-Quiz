from quizmanager import QuizManager
from colorama import Fore, Back

class QuizApp:
    QUIZ_FOLDER = "Quizzes"

    def __init__(self):
        self.username = ""
        self.qm = QuizManager(QuizApp.QUIZ_FOLDER)

    def startup(self):
        self.greeting()
        print("What's Your Name ? ")
        self.username = input()
        print()
        print(f"Welcome, {self.username}!")

    def greeting(self):
        print(Fore.GREEN + "~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print(Fore.GREEN + f"~~~~~~~ Welcome to SuperQuiz! ~~~~~~~~~")
        print(Fore.GREEN + "~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        # print()

    def header(self):
        print("------------------------------------")
        print("Please make a selection:")
        print("(M): Repeat this menu")
        print("(L): List Quizzes")
        print("(T): Take a Quiz")
        print("(E): Exit Program")
    def menu_error(self):
        print(Fore.RED + "That's not a valid selection. Please try again !!!")
    def goodbye(self):
        print("\n~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print(f"Thanks {self.username} for using SuperQuiz!")
        print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
    def menu(self):
        self.header()
        selection = ""
        while (True):
            selection = input(Fore.GREEN + "\nSelection ? ")
            if (len(selection)) == 0:
                self.menu_error()
                continue
            selection = selection.capitalize()
            if selection[0] == "E" or selection[0] == "Q":
                self.goodbye()
                break
            elif selection[0] == "M":
                self.header()
                continue
            elif selection[0] == "L":
                print("Available Quizzes are: ")
                self.qm.list_quizzes()
                print("-----------------------------------")
                continue
            elif selection[0] == "T":
                try:
                    quiznum = int(input("Quiz Number: "))
                    print(f"you have selected quiz {quiznum}")
                    self.qm.take_quiz(quiznum, self.username)
                    self.qm.print_results()
                    dosave = input(Fore.YELLOW + "Save the results? (y/n): ")
                    dosave = dosave.capitalize()
                    if len(dosave) > 0 and dosave == "Y":
                        self.qm.save_results()

                except:
                    self.menu_error()
            else:
                self.menu_error()

    def run(self):
        self.startup()
        self.menu()

if __name__ == "__main__":
    app = QuizApp()
    app.run()