def main():
    file_path = "books/frankenstein.txt"
    
    with open(file_path) as f:
        file_contents = f.read()
        
        # Count words
        word_count = count_words(file_contents)
        
        # Count characters
        character_counts = count_characters(file_contents)
        
        # Generate and print the report
        print_report(file_path, word_count, character_counts)

def count_words(text):
    """Counts the number of words in the text."""
    words = text.split()
    return len(words)

def count_characters(text):
    """Counts the occurrences of each alphabetic character in the text."""
    text = text.lower()
    char_count = {}
    
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            char_count[char] = char_count.get(char, 0) + 1
    
    return char_count

def print_report(file_path, word_count, character_counts):
    """Prints a report of word and character counts."""
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    
    # Convert dictionary to a sorted list of tuples by frequency in descending order
    sorted_characters = sorted(character_counts.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

# Run the main function
main()

    
