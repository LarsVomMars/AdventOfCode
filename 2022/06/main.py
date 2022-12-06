STREAM = open("input").read().strip()


def find_packet_by_size(size):
    for i in range(len(STREAM) - size):
        packet = STREAM[i:i + size]
        if len(set(packet)) == size:
            return i + size


def p1():
    return find_packet_by_size(4)


def p2():
    return find_packet_by_size(14)


print("1:", p1())
print("2:", p2())
