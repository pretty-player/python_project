import string

def count_word_frequency(file_path, target_word):
    count = 0
    target_word = target_word.lower().strip()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Remove punctuation and convert to lowercase
                line = line.translate(str.maketrans('', '', string.punctuation))
                words = line.lower().split()
                
                # Count occurrences of the specific word
                count += words.count(target_word)
                
        return count

    except FileNotFoundError:
        return "Error: The file was not found."

# Usage
file_to_check = "words.txt"
word_to_find = "Python"

result = count_word_frequency(file_to_check, word_to_find)
print(f"The word '{word_to_find}' appears {result} times.")