# Recommendation-system
Recommendation system in python using dynamic programming approach.

used Pandas to read the csv files
Started by initializing a 2D array “Mat” with the dimensions
[budget+1][num_cities+1] in order to store the maximum number of
attractions and be able to apply the “Bottom-Up” approach afterwards
we did the “+1” in both dimensions to include an extra row for the
initial state in which none of the cities are visited yet “base case”, and
an extra column for the state of “no budget constraints”
We then iterate over the cities starting from 1 to number of desired
cities +1 we did the “+1” here to include the right number since in
python it excludes the stop.
We then iterate over the remaining budget variable starting from 1 to
budget + 1 we do budget +1 because of what was mentioned just
above.
At that point we will try to fill our Mat.
We then do a simple if statement to check if city_price “hotel price +
airline” &lt;= to our budget.

It will calculate the attractions count for the current city which is
attractions_count = Mat[city - 1][remaining_budget - city_price] +
len(attractions_dict[city_name])
(City-1) which represents the index of the previous city in our Matrix
and the (remaining_budget - city_price) is the new budget


And it does the same and tries all the combination then it starts to
backtrack to the optimal sequence of cities that suits the given budget


![image](https://github.com/adham208/Recommendation-system/assets/68466492/964cdcaa-f41c-40f4-b3bb-b208769418ad)

![image](https://github.com/adham208/Recommendation-system/assets/68466492/1d80feb5-a446-4132-8f18-de67192bf949)

