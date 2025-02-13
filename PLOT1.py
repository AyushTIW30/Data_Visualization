import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# price = [40000,48000,30000,50000,60000]
# year = [2014,2015,2016,2017,2018]
# plt.plot(year,price)
# plt.show()
# match = pd.read_csv("sharma-kohli.csv")
# print(plt.plot(match["index"],match["V Kohli"],color="green",linestyle="solid",linewidth=2 ))
# print(plt.plot(match["index"],match["RG Sharma"],color="blue",linestyle='dashdot',linewidth = 5))
# plt.title("Rohit VS Kohli Runs")
# plt.xlabel("season")
# plt.ylabel("Runs score")
# plt.show()

#################################################################

# match = pd.read_csv("sharma-kohli.csv")
# print(plt.plot(match["index"],match["V Kohli"],marker = "+",markersize="10"))
# print(plt.plot(match["index"],match["RG Sharma"],marker="*"))
# plt.title("Rohit VS Kohli Runs")
# plt.xlabel("season")
# plt.ylabel("Runs score")
# plt.show()


#################################################################

match = pd.read_csv("sharma-kohli.csv")
# print(plt.plot(match["index"],match["V Kohli"],label="Kohli"))
# print(plt.plot(match["index"],match["RG Sharma"],label="Rohit"))
# plt.title("Rohit VS Kohli Runs")
# plt.xlabel("season")
# plt.ylabel("Runs score")
# plt.legend(loc="upper right")
# plt.show()


#################################################################

# price = [40000,48000,30000,50000,6000000]
# year = [2014,2015,2016,2017,2018]
# plt.plot(year,price)
# plt.ylim(0,100000)
# plt.xlim(2014.0,2017.0)
# plt.show()



#################################################################

# x = np.linspace(-10,10,50)
# y = 10*x+3+np.random.randint(0,300,50)

# plt.scatter(x,y)
# plt.show()

# bat = pd.read_csv("batter.csv")
# head = bat.head(50)
# plt.scatter(head["avg"],head["strike_rate"],marker='+')
# plt.xlabel("Avg")
# plt.ylabel("Sr")
# plt.show()

# # tip = sns.load_dataset("tips")
# tip = pd.read_csv("tips.csv")
# # a = tip["total_bill"].sort_values(ascending=False)
# # print(a["tip","sex"])
# a = tip.sort_values("total_bill", ascending=False)
# # Now, select the "tip" and "sex" columns from the sorted DataFrame
# result = a[["total_bill","tip", "sex"]].reset_index()
# print(result)
# # plt.scatter(tip["total_bill"],tip["tip"],s=tip["size"])
# # plt.show()



# tip = sns.load_dataset("tips")
# # plt.scatter(tip["total_bill"],tip["tip"],s=tip["size"])
# # plt.plot(tip["total_bill"],tip["tip"],"o")
# plt.show()
##############################################################
# child = [10,5,20,15]
# color = ["red",'green','blue','pink']
# # plt.plot(child,color,kind="bar")
# ############ FOR VERTICAL BAR CHAT    ###########################
# # plt.bar(color,child,color="red")
# ############ FOR VHORIZONTALL BAR CHAT    ###########################
# plt.barh(color,child,color="red")
# plt.show()

#################################################################

df = pd.read_csv("batsman_season_record.csv")
# plt.bar(np.arange(df.shape[0])-.2,df["2015"],width=.2,color="orange")
# plt.bar(np.arange(df.shape[0]),df["2016"],width=.2,color="blue")
# plt.bar(np.arange(df.shape[0])+.2,df["2017"],width=.2,color="green")
# # plt.bar(df["batsman"],df["2015"],width=.5)
# # plt.bar(df["batsman"],df["2015"],width=.10)
# plt.xticks(np.arange(df.shape[0]),df["batsman"],rotation="vertical")
# plt.show()

#################################################################
###              stack /Merging bargraph                     ####


# plt.bar(df["batsman"],df['2015'])
# plt.bar(df["batsman"],df['2016'],bottom=df["2015"])
# plt.bar(df["batsman"],df['2017'],bottom=(df["2015"]+df["2016"]))
# plt.show()


#################################################################
###                 Histogram                           #####
# df = pd.read_csv("vk.csv")
# print(df.describe())
# plt.hist(df["batsman_runs"],bins=[0,20,40,60,80,100,120])
# print(plt.style.available)
arr = np.load("big-array.npy")
# plt.style.use('fast')
plt.hist(arr,bins=[10,20,30,40,50,60,70],log=True)
plt.show()


#################################################################
###                 Pie chart                           #####
# data = [10,20,30,40,50]
# sub = ["Maths","English","Science","Sst","Gk"]
# plt.pie(data,labels =sub)

# plt.show()
# df = pd.read_csv("gayle-175.csv")
# plt.pie(df["batsman_runs"],labels=df["batsman"],autopct="%0.1f%%",colors=["grey","green","red","orange","pink","blue"],explode=[.1,0,.1,0,.1,0,])
# plt.style.use("fivethirtyeight")
# plt.show()


























