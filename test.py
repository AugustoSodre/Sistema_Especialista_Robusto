from inference_engine import InferenceEngine
import database

def run_tests():
    # Initialize the database just in case any downstream calls require it
    database.init_db()
    
    engine = InferenceEngine()

    print("======================================================")
    print("      TEST 1: FORWARD CHAINING (Myopia Match)")
    print("======================================================")
    # Symptoms perfectly matching "Myopia"
    symptoms_myopia = {
        'itching': '0', 'blurring': '1', 'redness': '0', 'night': '1', 
        'mucus': '0', 'tear': '0', 'yellowing': '0', 'headache': '1', 
        'cough': '0', 'pain': '0', 'overstrain': '1', 'sensitivity': '0', 
        'rainbow': '0', 'double': '0', 'sightedness': '1', 'sight': '0', 
        'nausea': '0', 'dilated': '0', 'eyelid': '1'
    }
    
    disease, desc, photo = engine.forward_chaining(symptoms_myopia)
    print(engine.explanation.get_explanation())
    print(f"\n[RESULT] Diagnosis: {disease if disease else 'Unknown'}")
    print("Expected: Myopia\n")


    print("======================================================")
    print("      TEST 2: FORWARD CHAINING (No Match)")
    print("======================================================")
    # Random symptoms that shouldn't match any specific disease perfectly
    symptoms_unknown = {
        'itching': '1', 'blurring': '0', 'redness': '0', 'night': '0', 
        'mucus': '1', 'tear': '0', 'yellowing': '1', 'headache': '1', 
        'cough': '1', 'pain': '0', 'overstrain': '0', 'sensitivity': '0', 
        'rainbow': '0', 'double': '0', 'sightedness': '0', 'sight': '0', 
        'nausea': '0', 'dilated': '0', 'eyelid': '0'
    }
    
    disease, desc, photo = engine.forward_chaining(symptoms_unknown)
    print(engine.explanation.get_explanation())
    print(f"\n[RESULT] Diagnosis: {disease if disease else 'Unknown'}")
    print("Expected: Unknown\n")


    print("======================================================")
    print("      TEST 3: BACKWARD CHAINING (Proving Glaucoma)")
    print("======================================================")
    # Symptoms perfectly matching "Glaucoma"
    symptoms_glaucoma = {
        'itching': '0', 'blurring': '1', 'redness': '1', 'night': '1', 
        'mucus': '0', 'tear': '0', 'yellowing': '1', 'headache': '0', 
        'cough': '0', 'pain': '1', 'overstrain': '0', 'sensitivity': '0', 
        'rainbow': '1', 'double': '0', 'sightedness': '0', 'sight': '1', 
        'nausea': '1', 'dilated': '1', 'eyelid': '0'
    }
    
    # Hypothesis: Does the user have Glaucoma?
    hypothesis_true = engine.backward_chaining("Glaucoma", symptoms_glaucoma)
    print(engine.explanation.get_explanation())
    print(f"\n[RESULT] Hypothesis Proved: {hypothesis_true}")
    print("Expected: True\n")


    print("======================================================")
    print("      TEST 4: BACKWARD CHAINING (Disproving Cataract)")
    print("======================================================")
    # Using the Glaucoma symptoms from above, but checking the "Cataract" hypothesis
    hypothesis_false = engine.backward_chaining("Cataract", symptoms_glaucoma)
    print(engine.explanation.get_explanation())
    print(f"\n[RESULT] Hypothesis Proved: {hypothesis_false}")
    print("Expected: False\n")

if __name__ == "__main__":
    run_tests()