class ExplanationFacility:
    def __init__(self):
        self.chain_of_thought = []

    def log(self, message):
        """Adds a reasoning step to the chain of thought."""
        self.chain_of_thought.append(message)

    def get_explanation(self):
        """Returns the full log of how the conclusion was reached."""
        return "\n".join(self.chain_of_thought)

    def clear(self):
        """Clears the reasoning log for a new run."""
        self.chain_of_thought = []