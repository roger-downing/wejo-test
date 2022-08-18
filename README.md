# wejo-test
Wejo recruitment test code and data

This is a simple public repository holding some code and data we use to test candidates as part of our recruitment process.

In the "data" directory is a file "data.zip". This contains two source data files, both in CSV format. There is also a file "taxi_zones.zip" which is useful for an optional final question.

In the "code" directory are two files. One is a working Python script and the other is a text file containing Python code.

## Test questions
### Python coding
1. What does the code in the file "example-1.py" do? Give a text description of its output.
2. Do you have any suggestions on how this code could be improved to run more quickly?
3. Find all the mistakes in the Python code in the file "example-2.txt" and correct them, provide the output to show you have found them all.

### Data analysis
Download the file "data.zip" and unzip it on your machine. Inside are two files. Load the file "taxis_tripdata.csv" in your preferred data analysis tool and answer these questions.

1. How many rows of data are there in this file?
2. How many different vendor IDs are included?
3. What is the average count of passengers over all trips?
4. If trips with a passenger count of zero are excluded, what is the new average?
5. Looking at passenger counts, what is likely to be the correct maximum number of occupants? This information has been manually entered by the driver of the taxi.

If payment types are as follows:
| Type | Name |
| ---- | ---- |
|  1   | Credit card |
|  2   | Cash |
|  3   | No charge |
|  4   | Dispute |
|  5   | Unknown |
|  6   | Voided trip |

6. What is the total amount of fares paid in cash?

Using the pickup time to indicate the date of a trip:
7. Which day was the quietest?

Now you must also use the second CSV file "taxi+_zone_lookup.csv".
8. How many trips started in the borough of Queens?
9. How many trips ended in Staten Island?
10. How many trips started in Manhattan on April 4th and ended in Brooklyn?
11. Between which two boroughs were there the most daily trips?
12. On which day? 

An optional final question:
Geospatial data is a very important part of what Wejo do. Choropleths are maps where different parts are coloured according to a key or a scale. Included in this repository is a file
called "taxi_zones.zip" which is some geospatial data in ESRO Shapefile format.

Can you also use the file "taxi_zones.zip" to make a map of New York where the different boroughs are coloured according to the total number of trips starting there?
