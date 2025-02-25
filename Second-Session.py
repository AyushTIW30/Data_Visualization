import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import numpy as np
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
# sns.stripplot(data=tips,x="day",y="total_bill")
# plt.show()
#############################################################
#                      catplot                             #
# sns.catplot(data=tips,x="day",y="total_bill",kind="strip",jitter=0.2,hue="sex")
# plt.show()
#############################################################

# sns.catplot(data=tips,x="day",y="total_bill",kind="swarm")
# plt.show()

#############################################################

# sns.swarmplot(data=tips,x="day",y="total_bill",hue="sex")
# plt.show()
#############################################################
#                       Box plot                           #
# sns.boxplot(data=tips,x="day",y="total_bill",hue="sex")
# plt.show()

# sns.boxplot(data=tips,y="total_bill")
# plt.show()

#############################################################
#                violinplot=(boxplot+kdeplot)              #

# sns.violinplot(data=tips,x="day", y ="total_bill")
# plt.show()
#

# sns.catplot(data=tips,x="day", y ="total_bill",kind="violin",hue="sex",split=True)
# plt.show()

#############################################################
#               barplot                                    #
# sns.barplot(data=tips,x="sex",y="total_bill",errorbar=None,hue="smoker",estimator=np.max)
# plt.show()


#############################################################
#                       point plot                          #

# sns.pointplot(data=tips,x="sex",y="total_bill",hue="smoker",estimator=np.mean)
# plt.show()


# sns.pointplot(data=tips,x="sex",y="total_bill")
# plt.show()


#############################################################
#                       count plot                          #
# sns.countplot(data=tips,x="sex",hue="day")
# plt.show()


# sns.catplot(data=tips , x="sex", y="total_bill", col ="smoker",kind="box",row="time")
# plt.show()


#############################################################
#                      regression plot                      #

# sns.regplot(data=tips, x='total_bill',y="tip")
# plt.show()    #hue parameter is not available

# sns.lmplot(data=tips, x='total_bill',y="tip",hue="sex")
# plt.show()


# sns.residplot(data=tips, x='total_bill',y="tip")
# plt.show()


#############################################################
#                      facitgrid plot                      #
# g = sns.FacetGrid(data=tips,col="day",row="time",hue="smoker")
# g.map(sns.scatterplot,"tip","total_bill")
# g.add_legend()
# plt.show()



#############################################################
#                       paired plot                         #
#
# sns.pairplot(iris,hue="species")
# plt.show()



#############################################################
#                       paired grid                         #
# g = sns.PairGrid(data=iris)
# g.map_diag(sns.histplot)
# g.map_offdiag(sns.scatterplot)
# g.map_lower(sns.violinplot)
# g.map_upper(sns.boxplot)

# plt.show()



#############################################################
#                       joint plot                         #

# sns.jointplot(data=tips,x="total_bill",y="tip",kind="hist",hue="sex")
# plt.show()


#############################################################
#                       joint grid                         #

g = sns.JointGrid(data=tips,x="total_bill",y="tip")
g.plot(sns.kdeplot, sns.violinplot)
plt.show()















