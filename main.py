frankenstein_path = "books/frankenstein.txt"

def main():
    file_contents = get_file_contents(frankenstein_path)
    word_count = len(get_words(file_contents))
    char_counts = get_char_counts(file_contents)
    char_counts_dict = sort_dictionary(char_counts)
    print_report(frankenstein_path, word_count, char_counts_dict)


def get_file_contents(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read();
        return file_contents
    
def get_words(file_contents):
    words = file_contents.split()
    return words

def get_char_counts(file_contents):
    char_counts = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    for char in char_counts:
        count = file_contents.lower().count(char)
        char_counts[char] = count

    return char_counts

def sort_dictionary(dictionary):
    sorted_dict = dict(sorted(dictionary.items(),key=lambda item: item[1], reverse=True))
    return sorted_dict
    
def print_report(path, word_count, char_counts_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    
    for char, value in char_counts_dict.items():
        print(f"The '{char}' character was found {value} times")
    print("--- End report ---")

main()