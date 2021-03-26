# Socrata FME

* Is it's own application that handles ETL 
* FME can create a dataset
* FME's log file tells you about eh writing process
* FME can UPSERT (Append), Delete, or Replace Rows
* Stands for Feature Manipulation Engine
    * Pulling data in
    * Transform the data
    * no coding required
* Use when transformations are a complex or dont fit the basic transformations avaialble in edit data 
* Use in conjunction with Windows Task Scheuler to have it run regularly
* Select read in data (db with right arrow and plus sign in toolbar)
    * enter in the data source of the data you want to use it 
    * features are the rows of data 
    * attributres are the columns
* Select write in data (right arrow to db and plus sign in toolbar)
    * enter in the type of data you want to end up with
* open transformer gallery to bring up transformer list 

**Key transformers:**
    * Reprojector - Convert from your local projection to Socrata friendly Latitude/Longitude (LL-83)
    * DateFormatter - Convert from any date format into Socrata friendly ISO8601
    * AttributeManager - Rename, reorder, calculate, remove columns

**Resources**
* Socrata-FME-Templates - http://socrata.github.io/connectors/#fme-templates
* FME Platform - https://www.safe.com/how-it-works/ 
* 