from random import choice

d = {
    'Q1': ["Q 1) Which of the following is not a data type in Python?",
           "A) address", "B) int", "C) float", "D) none"],

    'Q2': ["Q 2) Which datatype is mutable in Python?",
           "A) string", "B) int", "C) tuple", "D) list"],

    'Q3': ["Q 3) What is the output of print(type(10.5))?",
           "A) <class 'int'>", "B) <class 'float'>",
           "C) <class 'bool'>", "D) <class 'none'>"],

    'Q4': ["Q 4) List is:",
           "A) mutable", "B) immutable", "C) function", "D) none"],

    'Q5': ["Q 5) Dictionary is:",
           "A) collection of key-value pairs",
           "B) collection of keys",
           "C) collection of values",
           "D) collection of elements"],

    'Q6': ["Q 6) Which keyword is used to define a function?",
           "A) function", "B) def", "C) fun", "D) define"],

    'Q7': ["Q 7) Recursion means:",
           "A) function calling itself",
           "B) function calling another function",
           "C) function calling a variable", "D) none"],

    'Q8': ["Q 8) What is the output of type([1, 2, 3])?",
           "A) <class 'list'>", "B) <class 'tuple'>",
           "C) <class 'set'>", "D) <class 'dict'>"],

    'Q9': ["Q 9) What is the output of type((1, 2, 3))?",
           "A) <class 'list'>", "B) <class 'tuple'>",
           "C) <class 'set'>", "D) <class 'dict'>"],

    'Q10': ["Q 10) What is the output of type({1, 2, 3})?",
            "A) <class 'list'>", "B) <class 'tuple'>",
            "C) <class 'set'>", "D) <class 'dict'>"]
}

anslist = ["A", "D", "B", "A", "A", "B", "A", "A", "B", "C"]

score = 0

l = list(d.keys())

for i in range(len(d)):

    x = choice(l)

    print("\n", d[x][0])

    for j in range(1, 5):
        print(d[x][j])

    answer = input("Enter your answer (A/B/C/D): ").upper()
    if answer=="a" or answer=="b" or answer=="c" or answer=="d":
        pass
    else:
        print("Invalid input. Please enter A, B, C, or D.")
        continue
    index = int(x[1:]) - 1

    if answer == anslist[index]:
        print("Correct answer!")
        score += 1

    else:
        print("Incorrect answer!")
        print("Correct answer:", anslist[index])

    l.remove(x)

print("\nYour final score:", score, "/", len(d))
