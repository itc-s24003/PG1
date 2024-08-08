data = "すもももももももものうち"
count_dic = {}
for v in data:
    if v in count_dic:
        count_dic[v] += 1
    else:
        count_dic[v] = 1
count_dic

import collections
count_dic = collections.defaultdict(int)
for v in data:
    count_dic[v] += 1
count_dic

print(int())

count_dic = collections.defaultdict(list)
for v in data:
    count_dic[v].append(v)
count_dic

count_dic = {}
for v in data:
    count_dic.setdefault(v, []).append(v)
count_dic

counter = collections.Counter(data)
counter

counter["す"]
counter["ぽ"]
counter.most_common()
counter.most_common(1)

top = counter.most_common()[0]
print(top[0], top[1])

CharCount = collections.namedtuple("CharCount", ["char", "count"])

mo = CharCount("も", 8)
mo

print(mo.char, mo.count)


cc_list = [CharCount(*v) for v in counter.most_common()]