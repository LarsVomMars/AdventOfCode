data = [int(timer) for timer in open("input").read().split(",")]


def run(data, days):
    fishies = [0, ] * 9
    new_fishies = [0, ] * 9
    for d in data:
        fishies[d] += 1

    for _ in range(days):
        for i, f in enumerate(fishies):
            if i == 0:
                new_fishies[6] += f
                new_fishies[8] += f
            else:
                new_fishies[i - 1] += f

        fishies = new_fishies.copy()
        new_fishies = [0, ] * 9

    return sum(fishies)


print("1:", run(data, 80))
print("2:", run(data, 256))
