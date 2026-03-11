from knowledge_base import RULES
from explanation import ExplanationFacility

class InferenceEngine:
    def __init__(self):
        self.explanation = ExplanationFacility()

    def infer(self, user_symptoms):
        """Infer the most probable disease using forward chaining."""
        disease, desc, photo, match_pct = self.forward_chaining(user_symptoms)
        return disease, match_pct

    def forward_chaining(self, user_symptoms):
        """Finds the most probable disease using fuzzy percentage matching."""
        self.explanation.clear()
        self.explanation.log("START FORWARD CHAINING (Fuzzy Match): Evaluating symptoms...\n")
        
        best_disease = ""
        best_desc = ""
        best_photo = ""
        max_percentage = 0.0

        for disease, data in RULES.items():
            self.explanation.log(f"Evaluating rule for: {disease}")
            score = 0
            total_symptoms = len(data["symptoms"])

            for symptom, required_val in data["symptoms"].items():
                user_val = str(user_symptoms.get(symptom, '0'))
                if user_val == required_val:
                    score += 1
                    self.explanation.log(f"  [+] Match on '{symptom}'")
                else:
                    self.explanation.log(f"  [-] Mismatch on '{symptom}' (Expected: {required_val}, Got: {user_val})")
            
            percentage = (score / total_symptoms) * 100
            self.explanation.log(f"  -> Score for {disease}: {score}/{total_symptoms} ({percentage:.1f}% match)\n")

            # Track the highest matching disease
            if percentage > max_percentage:
                max_percentage = percentage
                best_disease = disease
                best_desc = data["description"]
                best_photo = data["photo"]

        # Only return a diagnosis if it is reasonably confident (e.g., >= 50% match)
        if max_percentage >= 50.0:
            self.explanation.log(f"=> CONCLUSION: Best match is {best_disease} with {max_percentage:.1f}%.")
            return best_disease, best_desc, best_photo, max_percentage
        else:
            self.explanation.log(f"=> CONCLUSION: No disease met the 50% minimum threshold. Highest was {max_percentage:.1f}%.")
            return "", "", "", 0.0

    def backward_chaining(self, target_disease, user_symptoms):
        """Checks if a specific disease matches the user symptoms."""
        self.explanation.clear()
        self.explanation.log(f"START BACKWARD CHAINING: Attempting to prove hypothesis '{target_disease}'.")
        
        if target_disease not in RULES:
            self.explanation.log(f"  -> Error: {target_disease} is not in the knowledge base.")
            return False
        
        rule_symptoms = RULES[target_disease]["symptoms"]
        for symptom, required_val in rule_symptoms.items():
            user_val = str(user_symptoms.get(symptom, '0'))
            self.explanation.log(f"  -> Checking '{symptom}': Requires {required_val}, User has {user_val}.")
            if user_val != required_val:
                self.explanation.log(f"CONCLUSION: Hypothesis Disproved. Failed on symptom '{symptom}'.")
                return False
        
        self.explanation.log(f"CONCLUSION: Hypothesis Proved. User has {target_disease}.")
        return True