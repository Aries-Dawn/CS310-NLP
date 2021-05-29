import re
import random

beginning = '<s>'
with open('./bigram.lm') as f:
    lines = f.readlines()
    index = lines.index('\\2-grams:\n')
    data = {'<s>':[-70,'ni']}
    for i in range(index+1, len(lines)):
        getted_line = lines[i]
        getted_line = getted_line.replace("\n", "")
        if getted_line == '' or getted_line == '\\end\\':
            continue
        getted = re.split(r'[ \t]',getted_line)
        prob = float(getted[0])
        start = getted[1]
        next = getted[2]
        if start in data:
            old_prob = data[start][0]
            if old_prob < prob:
                data[start] = [prob,next]
            elif old_prob == prob and random.randint(0,10) > 5:
                data[start] = [prob,next]
        else:
            data[start] = [prob,next]
    result = ''
    tmp = beginning
    for i in range(30):
        getting = data[tmp][1]
        if getting=='</s>':
            break
        result = result+getting
        tmp = getting
    print(result)