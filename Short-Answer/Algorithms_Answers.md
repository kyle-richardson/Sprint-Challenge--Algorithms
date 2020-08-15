#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n).  n3 for condition/n2 in block of code = n


b) O(n^2).  2 nested loops that always reach the end, which is n. 


c) O(n).  single recursive call

## Exercise II

very similar to binary search.  I would 

1) find midpoint of building (low(1 to start) + high(n to start) //2)
2) throw an egg off that mid floor
3a) if it breaks, then I make the floor one below the new high and start over with step 1
3b) if it doesnt break, then I first check if there are any other floors above in my current list of floors. If not, then the floor right above (curr+1) is f.  Otherwise, make the floor one above the new low and start over with step 1

runtime O(logn) since you are dividing floors in half each time

