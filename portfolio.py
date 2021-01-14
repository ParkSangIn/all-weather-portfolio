import pandas as pa
import yfinance as yf
import math

all_weather_ratio = dict(
	bci=0.08, 
	edv=0.16,
	emlc=0.07,
	iau=0.08,
	ltpz=0.20,
	vclt=0.05,
	vea=0.12,
	vti=0.12,
	vwo=0.12)

all_weather_price = {}

for ticker in all_weather_ratio.keys():
	all_weather_price[ticker] = yf.Ticker(ticker).history(period='1d').tail(1)['Close'].iloc[0]

maximum = float(input("Enter a total amount : "))

minimum = 0

for (t, r), (t, p) in zip(all_weather_ratio.items(), all_weather_price.items()):
	print(t, r, p, math.floor(maximum * r / p))
	minimum += math.floor(maximum * r / p) * p

print(minimum)

calculated_total = 0
variable = maximum
while calculated_total < maximum:
	calculated_total = 0
	all_weather_num_temp = {}
	for (t, r), (t, p) in zip(all_weather_ratio.items(), all_weather_price.items()):
		calculated_total += math.floor(variable * r / p) * p
		all_weather_num_temp[t] = math.floor(variable *r / p)
	variable += 1
	if calculated_total < maximum:
		last_saved = calculated_total
		all_weather_num = all_weather_num_temp

print(last_saved)
print(all_weather_num)