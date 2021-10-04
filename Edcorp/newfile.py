def linear(numberheads, numberlegs):
    for numberhens in range (0, numberheads + 1):
        numbercows = numberheads - numberhens
        totallegs = 2*(numberhens) + 4*(numbercows)
        if totallegs == numberlegs:
           print('cows = {} and hens = {}'.format(numbercows, numberhens))
            
linear(8, 20)
