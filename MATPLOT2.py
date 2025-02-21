import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# iris = pd.read_csv("iris.csv")
# print(iris.head())
# iris["Species"] = iris["Species"].replace({"Iris-setosa":0,"Iris-versicolor":1,"Iris-virginica":2})
# plt.figure(figsize=(15,10))
# plt.scatter(iris["SepalLengthCm"],iris["PetalLengthCm"],c=iris["Species"],cmap="winter",alpha=.7)
# plt.xlabel("Sepal Length")
# plt.ylabel("Petal Length")
# plt.colorbar()
# plt.show()

batter = pd.read_csv("batter.csv")
# df = batter.head(100).sample(25,random_state=5)
# plt.figure(figsize=(10,10))
# plt.scatter(df["avg"],df["strike_rate"],s=df["runs"])
# plt.axhline(130,color="red")
# plt.axvline(30,color="red")
# for i in range(df.shape[0]):
#     plt.text(df["avg"].values[i],df["strike_rate"].values[i],df["batter"].values[i])
# # plt.colorbar()
# plt.show()
# fig, ax = plt.subplots(nrows=2,ncols=1,sharex=True,figsize=(10,6))
# ax[0].scatter(batter['avg'],batter["strike_rate"],color="red")
# ax[1].scatter(batter['avg'],batter["runs"])
# ax[0].set_title("Avg Vs Strike_rate")
# ax[0].set_ylabel("Strike rate")
# ax[1].set_title("Avg Vs Runs")
# ax[1].set_ylabel("Runs")
# ax[1].set_xlabel("Avg")
# plt.show()

#####################       SUBPLOTS        #####################
# fig,ax = plt.subplots()
# ax.scatter(batter["avg"],batter["strike_rate"])
# plt.set_title("Avg VS Strike rate")
# plt.set_xlabel("Avg")
# plt.set_ylabel("Strike_rate")


# fig,ax=plt.subplots(nrows=2,ncols=2,figsize=(10,10))
# ax[0,0].scatter(batter['avg'],batter["strike_rate"],color="red")
# ax[0,1].scatter(batter['avg'],batter["runs"])
# ax[1,0].hist(batter['avg'])
# ax[1,1].hist(batter["runs"])
# # plt.figure(figsize=(10,10))
# # ax[0].set_title("Avg Vs Strike_rate")
# # ax[0].set_ylabel("Strike rate")
# # ax[1].set_title("Avg Vs Runs")
# # ax[1].set_ylabel("Runs")
# # ax[1].set_xlabel("Avg")

# plt.show()

################################################################
#                       SUBPLOTS                               #

# fig , ax = plt.subplots()
# ax.scatter(batter["avg"],batter["strike_rate"],color="green",marker=">")
# ax.set_title("Avg Vs Strike rate")
# ax.set_xlabel("Avg")
# ax.set_ylabel("Strike rate")
# fig.show()
# plt.show()

#################################################################


# fig , ax = plt.subplots(nrows=2,ncols=2,sharex = True)
# ax[0].scatter(batter["avg"],batter["strike_rate"],color="green")
# ax[1].scatter(batter["avg"],batter["runs"])
# ax[0].set_title("Avg Vs Strike_rate")
# ax[1].set_title("Avg Vs Runs")
# ax[0].set_xlabel("Avg")
# ax[0].set_ylabel("Strike_rate")
# ax[1].set_xlabel("Avg")
# ax[1].set_ylabel("Runs")


# plt.show()

#################################################################
# fig , ax = plt.subplots(nrows=2,ncols=2)
# ax[0,0].scatter(batter["avg"],batter["strike_rate"],color="green")
# ax[0,1].hist(batter["avg"],)
# ax[1,0].hist(batter["runs"],color="green")
# ax[1,1].scatter(batter["avg"],batter["runs"])
# ax[0,0].set_title("Avg Vs Strike_rate")
# ax[0,1].set_title("Avg Vs Runs")
# ax[1,0].set_xlabel("Avg")
# ax[1,0].set_ylabel("Strike_rate")
# ax[0,1].set_xlabel("Avg")
# ax[0,1].set_ylabel("Runs")

# plt.show()

#################################################################


# fig = plt.figure()
# ax1 = fig.add_subplot(2,3,1)
# ax1.scatter(batter["avg"],batter["strike_rate"],color="green")
# ax2 = fig.add_subplot(2,3,2)
# ax2.hist(batter["avg"])
# ax3 = fig.add_subplot(2,3,3)
# ax3.hist(batter["runs"])

# plt.show()

#################################################################
#               3D Scatter PLot                                 #

# fig = plt.figure(figsize=(10,10))
# ax = plt.subplot(projection="3d")
# ax.scatter3D(batter["runs"],batter["avg"],batter['strike_rate'],marker = "+",color="green", cmap='viridis')
# ax.set_title("Runs Vs Avg Vs Strike rate")
# ax.set_xlabel("Runs")
# ax.set_ylabel('Avg')
# ax.set_zlabel("Strike_rate")

# plt.show()


#################################################################
#                   3d line plot                                #

# x = [0,5,20,40]
# y = [0,10,20,50]
# z = [0,20,40,80]

# fig = plt.figure()
# ax = plt.subplot(projection = '3d')
# ax.scatter3D(x,y,z,s=[100,100,100,100])
# ax.plot3D(x,y,z,color="pink")

# plt.show()




#################################################################
#                      3D surface plot                          #


# x = np.linspace(-10,10,100)
# y = np.linspace(-10,10,100)
# xx,yy = np.meshgrid(x,y)
# z = xx**2+yy**2
# fig = plt.figure(figsize=(12,8))
# ax = plt.subplot(projection="3d")
# p = ax.plot_surface(xx,yy,z,cmap="viridis")
# fig.colorbar(p)
# plt.show()



#################################################################

# z= np.sin(xx)**np.log(yy)
# fig = plt.figure(figsize=(12,8))
# ax = plt.subplot(projection="3d")
# p = ax.plot_surface(xx,yy,z,cmap="viridis")
# fig.colorbar(p)
# plt.show()


################################################################
#                      Contour map                             #


# x = np.linspace(-10,10,100)
# y = np.linspace(-10,10,100)
# xx,yy = np.meshgrid(x,y)
# z = xx**2+yy**2
# fig = plt.figure(figsize=(12,8))
# ax = plt.subplot()
# p = ax.contour(xx,yy,z,cmap="viridis")
# fig.colorbar(p)
# plt.show()


################################################################

# x = np.linspace(-10,10,100)
# y = np.linspace(-10,10,100)
# xx,yy = np.meshgrid(x,y)
# z = xx**2+yy**2
# fig = plt.figure(figsize=(12,8))
# ax = plt.subplot()
# p = ax.contourf(xx,yy,z,cmap="viridis")
# fig.colorbar(p)
# plt.show()
###############################################################


x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
xx,yy = np.meshgrid(x,y)
z= np.sin(xx)+np.cos(yy)
fig = plt.figure(figsize=(12,8))
ax = plt.subplot()
p = ax.contourf(xx,yy,z,cmap="viridis")
fig.colorbar(p)
plt.show()






















































































