def text_indentation(text):
    # Check if the input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define the characters that require 2 new lines after them
    special_characters = ['.', '?', ':']

    # Split the text into sentences based on the special characters
    sentences = []
    current_sentence = ""
    for char in text:
        current_sentence += char
        if char in special_characters:
            sentences.append(current_sentence.strip())
            current_sentence = ""

    # Print each sentence with two new lines after each special character
    for sentence in sentences:
        print(sentence)
        print("\n")

