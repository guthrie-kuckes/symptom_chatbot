# Symptom Chatbot For Underserved Populations
### Resiliency Challenge Hackathon Sprint #3




## The Problem: 
 In low-resource areas of Boston, vulnerable populations such as undocumented immigrants and those experiencing 
 homelessness may not have the luxury of visiting hospitals or clinics for baseline COVID-19 screenings. Furthermore, 
 visiting the hospital for baseline screenings that are often inaccurate puts these populations even more at risk. 
 Due to this fact, the severity of all symptoms and cases may go unmonitored. Areas such as Chelsea and Everett have a 
 much higher rate of positive COVID-19 tests than the Boston and Cambridge area which is extremely disconcerting. 
 
## Goals:
* Allows for efficient healthcare delivery and preparedness in areas that exhibit spikes in symptoms
* Equitability in technology-based symptom tracking
* Prevents spread of miseducation through health recommendations regarding specific symptoms
* Reduce time and money spent looking for information on mobile data
* Gather information about populations that popular testing methods may not reach
* Support equity in symptom tracking by having questions in accessible languages and local vernacular 

 [For more information on th problem and solution click here](https://docs.google.com/document/d/1gxbA9LDHWn-PT-baF3bczof_DNbejiGAD6M3sFGeZ8M/edit?usp=sharing)



## Project Specifications
* SMS/Messaging symptom tracker
  - Twilio
  - Symptom checker API
* Data tracking/visualization
  - Vue.js
  - Firebase

## Install Instructions


For mac: 


You need to have homebrew installed. 

To test messaging, you will need to:

- Install the twiliio CLI

     brew tap twilio/brew && brew install twilio
     
- Install pipenv:
    
    brew install pipenv
    
    To test locally and recieve messages, run something like
    
    twilio phone-numbers:update "+15017122661" --sms-url="http://localhost:5000/sms"
    
    (see https://www.twilio.com/docs/sms/quickstart/python)
    
    To run the code, run the followiing to enter the virtual environment
    
    pipenv shell
    
    

    
    

  
