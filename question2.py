def build_nested_dictionary_from_string_list(list_of_strings):
    nested_dictionary_result = {}

    for current_string in list_of_strings:
        length_of_current_string = len(current_string)

        if length_of_current_string % 2 == 0:
            parity_of_string_length = "even"
        else:
            parity_of_string_length = "odd"

        nested_dictionary_result[current_string] = {
            "length": length_of_current_string,
            "parity": parity_of_string_length
        }

    return nested_dictionary_result


user_input_string = input("Enter a list of words separated by commas: ")


list_of_user_strings = user_input_string.split(",")


cleaned_list_of_user_strings = []
for word in list_of_user_strings:
    cleaned_list_of_user_strings.append(word.strip())


final_nested_dictionary = build_nested_dictionary_from_string_list(cleaned_list_of_user_strings)

print("\nFinal Nested Dictionary:")
print(final_nested_dictionary)
