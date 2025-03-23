# Python

Please run the main function to reproduce the results of this project. Note that this project requires matplotlib as a dependency.

## Question 1
Please see Question1output.csv.

## Question 2

### a.
![Boxplot](/Boxplot.png)

### b.
Based on this limited sample size, I would not be very confident in this data. However, based on the available data, all of the cell groups differ significantly except for the cd8 t-cells for the following reasons:

100% of the responsive b-cells are present in greater percentages than over 50% of the non-responsive b-cells.

The overlap in percentages between the responsive and non-responsive cd8 t-cells are nearly identical with the first, second, and third quartiles of each being close together.

Nearly 100% of the responsive cd4 t-cells are present in higher percentages than almost 100% of the non-responsive cd4 t-cells.

Nearly 75% percent of the responsive nk cells are present in higher percentages than all of the non-responseive couterparts.

Lastly, roughly 75% of the non-responsive monocytes are present in higher numbers than the all of the responsive monocytes.

# Database

## Question 1
![Rough Schema](/SchemaPrototype.png)
This schema divides the data into the 4 main categories of data used: project data, subject demographics, individual samples, and, for simplicity, cell counts. This design allows data to be accessed quickly with a minimum of unnecessary table references. This is accomplished using the sample, subject, and project IDs, all of which are present in the original data.

## Question 2
Capturing this data in a database would allow for simpler access and data processing. Instead of needing to write more custom code, a simple query can get just the information you need and expect. This will save time and energy. In addition having all of the data together in a database will allow for larger analysises of data where you would otherwise need to load huge amounts of data any time you wanted to analyze it or be limited to analyzing much smaller subsets.

## Question 3
USE CELLDB
SELECT COUNT(SubjectID), Condition FROM SUBJECTS GROUP BY Condition

## Question 4
USE CELLDB
SELECT SAMPLES.SampleID, SAMPLES.SampleType, SAMPLES.Response, SAMPLES.ProjectID, SUBJECTS.Sex, CELLS.BCell, CELLS.Cd8T, CELLS.Cd4T, CELLS.NK, CELLS.Monocyte FROM SUBJECTS INNER JOIN SAMPLES INNER JOIN ON SAMPLES.SampleID=SUBJECTS.SampleID=CELLS.SampleID WHERE SUBJECTS.Condition='melanoma' SAMPLES.sampleType='PBMC' SAMPLES.TimeFromStart=0 SUBJECTS.Treatment='tr1'

## Question 5
First add "CREATE VIEW RESULTS AS" to the beginning of question 4.

### a.
SELECT COUNT(SampleID), ProjectID FROM RESULTS GROUP BY ProjectID

### b.
SELECT COUNT(SampleID), Response FROM RESULTS GROUP BY Response

### c.
SELECT COUNT(SampleID), Sex FROM RESULTS GROUP BY Sex