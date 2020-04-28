# OPC-DA-PY-P7 Project


## 1.1 Purpose 
This project has been created in a context of Application developer learning path provided by OpenClassRooms. This project is a pratice for evaluation. The practice description is [here](https://openclassrooms.com/fr/projects/158/assignment) (Description in French)

## 1.2 Solution description

The proposed solution is to develop a web application. From a single page, user submits a request to get a location adress. The solution mocks a bot chatting with the end users
The answer provides the following elements : 

* 1 - The address of the location if it exists.
* 2 - The map with a maker for the location if it exists. 
* 3 - Some content related to the spotted area if exits.
* 4 - In case the bot is not able to provide answer then bot uses appropriate answer. 

### 1.2.1 Integrated features to the solution. 
To satisfy the business need , several features have been implemented 

#### 1.2.1.1 - Parser :
From the raw user entry apply a pattern in order to identify an address request. The pattern to identify the address
is a follow : 'adresse'+request+' ?'
```
project
│   README.md   
│   ...
└───p7app
│   └───utils
│       │   parser.py
```

#### 1.2.1.2 Identify the location
In order to retrieve the location, we need to identify the location id. after extracting the request from user entry,
we use google map search api being able to give the location id from a text request. Find the API notes see 
[here](https://developers.google.com/places/web-service/search)
```
project
│   README.md   
│   ...
└───p7app
│   └───utils
│       │   google.py
```

#### 1.2.1.3 Getting lat and long 
Once the place has been retrieved we will get the latitude & longitude from Google details API
. see [here](https://developers.google.com/places/web-service/details)
```
project
│   README.md   
│   ...
└───p7app
│   └───utils
│       │   google.py
```

#### 1.2.1.4 Getting information on spotted location 
The purpose is to provide 4 lines of description about the location retrieved according latitude and longitude
 and also URL. In order to get those information , it has been used media wiki API. See description
 [here](https://www.mediawiki.org/wiki/API:Tutorial)
```
project
│   README.md   
│   ...
└───p7app
│   └───utils
│       │   wikimedia.py
```
#### 1.2.1.5 Handling user request
The management of the request set at the front level is managed at the back level as a request 
object. The answer is returned after executing different features API calls described above.
```
project
│   README.md   
│   ...
└───p7app
│   └───models
│       │   request.py
```



#### 1.2.1.5 Displaying map 
Once answer has been received by the back end part then display the map at the view level. In order to manage the display 
we use map function provided by Google. see documentation [here](https://developers.google.com/maps/documentation/javascript/tutorial?hl=fr) 
```
project
│   README.md   
│   ...
└───p7app
│   └───static
│       └───js
|            |   index.js
```

# 2. Project settings

## 2.1 Third part software & system

### 2.1.1 Python version 
The solution has been developed from 3.7.5 Python version -> see [Release note](https://www.python.org/downloads/release/python-375/)

### 2.1.2 Flask 
The solution has been developped on top of Flask 1.1.2 version -> see  [here](https://flask.palletsprojects.com/en/1.1.x/)

### 2.1.3 Requests 
In order to manage call to API and answer the librairy requests version 2.23.0 has been used -> see  [here](https://2.python-requests.org/en/master/)

### 2.1.4 Pytest
Into the project, units tests have been provided to execute. The same have been executed by usin PYTest librairy. see -> [here](https://docs.pytest.org/en/latest/)
See payload configuration section.


 



