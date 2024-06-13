from itertools import permutations


def generate_sentences():
    manga_name = input("Manga adını giriniz: ")
    keywords = ['oku', 'türkçe', input("Kaçıncı bölüm olduğunu giriniz: "), "manga", "bölüm"]
    sentences = []

    for i in range(1, len(keywords) + 1):
        word_permutations = permutations(keywords, i)
        for perm in word_permutations:
            sentences.append(manga_name + ' ' + ' '.join(perm))

    return sentences


def main():
    sentences = generate_sentences()

    for sentence in sentences:
        print(sentence)


if __name__ == "__main__":
    main()
