import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
tips = sns.load_dataset("tips")
# print(tips)
# plt.scatter(tips["total_bill"],tips["tip"])

# plt.show()
##########   Scatter plot -> Axis level function     ########
# sns.scatterplot(data=tips, x="total_bill", y="tip",hue="sex",style="time",size="size")
# ##########   replot -> figure level -> sqr shape     ########
# sns.relplot(data=tips, x="total_bill", y="tip",kind="scatter",hue="sex",style="time",size="size")
# plt.show()

#########################################################

gap = px.data.gapminder()
# ind = gap[gap["country"] == "India"]
# sns.lineplot(data=ind,x="year",y="lifeExp")

# plt.show()

###########################################################
# sns.relplot(data=ind,x="year",y="lifeExp",kind="line")
# plt.show()

# temp = gap[gap["country"].isin(["India","Brazil","Egypt","China","Canada","Australia","France"])]
# sns.relplot(data=temp,x="year",y="lifeExp",kind="line",hue='country',style='continent')
# # sns.lineplot(data=temp,x="year",y="lifeExp",hue='country')
# plt.show()


############################################################

# sns.relplot(data=tips,x="total_bill",y="tip",kind="scatter",col="sex",row="smoker",hue="day",style="time")
# plt.show()
###########################################################

# sns.relplot(data=gap,x="lifeExp",y="gdpPercap",kind="scatter",col="year",col_wrap=3)

# plt.show()

#############################################################


# sns.histplot(data=tips,x="total_bill")
# plt.show()
#############################################################

# sns.displot(data=tips,x="total_bill",kind="hist",bins=20)
# plt.show()
#########################################################

# sns.displot(data=tips,x="day",kind="hist",hue="sex")
# plt.show()

###########################################################


# sns.displot(data=tips,x="total_bill",kind="hist",hue = "sex")
# plt.show()

# sns.displot(data=tips,x="total_bill",kind="hist",hue = "sex",element="step")
# plt.show()


#############################################################


ship = sns.load_dataset("titanic")
# sns.displot(data=ship,x="age",kind="hist",col="sex")
# plt.show()

#############################################################


# sns.kdeplot(data=tips,x='total_bill')
# plt.show()


# sns.displot(data=tips,x="total_bill",kind='kde',hue="sex",fill=True)
# plt.show()

#############################################################
# sns.kdeplot(data=tips,x="total_bill")
# sns.rugplot(data=tips,x="total_bill")
# plt.show()

###########################################################
# sns.histplot(data=tips, x="total_bill", y ="tip")
# sns.kdeplot(data=tips, x="total_bill", y ="tip")

# plt.show()

############################################################

# a = gap.pivot(index='country',columns="year",values="lifeExp")
# sns.heatmap(a)
# plt.show()
# print(gap["continent"].head(400))
a = gap[gap["continent"] == "Americas"].pivot(index="country", columns= "year",values="lifeExp")
sns.heatmap(a,annot=True,linecolor="red",linewidths=0.5,cmap="viridis")
plt.show()


































































































































































