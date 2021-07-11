# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular votes.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.3831

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the votes and 85,213 total votes.
    - Diana DeGette received 73.8% of the votes and 272,892 total votes.
    - Raymon Anthony Doane received 3.1% of the votes and 11,606 total votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of all votes with a total of 85,213 votes.

## Challenge Overview
The election commission has requested some additional data to complete the audit

1. The voter turnout for each county.
2. The percentage of votes from each county of the total count.
3. The county with the highest turnout.

## Election-Audit Results
* There were a total of 369, 711 votes in this congressional election.
* Number of votes and the percentage of the total votes for each county:
    * Jefferson county had 38,855 votes, which was 10.5% of the total votes.
    * Denver county had 306,055 votes, which was 82.8% of the total votes.
    * Arapahoe county had 24,801 votes, which was 6.7% of the total votes.
* Denver county had the largest number of votes (306, 055).
* Number of votes and the percentage of the total votes for each candidate:
    * Charles Casper Stockham had 85,213 votes, which was 23.0% of the total votes.
    * Diana DeGette had 272,892 votes, which was 73.8% of the total votes.
    * Raymon Anthony Doane had 11,606 votes, which was 3.1% of the total votes.
* Diana DeGette won the election with 272,892 votes, which was 73.8% of the total votes.

## Challenge Summary
This analysis script could be used for other future elections if provided with additional data. The script could be modified to look at districs instead of counties by changing the index in this line of the code and a further analysis could be run by changing the associated variable names to keep the code organized. 

![6](https://user-images.githubusercontent.com/85372441/125207430-f70d3b80-e251-11eb-9883-53581b32fd0d.png)

Also, if the business would like to the way the winner is determined, the script could be modified to their needs by looking more deeply in this script, which looks at the popular vote in each county. For instance, if it were for a presidential race they could use this code as a template and then additionally include electoral college votes to the analysis to assist in predicting a winner.
![7](https://user-images.githubusercontent.com/85372441/125207570-b6fa8880-e252-11eb-9c58-06a59edf43d3.png)

