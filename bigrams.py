f = open("moviedescriptions.txt",encoding = "utf8")
data = f.readlines()
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in range(3):
    data[i] = data[i].split("\t")
    data[i][1] = data[i][1].lower()
    for ele in data[i][1]:
        if ele in punc:
            data[i][1] = data[i][1].replace(ele, "")
    data[i][1] = data[i][1].split()

new_list = []
for i in range(3):
    for j in data[i][1]:
        new_list.append([j,i])
new_list = sorted(new_list)
inverted_index = []
dict_index = {}
words = []
for i in new_list:
    if i[0] not in words:
        words.append(i[0])
        inverted_index.append([i[0],1,[i[1]]])
        dict_index[i[0]] = [1,[i[1]]]
    else:
        if i[1] not in inverted_index[-1][2]:
            inverted_index[-1][2].append(i[1])
            inverted_index[-1][1]+=1
            dict_index[i[0]][0]+=1
            dict_index[i[0]][1].append(i[1])

for key in dict_index:
    print(key,dict_index[key])
bigrams = {}
words = []
for i in range(3):
    for word in data[i][1]:
        if word not in words:
            words.append(word)
            new = '$'+word+'$'
            for i in range(len(word)):
                if new[i:i+2] not in bigrams:
                    bigrams[new[i:i+2]] = [word]
                else:
                    bigrams[new[i:i+2]].append(word)
print(bigrams)

            
        
    

