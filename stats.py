def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    text = text.lower()
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

def get_sorted_char_counts(char_counts):
    # Create a list of dictionaries for alphabetic characters only
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    # Helper function for sorting by count
    def sort_on(item):
        return item["num"]
    
    # Sort the list in descending order by count
    char_list.sort(reverse=True, key=sort_on)
    return char_list