import random

# Data stored in a dictionary (key = Country, value = Capital)
def my_database():
    return {
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "United Kingdom": "London",
        "Japan": "Tokyo",
        "China": "Beijing",   
        "Marshall Islands": "Majuro",
        "Cape Verde": "Praia",
        "Vanuatu": "Port Vila",
        "Russia": "Moscow",
        "Egypt": "Cairo",
        "Canada": "Ottawa",
        "Brazil": "Brasilia",
        "Australia": "Canberra",
        "India": "New Delhi",
        "Kenya": "Nairobi",
        "Mexico": "Mexico City",        
        "Comoros": "Moroni",
        "São Tomé and Príncipe": "São Tomé",
        "Kiribati": "South Tarawa",
        "Tuvalu": "Funafuti",
        "Djibouti": "Djibouti",
        "Eritrea": "Asmara",
        "Timor-Leste": "Dili",
        "Bhutan": "Thimphu",
        "Lesotho": "Maseru",
        "Lithuania": "Vilnius",
        "Latvia": "Riga",
        "Estonia": "Tallinn",
        "Cyprus": "Nicosia",
        "Iceland": "Reykjavík",
        "San Marino": "San Marino",
        "Liechtenstein": "Vaduz",
        "Monaco": "Monaco",
        "Vatican City": "Vatican City",
        "Malta": "Valletta",
        "Luxembourg": "Luxembourg",
        "North Macedonia": "Skopje"
    }

# LOGIC - specific task functions

def set_quiz_questions(full_database, num_questions = 5):
    """
    Picks 'num_questions' random items from the database.
    """
    # Convert dictionary items to a list so we can pick from them
    all_items = list(full_database.items()) 
    
    # Pick value of 'num_questions' random pairs
    selected_questions = random.sample(all_items, num_questions)
    return selected_questions

def generate_options(correct_capital, all_capitals):
    """
    Creates a list of 4 options: 1 correct, 3 wrong.
    """
    options = [correct_capital]
    
    # Loop until we have 4 distinct options
    while len(options) < 4:
        random_city = random.choice(all_capitals)
        # Only add if it's not already in our list (no duplicates)
        if random_city not in options:
            options.append(random_city)
    
    # Shuffle them so the answer isn't always 'A'
    random.shuffle(options)
    return options

# CONTROLLER: The main quiz loop
def run_quiz():
    print("--- 🗺️ COUNTRY CAPITALS QUIZ!!! 🗺️ ---")
    print("Type A, B, C, or D to answer.\n")
    
    score = 0
    full_data = my_database()
    
    # Get a list of ALL capitals to use as "wrong answers" during the quiz
    all_capitals_list = list(full_data.values())
    
    # Get our 5 random questions - This returns a list of pairs
    quiz_questions = set_quiz_questions(full_data, 5)
    
    # Loop through the 5 selected questions
    for country, correct_answer in quiz_questions:
        print(f"What is the capital of {country}?")
        
        # Generate the multiple choice options
        options = generate_options(correct_answer, all_capitals_list)
        
        # Display options A, B, C, D
        labels = ['A', 'B', 'C', 'D']
        for i in range(4):
            print(f"{labels[i]}. {options[i]}")

        # 1. Create a map for the labels
        label_to_index = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3
        }

        # 2. Get User Input and format string to uppercase and strip leading space
        user_answer = input("Your answer (A, B, C, or D): ").upper().strip()

        # 3. Use the dictionary to find the index
        if user_answer in label_to_index:
            index = label_to_index[user_answer]  
            selected_city = options[index]

            if selected_city == correct_answer:
                print(f"✅ 🎢 Correct! It is {correct_answer}.")
                score += 1
            else:
                print(f"❌ Good try, but that’s not it. The correct answer was {correct_answer}.")
        else:
            print(f"🚫 Invalid input. Please type A, B, C, or D to make your selection.")
            
        print("=" * 50) # Separator line            

    print(f"GAME OVER: You scored {score}/5")

if __name__ == "__main__":
    run_quiz()