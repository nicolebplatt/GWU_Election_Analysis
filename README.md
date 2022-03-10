# GWU Election Analysis
## Overview of Election Audit
Two Colorado Board of Elections employees need to complete an audit of a recent local congressional election. The Board of Election employees need the following information:
1. Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. The winner of the election based on popular vote

The Election Commission has requested some additional data to complete the audit:

- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout


## Resources
- Data source: election_results.csv
- Software: 
	- Python 3.8.8
	- Visual Studio Code 1.65.1
	- Visual Studio Code Python Extension v2022.2.1924087327

## Election Audit Results: Candidate Summary
The results of the election by candidate show:
- There were 369,711 total votes cast.
- The candidates were:
	- Charles Casper Stockham
	- Diana DeGette
	- Raymon Anthony Doane
- The candidate results were:
	- Charles Casper Stockham: 23.0% (85,213)
	- Diana DeGette: 73.8% (272,892)
	- Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was Diana DeGette with 73.8% of the vote and 272,892 total votes.

![Screen Shot 2022-03-10 at 3 21 14 PM](https://user-images.githubusercontent.com/99286327/157756944-8215d16a-9ab3-4c7f-b77a-b370276bdbce.png)

## Election Audit Results: County Summary
Of the 369,711 total votes cast, the results of the election by county show:
- There were three counties included in this particular local congressional election:
	- Jefferson
	- Denver
	- Arapahoe
- The county results were:
	- Jefferson: 10.5% (38,855)
	- Denver: 82.8% (306,055)
	- Arapahoe: 6.7% (24,801)
- The county with the highest turnout was Denver county with 82.8% of the votes cast and 306,055 total votes.

## Business Proposal to Election Commission
The Python code included in this repository can be used for any future local election, provided that the raw data is in the same CSV format (Ballot ID, County, Candidate). If the data is not provided in this particular format, the script would need to be modified accordingly. However, the script contains only indexing of lists/dictionaries and no hard-coded number so it is extremely versatile. 

The script can be used as-is in the next election cycle of this particular electoral/congressional district, regardless of the number of candidates running or if redistricting occurs and additional counties are included in this district. Additionally, this code can be run on different datasets for other local congressional districts in the state (for example: Boulder or Colorado Springs).

Two additional considerations for future analysis would be:
- Include data on ballot type, such as mail-in, machine punch, or computer-read. The current script could be modified to include an analysis on how people are choosing to vote. The script would be adapted to include variables on ballot type and the results would show which ballot type is the most favorable.
- If the Election Commission wanted to include date/time data, the script could be adapted to see when the most popular times are for people to vote. This might be useful when thinking of staffing constraints and when to be sure there are enough officials on-site to assist with any surge of voters.

