

print(" Total 15 Questions \n Complete to Win a Prize\n")
questions = [

["What is the capital of India?", "Mumbai", "New Delhi", "Kolkata", "Hyderabad", 2],
["Which planet is closest to the Sun?", "Earth", "Mercury", "Mars", "Venus", 2]
["Who discovered gravity?", "Albert Einstein", "Isaac Newton", "Galileo", "Edison", 2],
["Which is the largest continent?", "Africa", "Asia", "Europe", "Australia", 2],
["What is the national animal of India?", "Tiger", "Lion", "Elephant", "Peacock", 1],
["Which organ pumps blood?", "Brain", "Heart", "Lungs", "Kidneys", 2],
["Who is known as the Father of Computers?", "Alan Turing", "Charles Babbage", "Bill Gates", "Steve Jobs", 2],
["What is the boiling point of water?", "50°C", "100°C", "150°C", "200°C", 2],
["Which gas do humans need to breathe?", "Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen", 1],
["Which festival is called Festival of Lights?", "Holi", "Diwali", "Onam", "Eid", 2],
["Which animal gives us wool?", "Cow", "Sheep", "Goat", "Horse", 2],
["What is the square root of 81?", "7", "8", "9", "10", 3],
["Who invented the telephone?", "Alexander Graham Bell", "Thomas Edison", "Tesla", "James Watt", 1],
["Which is the longest river?", "Ganga", "Nile", "Amazon", "Yangtze", 2],
["How many states are in India?", "29", "30", "28", "31", 3]

]


Prize = 100000

for question in questions:
    print(question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    a = int(input("Enter your Answer : "))
    
    if(question[5] == a):
        print("Correct Answer ✅\n")
    else:
        print(f"Incorrect ❌  The Correct Answer was {question[5]}")
        print("\n")
        break
    print("You Won:",Prize)
       
