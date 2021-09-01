# Forecasting future data by Machine Learning Model

## Contents

1. Overview of the implementation
 2. Input Data
 3. Data Preparation and training
 4. Output
 5. About the Model and Factors considered for Training:
	 1. Trend
	 2. Seasonality
	 3. Cyclic Variations
	 4. Internal and External factors

[](#section-1)


### Overview of the implementation <a name="section-1"></a>
The goal of integrating temporal AI model for our scenario is to predict the certain time period of future from current real time. lets say '$t$' is real-time and we estimate the future of 30 minutes. the model's task is to estimate the value of $t+30$ which considers several factors as parameters for example our past data, trend, noise, seasonality with addition to make our model more robust external factors like state of windows/doors (open or closed), number of peoples in room, air ventilation or air-conditioner (on or off) can also considered in our model. This model should be based on ARIMA (Auto Regressive Integrated Moving Average) used to estimate the basic $t+30$ value and based on our internal and external factors the results changes according to respective time.
Then the final predicted data flows to the visualization part for comparison and to get overview to the client via inferencing our model either in-environment or remote devices via cloud based inference (depending on individual cases and usage). 
Future upgrade could based on automating and upgrading model's knowledge itself to achieve robust results. But ever since the below points represents the current challenges.


#### Input data
the data that  we planed to use to feed to the ML model will be taken as Time Series database as source. the format will be as following table it will be in `str` Data Type.

```json
"Time","s30076"
2021-08-18 13:36:01,469.11 ppm
2021-08-18 13:36:07,468.87 ppm
2021-08-18 13:40:18,478.92 ppm
```
#### Data Preparation and training

Before continuing the data should be converted pandas dataframe structure so it will be easy to feed it for training the model. Since we use `pandas` lybrary to manage the data its required that we use the date stamp in specific format the standard format is shown [here](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).

```json
% reading the csv
df = pd.read_csv('co2_data.csv')
% modyfying 'Time' column in format we need 
df['Time'] = pd.to_datetime(df["Time"], format='%Y-%m-%d %H:%M:%S')
```


After that the data is been transferred in following way:
ds spcifies DateTimes Stamp, y specifies the values for the respective time

| ds  				| y   		| 
| :---        			|    :----:   	|     
| 2021-08-18 13:36:01   | 468.87     | 
| 2021-08-18 13:40:18   | 478.95 	|
| 2021-08-18 15:38:14   | 456.43     | 

The data then is splited wihtout any bias as Trainng and Test sets in the format of 80-20 split. the we use the ARIMA (Auto Resgressive Integrated Moving Avarage) as our model.
the the data uses pretrained model for the runningt he inference which can be done by running the 'prediction.py' script under 'application/machine_learning/'.

### Output
This will run the pretrained model and send the predicted values to the Time Seires Visulaization for visualising process.

The output data will be same as feeded data for example: It will be in Pandas dataframe structure.

| future  				| predicted value   		| 
| :---        			|    :----:   	|     
| 2021-08-18 13:36:01   | 478.87     | 
| 2021-08-18 13:40:18   | 448.95 	|
| 2021-08-18 15:38:14   | 406.43     | 

### Implementation and Inferencing
For Implinting the trained model into our each raspberry pi's we use the Auto-Deployment script inder '/physical_twin/hardware_setup/auto_deployment.py'

Procedures:
add the local `ip_address` of all connected respberries in the string. It will always have the default path to deploy the script under `/home/pi/IndoorAirQuality_Digital_Exemplar`. 
and for inferencing just start the script `prediction.py`

### About the Model and Factors considered for Training
Since our data is Univariate and Based on Time we can use ARIMA (AutoRegressive Integrated Moving Avarage) model for our case. ARIMA is a type of AR (AutoRegressive Model). Auto Regression is common statistical way used that are used more commonly if we want to predict future based on past data we hold. Before we start our model we just have raw data which has undoubtedly a lot of noise and much move outlayers. According to “book” it is neccessarry to “Stationary” our data to train our model it is kind of pre-processing state i.e preparing our data before streaming our data to the model. Stationary is nothing but making our data which exhibits or computing it to have constant mean, variance and autocorrelation. If the data is already said to have constant values of those then its already stationary details shown.
Harijill@7
As we plan to use this data for our predicting the futre by an Machine learning algorithm there is some factors to be noted as follows for better understanding of what we going to do:
- Trend
- Seasonality
- Cyclic Variations
- Internal and External factors


#### 1.1 Trend

Its nothing but one of characteristic of a data which says about increasing or decreasing trend. This can be easily calculated by averaging the a specific amount of past data.

#### 1.2 Seasonality

Its about extracting or reviewing our data weather does it contain any seasonal variations (eg. any sequence of change which occurs often based on something). For better understanding from our temperature example from before we can say at each day night will be little low heat then in morning time. This is due to time and this can be taken as seasonality changes. Any frequent changes can be referred as seasonality if the frequency it next change is more or less same as their past changes.
#### 1.3 Cyclic Variations
Cyclic Variations are more or less same as ”Seasonality” as we described it earlier but the difference is this occurs
not more often like seasonality. In seasonality there is high probability that it will occur each day. In here it could happen often but not as frequent. There is not in need of frequency of changes should be same as their past.
#### 1.4 Internal and External factors
As this is more common and important factor to data observations predicting right factors will reflect the accuracy of predicting in our final results. All internal and external factors should be taken into account and it should be checked by means of correlation method to our data that is to be compared. And whatever factors which affects up to observable level it should be considered as important factor. For our machine learning case there are the steps to be followed: 
- Data Abstraction
- Pre-process and Data Wrangling
- Choose appropriate Learnining function
- Efficiency and Loss function
- Final Algorithm and use for inference

Further upon theses if there is need we need to use further processing like ”Smoothing Data”, ”Out-layers”, ”Data Noise Reduction”, ”Regression Techniques” and ”Biases - Variance estimation”.
