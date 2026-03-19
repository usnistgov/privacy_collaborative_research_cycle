## CRC Data Bundle v1.3

Download the data and analysis notebooks from [Releases](https://github.com/usnistgov/privacy_collaborative_research_cycle/releases/tag/v1.3)

This Bundle contains all deidentified data submitted to the CRC from 2023 through 2024. The [CRC homepage](https://pages.nist.gov/privacy_collaborative_research_cycle/index.html) provides more detailed information about the program, its goals, and how to participate.   In short, the CRC seeks to equip the research community with resources to explore, evaluate, and discuss deidentification approaches.  

The crc-data-bundle file contains:

- All of the deidentified data submissions from 2023 through 2024.  
-- The .csv file contains the deidentified data itself. 
-- The .json file contains all metadata about the generation of the data. 
- An index.csv file that tracks metadata across all submissions, algorithm properties and definitions,
- An index definition file that explains the metadata 
- The ground truth target data (NIST ACS Data Excerpts) and data dictionaries as json files.

To learn more about the techniques used to deidentify the data, see the [CRC Techniques page](https://pages.nist.gov/privacy_collaborative_research_cycle/pages/techniques.html). 

These data are available for any investigation a user sees fit.  See the license statement contained in the repo for terms and conditions.


## Privacy Metric Benchmark Data

This folder contains a much smaller, curated collection of samples from high performing deidentification algorithms.  It includes traditional statistical disclosure control techniques from the sdcMicro library, non-differentially private synthetic data from the R Synthpop library and several proprietary techniques, and differentially private data from the SmartNoise synthesizers (AIM and MST) at several levels of epsilon.  It also includes the original ground truth target data and a "withheld" data set from the same schema, for comparison and control/baseline purposes.  

This data is intended for benchmarking new privacy metrics, as part of the 2025 CRC work analyzing the privacy of deidentified data.  See the [Red Team page](https://pages.nist.gov/privacy_collaborative_research_cycle/pages/red_team.html) on the CRC website for details.  Which of these deidentification provides the best privacy?  How do we define privacy, and where do our definitions agree or disagree with each other? 


## Please cite these resources

If you use these resources, we ask that you cite as follows:

Task C., Bhagat K., Howarth G.S. (2024), NIST Collaborative Research Cycle Acceleration Bundle, National Institute of Standards and Technology, https://doi.org/10.18434/mds2-3024

bibtex:
@misc{task_nist_2024, title = {{NIST} {Collaborative} {Research} {Cycle} {Data} and {Metrics} {Archive}}, url = {https://data.nist.gov/od/id/mds2-3024}, doi = {10.18434/MDS2-3024}, author = {Task, Christine and Bhagat, Karan and Streat, Damon and Howarth, Gary}, month = feb, year = {2025}}
