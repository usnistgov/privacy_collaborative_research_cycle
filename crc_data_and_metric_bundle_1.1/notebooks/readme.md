## CRC Release Bundle

### Setup for running jupyter notebooks:
1. Using a terminal (on max or linux) or powershell (on windows) navigate to the **crc_data_and_metric_bundle_1.1/notebooks** directory.  
2. In **notebooks** directory create a new python virtual environment using following command:  
`python -m venv venv`  
3. Now activate the newly created virtual environment using command:   
on mac or linux  
`. venv/bin/activate`  
on windows  
`. venv/Scripts/activate`  
4. Virtual environment is activated if you see *(venv)* append to the terminal or powershell prompt.  
5. Install python packages:  
`pip install -r requirements.txt`  
6. Now add the virtual environment to the jupyter notebooks:  
`python -m ipykernel install --user --name crc`  
This will add the current activated environment to the jupyter notebooks. This environment can be used in the jupyter notebook by selecting kernel **crc**.   
7. Start jupyter notebook:  
`jupyter notebook`
8. In jupyter notebook menubar go to **kernel** menu, press **change kernel**, and select **crc** kernel from the options.
