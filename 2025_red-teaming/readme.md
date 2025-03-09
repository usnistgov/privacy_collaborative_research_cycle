# 2025 CRC Red Team Phase 1 Competitor's Pack 

This folder contains the competitor's pack maerials for participating in the CRC's Phase 1 Red Team Challenge.  Check out the [website](https://pages.nist.gov/privacy_collaborative_research_cycle/pages/red_team.html) for the problem statement and participation directions. 

## Content List
- **Red Team Problems**: Problems 1-24 are the problems to attack.  For each problem, use the deidentified data (Deid) to predict values for the missing columns in the Attack Targets for each problem. 

- **Practice Problem**: Problem 25 includes a ground truth data file with all columns (both public fingerprint and confidential columns), along with one deidentified version of that file from each of our privacy approaches.  You can use this to test your reconstruction attacks. 

## Data Notes:
- The data is real anonymized data. 
- Each problem uses a different uniform random sample of the original population.  Every problem has different individuals, but they should have similar data distributions. 
- The feature names have been obfuscated.  There are 50 features total (see the 50f problems), but most problems focus on a select subset of 25 features (25f). 

## Contributors:
Damon Streat
Christine Task 
Karan Bhagat 
Gary Howarth
