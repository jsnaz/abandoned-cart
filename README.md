# abandoned-cart

Link for data:
https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data?select=articles.csv

## Structure of the project
The project is made of two modules (services).
- dbadmin
- recommender 
Breaking down the project into two services allows the separation of concern.  
These two services are very different (one is for infrastructure, the other one is purely the recommendation engine).  
In a real company, these two services would be done by two different teams.  
DBAdmin would be done by a Data Engineering team.  
Recommender would be done by a Data Science team.


### Description of the services

#### DBamin
DBAdmin is a service responsible the administration the project infrastructure on Google Cloud.  
DBAdmin does the following:
- Creation of the project dataset
- Creation of the article table
- Populating the article with table from the csv file (downloaded from Kaggle) 
- Creation of the customer table
