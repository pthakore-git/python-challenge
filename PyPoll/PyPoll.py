#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Import os & csv packacges
import os
import csv


# In[9]:


# Path to collect data from Resources folder
poll_path = os.path.join(".","Resources","election_data.csv")
# Path to output the results
file_to_output = os.path.join(".","analysis","poll_analysis.txt")
print(file_to_output)


# In[25]:


# Open path
with open(poll_path) as csvfile:
    pollReader = csv.reader(csvfile)


#Variable declarations
    total_votes = 0
    vote_Charles = 0
    vote_Diana = 0
    vote_Raymon = 0
    winner = ""


#Store header
    header = next(pollReader)

    #track the total & votes
    for row in pollReader:
        total_votes += 1
        if(row[2] == "Charles Casper Stockham"):
            vote_Charles += 1
        if(row[2] == "Diana DeGette"):
            vote_Diana += 1
        if(row[2] == "Raymon Anthony Doane"):
            vote_Raymon += 1

    #Calculate %
    percentage_Charles = (vote_Charles/total_votes)*100
    percentage_Diana = (vote_Diana/total_votes)*100
    percentage_Raymon = (vote_Raymon/total_votes)*100
    
    #Calculate winner
if(vote_Charles > vote_Diana and vote_Charles > vote_Raymon):
    winner = "Charles Casper Stockham"
    
if(vote_Diana > vote_Charles and vote_Diana > vote_Raymon):
    winner = "Diana DeGette"

if(vote_Raymon > vote_Charles and vote_Raymon > vote_Diana):
    winner = "Raymon Anthony Doane"

output = (
    f"Election Results\n"
    f"--------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"--------------------------\n"
    f"Charles Casper Stockham: {percentage_Charles:.3f}% ({vote_Charles})\n"
    f"Diana DeGette: {percentage_Diana:.3f}% ({vote_Diana})\n"
    f"Raymon Anthony Doane: {percentage_Raymon:.3f}% ({vote_Raymon})\n"
    f"--------------------------\n"
    f"Winner: {winner}\n"
    f"--------------------------\n"
)    
print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


# In[ ]:




