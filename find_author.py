import os.path, math
def clean_up(s):
    punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
    result = s.lower().strip(punctuation)
    return result
def average_word_length(text):
    word=""
    punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
    i=0
    while i<len(text):
        for j in text[i]:
            j=clean_up(j)
            for char in j:
                if char not in punctuation:
                    word=word+char
        i=i+1
        word=word+" "
    print(word)
    word=word.split()
    letter=[]
    k=0
    while k<len(word):
        for m in word[k]:
            letter.append(m)
        k=k+1
    print(word)
    print(len(letter))
    return len(letter)/len(word)
def type_token_ratio(text):
    word=""
    punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
    i=0
    while i<len(text):
        for j in text[i]:
            j=clean_up(j)
            for char in j:
                if char not in punctuation:
                    word=word+char
        i=i+1
        word=word+" "
    word=word.split()
    letter=[]
    k=0
    while k<len(word):
        for m in word[k]:
            letter.append(m)
        k=k+1
    return len(set(word))/len(word)
def hapax_legomana_ratio(text):
    word=""
    punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
    i=0
    while i<len(text):
        for j in text[i]:
            j=clean_up(j)
            for char in j:
                if char not in punctuation:
                    word=word+char
        i=i+1
        word=word+" "
    word=word.split()
    k=0
    for j in word:
        if word.count(j)==1:
            k=k+1
    return k/len(word)
def split_on_separators(hooray, separators):
    word=""
    for char in hooray:
        if char not in separators:
            word=word+char
        if char in separators:
            char="&&&"
            word=word+char
    word=word.split("&&&")
    return word
def average_sentence_length(text):
    word=0
    for l in text:
        for w in l.strip().split(" "):
            word=word+1
    sentence=0
    for a in text:
        for i in a:
            if i in "?!.":
                sentence=sentence+1
    return word/sentence
def avg_sentence_complexity(text):
    sentence=0
    i=0
    word=0
    while i<len(text):
        for j in text[i]:
            for k in "?!.":
                if j==k:
                    sentence=sentence+1
            for x in ",;:":
                if j==x:
                    word=word+1
        i=i+1
    return (sentence+word)/sentence
def compare_signatures(sig1, sig2, weight):
    dif=0
    for i in range(1,6):
        dif=dif+abs(sig1[i]-sig2[i])*weight[i]
    return dif
def read_signature(filename):
    file = open(filename, 'r')
    # the first feature is a string so it doesn't need casting to float
    result = [file.readline()]
    # all remaining features are real numbers
    for line in file:
        result.append(float(line.strip()))
    return result
def get_valid_filename(prompt):
     import os
     if os.path.exists(prompt):
         return prompt
     else:
         print('This directory does not exist.')
         return get_valid_filename(prompt)
def read_directory_name(prompt):
     import os
     if os.path.isdir(prompt):
         return prompt
     else:
         print('This directory does not exist.')
         return read_directory_name(prompt)
if __name__ == '__main__':
    
    prompt = input('enter the name of the file with unknown author:')
    mystery_filename = get_valid_filename(prompt)

    # readlines gives us a list of strings one for each line of the file
    text = open(mystery_filename, 'r').readlines()
    
    # calculate the signature for the mystery file
    mystery_signature = [mystery_filename]
    mystery_signature.append(average_word_length(text))
    mystery_signature.append(type_token_ratio(text))
    mystery_signature.append(hapax_legomana_ratio(text))
    mystery_signature.append(average_sentence_length(text))
    mystery_signature.append(avg_sentence_complexity(text))
    
    weights = [0, 11, 33, 50, 0.4, 4]
    
    prompt = input('enter the path to the directory of signature files: ')
    dir = read_directory_name(prompt)
    # every file in this directory must be a linguistic signature
    files = os.listdir(dir)

    # we will assume that there is at least one signature in that directory
    this_file = files[0]
    signature = read_signature('%s/%s'%(dir,this_file))
    best_score = compare_signatures(mystery_signature, signature, weights)
    best_author = signature[0]
    for this_file in files[1:]:
        signature = read_signature('%s/%s'%(dir, this_file))
        score = compare_signatures(mystery_signature, signature, weights)
        if score < best_score:
            best_score = score
            best_author = signature[0]
    print("best author match: %s with score %s"%(best_author, best_score))    
    print(mystery_signature)

