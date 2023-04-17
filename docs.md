# core: Database
This xml strucure contains the main pieces of information to document in a dataset
## dataset: Table
Documentation related to dataset type, function, and interpretation.
### attribute: DataCategory
A classification of original into broad categories of mechanisms. e.g., neighborhood economic activity v.s. envioronmental readings.
This attribute is populated with the following values: 
* **EnvironmentalData**: Data which refer to measurements of environmental contaminants/conditions such as air pollution, light, noise, and temperature.
* **DemographicData**: Data which refer to commonly used demographic variables such as race/ethnicity, income, eductional level, and household make up.
* **PropertyData**: Data which refers to condition, values, or age of individual properties in a region.
* **SafetyData**: Data which refers to observations about crime, safety, and other related risk factors in a region.
* **AccessData**: Data which refers to observations about proximity and access to certain neighborhood resources.
* **EconomicActivityData**: Data which refers to measurements of economic activity in a certain region.
### attribute: DataType
A classification of original data format which has implications on how the data can be stored, processed, and interpreted. In essence, it defines the main population unit of interest for this data
This attribute is populated with the following values: 
* **IndividualData**: Data that are linked to an individual patient.
* **OrganizationData**: Data that are linked to associations, institutions, agencies, businesses, political parties, schools, etc..
* **HouseholdData**: Data that are linked to a person or a group of persons who share the same dwelling unit and common living arrangements.
* **EventData**: Data that are linked to any type of incident, occurrence, or activity. Events are linked to GeographicUnits
* **LocationData**: Data that are linked to a some GeographicalUnit.
### attribute: GeographicUnit
Any entity that can be spatially defined as a geographic area, with either natural (physical) or administrative boundaries.
This attribute is populated with the following values: 
### attribute: TimeUnit
Any period of time: year, week, month, day, or bimonthly or quarterly periods, etc.
This attribute is populated with the following values: 
* **NoneUnit**: Observation is not tied to a particular time instant or period.
* **InstantUnit**: Capture one-time, individual occurrences, with a limited, or short duration.
* **MonthlyUnit**: Capture on going processes with a one-month update cycle.
* **QuarterlyUnit**: Capture on going processes with a one-quarter update cycle.
* **YearlyUnit**: Capture on going processes with a one-year update cycle.
### attribute: CollectingOrganization
The name of the original organization that collected the data. The data may have been subsequently processed, but this captures the original data source.

This attribute is a text field.

### attribute: Name
An internal unique name that we will refer to this data asset.

This attribute is a text field.

### attribute: ProcessingCode
A link to a computational notebook that converts the source data into the final format. This includes cleaning, reformatting, and aggregating.

This attribute is a url.

### attribute: TermsOfUse
A description of any stipulations of how this data can be used

This attribute is a text field.

## quality: Table
Documentation related to data quality.
### attribute: Dataset:Name
An internal unique name that we will refer to this data asset. All quality records are linked to a particular dataset. 
This attribute is populated with the following values: 
### attribute: Missingness
A description of any incompleteness in this dataset.
This attribute is populated with the following values: 
* **InRecordMissing**: The collected records have known missing cell values marked by a common indicator such as None, NaN, etc.
* **CompletelyMissing**: The collected records are known to be incomplete where known units are missing from the dataset.
### attribute: Incorrectness
A description of any incorrect values in this dataset.
This attribute is populated with the following values: 
* **SensorFailure**: The collected records have apparently incorrect values due to failures in the collection device
* **ResponseBias**: The collected records have apparently incorrect values due to survey subjects misrepresenting (either intentionally or unintentionally) the data
* **EstimationError**: The collected records have apparently incorrect values due to estimation
* **CodingError**: The collected records have apparently incorrect values due to inconsistent data coding
