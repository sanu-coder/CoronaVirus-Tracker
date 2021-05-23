# CoronaVirus-Tracker
In this project, we required two python modules : 
<h3>1. covid-india : </h3>
    It is the python package for providing data for the COVID-19 cases in India.This can provide data both online as well as offline.
    
   <h4>Installation:</h4>
    For windows :<br>  
    
    pip install covid-india
    
   For linux and Mac :<br> 
    pip3 install covid-india
    
   <h4>Examples:</h4>
   
   <h5>a. All the states :</h5>
   
    from covid_india import states
    print(states.getdata())
   
   This returns a json object which contains the datas of all the states in India.<br>
   <h5>b. Specific state :</h5>
   
    from covid_india import states
    print(states.getdata('West Bengal'))
   
   This returns a json object which contains the datas of all the states in India.<br>
   <h5>c. Total Count :</h5>
   
    from covid_india import states
    print(states.getdata('Total'))
    
   This returns a json object which contains the datas of all the states in India.<br>
   
  <hr>
  
  <h3>2. pywebio : </h3>
  
  PyWebIO provides a series of imperative functions to obtain user input and output on the browser, turning the browser into a “rich text terminal”, and can be used to build simple web applications or browser-based GUI applications. Using PyWebIO, developers can write applications just like writing terminal scripts (interaction based on input and print), without the need to have knowledge of HTML and JS. 
  <h4>Installation:</h4>
  
  Stable version:
  
    pip3 install -U pywebio
  Development version:
  
    pip3 install -U https://code.aliyun.com/wang0618/pywebio/repository/archive.zip
  
