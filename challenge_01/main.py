def get_input():
    with open('input.txt', 'r') as f:
        return f.read()

def clean_text():
    text_no_clean = get_input()
    text_clean = text_no_clean.lower().split()
    return text_clean

def main():
    count = {}
    text = clean_text()
    for word in text:
        count[word] = count.get(word, 0) + 1
    result = ''.join(f'{word}{count_}' for word, count_ in count.items())
    return result

if __name__ == '__main__':
    print(main())