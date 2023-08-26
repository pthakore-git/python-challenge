#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import os & csv packacges
import os
import csv


# In[50]:


# Path to collect data from Resources folder
bank_path = os.path.join(".","Resources","budget_data.csv")
# Path to output the results
file_to_output = os.path.join(".","analysis","financial_analysis.txt")
print(file_to_output)


# In[51]:


# Open path
with open(bank_path) as csvfile:
    bankReader = csv.reader(csvfile)

#Variable declarations
    total_months = 1
    total_net = 0
    net_change_list = []
    month_of_changes = []
    greatest = ["",0]
    least = ["",9999999999999]
    
#Store header
    header = next(bankReader)
    first_row = next(bankReader)
    total_net = int(first_row[1])
    prev_net = int(first_row[1])
    
    
    #track the total
    for row in bankReader:
        total_months += 1
        total_net += int(row[1])
        
    #track the net change
        net_change = int(row[1]) - prev_net
 
        prev_net = int(row[1])
        net_change_list.append(net_change)
        

    #Calculate the greatest increase
        if(net_change > greatest[1]):

            greatest[0] = row[0]
            greatest[1] = net_change
        
    #Calculate the greatest decrease
        if(net_change < least[1]):

            least[0] = row[0]
            least[1] = net_change

    net_monthly_avg = sum(net_change_list)/len(net_change_list)
output = (
    f"Financial Analysis\n"
    f"--------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest[0]} (${greatest[1]})\n"
    f"Greatest Decrease in Profits: {least[0]} (${least[1]})"
)    
print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)


# In[ ]:




    


# In[ ]:




