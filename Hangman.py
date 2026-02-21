import random

def hangman():
    
    words = ["PYTHON", "JAVA", "PROGRAMMING", "DEBUGGING", "BUGS", "COMPILER", "LINKER", "CODE", "LOADER", "ASSEMBLER", "SYNTAX", "ARRAYS", "DICTIONARIES", "LISTS", "TUPLES", "SETS", "DATA", "ARGUMENT", "STRING", "BOOLEAN", "ERROR", "LOOP", "FUNCTION", "DEVELOPER", "ALGORITHM", "FLOWCHART", "ARGUMENT", "BINARY", "COMMENTS", "CONDITIONALS", "INPUT", "OUTPUT", "LIBRARY", "BACKEND", "FRONTEND", "COMMAND", "FRAMEWORK", "SERVER", "STACK", "INTERFACE", "INTEGRATE", "LINTER", "LINUX", "CACHE", "MEMORY", "PROCESSOR", "LANGUAGE", "SOFTWARE", "HARDWARE"]
    chosen_word = random.choice(words)

    display = "_" * len(chosen_word)
    guessed_words = []
    Total_Attempts = 6
    print("WELCOME TO HANGMAN!")
    print("TOTAL ATTEMPTS: ",Total_Attempts)

hangman()