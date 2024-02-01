# CRC DATA AND METRIC BUNDLE

## Version 1.2
* Added new deid datasets:
  * aifairness_smote
  * aindo_synth_Aindo
  * anonos_sdk_Anonos
  * rsynthpop_ipf
  * smartnoise_aim
  * ydata_fabric_synthesizers_YData
  * ydata_synthetic_ctgan_DCAICommunity
* Update index.csv to contain new deid data files.
* Change library name of subsample deid data to: subsample
* Fixes to the notebooks.
* Freeze versions in requirements.txt.

* Added tutorial ipython notebooks for demonstrating the use of **crc data and metric bundle**.
    * Notebook0: Basic introduction notebook.
    * Notebook1: K-marginal barplot notebook.
    * Notebook2: Imposter plot notebook.
    * Notebook3: Race distribution notebook.
    * Notebook4: Privacy utility tradeoff notebook.
* Updated deid_data:
    * Added new deid data samples for *sdcmicro_k_anonymity* and *sdcmicro_pram*.
    * Added new deid data samples: *subsample_1pcnt* and *subsample_5pcnt*.
    * Created new SDNIST evaluation reports for all the deid data samples. New SDNIST evaluation reports:
        * Added explanatory text to inconsistencies and UEM metric, fixed typographic errors, improved formatting in privacy section, renamed 'k-marginal breakdown' to 'worst-performing PUMA breakdown' and adjusted json structure accordingly.
        * Improved readability of propensity image
        * Fixed feature space size in UEM
        * Fixed deid percentage in UEM metric
        * Added 1% and 5% sampling error on the k-marginal
        * More detailed variant labels including new columns to align with index csv

* Updated *index.csv* file:
    * Added new deid data samples in the index.
    * Updated index file data columns.
* Updated *diverse_communities_data_excerpts*.
    * Updated *INDP* feature description in *data_dictionary.json*.

## Version 1.1
* Added tutorial ipython notebooks for demonstrating the use of **crc data and metric bundle**.
    * Notebook0: Basic introduction notebook.
    * Notebook1: K-marginal barplot notebook.
    * Notebook2: Imposter plot notebook.
    * Notebook3: Race distribution notebook.
    * Notebook4: Privacy utility tradeoff notebook.
* Updated deid_data:
    * Added new deid data samples for *sdcmicro_k_anonymity* and *sdcmicro_pram*.
    * Added new deid data samples: *subsample_1pcnt* and *subsample_5pcnt*.
    * Created new SDNIST evaluation reports for all the deid data samples. New SDNIST evaluation reports:
        * Added explanatory text to inconsistencies and UEM metric, fixed typographic errors, improved formatting in privacy section, renamed 'k-marginal breakdown' to 'worst-performing PUMA breakdown' and adjusted json structure accordingly.
        * Improved readability of propensity image
        * Fixed feature space size in UEM
        * Fixed deid percentage in UEM metric
        * Added 1% and 5% sampling error on the k-marginal
        * More detailed variant labels including new columns to align with index csv

* Updated *index.csv* file:
    * Added new deid data samples in the index.
    * Updated index file data columns.
* Updated *diverse_communities_data_excerpts*.
    * Updated *INDP* feature description in *data_dictionary.json*.