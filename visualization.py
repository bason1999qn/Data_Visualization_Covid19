#
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from preprocess import *
import seaborn as sns


#
# #***Tien xu ly du lieu********************:
# #read dataframe from csv file
# df = pd.read_csv('19thg5_test.csv', encoding='unicode_escape')
# #replace NaN value to 0
# df = df.fillna(0)
# #Xoa row tong hop:
# df = df[:-1]
# #Xoa cot chua du lieu k dung den:
# df= df.drop("#", axis=1)
# print(df)

# *** Truc quan hoa du lieu*************
# Lay du lieu vao bien df
# df = dataframe
df = get_data('03thg6.csv')
df = data_preprocessing(df)
df.to_csv("abc.csv")


# Cac ham truc quan
# Top 15 nuoc co so ca nhiem cao nhat
def top15(dataframe):
    df_top15 = dataframe.sort_values(by='TotalCases', ascending=True).tail(15)['TotalCases']
    print(df_top15)

    df_top15.plot(kind='barh', figsize=(10, 10), rot=0)
    plt.title('Immigrants from Top 15 Countries')
    plt.xlabel('Number of Immigrants')
    plt.ylabel('Countries')
    # Annotate Text
    for index, value in enumerate(df_top15):
        print(index, value)
        label=format(int(value), ',')
        print(index-0.10)
        plt.annotate(label, xy=(value-500,index-0.10), fontsize=7, color='red')

    plt.show()

# ti le tu vong, phuc hoi/ so ca mac
# x = df.loc[:,"Total Cases"].median()



# Ti le % nuoc nhiem/tong
# Pie Charts



# Scatter Plots
# link: https://python-graph-gallery.com/46-add-text-annotation-on-scatterplot/
def scatter_deaths_cases(dataframe):
    # df.plot(data = df, label = 'Country', kind='scatter', x='Total Cases', y='Total Deaths', figsize=(10, 6), color='darkblue')
    p1 = sns.regplot(data=dataframe, y="TotalCases", x="TotalDeaths", fit_reg=False, marker="o", color="skyblue",
                     scatter_kws={'s':50})
    # p1 = sns.scatterplot(data=dataframe, y="TotalCases", x="TotalDeaths", marker="o", color="skyblue")
    # Show names's point
    # for line in range(0, df.shape[0]):
    for line in range(0, 15):
        p1.text(dataframe.TotalDeaths[line] + 0.2, dataframe.TotalCases[line], dataframe.index[line],
                horizontalalignment='left', size='xx-small', color='black',weight='semibold')
    plt.title('Total Deaths vs. Total Cases')
    plt.xlabel('Total Deaths Logarithmic')
    plt.ylabel('Total Cases Logarithmic')
    # Chay duong phan tach tuyen tinh
    y = dataframe['TotalCases']  # year on x-axis
    x = dataframe['TotalDeaths']  # total on y-axis
    # fit tra ve [a b] voi a,b la he so trong y = ax + b
    fit = np.polyfit(x, y, deg=1)
    plt.plot(x, fit[0] * x + fit[1], color='red')  # recall that x is the Years
    # plt.annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1]), xy=(2000, 150000))

    plt.show()


def scatter_deaths_cases1M(dataframe):
    # df.plot(data = df, label = 'Country', kind='scatter', x='Total Cases', y='Total Deaths', figsize=(10, 6), color='darkblue')
    p1 = sns.regplot(data=dataframe, x="TotCases_1MPop", y="Deaths_1MPop", fit_reg=False, marker="o", color="skyblue",
                     scatter_kws={'s':50})
    # p1 = sns.scatterplot(data=dataframe, y="TotalCases", x="TotalDeaths", marker="o", color="skyblue")
    # Show names's point
    # for line in range(0, df.shape[0]):
    for line in range(0, 20):
        p1.text(dataframe.TotCases_1MPop[line] + 0.2, dataframe.Deaths_1MPop[line], dataframe.index[line],
                horizontalalignment='left', size='xx-small', color='black',weight='semibold')
    plt.title('Total Deaths/1M Pop vs. Total Cases/1M Pop')
    plt.xlabel('Total Cases/1M Pop Logarithmic')
    plt.ylabel('Total Deaths/1M Pop Logarithmic')
    # Chay duong phan tach tuyen tinh
    x = dataframe['TotCases_1MPop']  # year on x-axis
    y = dataframe['Deaths_1MPop']  # total on y-axis
    # fit tra ve [a b] voi a,b la he so trong y = ax + b
    fit = np.polyfit(x, y, deg=1)
    plt.plot(x, fit[0] * x + fit[1], color='red')  # recall that x is the Years
    # plt.annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1]), xy=(2000, 150000))

    plt.show()

def death_per_1M(dataframe):
    df_dM = dataframe.sort_values(by='Deaths/1MPop', ascending=True).tail(15)['Deaths/1MPop']


    df_dM.plot(kind='barh', figsize=(10, 10), rot=0, color='red')
    plt.title('Top 15 Countries deaths per 1M')
    plt.xlabel('Number of Immigrants')
    plt.ylabel('Countries')
    # Annotate Text
    for index, value in enumerate(df_dM):
        print(index, value)
        label=format(int(value), ',')
        print(index-0.10)
        plt.annotate(label, xy=(value-50,index-0.11), fontsize=7, color='blue')

    plt.show()


#cases per million people
def cases_per_1M(dataframe):
    df_dM = dataframe.sort_values(by='TotCases/1MPop', ascending=True).tail(15)['TotCases/1MPop']


    df_dM.plot(kind='barh', figsize=(10, 10), rot=0, color='red')
    plt.title('Top 15 Countries deaths per 1M')
    plt.xlabel('Number of Immigrants')
    plt.ylabel('Countries')
    # Annotate Text
    for index, value in enumerate(df_dM):
        print(index, value)
        label=format(int(value), ',')
        print(index-0.10)
        plt.annotate(label, xy=(value-50,index-0.11), fontsize=7, color='blue')

    plt.show()



# autopct create %, start angle represent starting point
#Bieu do hinh quat
# % so nguoi chet tren toan TG:
def cases_pie_charts(dataframe):
    df_top15 = dataframe.sort_values(by='TotalCases', ascending=True).tail(15)['TotalCases']
    df_top15['TotalCases'].plot(kind='pie',
                                figsize=(5, 6),
                                autopct='%1.1f%%', # add in percentages
                                startangle=90,     # start angle 90° (Africa)
                                shadow=False,       # add shadow
                                )

    plt.title('Immigration to Canada by Continent [1980 - 2013]')
    plt.axis('equal') # Sets the pie chart to look like a circle.

    plt.show()
# Thuc thi

# top15(df)
# scatter_deaths_cases(df)
scatter_deaths_cases1M(df)
# death_per_1M(df)
# cases_per_1M(df)
# cases_pie_charts(df)


#
# df['TotalCases'].plot(kind='pie',
#                             figsize=(5, 6),
#                             autopct='%1.1f%%', # add in percentages
#                             startangle=90,     # start angle 90° (Africa)
#                             shadow=False,       # add shadow
#                             )
#
# plt.title('Immigration to Canada by Continent [1980 - 2013]')
# plt.axis('equal') # Sets the pie chart to look like a circle.
#
# plt.show()










