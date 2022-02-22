def convert(number):
    if(number%3==0):
        if((number%3==0)and(number%5==0)and (number%7==0)):
            return 'PlingPlangPlong'
        elif((number%3==0)and(number%5==0)):
            return 'PlingPlang'
        elif((number%3==0)and(number%7==0)):
            return 'PlingPlong' 
        else:
            return 'Pling'
    elif(number%5==0):
        if((number%3==0)and(number%5==0)and(number%7==0)):
            return 'PlingPlangPlong'
        elif((number%5==0)and(number%3==0)):
            return 'PlangPling'
        elif((number%5==0)and(number%7==0)):
            return 'PlangPlong' 
        else:
            return 'same number'