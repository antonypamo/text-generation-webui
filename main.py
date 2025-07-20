import json
import os
from savant_core.nodes import MentalMap
from savant_core.resonance import ResonanceEngine
from savant_core.feedback_loop import FeedbackLoop

def load_profile(path):
    with open(path, 'r') as f:
        return json.load(f)

def main():
    profile_path = os.path.join('data', 'perfil_simbotico_antony.json')
    profile = load_profile(profile_path)
    print(f"Loaded profile: {profile['nombre_simbolico']}")
    # Initialize components
    mental_map = MentalMap(profile)
    engine = ResonanceEngine(profile)
    feedback = FeedbackLoop(profile)
    # Simple CLI loop
    print("Syntagma AGI Φ₅.0 CLI - Type 'exit' to quit.")
    while True:
        user_input = input('> ')
        if user_input.lower() in ['exit', 'quit']:
            break
        response = engine.respond(user_input)
        print(response)
        feedback.update(user_input, response)

if __name__ == '__main__':
    main()
