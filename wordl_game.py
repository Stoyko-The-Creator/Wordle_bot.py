def word_list(file_name):
    words=[]
    with open(file_name,'r') as file:
        for line in file:
            for word in line.split():
                stripped_line=word
                words.append(stripped_line)
        file.close()
    return(words)
    
def game(guess,answer):
    # determines if answers match 0=Red 1=Yellow 2=Green    truths=[]
    truths=[]
    for num in range(0,5):
        if answer[num]==guess[num]:
            truths.append(2)
        elif guess[num] in answer:
            truths.append(1) 
        else:
            truths.append(0)
    return truths
    
