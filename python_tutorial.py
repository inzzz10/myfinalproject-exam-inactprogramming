# ==========================================================
#  FINAL EXAM PROJECT: PYTHON TUTORIAL PROGRAM
#  Lesson 1 = Introduction to Programming (print, comments, input/output)
#  Lesson 2 = Basic Syntax (variables, data types, if-else, loops)
#  Lesson 3 = Arithmetic Operators (arithmetic, comparison, logical)
#  Lesson 4 = Quiz, 
#           = Exit
# ==========================================================

running = True                      # keeps the menu going

while running:
    print("\n==== PYTHON TUTORIAL ====")
    print()
    print("1. INTRODUCTION TO PROGRAMMING")
    print("2. BASIC SYNTAX")
    print("3. ARITHMETIC OPERATORS")
    print("4. QUIZ")
    print("5. EXIT")
    print()
    choice = input("choose lesson: ")

    # ================= LESSON 1: INTRODUCTION TO PROGRAMMING =================
    if choice == "1":
        print("\n--- LESSON 1: INTRODUCTION TO PROGRAMMING ---")
        print("Programming means telling a computer what to do.")
        print("Python is a computer language. It is easy to read and learn.")
        print("A program does 3 things: it takes INPUT, it works on it, and it shows OUTPUT.")
        print()

        print("1. print() shows words or numbers on the screen.")
        print('     print("Hello, World!")')
        print("   - Words (text) need quote marks.")
        print("   - Numbers do NOT need quote marks:  print(100)")
        print('   - Use a comma to show many things:  print("Age:", 18)')
        print()

        print("2. Python does not read comments. They are notes about the code.")
        print("     # This is a one-line comment")
        print('     """ This is a')
        print('         many-line comment """')
        print()

        print("3. input() asks the user to type something:")
        print('     name = input("Type your name: ")')
        print("   IMPORTANT: input() always gives text (str)!")
        print("   Use int() to change it to a whole number, or float() for a number with a dot:")
        print('     age = int(input("Type your age: "))')
        print()

        print("4. An f-string puts a variable inside words (put f before the quote marks):")
        print('     print(f"Student: {name}, Age: {age}")')
        print()

        # Try it: input and output
        name = input("Try it! Type your name: ")
        while name == "":                                   # CHECK: name is empty
            print("Error: Please type your name.")
            name = input("Try it! Type your name: ")

        valid = False
        while valid == False:
            text = input("Type your age: ")
            if text.isdigit():                              # CHECK: numbers only
                age = int(text)                             # change text to a whole number
                valid = True
            else:
                print("Error: Please type a whole number for your age.")

        print("Using a comma :", name, age)
        print(f"Using f-string: Student: {name}, Age: {age}")

    # ====================== LESSON 2: BASIC SYNTAX ======================
    elif choice == "2":
        print("\n--- LESSON 2: BASIC SYNTAX ---")

        # ----- Indentation -----
        print("\n[A] INDENTATION")
        print("Python uses spaces at the start of a line to group code. This is called indentation.")
        print("  CORRECT:                 INCORRECT:")
        print("  if age >= 18:            if age >= 18:")
        print('      print("Adult")        print("Adult")   <- no spaces (wrong)')
        input("\nPress Enter to continue...")

        # ----- Variables and data types -----
        print("\n[B] VARIABLES AND DATA TYPES")
        print("A variable is a box with a name. It keeps a value.")
        print('     name = "Maria"')
        print("     age = 20")
        print("Rules for variable names:")
        print("  - start with a letter or an underscore (_)")
        print("  - do not start with a number (1name is wrong)")
        print("  - no spaces and no special signs (my name and @name are wrong)")
        print("  - small and big letters are different (age and AGE are two different variables)")
        print("Data types:")
        print("  int   -> whole numbers      (10, 25, -7)")
        print("  float -> numbers with a dot (3.14, 2.0)")
        print('  str   -> text               ("Hello")')
        print("  bool  -> True or False")
        print()

        word = input("Try it! Type any words: ")
        number = 25
        decimal = 3.14
        flag = True
        print("word    =", word, "-> type:", type(word))
        print("number  =", number, "-> type:", type(number))
        print("decimal =", decimal, "-> type:", type(decimal))
        print("flag    =", flag, "-> type:", type(flag))
        input("\nPress Enter to continue...")

        # ----- Conditional statements -----
        print("\n[C] MAKING CHOICES (if, if-else, if-elif-else)")
        print("A condition is True or False. The program uses it to make a choice.")
        print("  if        -> runs the code only if the condition is True")
        print("  if-else   -> picks one of TWO things to do")
        print("  if-elif-else -> picks one of THREE or more things to do")
        print("Example:")
        print("  if score >= 90:")
        print('      print("Excellent")')
        print("  elif score >= 80:")
        print('      print("Very Good")')
        print("  elif score >= 75:")
        print('      print("Passed")')
        print("  else:")
        print('      print("Failed")')
        print("Python checks from top to bottom. It runs the FIRST one that is True.")
        print()

        valid = False
        while valid == False:
            text = input("Try it! Type a score (0 to 100): ")
            if text.isdigit():
                score = int(text)
                if score >= 0 and score <= 100:             # CHECK: number is in range
                    valid = True
                else:
                    print("Error: Score must be from 0 to 100.")
            else:
                print("Error: Score must be a whole number.")

        if score >= 90:
            print("Excellent")
        elif score >= 80:
            print("Very Good")
        elif score >= 75:
            print("Passed")
        else:
            print("Failed")
        input("\nPress Enter to continue...")

        # ----- Loops -----
        print("\n[D] LOOPS (REPEATING)")
        print("A loop repeats code. You do not need to write the same code many times.")
        print("  for loop   -> use it when you know how many times to repeat")
        print("     for number in range(1, 6):")
        print("         print(number)")
        print("     range(1, 6) gives 1, 2, 3, 4, 5  (the last number, 6, is NOT included)")
        print()
        print("  while loop -> repeats as long as the condition is True")
        print("     count = 1")
        print("     while count <= 5:")
        print("         print(count)")
        print("         count += 1        # same as count = count + 1")
        print()

        valid = False
        while valid == False:
            text = input("Try it! Type a number from 1 to 10: ")
            if text.isdigit():
                limit = int(text)
                if limit >= 1 and limit <= 10:              # CHECK: number is in range
                    valid = True
                else:
                    print("Error: Number must be from 1 to 10.")
            else:
                print("Error: Please type a whole number.")

        print("\nUsing a for loop:")
        for number in range(1, limit + 1):
            print(number)

        print("\nUsing a while loop:")
        count = 1
        while count <= limit:
            print(count)
            count += 1

    # ================= LESSON 3: ARITHMETIC OPERATORS =================
    elif choice == "3":
        print("\n--- LESSON 3: ARITHMETIC OPERATORS ---")

        # ----- Arithmetic operators -----
        print("\n[A] ARITHMETIC OPERATORS (used for math)")
        print("  +   Addition          5 + 3   = 8")
        print("  -   Subtraction      10 - 4   = 6")
        print("  *   Multiplication    7 * 2   = 14")
        print("  /   Division (with dot) 15 / 3 = 5.0")
        print("  //  Floor division (whole number) 17 // 3 = 5")
        print("  %   Remainder (what is left) 10 % 3 = 1")
        print("  **  Power (exponent)  2 ** 3  = 8")
        print()
        print("Python does math in this order (PEMDAS):")
        print("  Parentheses, Exponents, Multiplication, Division, Addition, Subtraction")
        print("  Example: 2 + 3 * 4 = 14   (multiply first)")
        print()

        print("Now you try! Type two whole numbers.")

        valid = False
        while valid == False:
            text = input("First number : ")
            if text.isdigit():                              # CHECK: numbers only
                num1 = int(text)
                valid = True
            else:
                print("Error: '" + text + "' is not a whole number. Please try again.")

        valid = False
        while valid == False:
            text = input("Second number: ")
            if text.isdigit():
                num2 = int(text)
                valid = True
            else:
                print("Error: '" + text + "' is not a whole number. Please try again.")

        print("\nResults:")
        print("Sum        :", num1 + num2)
        print("Difference :", num1 - num2)
        print("Product    :", num1 * num2)

        if num2 != 0:                                       # CHECK: no dividing by zero
            print("Quotient   :", num1 / num2)
            print("Floor div  :", num1 // num2)
            print("Remainder  :", num1 % num2)
        else:
            print("Error: You cannot divide by zero! (Quotient, Floor div, and Remainder are skipped)")

        if num2 > 1000:                                     # CHECK: number is not too big
            print("Error: The power number is too big (use 1000 or less).")
        else:
            print("Power      :", num1 ** num2)
        input("\nPress Enter to continue...")

        # ----- Comparison (relational) operators -----
        print("\n[B] COMPARISON OPERATORS (the answer is True or False)")
        print("  ==  equal to              !=  not equal to")
        print("  >   greater than          <   less than")
        print("  >=  greater than or equal to   <=  less than or equal to")
        print()
        print("Using your numbers:", num1, "and", num2)
        print(num1, "==", num2, ":", num1 == num2)
        print(num1, "!=", num2, ":", num1 != num2)
        print(num1, ">", num2, ":", num1 > num2)
        print(num1, "<", num2, ":", num1 < num2)
        print(num1, ">=", num2, ":", num1 >= num2)
        print(num1, "<=", num2, ":", num1 <= num2)
        input("\nPress Enter to continue...")

        # ----- Logical operators -----
        print("\n[C] LOGICAL OPERATORS (join conditions)")
        print("  and -> True only if ALL conditions are True")
        print("  or  -> True if ONE or MORE conditions are True")
        print("  not -> flips the answer (True becomes False)")
        print()
        print("  True  and True  = True    True  or True  = True    not True  = False")
        print("  True  and False = False   True  or False = True    not False = True")
        print("  False and True  = False   False or True  = True")
        print("  False and False = False   False or False = False")
        print()
        print("Using your numbers:", num1, "and", num2)
        print("(num1 > 5) and (num2 > 5) :", num1 > 5 and num2 > 5)
        print("(num1 > 5) or  (num2 > 5) :", num1 > 5 or num2 > 5)
        print("not (num1 > 5)            :", not (num1 > 5))

    # ============================== QUIZ ==============================
    elif choice == "4":
        print("\n--- QUIZ TIME! ---")
        print("Type the letter of your answer (a, b, c, or d).\n")
        score = 0

        print("Question 1: Which one is the right way to show text?")
        print("   a. print(Hello)")
        print('   b. print("Hello")')
        print("   c. Print Hello")
        print("   d. print[Hello]")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Wrong letter. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "b":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The right answer is b.\n")

        print("Question 2: Which one is a good variable name?")
        print("   a. 1name")
        print("   b. my name")
        print("   c. my_name")
        print("   d. @name")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Wrong letter. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "c":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The right answer is c.\n")

        print("Question 3: What type of data does input() give?")
        print("   a. int")
        print("   b. float")
        print("   c. str")
        print("   d. bool")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Wrong letter. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "c":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The right answer is c.\n")

        print("Question 4: Python uses ______ to group code.")
        print("   a. braces { }")
        print("   b. indentation")
        print("   c. semicolons")
        print("   d. parentheses")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Wrong letter. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "b":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The right answer is b.\n")

        print("Question 5: What is the result of 10 % 3 ?")
        print("   a. 3")
        print("   b. 1")
        print("   c. 0")
        print("   d. 3.33")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Wrong letter. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "b":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The right answer is b.\n")

        print("Question 6: What is the result of 17 // 3 ?")
        print("   a. 5")
        print("   b. 6")
        print("   c. 5.67")
        print("   d. 2")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Wrong letter. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "a":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The right answer is a.\n")

        print("Question 7: What is the result of 2 + 3 * 4 ?")
        print("   a. 20")
        print("   b. 14")
        print("   c. 24")
        print("   d. 9")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Wrong letter. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "b":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The right answer is b.\n")

        print("Question 8: Which one do we use for THREE or more choices?")
        print("   a. if")
        print("   b. if-else")
        print("   c. if-elif-else")
        print("   d. print")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Wrong letter. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "c":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The right answer is c.\n")

        print("Question 9: What is the result of True and False ?")
        print("   a. True")
        print("   b. False")
        print("   c. Error")
        print("   d. None")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Wrong letter. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "b":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The right answer is b.\n")

        print("Question 10: What does range(1, 6) give?")
        print("   a. 1, 2, 3, 4, 5")
        print("   b. 1, 2, 3, 4, 5, 6")
        print("   c. 0, 1, 2, 3, 4, 5")
        print("   d. 2, 3, 4, 5, 6")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Wrong letter. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "a":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The right answer is a.\n")

        print("--- QUIZ RESULT ---")
        print("Your score:", score, "out of 10")

        if score == 10:
            print("Perfect! Great job!")
        elif score >= 8:
            print("Very Good! Keep it up!")
        elif score >= 6:
            print("Passed. Read the lessons again to do better.")
        else:
            print("Failed. Please study the lessons again.")

    # ============================== EXIT ==============================
    elif choice == "5":
        print("Thank you for learning Python. Goodbye!")
        running = False

    # CHECK: the choice is not 1 to 5
    else:
        print("Error: '" + choice + "' is not on the menu. Please type a number from 1 to 5.")
