# question: How many Citi Bike rides each day are taken
# by "subscribers" versus "customer"

# answer: Choose a single day of rides to examine.
# the dataset used for this exercise was generated from the original
# Citi Bike system data found here: ...

# programm Outline:
# 1. read in the data file: file.csv
# 2. create variables to count: subscribers, customers and other
# 3. for each row in the file:
#   a. If the user type is subscriber, add 1 to subscriber count
#   b. If the user type is customer, add 1 to customer count
#   c. Otherwise, add 1 to other count
# 4. print out results
