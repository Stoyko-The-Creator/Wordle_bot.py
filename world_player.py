from random import choice
import wordl_game
words=Wordl_game.word_list('Five-letters.txt') # setup command line flag
pool=words.copy()

first=''
second=''
#The idea is to sort by letters with keys and find a list of words 

def run():
    global first
    global second
    first=split(choice(words))
    second='null'
    play(first)
 
def split(word:str):
    return[char for char in word]

def play(guess):
    # collects and deposits data to play the game
    global second
    for num in range(0,7):
     
        guess_result=Wordl_game.game(guess,answer)
        print(guess)
        print(guess_result)        
        if guess_result==[2,2,2,2,2]:
            record(first,second,num)
            print('win ')
            break
        if num==6:
            print('lose ')
            record(first,second,7)
            break
        guess=logic(guess,guess_result)

        if num==0:
            second=guess
    

def logic(guess, guess_result):
          # identifies truth values of words and then removes required words from the pool of possible answers.
    word_list=pool.copy()
    print(len(word_list))
       
    for mun in range(0,5):
        if guess_result[mun]==2:
            for item in word_list:
                item_split= split(item)
                if  not item_split[mun]==guess[mun]:
                    try:
                        pool.remove(item)
                    except ValueError:
                        pass
                                 
    
        if guess_result[mun]==0:
            for item in word_list:
                item_split=split(item)
                if guess[mun] in item_split:
                    try:
                        pool.remove(item)
                    except ValueError:
                        pass                    
                       
                        
        if guess_result[mun]==1:
            for item in word_list:
                item_split=split(item)
                if item_split[mun]==guess[mun] or guess[mun] not in item_split:
                    try:
                        pool.remove(item)
                    except ValueError:
                        pass                    
                    
    return (split(frequency(pool)))

def record(first,second,score):
    # After win or loss records the first two guesses and the final score for analysis
    global pool
    pool=words.copy()
    first =''.join([str(elem) for elem in first])
    second=''.join([str(elem) for elem in second])
    with open('results.csv','a',newline='') as out:
        csv_out=csv.writer(out, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_out.writerow([first,second,score])
        out.close()
    
    


def frequency(pool):
    ### meant to guess next word based on the frequency of the letters inside said word. Will replace eventually with completely self thinking code
    letters=['E','T','A','O','I','N','S','R','H','D','L','U','C','M','F','Y','W','G','P','B','V','K','X','Q','J','Z']
    values=[21912,16587,14810,14003,13318,12666,11450,10977,10795,7874,7253,5246,4943,4761,4200,3853,3819,3693,3316,2715,2019,1257,315,205,188,128]
    letter_values={}
    
    for num in range(0,26):
        letter_values[letters[num]]=values[num]
    
    letter_vals={}
    for word in pool:
        score_buffer=[]
        word_split= split(word)
        for item in word_split:
            if word_split.count(item)>1:
                score_buffer.append((letter_values [item])/(word_split.count(item)))
                for num in range(1,word_split.count(item)):
                    word_split.remove(item)
            else :
                score_buffer.append(letter_values[item])
        score=sum(score_buffer)
        letter_vals[word]=score
    return(max(letter_vals,key=letter_vals.get))
    
            


if __name__ == "__main__":
    print("Lets Get Started")
    # Set up to work with command line flags to set amount looped
    for num in range(1,100000000000):
        answer= split(choice(words))
        run()

