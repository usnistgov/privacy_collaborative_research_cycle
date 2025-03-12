# 2025 CRC Red Team Phase 1 Competitor's Pack 

This folder contains the competitor's pack maerials for participating in the CRC's Phase 1 Red Team Challenge.  Check out the [website](https://pages.nist.gov/privacy_collaborative_research_cycle/pages/red_team.html) for the problem statement and participation directions. In particular, the problem statement suggests several ways you might try reconstructing a record belonging to a specific individual ("Bob").

## Content List
- **Red Team Problems**: Problems 1-24 are the problems to attack.  Each problem comes with a deidentified data file (Deid.csv) and a AttackTargets file (AttackTargets.csv).  Use the deidentified data to predict values for the missing columns in the attack targets file.  Note that the set of missing columns will be different for different problems, so start each problem by checking the list of features in the deid file to see which ones you need to add to the attack targets file.   

- **Practice Problem**: Problem 25 includes the answers (the full ground truth records), so you can practice your attacks and see how well they work.   The ground truth file has the original features values for all columns, both the public fingerprint columns and confidential columns.  The deidentified files are deidentified versions of that data, from each of our methods.  To test QID1 attacks, grab features F37, F41, F2, F17, F22, F32, F47 from the ground truth data to use as as your attack targets data. To test QID2 attacks, use F37, F41, F3, F13, F18, F23, F30 from the ground truth data as as your attack targets.  

## Data Notes:
- The data is real anonymized data. 
- Each problem uses a different uniform random sample of the original population.  This means that every problem has different individuals, but they should have similar data distributions.
- The feature names have been obfuscated.  There are 50 features total (see the 50f problems), but most problems focus on a select subset of 25 features (25f).  

## Deidentification Method Notes: 
You don't need to look at the references below before you try attacking the problems in the competitors pack; sometimes the best approaches are blind, just based on the actual patterns you find in the data.  But if you want to have a better understanding of the different deidentification appraoches,  below are the research papers and code links for the eight approaches we're exploring in Phase 1.  

Note that the Statistical Disclosure Control methods are anonymization approaches; they take the original ground truth records and edit them (redacting or changing some features values) to produce a version of the record that's harder to identify.  That means for those problems the deidentified data contains an anonymized version of each record in the attack targets file.   By contrast, synthetic data methods use models trained on the original data to produce entirely new records, so there isn't a one-to-one mapping between the target records and the deidentified records.  But synthetic data  methods may still overfit the data and leak a lot of sensitive information about individuals.  You'll get to find out how much different methods leak.     

### Differentially Private Synthetic Data Methods 
- SmartNoise MST (Maximum Spanning Tree): [Paper](https://arxiv.org/abs/2108.04978), [Tool](https://docs.smartnoise.org/synth/synthesizers/mst.html) 
- SmartNoise AIM (Adaptive Iterative Mechanism) : [Paper](https://arxiv.org/abs/2201.12677), [Tool](https://docs.smartnoise.org/synth/synthesizers/aim.html)

### Non-Differentially Private Synthetic Data Methods 
- R Synthpop CART (Classification and Regression Tree): [Paper](https://www.jstatsoft.org/article/view/v074i11), [Tool](https://cran.r-project.org/web/packages/synthpop/index.html)
- SynthCity ARF (Adverserial Random Forests: [Paper](https://arxiv.org/abs/2205.09435), [Tool](https://synthcity.readthedocs.io/en/latest/generated/synthcity.plugins.generic.plugin_arf.html)
- Synthetic Data Vault TVAE (Tabular Variation Auto Encoder): [Paper](https://arxiv.org/abs/1907.00503), [Tool](https://docs.sdv.dev/sdv/single-table-data/modeling/synthesizers/tvaesynthesizer)

### Traditional Statistical Disclosure Control (Anonymization) Methods
- sdcmicro Cell Suppression (Redacts demographic outlier records): [Paper](https://doi.org/10.1007/978-3-319-50272-4), [Tool](https://sdctools.github.io/sdcMicro/reference/localSuppression.html) 
- sdcmiro Rank Swapping (Alters numerical features: [Paper (pg 6)](https://www.census.gov/content/dam/Census/library/working-papers/1996/adrm/rr96-4.pdf), [Tool](https://sdctools.github.io/sdcMicro/reference/rankSwap.html) 


## Contributors:
- Damon Streat
- Christine Task 
- Karan Bhagat 
- Gary Howarth
