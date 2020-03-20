#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
###### o(1)- (answer)
###### while loop with one comparison
###### doesnt matter what n is, it will be the same process
###### one function run on A
###### operations is in direct relation to the size of n
######

b)
###### O(n^2) - (answer)
###### main loop is O(n) 1:1 ratio of operations to size of n
###### inner loop , iterating each N and then doing 2 operations on each
###### Each loop is O(n) since one is inside the other, its going to be n to the power of n operations

c)
###### O(n)
###### recursive code
###### one input as bunnies gets bigger, as bunnies grows by one it will recurse one time for each
###### will grow in direct relation to N but not exponentially it just runs again until bases case is hit


## Exercise II

##### N  = number of stories - N Story building
##### starting at base floor 1 (cause gravity and velocity) at what floor do we hit our breakage
##### egg gets broken if its dropped from floor F floor or above
#####   if floor >= n(i)  egg will break / else  egg not broken

 
    f = 1 (floor we are on)
    n = (array of floors)
    
    while f <= n[highest number] and >= 1 (means we are inside the building) 
        for i in n: (looping through each floor)
            if f >= 1 (drop egg)
                if egg does not break,  
                f +=1 (increase f by 1 )
                else:  
                    return egg broke at floor f
                
##### complexity of this is          
            
##### we will not actually be able to run this since we dont actually know what floor an egg will break on
##### YET (quarantine weekend plans confirmed)