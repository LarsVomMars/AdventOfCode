from collections import defaultdict


LINES = [word.strip() for word in open("input").read().split(",")]


def algo(word):
    value = 0
    for c in word:
        value += ord(c)
        value *= 17
        value %= 256
    return value


def get_split(word):
    if "-" in word:
        return word[:-1], 0
    word, focal = word.split("=")
    return word, int(focal)


def p1():
    return sum(map(algo, LINES))


def p2():
    box = defaultdict(list)

    for line in LINES:
        word, focal = get_split(line)
        score = algo(word)
        if focal == 0:
            box[score] = list(filter(lambda x: x[0] != word, box[score]))
            pass
        else:
            b = box[score]
            for i in range(len(b)):
                if b[i][0] == word:
                    b[i] = (word, focal)
                    break
            else:
                b.append((word, focal))

    sm = 0
    for score, words in box.items():
        for i, (word, focal) in enumerate(words, 1):
            sm += (score + 1) * focal * i
    return sm


print("1:", p1())
print("2:", p2())
