def build_dictionary(word_list):
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict
input_text = input(":> ").lower()
word_list = input_text.split()
bag_of_words = build_dictionary(word_list)
print(f'\nWord list:\n{word_list}\n\nBag of Words:')
for word in sorted(bag_of_words.keys()):
    print(f"{word} - {bag_of_words[word]}")
