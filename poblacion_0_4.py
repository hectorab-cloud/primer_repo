import pandas as pd
import openpyxl as pxl 
df= pd.read_excel('Participación población 0 a 4.xlsx')
print(df['Lugar'])
col_filtradas= df.loc[:,df.columns.str.contains('Location')]
print(col_filtradas)
df_sn_loc= df.drop(columns=df.filter(like='Location').columns)
print(df_sn_loc)