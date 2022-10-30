def main():
    number = int(input())
    sentence = [input() for _ in range(number)]
    sentence_joined = ''.join(sentence)
    sentence_joined2 = ' '.join(sentence)
    sentence_lower = lower(sentence_joined)
    sentence_upper = upper(sentence_joined)

    if (len(sentence_lower) == 0):
        print ("No lowercase letters")
    else:
        for i in sentence_lower:   
            print(i,end="")
        print("")

    if (len(sentence_upper) == 0):
        print ("No uppercase letters")
    else:  
            print(len(sentence_upper))

    print(len(sentence_joined))

    longest = max(sentence_joined2.split(), key=len)
    print(longest)

def lower(x):
    new_sentence =[]
    for i in x:
        if (i.islower()):
            new_sentence += i
    return new_sentence

def upper(x):
    new_sentence =[]
    for i in x:
        if (i.isupper()):
            new_sentence += i
    return new_sentence

main()
    