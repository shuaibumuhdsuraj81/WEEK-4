#file reading and writing

with open('original_text.txt', 'r') as file:
    words = file.read()
    lower_case = words.lower()
    print(lower_case)

    word_count = len(words)
    print(word_count)

with open('processed_text.txt', 'w') as file:
    file.write(lower_case)
    file.write(f'word count: {word_count}')

print('NEW FILE HAS BEEN CREATED SUCCESSFULLY')