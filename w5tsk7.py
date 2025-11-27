# Constant for word separation
DELIMITER = ','

def collectWords():
    words = []
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    return DELIMITER.join(words)

def analyseWords(all_words):
    if all_words == "":
        word_list = []
    else:
        word_list = all_words.split(DELIMITER)
    
    word_count = len(word_list)
    char_count = sum(len(word) for word in word_list)
    
    if word_count > 0:
        avg_length = char_count / word_count
    else:
        avg_length = 0
    
    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print("- {:.2f} Average word length".format(avg_length))
    return None

def main():
    print("Program starting.")
    all_words = collectWords()
    analyseWords(all_words)
    print("Program ending.")

main()
