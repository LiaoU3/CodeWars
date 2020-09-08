# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python

def top_3_words(text):
    text = text.lower()
    text += ' '
    words = []
    in_word = True if text[0].isalpha() else False
    start = 0
    for pos in range(len(text)):
        if (in_word == True and (not (text[pos].isalpha() or text[pos] =='\''))):           
            words.append(text[start:pos])
            in_word = False
        elif in_word ==False:
            if text[pos].isalpha() or (text[pos] =='\'' and (text[pos+1].isalpha() or text[pos-1].isalpha())):
                start = pos
                in_word = True
                
    totals = [[] for i in range(len(list(set(words))))]

    for pos in range(len(totals)):
        totals[pos].append(sorted(set(words), key = words.index)[pos])
        totals[pos].append(words.count(totals[pos][0]))

    ans = []
    for cnt in range(3):
        if not totals:
            break
        maxvalue = 0
        for pos in range(len(totals)):
            if totals[pos][1] >maxvalue:
                maxvalue = totals[pos][1]
                maxkey = totals[pos][0]
                maxpos = pos
        ans.append(maxkey)
        del totals[maxpos]

    return ans

# from collections import Counter
# import re


# def top_3_words(text):
#     c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
#     return [w for w,_ in c.most_common(3)]

print(top_3_words("a a a  b  c c  d d d d  e e e e e"))
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
print(top_3_words("  //wont won't won't "))
print(top_3_words("  , e   .. "))
print(top_3_words("  ...  "))