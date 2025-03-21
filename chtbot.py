import spacy

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Medication database
medications = {
    "paracetamol": {
        "usage": "Paracetamol is used to relieve pain and reduce fever.",
        "side_effects": "Side effects may include nausea, vomiting, and liver damage if taken in excess.",
        "dosage": "The typical adult dose is 500 mg to 1000 mg every 4 to 6 hours."
    },
    "ibuprofen": {
        "usage": "Ibuprofen is used to reduce inflammation and treat pain.",
        "side_effects": "Side effects may include stomach pain, heartburn, and dizziness.",
        "dosage": "The typical adult dose is 200 mg to 400 mg every 4 to 6 hours."
    },
    "amoxicillin": {
        "usage": "Amoxicillin is an antibiotic used to treat bacterial infections.",
        "side_effects": "Side effects may include diarrhea, nausea, and rash.",
        "dosage": "The typical adult dose is 250 mg to 500 mg every 8 hours."
    }
    # Add more medications as needed
}

# Injury database
injuries = {
    "sprain": {
        "description": "A sprain is an injury to the ligaments caused by twisting or stretching.",
        "treatment": "Rest, ice, compression, and elevation (R.I.C.E). Over-the-counter pain relievers may help."
    },
    "fracture": {
        "description": "A fracture is a break in a bone.",
        "treatment": "Immobilize the area, apply ice, and seek medical attention immediately."
    },
    "burn": {
        "description": "A burn is an injury to the skin caused by heat, chemicals, electricity, or radiation.",
        "treatment": "Cool the burn with running water, cover with a sterile bandage, and seek medical advice for severe burns."
    }
    # Add more injuries as needed
}

def get_medication_info(medication):
    if medication in medications:
        return medications[medication]
    else:
        return None

def get_injury_info(injury):
    if injury in injuries:
        return injuries[injury]
    else:
        return None

def get_response(user_input):
    doc = nlp(user_input.lower())  # Process the user input
    for token in doc:
        if token.text in medications:  # Check if the token is a medication
            med_info = get_medication_info(token.text)
            if med_info:
                return (
                    f"**{token.text.capitalize()}**\n\n"
                    f"**Usage:** {med_info['usage']}\n"
                    f"**Side Effects:** {med_info['side_effects']}\n"
                    f"**Dosage:** {med_info['dosage']}"
                )
        elif token.text in injuries:  # Check if the token is an injury
            injury_info = get_injury_info(token.text)
            if injury_info:
                return (
                    f"**{token.text.capitalize()}**\n\n"
                    f"**Description:** {injury_info['description']}\n"
                    f"**Treatment:** {injury_info['treatment']}"
                )
    return "I'm sorry, I couldn't find information on that medication or injury. Please check the spelling or try another query."

def main():
    print("Welcome to the Medicine and Injury Detection Chatbot! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Stay safe.")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
