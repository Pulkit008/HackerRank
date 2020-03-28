import collections as cl
for i in cl.Counter(sorted(input())).most_common(3):
    print(*i)
