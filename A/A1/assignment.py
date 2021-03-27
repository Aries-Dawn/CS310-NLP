import sys

def read_in():
    inputFile = sys.argv[1]

    with open(inputFile) as f:
        inputContext = f.read()

    # print(inputContext)

    inputList = inputContext.split('\n')

    sortList = []
    for s in inputList:
        if len(s) != 0:
            sortList.append((s,counting(s)))
    
    return sortList


def write_out(sortedList):
    outputFile = sys.argv[2]
    with open(outputFile,'w') as f:
        for a,b in sortedList:
            f.write(a)
            f.write('\n')
    


def counting(s:str):
    count = 0
    isEn = False
    for char in s:
        if (not ord('A') <= ord(char) <= ord('z')) and char != ' ' :
            if char == 'b':
                print('ctmct')
            count += 1
        if isEn and ((not ('A' <= char <= 'z')) or char == ' ') :
            isEn = False
            count += 1
        if 'A' <= char <= 'z':
            isEn = True
    if isEn:
        count += 1
    if count == 0:
        return 9223372036854775807
    return count


# class Node:
#     s = ''
#     words_count = 0
#     def __init__(self,s,words_count):
#         self.s = s
#         self.words_count = words_count

if __name__ == "__main__":
    sortList = read_in()
    
    sortedList = sorted(sortList,key=lambda x:(x[1],x[0]))

    write_out(sortedList)
    print(sortedList[1])