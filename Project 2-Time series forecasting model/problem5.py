from problem4 import *
import matplotlib.pyplot as plt
print("\n ********************     Question 5.1    ******************* ")
def money_growth(data, label):
    money = []
    principal = 100
    for i in range(len(data)):
        if data[label].values[i] == "+":
            # if we predict next day is up, we will buy the stock at open price and sell at close price.
            principal = (principal / data['Open'].values[i]) * data['Close'].values[i]
            money.append(principal)
        else:
            # if we predict next is up, we do nothing.
            money.append(principal)
    return money


# get ZG stocks trade history base on W =2,3 and 4 and ensemble
X=range(len(ZG_testing))
W2_history = money_growth(ZG_testing, 'W2_label')
ensemble_history = money_growth(ZG_testing, 'ensemble_label')
buy_and_hold_X = [0,len(ZG_testing)]
buy_and_hold_Y = [100,(100/ZG_testing['Open'].values[0])*ZG_testing['Close'].values[len(ZG_testing)-1]]


# plot the results
# For ZG stocks
plt.plot(X, W2_history, label="ZG best W:2")
plt.plot(X, ensemble_history, label="ZG ensemble")
plt.plot(buy_and_hold_X, buy_and_hold_Y, label="ZG buy and hold")
plt.legend()
plt.show()

print("\n ********************     Question 5.2    ******************* ")
print(" Any patterns: "
      "\n 1.W=2 has the same trend with ensemble result"
      "\n 2.About at the end of 4 years(280 days) the result of buy-and-hold exceed the result of ensemble")


