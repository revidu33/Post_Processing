import re

def process_jetpack_commands(text):
    # Map directional words to corresponding actions
    direction_mapping = {
        'up': 'Ascend',
        'down': 'Descend',
        'left': 'Move Left',
        'right': 'Move Right',
        # Add more directional mappings as needed
    }

    # Remove common filler words and repeated phrases
    cleaned_text = re.sub(r'\b(?:and|to|the)\b', '', text, flags=re.IGNORECASE)
    cleaned_text = re.sub(r'\b(\w+)\b\s+\1\b', r'\1', cleaned_text, flags=re.IGNORECASE)

    # Extract potential directional words from the cleaned text
    potential_directions = re.findall(r'\b(?:up|down|left|right)\b', cleaned_text, flags=re.IGNORECASE)

    # Only consider the last directional command
    selected_direction = potential_directions[-1].lower() if potential_directions else None

    # Handle additional noise reduction (removing irrelevant words)
    relevant_words = ['move', 'go', 'navigate', 'travel']  # Customize as needed
    cleaned_text = ' '.join(word for word in cleaned_text.split() if word.lower() in relevant_words)

    # Perform action based on the selected direction
    action = direction_mapping.get(selected_direction, 'Unknown Action')

    return action

def main():
    # Example text obtained from speech-to-text conversion
    speech_to_text_output = "Move up and to the right and then navigate to the destination."

    # Process jetpack command
    jetpack_action = process_jetpack_commands(speech_to_text_output)

    # Display the results
    print("Original Text:")
    print(speech_to_text_output)
    print("\nJetpack Action:")
    print(jetpack_action)

if __name__ == "__main__":
    main()
