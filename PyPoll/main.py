# PyPoll main for U of M assignment
import os
import csv

total_votes = 0
candidate_dictionary = { }
percent_votes_candidate_won = 0
total_votes_candiate_won = 0
winner_of_popular_vote = ""

# parse csv file
path = os.path.join("02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

# open the file using "write" mode. Specify the variable to hold the contents
with open(path, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # skipping over column headers
    next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # calculate total votes
        total_votes = total_votes + 1
        candidate_name = row[2]

        # If we have them in the dictionary, update their total vote count
        if candidate_name in candidate_dictionary:
            current_vote_count = candidate_dictionary[candidate_name]
            candidate_dictionary[candidate_name] = current_vote_count + 1
        else:
            # Otherwise initalize them with 1 vote
            candidate_dictionary[candidate_name] = 1

		
print("Election Results")
print("----------------------------")
print('Total Votes: ' +str(total_votes))
print("----------------------------")
#Loop over dictionary of candidates and votes
highest_vote_count = 0
for candidate_name, candidate_votes in candidate_dictionary.items():
    # is the current candidate vote count greater than the current high count
    if candidate_votes > highest_vote_count:
        # if it is then we have a potential winner
        winner_of_popular_vote = candidate_name
        # set their vote count as the new bar to compare against
        highest_vote_count = candidate_votes

    percentage_won = (candidate_votes / total_votes) * 100
    percent_display = '{:0.3f}'.format(percentage_won)
    print(candidate_name + ": " + percent_display + "%  (" + str(candidate_votes) + ")")
print("----------------------------")
print('Winner: ' + winner_of_popular_vote)