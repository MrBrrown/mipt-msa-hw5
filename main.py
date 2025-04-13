import requests
from collections import Counter


def get_text(url):
    return requests.get(url).text()

def parse_text(url: str) -> dict[str, int]:
    return dict(Counter(get_text(url).split()))

def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"
    text_dict = parse_text(url)

    frequencies = {}
    with open(words_file, 'r') as file:
        for line in file:
            word = line.strip()
            if word:
                if word in text_dict:
                    frequencies[word] = text_dict[word]
    
    print(frequencies)

if __name__ == "__main__":
    main()