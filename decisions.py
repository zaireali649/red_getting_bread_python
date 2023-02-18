import random

#%%

def compare_number_thresh(number, thresh):
    if(number < thresh): 
        return("small number")
    elif(number > thresh): 
        return("big number")
    else: # Nothing
        return(" ".join(["number is", str(thresh)]))

if(__name__ == '__main__'):
    # Basics

    number = random.randint(0,10)

    if(number < 6):
        print("small number")
    elif(number > 6):
        print("big number")
    else: # elif(number == 6):
        print("number is 6")
        
    print(number)

    #%%
    # Adv

    number = random.randint(0,10)

    if(number < 9): # 0,1,2,3,4,5,6,7,8
        print("small number")
    elif(number > 4): # 9,10
        print("big number")
    else: # Nothing
        print("number is 6")
        
    print(number)

    #%%
    # Error Knowledge

    number = random.randint(0,10)
    thresh = 4

    response = compare_number_thresh(number, thresh)
    print(response)
        
    print(number)