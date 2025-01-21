def reverse_words_in_string(sentence):
    words_list = sentence.split()

    reversed_words_list = words_list[::-1]

    reversed_sentence = ' '.join(reversed_words_list)

    return reversed_sentence


# Example usage:
input_sentence_1 = "The weather is so sunny nowadays"
output_sentence_1 = reverse_words_in_string(input_sentence_1)
print(output_sentence_1)

input_sentence_2 = "Life is so beautiful"
output_sentence_2 = reverse_words_in_string(input_sentence_2)
print(output_sentence_2)
