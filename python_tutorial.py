# ==========================================================
#  FINAL EXAM PROJECT: PYTHON TUTORIAL PROGRAM
#  Lesson 1 = Introduction to Programming (print, comments, input/output)
#  Lesson 2 = Basic Syntax (variables, data types, if-else, loops)
#  Lesson 3 = Arithmetic Operators (arithmetic, comparison, logical)
#  Lesson 4 = Quiz, 
#           = Exit
# ==========================================================

running = True                      # controls the main menu loop

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
        print("Programming is giving instructions to a computer.")
        print("Python is a programming language that is easy to read and learn.")
        print("A program usually does 3 things: gets INPUT, PROCESSES it, shows OUTPUT.")
        print()

        print("1. print() displays information on the screen.")
        print('     print("Hello, World!")')
        print("   - Text (string) must be inside quotation marks.")
        print("   - Numbers do NOT need quotes:  print(100)")
        print('   - Print many values using a comma:  print("Age:", 18)')
        print()

        print("2. Comments are ignored by Python. They explain the code.")
        print("     # This is a single-line comment")
        print('     """ This is a')
        print('         multi-line comment """')
        print()

        print("3. input() accepts data from the user:")
        print('     name = input("Enter your name: ")')
        print("   IMPORTANT: all input is a string (str) by default!")
        print("   Convert it using int() for whole numbers or float() for decimals:")
        print('     age = int(input("Enter your age: "))')
        print()

        print("4. An f-string puts variables inside text (put f before the quotes):")
        print('     print(f"Student: {name}, Age: {age}")')
        print()

        # Try-it: input and output
        name = input("Try it! Enter your name: ")
        while name == "":                                   # ERROR CHECK: empty name
            print("Error: Name cannot be empty.")
            name = input("Try it! Enter your name: ")

        valid = False
        while valid == False:
            text = input("Enter your age: ")
            if text.isdigit():                              # ERROR CHECK: digits only
                age = int(text)                             # convert str to int
                valid = True
            else:
                print("Error: Age must be a whole number. Try again.")

        print("Using a comma :", name, age)
        print(f"Using f-string: Student: {name}, Age: {age}")

    # ====================== LESSON 2: BASIC SYNTAX ======================
    elif choice == "2":
        print("\n--- LESSON 2: BASIC SYNTAX ---")

        # ----- Indentation -----
        print("\n[A] INDENTATION")
        print("Python uses indentation (spaces) to define blocks of code.")
        print("  CORRECT:                 INCORRECT:")
        print("  if age >= 18:            if age >= 18:")
        print('      print("Adult")        print("Adult")   <- not indented')
        input("\nPress Enter to continue...")

        # ----- Variables and data types -----
        print("\n[B] VARIABLES AND DATA TYPES")
        print("A variable is a named storage location used to keep data.")
        print('     name = "Maria"')
        print("     age = 20")
        print("Variable naming rules:")
        print("  - must start with a letter or underscore (_)")
        print("  - cannot start with a number (1name is wrong)")
        print("  - no spaces or special characters (my name, @name are wrong)")
        print("  - case-sensitive (age and AGE are different variables)")
        print("Data types:")
        print("  int   -> whole numbers      (10, 25, -7)")
        print("  float -> decimal numbers    (3.14, 2.0)")
        print('  str   -> text               ("Hello")')
        print("  bool  -> True or False")
        print()

        word = input("Try it! Type anything (text): ")
        number = 25
        decimal = 3.14
        flag = True
        print("word    =", word, "-> type:", type(word))
        print("number  =", number, "-> type:", type(number))
        print("decimal =", decimal, "-> type:", type(decimal))
        print("flag    =", flag, "-> type:", type(flag))
        input("\nPress Enter to continue...")

        # ----- Conditional statements -----
        print("\n[C] CONDITIONAL STATEMENTS (if, if-else, if-elif-else)")
        print("A condition is either True or False. The program makes decisions.")
        print("  if        -> runs a block only if the condition is True")
        print("  if-else   -> chooses between TWO actions")
        print("  if-elif-else -> chooses between THREE or more actions")
        print("Example:")
        print("  if score >= 90:")
        print('      print("Excellent")')
        print("  elif score >= 80:")
        print('      print("Very Good")')
        print("  elif score >= 75:")
        print('      print("Passed")')
        print("  else:")
        print('      print("Failed")')
        print("Python checks from top to bottom and runs the FIRST True condition.")
        print()

        valid = False
        while valid == False:
            text = input("Try it! Enter a score (0 to 100): ")
            if text.isdigit():
                score = int(text)
                if score >= 0 and score <= 100:             # ERROR CHECK: range
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
        print("\n[D] LOOPS (ITERATION)")
        print("A loop repeats code so you do not write it many times.")
        print("  for loop   -> use when you know how many times to repeat")
        print("     for number in range(1, 6):")
        print("         print(number)")
        print("     range(1, 6) gives 1, 2, 3, 4, 5  (stop value 6 is NOT included)")
        print()
        print("  while loop -> repeats while a condition is True")
        print("     count = 1")
        print("     while count <= 5:")
        print("         print(count)")
        print("         count += 1        # same as count = count + 1")
        print()

        valid = False
        while valid == False:
            text = input("Try it! Enter a number from 1 to 10: ")
            if text.isdigit():
                limit = int(text)
                if limit >= 1 and limit <= 10:              # ERROR CHECK: range
                    valid = True
                else:
                    print("Error: Number must be from 1 to 10.")
            else:
                print("Error: Please enter a whole number.")

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
        print("\n[A] ARITHMETIC OPERATORS (used for calculations)")
        print("  +   Addition          5 + 3   = 8")
        print("  -   Subtraction      10 - 4   = 6")
        print("  *   Multiplication    7 * 2   = 14")
        print("  /   Division (float) 15 / 3   = 5.0")
        print("  //  Floor division   17 // 3  = 5")
        print("  %   Modulus (remainder) 10 % 3 = 1")
        print("  **  Exponent          2 ** 3  = 8")
        print()
        print("Python follows PEMDAS (order of operations):")
        print("  Parentheses, Exponents, Multiplication, Division, Addition, Subtraction")
        print("  Example: 2 + 3 * 4 = 14   (multiplication first)")
        print()

        print("Now you try! Enter two whole numbers.")

        valid = False
        while valid == False:
            text = input("First number : ")
            if text.isdigit():                              # ERROR CHECK: digits only
                num1 = int(text)
                valid = True
            else:
                print("Error: '" + text + "' is not a valid whole number. Try again.")

        valid = False
        while valid == False:
            text = input("Second number: ")
            if text.isdigit():
                num2 = int(text)
                valid = True
            else:
                print("Error: '" + text + "' is not a valid whole number. Try again.")

        print("\nResults:")
        print("Sum        :", num1 + num2)
        print("Difference :", num1 - num2)
        print("Product    :", num1 * num2)

        if num2 != 0:                                       # ERROR CHECK: divide by zero
            print("Quotient   :", num1 / num2)
            print("Floor div  :", num1 // num2)
            print("Remainder  :", num1 % num2)
        else:
            print("Error: Cannot divide by zero! (Quotient, Floor div, Remainder skipped)")

        if num2 > 1000:                                     # ERROR CHECK: too big
            print("Error: Exponent is too big (use 1000 or below).")
        else:
            print("Power      :", num1 ** num2)
        input("\nPress Enter to continue...")

        # ----- Comparison (relational) operators -----
        print("\n[B] COMPARISON OPERATORS (result is True or False)")
        print("  ==  equal to              !=  not equal to")
        print("  >   greater than          <   less than")
        print("  >=  greater or equal      <=  less or equal")
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
        print("\n[C] LOGICAL OPERATORS (combine conditions)")
        print("  and -> True only if ALL conditions are True")
        print("  or  -> True if AT LEAST ONE condition is True")
        print("  not -> reverses the result (True becomes False)")
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
        print("Answer by typing the letter (a, b, c, or d).\n")
        score = 0

        print("Question 1: Which is the correct way to print text?")
        print("   a. print(Hello)")
        print('   b. print("Hello")')
        print("   c. Print Hello")
        print("   d. print[Hello]")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Invalid answer. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "b":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The correct answer is b.\n")

        print("Question 2: Which is a valid variable name?")
        print("   a. 1name")
        print("   b. my name")
        print("   c. my_name")
        print("   d. @name")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Invalid answer. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "c":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The correct answer is c.\n")

        print("Question 3: What data type does input() return by default?")
        print("   a. int")
        print("   b. float")
        print("   c. str")
        print("   d. bool")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Invalid answer. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "c":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The correct answer is c.\n")

        print("Question 4: Python uses ______ to define blocks of code.")
        print("   a. braces { }")
        print("   b. indentation")
        print("   c. semicolons")
        print("   d. parentheses")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Invalid answer. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "b":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The correct answer is b.\n")

        print("Question 5: What is the result of 10 % 3 ?")
        print("   a. 3")
        print("   b. 1")
        print("   c. 0")
        print("   d. 3.33")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Invalid answer. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "b":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The correct answer is b.\n")

        print("Question 6: What is the result of 17 // 3 ?")
        print("   a. 5")
        print("   b. 6")
        print("   c. 5.67")
        print("   d. 2")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Invalid answer. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "a":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The correct answer is a.\n")

        print("Question 7: What is the result of 2 + 3 * 4 ?")
        print("   a. 20")
        print("   b. 14")
        print("   c. 24")
        print("   d. 9")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Invalid answer. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "b":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The correct answer is b.\n")

        print("Question 8: Which statement is used for THREE or more outcomes?")
        print("   a. if")
        print("   b. if-else")
        print("   c. if-elif-else")
        print("   d. print")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Invalid answer. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "c":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The correct answer is c.\n")

        print("Question 9: What is the result of True and False ?")
        print("   a. True")
        print("   b. False")
        print("   c. Error")
        print("   d. None")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Invalid answer. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "b":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The correct answer is b.\n")

        print("Question 10: What does range(1, 6) produce?")
        print("   a. 1, 2, 3, 4, 5")
        print("   b. 1, 2, 3, 4, 5, 6")
        print("   c. 0, 1, 2, 3, 4, 5")
        print("   d. 2, 3, 4, 5, 6")
        answer = input("Your answer: ").lower()
        while answer != "a" and answer != "b" and answer != "c" and answer != "d":
            print("Error: Invalid answer. Please type only a, b, c, or d.")
            answer = input("Your answer: ").lower()
        if answer == "a":
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong. The correct answer is a.\n")

        print("--- QUIZ RESULT ---")
        print("Your score:", score, "out of 10")

        if score == 10:
            print("Perfect! Excellent work!")
        elif score >= 8:
            print("Very Good! Keep it up!")
        elif score >= 6:
            print("Passed. Review the lessons to improve.")
        else:
            print("Failed. Please study the lessons again.")

    # ============================== EXIT ==============================
    elif choice == "5":
        print("Thank you for learning Python. Goodbye!")
        running = False

    # ERROR CHECK: anything that is not 1 to 5
    else:
        print("Error: '" + choice + "' is not a valid choice. Please enter a number from 1 to 5.")
