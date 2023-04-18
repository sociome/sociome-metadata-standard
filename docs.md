# core:  Database
This xml strucure contains the main pieces of information to document in a dataset
## dataset:  Table
Documentation related to dataset type, function, and interpretation.
### attribute: DataCategory 
A classification of original into broad categories of mechanisms. e.g., neighborhood economic activity v.s. envioronmental readings.

 This attribute is populated with the following values: 
### attribute: DataType 
A classification of original data format which has implications on how the data can be stored, processed, and interpreted. In essence, it defines the main population unit of interest for this data

 This attribute is populated with the following values: 
### attribute: GeographicUnit 
Any entity that can be spatially defined as a geographic area, with either natural (physical) or administrative boundaries.

 This attribute is populated with the following values: 
### attribute: TimeUnit 
Any period of time: year, week, month, day, or bimonthly or quarterly periods, etc.

 This attribute is populated with the following values: 
### attribute: CollectingOrganization 
The name of the original organization that collected the data. The data may have been subsequently processed, but this captures the original data source.

This attribute is a string field.

### attribute: Name 
An internal unique name that we will refer to this data asset.

This attribute is a string field.

### attribute: ProcessingCode 
A link to a computational notebook that converts the source data into the final format. This includes cleaning, reformatting, and aggregating.

This attribute is a url field.

### attribute: TermsOfUse 
A description of any stipulations of how this data can be used

This attribute is a string field.

### attribute: WhenAccessed 
The date at which the artifact was accessed

This attribute is a date field.

### attribute: ProcessingOrganization 
The organization that processed the data into its current form.

This attribute is a string field.

## quality:  Table
Documentation related to data quality.
### attribute: Dataset:Name 
An internal unique name that we will refer to this data asset. All quality records are linked to a particular dataset. 

This attribute is a string field.

### attribute: Missingness 
A description of any incompleteness in this dataset.

 This attribute is populated with the following values: 
### attribute: Incorrectness 
A description of any incorrect values in this dataset.

 This attribute is populated with the following values: 
