dic = {'Ari': [79, 77],
       'Tom': [89, 98],
       'Jom': [78, 88],
       'Jerry': [88, 25],
       'kot': [99, 43]
       }
x = 0
y = 0
for k, v in dic.items():
    # print(v[1])
    x += v[0]
    y += v[1]
x /= 5
y /= 5
i = int(input())
if i == 0:
    print('%.2f, %.2f' % (x, y))
else:
    for k, v in dic.items():
        print(k, v[0], v[1])
