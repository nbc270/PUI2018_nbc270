HW 12's goal was to practice working with clustering and time series analysis. For part 1, the goal was to cluster zip codes by business 
estimates over time. This was done via kmeans and heirarchial clustering. The data was provided from FB55 github repo, where a for loop was
used to read them all into python. I colaborated with Ursula Kaczmarek, Andrew Hill, Eve Marenghi, and Christine Biddlecombe. Andrew Hill
provided the code for an inertia plot which determined the number of clusters to use, being 4. 

The goal for part two was to perform time series analysis on MTA swipes per station using the data from HW 11. Again, I was unable to use 
the wget command on my local or my ADRF so I made note to download it manually and move it to PUIDATA. The data was transformed using an 
FFT function. Peridoicty was found at 48.5 weeks and the top four stations were found by an nlargest function from heapq. I colraborated 
with Eve Marenghi, Ursula Kazcmarek, and Christine Biddlecombe. Eve had taken the reigns and had assisted me with most of this. I later 
assisted Mingyi Hi and Sam. 
