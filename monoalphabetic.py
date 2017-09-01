import re
endl = "\n\n"
def sortDictByCount(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x['count'] < pivot['count']:
                less.append(x)
            if x['count'] == pivot['count']:
                equal.append(x)
            if x['count'] > pivot['count']:
                greater.append(x)
        # Don't forget to return something!
        return sortDictByCount(less)+equal+sortDictByCount(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

# def quickSort(array):
#     less = []
#     equal = []
#     greater = []

#     if len(array) > 1:
#         pivot = array[0]
#         for x in array:
#             if x < pivot:
#                 less.append(x)
#             if x == pivot:
#                 equal.append(x)
#             if x > pivot:
#                 greater.append(x)
#         # Don't forget to return something!
#         return quickSort(less)+equal+quickSort(greater)  # Just use the + operator to join lists
#     # Note that you want equal ^^^^^ not pivot
#     else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
#         return array

def getFromTextFile(_file):
    opened_file = open(_file)
    from_file = opened_file.read()
    #remove new line characters
    from_file = "".join(from_file.split())
    return from_file



fromFile = getFromTextFile('./cipher1.txt')
fileLen = len(fromFile)
print
print "File Length: " + str(fileLen)

alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher = alphabet
alpha_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


#Count the number of occurences of each letter
for char in fromFile:
    index = alphabet.find(char)
    alpha_count[index] += 1

#Match the count with the respective letter
freq_dict = []
for i in range(len(alpha_count)):
    freq_dict.append({"letter":alphabet[i], "count":alpha_count[i]})

#Sort the dict array
freq_dict = sortDictByCount(freq_dict)
freq_dict.reverse()
print
print "-"*10+ " Frequencies of Occurence " +"-"*10 +"\n"
for item in freq_dict:
    count = float(item['count'])
    freq = (count / fileLen) * 100
    print item['letter'] + ": " + str(freq) + "  %."



temp = fromFile

# for i, char in enumerate(temp,1):
#     if char == 't':
#         if i < len(temp):
#             if temp[i] == 't':
#                 print temp[i-3:i+2]
#         # print temp[i-3:i]


# double letter occurences
print endl
print "-"*10 + " doubles " + "-"*10
print
double_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i,char in enumerate(temp,1):
    for j,alp in enumerate(alphabet,1):
        if i < len(temp) and char == alp and temp[i] == alp:
            double_count[j-1] += 1

doub_dict = []
for i,char in enumerate(double_count,1):
    doub_dict.append({"letters":alphabet[i-1]+alphabet[i-1],"count":double_count[i-1]})

doub_dict = sortDictByCount(doub_dict)
doub_dict.reverse();

for item in doub_dict:
    if item['count'] != 0:
        print item

#finding bigrams
bigrams = []
bi_count = []
for char in alphabet:
    for i in range(len(alphabet)):
        bigrams.append(char+alphabet[i])
        bi_count.append(0)



for i,char in enumerate(temp, 1):
    for j,bigram in enumerate(bigrams,1):
        if temp[i-1:i+1] == bigram:
            bi_count[j-1] = bi_count[j-1] + 1
bi_dict = []
for i,bigram in enumerate(bigrams,1):
    bi_dict.append({"bigram":bigram,"count":bi_count[i-1]})

bi_dict = sortDictByCount(bi_dict)
bi_dict.reverse()
print endl
print "-"*10 + " Top 10 bigrams" + "-"*10
print
for i in range(10):
    print bi_dict[i]
# for item in bi_dict:
#     if item['count'] >= 5:
#         print item

# Based on all of the information collected so far I believe t -> e  j -> t  p -> a
print endl
print "-"*10 + " 3 letter sequences containing j(\"t\") and t(\"e\") " + "-"*10
print
jmatch = re.find("(j\wt)",temp)
tmatch = re.findall("tj\w",temp)

print jmatch
print 
print tmatch


print endl
print "Count of jgt occurences, possibly \"the\": " +  str(jmatch.count('jgt'))
print endl
print "Unaltered CipherText"
print
print temp + endl

print "Replaced all t's with e's"
temp = temp.replace('t', 'e')
print

print temp + endl


print "Replaced all j's with t's"
print
temp =  temp.replace('j', 't')
print temp + endl


print "Replaced all p's with a's"
print

temp =  temp.replace('p','a')
print temp + endl

print "Replaced all g's with h's"
print

print temp.replace('g','h')

