import pandas as pd

# filename = 'datasets/titanic_dataset.csv'

# df = pd.read_csv(r'C:\Users\Anast\Downloads\titanic_dataset.csv')
# print(df.head())


# my_list = [10, 20, 2, 3, 17, 23, 0]
# df_series = pd.Series (my_list)
# print (df_series) # mas deixnei th thesh (to index) tou kathe dedomenou

# data_dict = { 'a' : 10, 'b':20, 'c': 30}
# series_from_dict = pd.Series (data_dict)
# print (series_from_dict)

# sales = {"Jan": 350, "Feb": 480, "Mar":530, "Apr":460}
# my_sales_series= pd.Series (sales)
# print (f'my sales series is \n {my_sales_series}')
# print (my_sales_series.iloc[1]) #isodunamo me to apo katw (koitaei th thesh)
# print (my_sales_series.loc["Feb"]) #koitaei akribws auto pou grafoume

# value_position_5 = df_series.iloc [5]
# print (f"In position 5 the values is {value_position_5} ")

# print (type (my_sales_series))

# names = ['Rafail', 'Katerina', 'Giorgos', 'Maria', 'Nikos', 'Ioanna']
# ages = [30,32,37, 23, 27, None]
# grades = [92, 99, 86, None, 87, 75]

# data = {'names':names, 'ages': ages, "grades": grades}

# df=pd.DataFrame (data)
# print (df)

# my_movies = [
#     [" Shrek", "Giorgos", 1997],
#     ["Kill Bill", "Tarantino", 1988],
#     ["Avengers endgamer", "Rouso", 2024],
#     ["Titanikos", "Cameron", 2002]]

# df=pd.DataFrame (data= my_movies, columns= ["name", "author", "year"])
# print (df)


df_titanic=pd.read_csv ("titanic_dataset.csv")
# print (df_titanic)

# print ("First 3 rows of the dataframe:")
# # print (df_titanic.head (3))
# # print (df_titanic.tail(4))

# print (df_titanic.sample(10))
# print (df_titanic.columns)

# df_titanic.info()
# print (df_titanic.describe())

# print (df_titanic.shape) #returns the numbers of rows and columns as a tuple
# print (df_titanic.size) # returns the total number of elements in the dataframe

print (df_titanic.loc [0:4])