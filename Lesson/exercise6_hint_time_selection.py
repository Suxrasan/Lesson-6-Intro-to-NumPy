
 " ... stuff that was coded earlier ... "
 
 for i in range(1926, 2016):
  # Create variables for this and last year
  this_year = i
  last_year = this_year - 1
  
  # Calculate numerical values for December the 1st and Last day of February (29th)
  dec = last_year * 10000 + 1201
  feb = this_year * 10000 + 229
  
  # Create condition to select data from the data
  winter_cond = (MYDATA[:,1] >= dec) & (MYDATA[:,1] <= feb)
  
  # Use numpy.extract function to select such time window from MYDATA
  
 
