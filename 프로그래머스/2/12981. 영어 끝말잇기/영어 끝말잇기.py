def solution(n, words):
    test = []
    idx = -1
    test.append(words[0])
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]:
            print(words[i-1], words[i])
            idx = i
            break
        elif words[i] in test:
            idx = i
            break
        test.append(words[i])
    if idx == -1:
        return [0, 0]

    return [idx % n + 1, words[idx % n::n].index(words[idx]) + 1]