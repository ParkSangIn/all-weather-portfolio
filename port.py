def cal_percentage(amount, port_price, port_shares):
    port_ratio = {}
    for (t, n), (t, p) in zip(port_price.items(), port_shares.items()):
        port_ratio[t] = (n * p) / amount
    return port_ratio

def print_ratio(port_ratio):
    for t, r in port_ratio.items():
        print("{}\t: {} %".format(t, round(r * 100, 2)).expandtabs(5))

if __name__ == '__main__':

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

    maximum = float(input("Enter a total_temp amount : "))

    # 곱하는 총액을 maximum으로 했을 때 나오는 투자 결과
    # minimum = 0
    # for (t, r), (t, p) in zip(all_weather_ratio.items(), all_weather_price.items()):
    #     print(t, r, p, math.floor(maximum * r / p))
    #     minimum += math.floor(maximum * r / p) * p
    # print(minimum)

    variable = maximum # 최댓값을 도출하기 위한 변수 - 초기값은 maximum으로 설정
    while True:
        total_temp = 0 # 계산을 위한 일시 저장 공간
        all_weather_shares_temp = {}

        for (t, r), (t, p) in zip(all_weather_ratio.items(), all_weather_price.items()):
            total_temp += math.floor(variable * r / p) * p
            all_weather_shares_temp[t] = math.floor(variable *r / p) # 종목당 갯수 저장
        
        if total_temp < maximum:
            total = total_temp
            all_weather_shares = all_weather_shares_temp
        else:
            break

        variable += 1 #증액

    print("result : {0}".format(total))
    print(all_weather_shares)

    result = 0
    for (t, p), (t, n) in zip(all_weather_price.items(), all_weather_shares.items()):
        result += n * p

    print("result check : {0}".format(result))
    print_ratio(cal_percentage(total, all_weather_price, all_weather_shares))

