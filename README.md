# OPC-DA-PY-P7 Project


## 1.1 Purpose 
This project has been created in a context of Application developer learning path provided by OpenClassRooms. This project is a pratice for evaluation. The practice description is [here](https://openclassrooms.com/fr/projects/158/assignment) (Description in French)

## 1.2 Solution description

The proposed solution is to develop a web application. From a single page, user submits a request to get a location adress. The solution mocks a bot chatting with the end users
The answer provides the following elements : 

* 1 - The adress of the location if it exists.
* 2 - The map with a maker for the location if it exists. 
* 3 - Some content related to the spoted area if exits.
* 4 - In case the bot is not able to provide answer then bot uses appropriate answer. 

### 1.2.1 Integrated features to the solution. 
To satisfy the business need , several features have been implemented 

#### 1.2.1.1 - Parser :
From the raw user apply a pattern in order to identify the location. 
```
project
│   README.md   
│   ...
└───p7app
│   └───utils
│       │   parser.py

```

#### 1.2.1.2 Identify the location

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
project
│   README.md   
│   ...
└───p7app
│   └───utils
│       │   google.py

```

#### 1.2.1.3 Getting lat and long 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
project
│   README.md   
│   ...
└───p7app
│   └───utils
│       │   google.py

```


#### 1.2.1.4 Getting information on spoted location 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
project
│   README.md   
│   ...
└───p7app
│   └───static
│       └───js
|            |   index.js

```

#### 1.2.1.5 Displaying map 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
project
│   README.md   
│   ...
└───p7app
│   └───utils
│       │   wikimedia.py

```

# 2. Project settings

## 2.1 Third part software & system

### 2.1.1 Python version 
The solution has been developed from 3.7.5 Python version -> see [Release note](https://www.python.org/downloads/release/python-375/)

### 2.1.2 Flask 
In order to access to database from installation. You have to set up the Python MySQL connector 8.0.18. Please find the link to download [here](https://dev.mysql.com/downloads/connector/python/)

### 2.1.3 Pytest

The setting of the OpenFoodFacts is required for the application usage. You can find the setting procedure for Python [here](https://github.com/openfoodfacts/openfoodfacts-python)
See payload configuration section.


# 3. Project design  

In this section, we follow the different stages (features) to complete in order to achieve the solution.  

 



