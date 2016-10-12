#Hints
Below are a selection of hints for Exercise 6.
As before, they are divided between pseudocode and practical tips.
Good luck!

## Problem 1: NOAA climate data revisited
### Pseudocode
For this problem we need to read in a data file, remove some "bad" values, and then calculate some average values using only parts of the contents of the file. The pseudocode for this case is below.

1. Read in a `.csv` data file using `np.loadtxt()`, separate the values by the commas, and read in only the date and temperature values.
2. Calculate the mean and standard deviation of the temperatures from the data file.
3. Remove any temperature value that is outside ±4 standard deviations of the mean.
  - We'll need an empty list to store the "bad" value locations
  - We can use a `for` loop to loop through all of the temperature values and check whether they are (1) less than the mean value minus 4 times the standard deviation, or (2) greater than the mean value plus 4 times the standard deviation.
  - If so, we can append the index value from the for loop to the array of bad values.
  - Then, we can loop through the "bad" value list after checking all of the values and remove values from the data using `np.delete()`.
    - We'll have to use the `np.reverse()` method to reverse the list of "bad" index values first so we don't end up removing the wrong values. *For example, if we remove value 4 from the list, the indexes of all values below the old value 4 will decrease by 1. If we remove the higher index values first, everything should be OK*.
4. Now that we have clean data, we need to calculate the seasonal average values by looping through all of the years in the dataset, calculating seasonal averages, and appending them to a list.
  - We should first make a pair of empty lists for the seasonal average temperatures before starting the loop through the years.
  - The `for` loop should start in year 1927 since we don't have data for the full winter of 1925. It should end in 2016, since that will make 2015 the last year in the calculated averages.
  - Finding the months and years will be tricky, since the date values are numerical when NumPy reads them.
    - We can start by defining two values to represent this year and last, where last is just the year from the `for` loop minus 1.
    - Since the dates are simply 8 numbers, where the first four are the year, we can make a comparison for a given year by multiplying it by 10000. For example, 1927 * 10000 = 19270000. Like this, we can use the other 4 digits to check for specific months.
    - We will need to identify the seasonal temperature range using a range of dates. Since winter is December of the last year through February, that number range should start at (previous year * 10000) + 1201 and end at (current year * 10000) + 0229. The same logic applies to the summer period.
    - Once we have the numbers that correspond to December 1 and February 29, for example, we just need to find the dates in the data file that match for a given year. The dates must meet two conditions to be in the range: Any date that is greater than or equal to the first value, **and** less than or equal to the second should be in the seasonal range.
    - With the ranges identified, we can use `np.extract()` to create a NumPy array of just the selected temperatures for summer and winter of a given year.
    - Then we can simply append the `.mean()` values of each array, along with the year, to the lists we created before the `for` loop started.
5. Finally we'll need to write the output to a file using `np.savetxt()`.

### Practical tips
1. Skipping headers.
2. Loading only certain "columns" of data from a `.csv` file.
3. Detecting and removing "bad" values.
4. Sorting data using NumPy.
5. Selecting data for a given range of dates.

## (*Optional*) Problem 2: Volcanoes again? Dealing with tricky data files
### Pseudocode

### Practical tips
