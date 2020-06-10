#
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from preprocess import *
import seaborn as sns




# *** Truc quan hoa du lieu*************
# Lay du lieu vao bien df
# df = dataframe
df = get_data('03thg6.csv')
df = data_preprocessing(df)
df.to_csv("abc.csv")


# Cac ham truc quan
# Top 15 nuoc co so ca nhiem cao nhat
#1712732
def top15_TotalCases(dataframe):
    #Sap xep top 15 theo tong so ca mac
    df_top15 = dataframe.sort_values(by='TotalCases', ascending=True).tail(15)['TotalCases']
    #truc quan len bieu do bang plot
    df_top15.plot(kind='barh', figsize=(10, 10), rot=0)
    #Chu thich truc bieu do
    plt.title('Top 15 quoc gia co ca mac nhieu nhat')
    plt.xlabel('So ca mac')
    plt.ylabel('Quoc gia')
    # Annotate Text (Them chu thich)
    for index, value in enumerate(df_top15):
        label=format(int(value), ',')
        plt.annotate(label, xy=(value-500,index-0.10), fontsize=7, color='red')

    plt.show()

# ti le tu vong, phuc hoi/ so ca mac
# x = df.loc[:,"Total Cases"].median()



# Ti le % nuoc nhiem/tong
# Pie Charts


#1712732
# Scatter Plots
# link: https://python-graph-gallery.com/46-add-text-annotation-on-scatterplot/
def scatter_deaths_cases(dataframe):
    # Truc quan bang bieu do scatter trong thu vien seaborn, dua vao thuoc tinh TotalCases, TotalDeaths
    p1 = sns.regplot(data=dataframe, y="TotalCases", x="TotalDeaths", fit_reg=False, marker="o", color="skyblue",
                     scatter_kws={'s':50})

    # Show names's point (Hien thi ten quoc gia o moi diem)
    # Hien thi toi 15 nuoc
    # for line in range(0, df.shape[0]):
    for line in range(0, df.shape[0]):
        p1.text(dataframe.TotalDeaths[line], dataframe.TotalCases[line], dataframe.index[line],
                horizontalalignment='left', size='xx-small', color='black',weight='semibold')
    plt.title('Total Deaths vs. Total Cases')
    plt.xlabel('Total Deaths')
    plt.ylabel('Total Cases')
    # Chay duong phan tach tuyen tinh
    y = dataframe['TotalCases']  # year on x-axis
    x = dataframe['TotalDeaths']  # total on y-axis
    # fit tra ve [a b] voi a,b la he so trong y = ax + b
    fit = np.polyfit(x, y, deg=1)
    # Hien thi duong
    plt.plot(x, fit[0] * x + fit[1], color='red')  # recall that x is the Years

    plt.show()

#1712732
def scatter_deaths_cases1M(dataframe):
    p1 = sns.regplot(data=dataframe, x="TotCases_1MPop", y="Deaths_1MPop", fit_reg=False, marker="o", color="skyblue",
                     scatter_kws={'s':50})
    # p1 = sns.scatterplot(data=dataframe, y="TotalCases", x="TotalDeaths", marker="o", color="skyblue")
    # Show names's point
    # for line in range(0, df.shape[0]):
    for line in range(0, df.shape[0]):
        p1.text(dataframe.TotCases_1MPop[line] + 0.2, dataframe.Deaths_1MPop[line], dataframe.index[line],
                horizontalalignment='left', size='xx-small', color='black',weight='semibold')
    plt.title('Total Deaths/1M Pop vs. Total Cases/1M Pop')
    plt.xlabel('Total Cases/1M Pop')
    plt.ylabel('Total Deaths/1M Pop')
    # Chay duong phan tach tuyen tinh
    x = dataframe['TotCases_1MPop']  # year on x-axis
    y = dataframe['Deaths_1MPop']  # total on y-axis
    # fit tra ve [a b] voi a,b la he so trong y = ax + b
    fit = np.polyfit(x, y, deg=1)
    plt.plot(x, fit[0] * x + fit[1], color='red')  # recall that x is the Years

    plt.show()

#1712732
def death_per_1M(dataframe):
    df_dM = dataframe.sort_values(by='Deaths_1MPop', ascending=True).tail(15)['Deaths_1MPop']


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

#1712732
#cases per million people
def cases_per_1M(dataframe):
    df_dM = dataframe.sort_values(by='TotCases_1MPop', ascending=True).tail(15)['TotCases_1MPop']


    df_dM.plot(kind='barh', figsize=(10, 10), rot=0, color='red')
    plt.title('Top 15 Countries cases per 1M')
    plt.xlabel('Number of cases')
    plt.ylabel('Countries')
    # Annotate Text
    for index, value in enumerate(df_dM):
        print(index, value)
        label=format(int(value), ',')
        print(index-0.10)
        plt.annotate(label, xy=(value-50,index-0.11), fontsize=7, color='blue')

    plt.show()

#1712732
# autopct create %, start angle represent starting point
#Bieu do hinh quat
# % so nguoi chet tren toan TG:
# tail(15)['TotalCases']
def cases_pie_charts(dataframe):
    dataframe['TotalCases'].plot(kind='pie',
                                 figsize=(5, 6),
                                 autopct='%1.1f%%',  # add in percentages
                                 startangle=90,  # start angle 90° (Africa)
                                 shadow=False,  # add shadow
                                 )

    plt.title('Ti le % ca nhiem cac quoc gia so voi the gioi')
    plt.axis('equal')  # Sets the pie chart to look like a circle.

    plt.show()

#Suong
def top15_recovery_rate(dataframe):
    df_top15 = dataframe[['TotalCases', 'TotalRecovered']]
    df_top15['RecoveryRate'] = df_top15.apply(lambda row: row.TotalRecovered / row.TotalCases, axis = 1)
    df_top15 = df_top15.sort_values(by='RecoveryRate', ascending=True).tail(15)['TotalCases']
    print(df_top15)
    # df_top15 = pd.DataFrame(df_top15.sort_values(by='RecoveryRate', ascending=True).tail(15)['RecoveryRate'])
    # print(df_top15)

    df_top15.plot(kind='barh', figsize=(10, 10), color='green')
    plt.title("Top 15 Countries have the highest revovery rate")
    plt.xlabel('Recovery rate')
    plt.ylabel('Countries')
    # Annotate Text
    for index, value in enumerate(df_top15):
        print(index, value)
        label=format(int(value), ',')
        plt.annotate(label, xy=(value,index), fontsize=10, color='black')

    plt.show()

#Suong
def top10_death_on_total(dataframe):
    dataframe = dataframe.head(10)
    dataframe['DeathOnTotal'] = dataframe.apply(lambda row: row.TotalDeaths / row.TotalCases, axis = 1)
    dataframe['ActiveAndRecovered'] = dataframe.apply(lambda row: 1 - row.DeathOnTotal, axis = 1)
    dataframe = dataframe[['DeathOnTotal', 'ActiveAndRecovered']]

    dataframe.plot(kind='bar', stacked=True, figsize=(10, 10), color=['red', 'orange'])
    plt.xticks(rotation=45)

    plt.show()
#Top 15 nuoc thuc hien xet nghiem nhieu nhat va ket qua dat duoc /1M
def top15_bar_chart(dataframe):
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.bar.html
    cases =['Tests_1MPop', 'TotCases_1MPop', 'Deaths_1MPop']
    #Bar Chart with Pandas
    dataframe.sort_values(by=['Tests_1MPop'], inplace=True, ascending=False)
    dataframe.head(15).plot.bar(y=cases)
    plt.ylabel('Case')
    plt.show()

#Son
# Ti le nguoi dươc xet nghiem so voi so ca nhiem
def scatter_test_newcases(dataframe):
    # df.plot(data = df, label = 'Country', kind='scatter', x='Total Cases', y='Total Deaths', figsize=(10, 6), color='darkblue')
    p1 = sns.regplot(data=dataframe, y="TotalCases", x="TotalTests", fit_reg=False, marker="o", color="red",
                     scatter_kws={'s': 50})
    # p1 = sns.scatterplot(data=dataframe, y="TotalCases", x="TotalDeaths", marker="o", color="skyblue")
    # Show names's point
    # for line in range(0, df.shape[0]):
    for line in range(0, 15):
        p1.text(dataframe.TotalTests[line] + 0.2, dataframe.TotalCases[line], dataframe.index[line],
                horizontalalignment='left', size='xx-small', color='black', weight='semibold')
    plt.title('Total Case vs Total Test')
    plt.xlabel('Total Test Logarithmic')
    plt.ylabel('Total Cases Logarithmic')
    # Chay duong phan tach tuyen tinh
    y = dataframe['TotalCases']  # cases on y-axis
    x = dataframe['TotalTests']  # tests on x-axis
    # fit tra ve [a b] voi a,b la he so trong y = ax + b
    fit = np.polyfit(x, y, deg=1)
    plt.plot(x, fit[0] * x + fit[1], color='blue')  # recall that x is the Years
    # plt.annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1]), xy=(2000, 150000))

    plt.show()

#Son
def top100_serious(dataframe):
    # https://blog.quantinsti.com/creating-heatmap-using-python-seaborn/#:~:text=A%20heatmap%20is%20a%20two,as%20per%20the%20creator's%20requirement.
    top15serious = pd.DataFrame(index=dataframe.index, columns=['ratio', 'Yrows', 'Xcols'])

    top15serious['ratio'] = dataframe['SeriousCritical'] * 100 / dataframe['TotalCases']
    top15serious = top15serious.head(100)

    symbol = ((np.asarray(top15serious.index.values.tolist())).reshape(10, 10))
    perchange = ((np.asarray(top15serious['ratio'])).reshape(10, 10))
    # print(symbol)
    # print(perchange)
    listx = []
    listy = []
    for i in range(1, 11):
        for j in range(10):
            listy.append(i)
        listx.append(list(range(1, 11)))
    listx = np.asarray(listx).reshape(100)
    listy = np.asarray(listy).reshape(100)
    # print(listx)
    # print(listy)
    top15serious['Yrows'] = listy
    top15serious['Xcols'] = listx
    result = top15serious.pivot(index='Yrows', columns='Xcols', values='ratio')
    # print(result)
    labels = (np.asarray(["{0} \n {1:.4f}".format(symb, value)
                          for symb, value in zip(symbol.flatten(),
                                                 perchange.flatten())])
              ).reshape(10, 10)
    # Define the plot
    fig, ax = plt.subplots(figsize=(15, 10))

    # Add title to the heat map
    title = "Ratio Serious Cases to Total Cases"

    # Set the font size and distance of the title from the plot
    plt.title(title, fontsize=20)
    ttl = ax.title
    ttl.set_position([0.5, 1.05])

    # Hide ticks for X & Y axis
    ax.set_xticks([])
    ax.set_yticks([])

    # Remove the axes
    ax.axis('off')

    # Create the heatmap
    sns.heatmap(result, annot=labels, fmt="", cmap='RdYlGn', linewidths=0.30, ax=ax)

    plt.show()

# Ti le xet nghiem so voi dan so & ti le ca nhiem moi so voi dan so
def scatter_test_cases(dataframe):
    newdf = pd.DataFrame(columns=['TestPerPopulation', 'NewCasesPerPopulation'])
    newdf['TestPerPopulation'] = dataframe['TotalTests'] * 100 / dataframe['Population']
    newdf['NewCasesPerPopulation'] = dataframe['NewCases'] * 100 / dataframe['Population']
    newdf = newdf.head(30)
    p1 = sns.regplot(data=newdf, y="NewCasesPerPopulation", x="TestPerPopulation", fit_reg=False, marker="o",
                     color="red",
                     scatter_kws={'s': 50})
    for line in range(0, 30):
        p1.text(newdf.TestPerPopulation[line] + 0.2, newdf.NewCasesPerPopulation[line], dataframe.index[line],
                horizontalalignment='left', size='xx-small', color='black', weight='semibold')
    plt.title('Ratio of TotalTests to Population & Ratio of NewCases to Population')
    plt.xlabel('Ratio of TotalTests to Population')
    plt.ylabel('Ratio of NewCases to Population')
    # Chay duong phan tach tuyen tinh
    y = newdf['NewCasesPerPopulation']  # year on x-axis
    x = newdf['TestPerPopulation']  # total on y-axis
    # fit tra ve [a b] voi a,b la he so trong y = ax + b
    fit = np.polyfit(x, y, deg=1)
    plt.plot(x, fit[0] * x + fit[1], color='blue')  # recall that x is the Years
    # plt.annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1]), xy=(2000, 150000))

    plt.show()

#1712732
def top10_total_death_recovered(dataframe):
    dataframe = dataframe.head(10)[['TotalCases', 'TotalDeaths', 'TotalRecovered']]
    dataframe.plot(kind='bar', figsize=(10, 10))
    plt.xticks(rotation=45)

    plt.show()


#1712732
# https://github.com/MrinmoiHossain/Online-Courses-Learning/blob/master/Coursera/Data%20Visualization%20with%20Python-IBM/Week-2/Excercise/Histograms.ipynb
# So ca mac moi ngay hien tai
def histogram_NewCases(dataframe):
    dataframe['NewCases'].plot(kind='hist')
    plt.title('So ca mac moi của 215 quoc gia trong ngay (03 thang 6)') # add a title to the histogram
    plt.ylabel('So quoc gia') # add y-label
    plt.xlabel('So ca mac moi') # add x-label
    plt.show()




# Thuc thi

# top15_TotalCases(df)
# scatter_deaths_cases(df)
# scatter_deaths_cases1M(df)
# death_per_1M(df)
# cases_per_1M(df)
# cases_pie_charts(df)
# top15_bar_chart(df)
# histogram_NewCases(df)
# scatter_test_newcases(df)
# top10_total_death_recovered(df)

#Fixxing
#top15_recovery_rate(df)












