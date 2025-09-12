def get_book_txt(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        print(file_contents)


def get_book_word(filepath):
    with open(filepath) as f:
        count = 0
        file_contents = f.read()
        fisk = file_contents.split()
        for word in fisk:
            count += 1
    print(f"{count} words found in the document")


def sort_on(items):
    return items["num"]


def get_letter_count(filepath):
    opslags_vark = {}
    opslags_list = []

    with open(filepath) as f:
        file_contens = f.read()
        fisk = file_contens.lower()
        for letter in fisk:
            if letter in opslags_vark:
                opslags_vark[letter] += 1
            else:
                opslags_vark[letter] = 1
    for fisk in opslags_vark:
        fiskeren = opslags_vark[fisk]
        opslags_list.append({"char": fisk, "num": fiskeren})

    # print(opslags_list)
    opslags_list.sort(reverse=True, key=sort_on)
    return opslags_list


def the_last():
    fisk = "books/frankenstein.txt"
    count = get_letter_count(fisk)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fisk}")
    print(count)
