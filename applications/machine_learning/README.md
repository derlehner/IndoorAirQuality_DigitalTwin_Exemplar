# Readme for Applications

### V. MACHINELEARNING

Due to vast range of applications of Machine learning,
its not exceptional to data driven engineering. As were are
working with real time data’s (time-series) based data’s the
utilization of machine learning would occupy big part in
predicting the future forecast.

Time series is a collection of data basted on some period of
time where each data points hold their respective data value
and its attributes. In addition the method of analysing, comput-
ing and predicting these kind of data is know as Time-Series
analysis. Entire time series predicting and analysing works
on with patterns and its seasonal sequences of behaviour.
These mathematical patters sometimes either visible directly
or need to be computed further with data’s with its attributes
if needed eg. Regression. This time series can me denoted by
chronological order over some period of years, months, weeks
or even in hours and minutes. most of the time these time based
data are used to be Univariate (doesn’t depend on internal
factors), But could be depend on external factors. For example
if we take temperature forecast as example for period of 1
day its not dependant on time (which is internal attribute) but
its depends on external factors such as environment, weather,
location and so on... As we plan to use this data for our
predicting the futre by an Machine learning algorithm there is
some factors to be noted as follows for better understanding
of what we going to do:

- Trend
- Seasonality
- Cyclic Variations
- Internal and External factors

A. Trend

Its nothing but one of characteristic of a data which says
about increasing or decreasing trend. This can be easily
calculated by averaging the a specific amount of past data.


B. Seasonality
Its about extracting or reviewing our data weather does it
contain any seasonal variations (eg. any sequence of change
which occurs often based on something). For better under-
standing from our temperature example from before we can
say at each day night will be little low heat then in morning
time. This is due to time and this can be taken as seasonality
changes. Any frequent changes can be referred as seasonality
if the frequency it next change is more or less same as their
past changes.
C. Cyclic Variations
Cyclic Variations are more or less same as ”Seasonality”
as we described it earlier but the difference is this occurs
not more often like seasonality. In seasonality there is high
probability that it will occur each day. In here it could happen
often but not as frequent. There is not in need of frequency
of changes should be same as their past.
D. Internal and External factors
As this is more common and important factor to data
observations predicting right factors will reflect the accuracy of
predicting in our final results. All internal and external factors
should be taken into account and it should be checked by
means of correlation method to our data that is to be compared.
And whatever factors which affects up to observable level it
should be considered as important factor.
For our machine learning case there are the steps to be
followed:

- Data Abstraction
- Pre-process and Data Wrangling
- Choose appropriate Algorithm
- Train, Test, Validate the model
- Efficiency and Loss function
- Final Algorithm and prediction
Further upon theses if there is need we need to use further
processing like ”Smoothing Data”, ”Out-layers”, ”Data Noise
Reduction”, ”Regression Techniques” and ”Biases - Variance
estimation”.
E. ML Model
Since our data is Univariate and Based on Time we can use
ARIMA (AutoRegressive Integrated Moving Avarage) model
for our case. ARIMA is a type of AR (AutoRegressive Model).
Auto Regression is common statistical way used that are
used more commonly if we want to predict future based on
past data we hold. Before we start our model we just have
raw data which has undoubtedly a lot of noise and much
move outlayers. According to “book” it is neccessarry to
“Stationary” our data to train our model it is kind of pre-
processing state i.e preparing our data before streaming our
data to the model. Stationary is nothing but making our data
which exhibits or computing it to have constant mean, variance
and autocorrelation. If the data is already said to have constant
values of those then its already stationary details shown 