# Readme for Applications
## Contents

- 1 Machine Learning Introduction
   - 1.1 Trend
   - 1.2 Seasonality
   - 1.3 Cyclic Variations
   - 1.4 Internal and External factors
- 2 ML Model
### MACHINE LEARNING Introduction

As we plan to use this data for our
predicting the futre by an Machine learning algorithm there is
some factors to be noted as follows for better understanding
of what we going to do:

- Trend
- Seasonality
- Cyclic Variations
- Internal and External factors

#### 1.1 Trend

Its nothing but one of characteristic of a data which says
about increasing or decreasing trend. This can be easily
calculated by averaging the a specific amount of past data.


#### 1.2 Seasonality

Its about extracting or reviewing our data weather does it
contain any seasonal variations (eg. any sequence of change
which occurs often based on something). For better under-
standing from our temperature example from before we can
say at each day night will be little low heat then in morning
time. This is due to time and this can be taken as seasonality
changes. Any frequent changes can be referred as seasonality
if the frequency it next change is more or less same as their
past changes.
#### 1.3 Cyclic Variations
Cyclic Variations are more or less same as ”Seasonality”
as we described it earlier but the difference is this occurs
not more often like seasonality. In seasonality there is high
probability that it will occur each day. In here it could happen
often but not as frequent. There is not in need of frequency
of changes should be same as their past.
#### 1.4 Internal and External factors
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

### 2 ML Model
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