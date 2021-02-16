#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:53:59 2021

@author: robinmevans
"""
import csv
import os

file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis","election_analysis.txt")
                              
                              
# variable fot total votes                              
total_votes = 0     
                    
# create a list for candidate option and a dictionary for candidate votes
candidate_options = []
candidate_votes = {}

# creating winning candidate as a string and winning count tracker

winning_candidate = ""
winning_count = 0

# open the file to load
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    # read the header
    header = next(reader)
    
    # create a for loop
    for row in reader:
        
        # update total votes
        total_votes += 1
        
        # candidate name for each row
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            
            # Add it to the list of candidate options
            candidate_options.append(candidate_name)
      
            # Begin tracking the candidate's voter count
            candidate_votes[candidate_name] = 0
            
        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
# Print the results to the output file
with open(file_to_output, "w") as txt_file:
    result = (
        f"Election Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"------------------------\n")
    print(result)
    txt_file.write(result)
    
    # Determine the winner by looping through the counts
    for candidate in candidate_votes:
        
        # Calculating vote count and %
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Finding winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        # Print each candidate's voter count and % 
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")
        
            
        # save each candidate's voter counct and % to text file
        txt_file.write(voter_output)
            
            
    # printing the winning candidate to text file
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"------------------------\n")
    print(winning_candidate_summary)
    
    
    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
          