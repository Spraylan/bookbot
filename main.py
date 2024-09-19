def main():
    file_path = "books/frankenstein.txt"
    text = get_text(file_path)
    words = count_words(text)
    lowercase = text.lower()
    letters = get_list(lowercase)
    totals = get_totals(letters)
    list_dict = [{'char' : key, 'num' : value} for key, value in totals.items()]
    list_dict.sort(reverse = True, key = sort_on)
    
    print("~=~ FrEaKy FrAnKeNsTeIn FaCtS ~=~")
    print(f"Frankenstein contains {len(words)} words")
    print("")
    for dict_char in list_dict:
        if dict_char['char'].isalpha():
            print(f"Whoa! The letter {dict_char['char']} appears {dict_char['num']} times!")
        
    
    #for t in totals:
        #if t.isalpha():
            #print(f"{t} appears {totals[t]} times!")

def sort_on(list_dict):
    return list_dict['num']

def get_totals(letters):
    let_dict = {}
    for key in letters:
        if key in let_dict:
            let_dict[key] += 1
        else:
            let_dict[key] = 1
    return let_dict


def get_list(lowercase):
    let_list = []
    for word in lowercase:
        for letter in word:
            let_list.append(letter)
    return let_list

def count_words(text):
    return text.split()

def get_text(file_path):
    with open(file_path) as f:
        return f.read()

    
    
    
    #print(f" Frankenstein contains {words} words")
    
main()