import random
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib as mat
from matplotlib import pyplot as plt 
import seaborn as sns
import pymssql
from distfit import distfit

#connect
connect = pymssql.connect(server = 'DESKTOP-WIN', user = '', password = '', 
                          database = 'test', charset = 'utf8')

cars = pd.read_sql(sql = "select * from sec_cars", con = connect)

connect.close()

#OVERVIEW
np.set_printoptions(threshold=np.inf)  
#pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
print(cars.head(20),'\n')
print(cars.shape)
print(cars.dtypes,'\n')

#PRE
#repeat
cars.drop_duplicates(inplace = True)

#format
cars.replace('暂无',NaN, inplace = True)
cars.replace('--',NaN, inplace = True)

#data type
cars.Boarding_time = pd.to_datetime(cars.Boarding_time,format = '%Y年%m月')
cars.New_price = cars.New_price.str[:-1].astype('float')
print(cars.dtypes,'\n')

#null
print('null:\n', any(cars.isnull()))

#distribution
plt.style.use('ggplot')
cars.Sec_price.plot(kind = 'hist',bins = 30)
cars.New_price.plot(kind = 'hist',bins = 30)
plt.show()

#abnormal
print('排序')
print(cars.sort_values(by = "New_price", ascending = False))

#fillna
#cars.fillna(value = {} )
 
#analysis
print(cars.describe(),'\n')
print(cars.describe(include = ['object']),'\n')
cars.describe(include = ['object']).to_csv('E:\Python\data\cars.describe.csv', encoding='ANSI')

#save
cars.to_csv('E:\cars_pre.scv', encoding = 'ANSI')
