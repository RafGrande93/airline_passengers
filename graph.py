from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd
import matplotlib.pyplot as plt
def graph(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["Passengers"])
    plt.xlabel("Date")
    plt.ylabel("Passengers")
    plt.figure(figsize=(12, 6))
    df["Month"]=df["Date"].dt.month
    Month = df["Month"].iloc[:12]
    avg_month=df.groupby("Month")["Passengers"].mean()
    plt.bar(Month,avg_month)
    plt.xlabel("Months")
    plt.ylabel("Average Passengers")
    plt.figure(figsize=(12, 6))
    decomposition=seasonal_decompose(df["Passengers"],model='additive',period=12)
    decomposition.plot()
    plt.show()