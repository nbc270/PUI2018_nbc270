## Citibike Review for Nathan Benjamin Caplan (nbc270).


## Hypothesis and Data

### a. verify Null and alternative hypotheses are formulated correctly, and that they are state in both words and formulae (with the proper definitions to accompany the formulae)

The null and alternative hypotheses are formulated clearly to understand. However, I was not able to locate the null hypotheses stated in words. 

Based on my understanding of the project, if the expectation is female's trip duration tends to be longer than male's by 10%, both are formulated correctly. 

### b. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values

The data processing steps are very clear, the necessary data, gender, and trip duration are presented and seperated into proper groups for plotting. 

It is a very good idea to convert trip duration from seconds to minutes so it is easier to interpret a bike trip length. In addition, cleaning up the no gender data rows is a very necessary step performed to avoid this category being randomly counted as either gender group. 

### c. chose an appropriate test to test _H0_ given the type of data, and the question asked.

The idea focuses on comparing the means of two groups, female and male riders. I think the Z-test (paired data) can be used for testing to measure the distance/differences between two groups' means and distribution (each sample has over 30 observations). The Z-test can also compare the mean of female and male groups to all the riders in January (including no gender records).

## Comments, Statistical Test, and Suggestions

It is a good idea to compare trip duration between genders. Particularly, during a winter month (in this project January data was selected), dress code, road condition under harsh weather, and physical conditions can affect trip duration. Using the mean for both genders for comparison is very easy to interpret. It would be a good concise statement for any quick fact reports.

Another item can possibly be conidered is visualizing the average trip duration of different duration group helpful to contrast the distribution. 

In addition to the Z-test, ANOVA can also be considered for identifying the difference between the female and male groups trip duration while the each duration group being the dependant variable. 


## Reference: 

For understanding variable types: http://www.indiana.edu/~educy520/sec5982/week_2/variable_types.pdf
For determining potential tests: lecture 5, page 8, Steps in Null-Rejection Hypothesis Testing.

