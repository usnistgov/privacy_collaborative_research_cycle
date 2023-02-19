<script src="https://pages.nist.gov/nist-header-footer/js/jquery-1.9.0.min.js" type="text/javascript" defer="defer"></script>
<script src="https://pages.nist.gov/nist-header-footer/js/nist-header-footer.js" type="text/javascript" defer="defer"></script>

<link rel="stylesheet" href="https://pages.nist.gov/nist-header-footer/css/nist-combined.css">
<link rel="stylesheet" href="https://pages.nist.gov/privacy_collaborative_research_cycle/static/css/NISTStyle.css">

<link rel="stylesheet" href="https://pages.nist.gov/privacy_collaborative_research_cycle/static/css/NISTPages.css">

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

<title>Collaborative Research Cycle Homepage</title> 



![alt_text](images/image1.png "image_tooltip")


The CRC is a program run by the[ NIST Privacy Engineering Program](https://www.nist.gov/itl/applied-cybersecurity/privacy-engineering) and designed to spur research, innovation, and understanding of data deidentification techniques.

Have questions? Please contact NIST scientist [Gary Howarth](mailto:gary.howarth@nist.gov?subject=[CRC]) or crowd-source them by [joining the CRC list-serv.](http://CRC+subscribe@list.nist.gov?subject=subscribe)


## TLDR:

The CRC invites researchers to contribute de-identified records from the [NIST Diverse Community Excerpts](https://github.com/usnistgov/SDNist/tree/main/nist%20diverse%20communities%20data%20excerpts) along with a brief abstract listing their methods. In May 2023, the CRC plans to release a machine-readable _research acceleration bundle_ of all contributions along with detailed evaluations using the [SDNist report tool](https://github.com/usnistgov/SDNist/). We invite researchers to use the acceleration bundle to perform analysis and submit their findings in 3-page-or-less_ [tiny papers](https://iclr.cc/Conferences/2023/CallForTinyPapers) _to a workshop to be held in November 2023. Submitted papers and NIST-contributed research will be packaged in a set of conference proceedings we expect to release in January 2024. Prizes and awards are not part of this program.


## How to Participate:


### Exploratory phase (February - May 2023)



1. [Join the CRC list-serv](CRC+subscribe@list.nist.gov?subject=subscribe). (optional)
2. [Register your team.](https://docs.google.com/forms/d/e/1FAIpQLSde8IklaZFEXlCBb0g_EVh6rf7tyxfCsB5yieZ-8hBomlRTGQ/viewform?usp=sf_link)
3. De-identify the [NIST Diverse Community Excerpts](https://github.com/usnistgov/SDNist/tree/main/nist%20diverse%20communities%20data%20excerpts).
4. Use the[ SDNist report tool ](https://github.com/usnistgov/SDNist/)to analyze your de-identified data.
5. Watch our introductory video (to be released 7 March 2023).
6. Submit data with an abstract. (submission links are sent after your team registers)
    1. Submit data by March 10th, and we’ll walk through your evaluation results with you during office hours on March 13th.
7. Attend office hours (see calendar below). We will send links out to the list-serv and registered teams before the sessions. (optional)
8. Make data contributions by 9 May 2023 to have your data included in the research acceleration bundle.
9. Join us or watch the recording of our Exploratory Workshop (16 May 2023).


### Exploratory phase (May - September 2023)



1. Download the research acceleration bundle and explore!
2. Pick a problem or two to play around with for yourself.
3. Follow our seminar series and blog posts as we share new things that we learn from your submissions, submissions from others, and from our subject matter experts.
4. Conduct some analysis, research some ideas, and/or find something interesting.
5. Write your findings in a 3-page-or-less tiny paper.
    1. For more information on the structure of tiny_ papers_, click[ here](https://iclr.cc/Conferences/2023/CallForTinyPapers).
    2. Contributors may also append proofs, data, additional experiments, etc. to their Tiny papers if they wish.
6. Submit an abstracts (25 SEP 2023) and then a paper (29 SEP 2023).
7. Await notification on peer-review.
8. Prepare a poster or slides as requested.
9. Attend the explanatory workshop 7 NOV 2023.
10. See your work contribute to our integrated proceedings in January 2024.


## Citing This Program:



* If you publish work that utilizes the SDNist Deidentified Data Tool, please cite the software. Citation recommendation:

        Task C., Bhagat K., and Howarth G.S. (2023), SDNist v2: Deidentified Data Report Tool, National Institute of Standards and Technology, [https://doi.org/10.18434/mds2-2943](https://doi.org/10.18434/mds2-2943) (NOTE: DOI is not yet active, but should be by 1 MAR 2023).

* If you publish work that utilizes the NIST Diverse Community Excerpt Data, please cite the resource. Citation recommendation:

        Task C., Bhagat K., and Howarth G.S. (2023), NIST Diverse Community Excerpt Data, National Institute of Standards and Technology,[https://doi.org/10.18434/mds2-2895](https://doi.org/10.18434/mds2-2895)   (NOTE: DOI is not yet active, but should be live by 1 MAR 2023).

* We plan to package the proceedings of this program NIST Special Publication and we will provide detailed citation information upon publication.


## Hints,Tips, and Recommendations:



* This program is designed to encourage apples-to-apples comparisons of various synthetic generator and de-identification techniques. Following these tips improves the likelihood of fair, meaningful comparisons.
* Read through the [SDNist](https://github.com/usnistgov/SDNist) and [NIST Diverse Community Data Excerpts](https://github.com/usnistgov/SDNist/tree/main/nist%20diverse%20communities%20data%20excerpts) READMEs.
* You will submit CSV data and your abstract. We will package those along with the SDNist evaluation reports in the research acceleration bundle.
* There are two main abstract types: those asserting publicly verifiable formal privacy (e.g., differential privacy), and everything else. To participate in the verifiable formal privacy track, you are expected to share a link to your code base so the community can verify your claims.
* The data has 22 features. In order to facilitate comparisons of techniques we recommend deidentifiying the entire feature set or choose one of the following subsets:
    * Full features without weights or INDP
    * Basic 9 features: AGEP, SEX, MSP, RAC1P, HOUSING_TYPE, OWN_RENT, EDU, PINCP_DECILE, DVET, DEYE
    * Small categorical: SEX, RAC1P, PUMA, PINCP_DECILE, OWN_RENT
    * Tiny categorical:  RAC1P, PUMA
* If you use differential privacy we ask you to provide values of epsilon and delta. If using a relaxation of differential privacy (e.g., Rényi DP), we ask you to convert your privacy guarantees to epsilon and delta values and highly recommend you set delta = 10<sup>-5 </sup>and from there determine your value of epsilon.


## Timeline:

These dates are subject to change.

|     Date     |&nbsp;-- &nbsp;| Event                                           |
|  ---------:  |    : --:      | :------------------------------------------     |
| 21 FEB 2023  |      --       | SDNist V2 launch CRC open for submissions       |
|  7 MAR 2023  |      --       | CRC releases instructional video                |
| 13 MAR 2023  |      --       | Office hours session 1 (11AM ET)                |
| 20 MAR 2023  |      --       | CRC releases call for abstracts for Exploratory |
| 22 MAR 2023  |      --       | Office hours session 2 (11AM ET)                |
|  5 MAR 2023  |      --       | Office hours session 3 (11AM ET)                |
| 19 APR 2023  |      --       | Office hours session 4 (11AM ET)                |
|  1 MAY 2023  |      --       | Notifications / release of Exploratory agenda   |
|  3 MAY 2023  |      --       | Office hours session 5 (11AM ET)                |
|  9 MAY 2023  |      --       | CRC closes for submissions                      |
| 16 MAY 2023  |      --       | ***Exploratory Workshop***                      |
|              |               | - Final release of acceleration bundle          |
|              |               | - Release of call for abstracts/papers          |
| 14 JUN 2023  |      --       | Office hours session 6 (11AM ET)                |
| 12 JUL 2023  |      --       | Office hours session 7 (11AM ET)                |
| 15 AUG 2023  |      --       | Office hours session 8 (11AM ET)                |
| 12 SEP 2023  |      --       | Optional early abstract submission for feedback |
| 25 SEP 2023  |      --       | Explanatory abstracts due                       |
| 29 SEP 2023  |      --       | Explanatory tiny papers due                     |
| 17 OCT 2023  |      --       | Explanatory tiny paper notifications            |
|  7 NOV 2023  |      --       | ***Explanatory Workshop***                      |
| 12 DEC 2023  |      --       | Optional final tiny paper camera-ready          |
|  9 JAN 2024  |      --       | CRC releases project findings and proceedings   |

