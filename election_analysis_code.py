# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
candidate_votes = {}
candidate_options = []

# Challenge
# Create a list for the counties
counties = []

# Create a dictionary where the county is the key and the votes cast for each county in the election are the values.
counties_dict = {}

# Create an empty string that will hold the county name that had the largest turnout.
county_largest_turnout = ""
largest_turnout = 0

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
         # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        # Check if county name has already been recorded.
        county_name = row[1]
        if county_name not in counties:
            # Add it to the list of counties.
            counties.append(county_name)
            # Begin tracking votes in county.
            counties_dict[county_name] = 0
        # Add a vote to that county's count.
        counties_dict[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine percentage of votes for each county.
    # 1. Iterate through county list.
    for county in counties_dict:
        # 2. Retrieve vote count of county.
        county_votes = counties_dict[county]
        # 3. Calculate percentage of votes.
        county_vote_percentage = float(county_votes) / float(total_votes) * 100
        # 4. Print the county name and the percentage of votes.
        county_results = (f"{county}: {county_vote_percentage:.1f}% ({county_votes:,})\n")
        # 5. Print each county, their voter count, and percentage.
        print(county_results)
    # Save the county results to our text file.
        txt_file.write(county_results)

    # Determine largest county turnout
    # 1. Determine if the county votes are greater than the winning count.
        if (county_votes > largest_turnout):
        # 2. If true then set largest_turnout = county_votes.
            largest_turnout = county_votes
        # 3. Set county_largest_turnout to the county's name.
            county_largest_turnout = county
        largest_turnout_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {county_largest_turnout}\n"
        f"-------------------------\n")
    print(largest_turnout_summary)
    #Save winning county's name to the text file.
    txt_file.write(largest_turnout_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n") 
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
#  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
