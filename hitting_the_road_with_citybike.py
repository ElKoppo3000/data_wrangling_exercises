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

# import the csv library
import csv

# open the file in read mode
# file is in same folder than this script
source_file = open('202009CitibikeTripdataExample.csv', 'r')

# pass our source file as ingridient to the csv library's dict reader
# store the result in citibike_reader
citibike_reader = csv.DictReader(source_file)

# print fieldnames (headers) of the dataset
#print(citibike_reader.fieldnames)

# count variables for subscriber, customer and other
subscriber_count = 0
customer_count = 0
other_user_count = 0

# iterate over dataset
for row in citibike_reader:
    # if usertype is subscriber
    if row['usertype'] == "Subscriber":
        # increment subscriber counter
        subscriber_count += 1
    # if usertype is customer
    elif row['usertype'] == "Customer":
        # increment subscriber counter
        customer_count += 1
    # catch the rest
    else:
        # increment other counter
        other_user_count += 1

# print results
print('Subscribers: ' + str(subscriber_count))
print('Customer: ' + str(customer_count))
print('Other: ' + str(other_user_count))
