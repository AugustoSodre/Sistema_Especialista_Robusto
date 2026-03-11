from inference_engine import InferenceEngine
from knowledge_base import QUESTIONS
import database

def run_cli():
    # Initialize SQLite Database
    database.init_db()
    engine = InferenceEngine()
    
    print("\nWelcome to the Expert System for Diagnosing Eye Disease\n")
    
    while True:
        user_symptoms = {}
        for symptom_key, question in QUESTIONS.items():
            ans = input(f"{question} (yes/no): ").strip().lower()
            user_symptoms[symptom_key] = '1' if ans == 'yes' else '0'

        disease, match_pct = engine.infer(user_symptoms)
        
        if disease:
            print(f"\n=> The most probable disease is: {disease} ({match_pct:.1f}% confidence)\n")
        else:
            print("\n=> Could not diagnose the disease based on the provided symptoms.\n")
        
        print("\n--- Diagnostic Reasoning (Chain of Thought) ---")
        print(engine.explanation.get_explanation())
        print("-----------------------------------------------")
        
        if disease:
            print(f"\n=> The most probable disease that you have is: {disease}\n")
        else:
            print("\n=> Could not diagnose the disease based on the provided symptoms.\n")
            disease = "Unknown"
            
        # Persist to SQLite
        database.save_diagnosis(user_symptoms, disease)
        
        print("Would you like to diagnose some other symptoms? (yes/no)")
        if input().strip().lower() == "no":
            break

if __name__ == "__main__":
    run_cli()