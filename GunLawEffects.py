from msilib.schema import tables
import pandas as pd
import numpy as np
import sqlite3
import xlrd
import matplotlib.pyplot as plt
import seaborn as sns

#Read Excel file to Pandas Dataframe and sort by Gun Sales Rank
df_mostsales = pd.read_excel('data\StatesWheretheMostPeopleBoughtGunsFebruary2023.xlsx')

sorted_df = df_mostsales.sort_values(by='Rank_2023', ignore_index=True)
print(sorted_df.loc[:9])

#Read Excel file to Pandas Dataframe, Join column to another Dataframe, sort by last 10
print('*********************************')
df_gunlaws = pd.read_excel('data\GiffordGunLawStrength.xlsx')
extracted_col = df_gunlaws["Grade"]
df_mostsales = df_mostsales.join(extracted_col)
df_last_10 = df_mostsales.iloc[-10:]
print(df_last_10)


#Set up Sqlite3 and create Database for StateGunSafetyLaws
print('*********************************')
connection = sqlite3.connect("StateGunSafetyLaws.db")
cursor = connection.cursor()

cursor.execute("create table if not exists StateGunSafetyLaws (my_State text, law_type text, restrictive text, bill_identifier text)")


state_gun_laws_list = [
    ('California', 'Background Check, Domentic Abuse Restriction, Extreme Risk Protection Orders, Community Violence Intervention, Ghost Guns, Gun Dealer Regulations, Safe Storage Laws Notifications for Kids, Access to Justice, Location Regulation', 'Y', 'AB2551, AB2239, AB2870, AB2697, AB200, AB1929, SB154, AB2552, AB1621, AB2156, SB1327, SB1384, AB228, AB1842, AB452, SB906, AB2571, AB1594, SB915'),
    ('Colorado', 'Community Violence Intervention, Sensitive Locations', 'Y', 'HB1329, SB145, HB1086'),
    ('Connecticut', 'Background Check, Community Violence Intervention, Gun Dealer Regulations', 'Y', 'HB5417, HB5506, HB5305'),
    ('Delaware', 'Assault Weapons Ban, Background Check, Large Capacity Magazines, Ghost Guns, 21 Age Limit, Access to Justice', 'Y', 'HB450, HB423, SB6, SB8, HB451, SB302'),
    ('Illinois', 'Domestic Abuse Restriction, Community Violence Intervention, Ghost Guns', 'Y', 'SB257, HB900, HB4383'),
    ('Iowa', 'Domestic Abuse Restriction', 'Y', 'HB825'),
    ('Maryland', 'Community Violence Intervention, Ghost Guns, Gun Dealer Regulations', 'Y', 'HB1005, SB290, SB350, HB425, SB387, HB1021'),
    ('Massachusetts', 'Extreme Risk Protection Orders, Community Violence Intervention', 'Y', 'HB5374, SB3097, HB5050'),
    ('Michigan', 'Community Violence Intervention', 'Y', 'HB5783'),
    ('Nebraska', 'Community Violence Intervention', 'Y', 'LB1011'),
    ('New Jersey', 'Large Capacity Magazines, Concealed Carry Licensing, Ammunition, Domestic Abuse Restriction, Extreme Risk Protection Orders, Enacted Microstamping, Access to Justice, Sensitive Locations, Prohibited Open Carry', 'Y', 'SB2905, AB4769, AB1302, AB3687, AB4368, AB1765, AB4769'),
    ('New Mexico', 'Community Violence Intervention', 'Y', 'HB2, HB68'),
    ('New York', 'Concealed Carry Licensing, Large Capacity Magazines, Background Check, Ammunition, Domestic Abuse Restriction, Extreme Risk Protection Orders, Community Violence Intervention, Gun Dealer Regulations, 18 Age Limit, Enacted Microstamping, Sensitive Locations, Seizure upon Revoked License', 'Y', 'SB1, SB9229, SB6443, SB9113, SB8000, SB8003, SB8004, SB4970, SB9458, AB7926, SB6363'),
    ('Oklahoma', 'Domestic Abuse Restriction', 'Y', 'HB3286'),
    ('Oregon', 'Background Check, Large Capacity Magazines, Community Violence Intervention', 'Y', 'Ballot Measure 114, HB4045, HB5202'),
    ('Pennsylvania', 'Community Violence Intervention', 'Y', 'SB1100, HB1421'),
    ('Rhode Island', 'Large Capacity Magazines, Community Violence Intervention, 21 Age Limit, Carrying Restrictions', 'Y', 'HB6614, HB7123, SB2637, HB7457, HB7358, SB2825'),
    ('Tennessee', 'Concealed Carry Licensing', 'Y', 'HB1018'),
    ('Vermont', 'Background Check, Extreme Risk Protection Orders, Sensitive Locations', 'Y', 'SB4'),
    ('Virginia', 'Community Violence Intervention', 'Y', 'HB29, HB30'),
    ('Washington', 'Large Capacity Magazines, Extreme Risk Protection Orders, Community Violence Intervention, Ghost Guns, Sensitive Locations', 'Y', 'SB5078, HB1901, SB5693, HB1705, HB1630'),
    ('Wyoming', 'Restricted Enforcement', 'N', 'SB102'),
    ('Alabama', 'Restricted Enforcement, Permit to Carry Hidden, Expanded Legal Carry Locations', 'N', 'SB2, HB272'),
    ('New Hampshire', 'Restricted Enforcement', 'N', 'HB1178'),
    ('Georgia', 'Permit to Carry Hidden, Expanded Legal Carry Locations', 'N', 'SB319'),
    ('Indiana', 'Permit to Carry Hidden', 'N', 'HB1296'),
    ('Ohio', 'Permit to Carry Hidden, Teachers Carry', 'N', 'SB215, HB99'),
    ('West Virginia', 'Expanded Legal Carry Locations', 'N', 'HB4048'),
    ('Tennessee', 'Allow Short Barrel Riffles and Shotguns', 'N', 'SB2628'),
    ('Utah', 'Private Right of Action', 'N', 'SB115')
    ]

cursor.executemany("insert into StateGunSafetyLaws values (?,?,?,?)", state_gun_laws_list)

#print database rows
#for row in cursor.execute("select * from StateGunSafetyLaws"):
    #print(row)
connection.commit()
#Create Sql Dataframe StateGunSafetyLaws 
sql = pd.read_sql_query("select * from StateGunSafetyLaws", connection)
df = pd.DataFrame(sql, columns=["my_State", "law_type", "restrictive", "bill_identifier"])

print(df)
connection.close()


#Add Excel Dataframes
print('*********************************')
GunLawStrength = pd.read_excel('data\GiffordGunLawStrength.xlsx', header=0)
HomicidesbyState = pd.read_excel('data\HomicidesbyState.xls', header=0)
MostGunSales = pd.read_excel('data\StatesWheretheMostPeopleBoughtGunsFebruary2023.xlsx', header =0)

GunLawStrength.head()
print(GunLawStrength)
print('*********************************')
HomicidesbyState.head()
print(HomicidesbyState)
print('*********************************')
MostGunSales.head()
print(MostGunSales)

#Create SQLite Database with excel files
print('*********************************')
db_conn = sqlite3.connect("data/allFiles.db")
c = db_conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS GunLawStrength (
        Gun_Law_Rank INTEGER,
        State_list TEXT,
        Grade TEXT,
        Death_Rank INTEGER,
        Rate_per_Hundred INTEGER,
        PRIMARY KEY(Gun_Law_Rank),
        FOREIGN KEY(State_list) REFERENCES HomicidesbyState(State),
        FOREIGN KEY(Death_Rank) REFERENCES MostGunSales(Rank_2023)
        );
    '''
    )

c.execute('''CREATE TABLE IF NOT EXISTS HomicidesbyState (
        allState TEXT,
        Total_Murders INTEGER,
        Total_Firearms INTEGER,
        Handguns INTEGER,
        Rifles INTEGER,
        Shotguns INTEGER,
        Type_unknown INTEGER,
        Cutting_instruments INTEGER,
        Other_Weapons INTEGER,
        PRIMARY KEY(allState),
        FOREIGN KEY(Total_Firearms) REFERENCES MostGunSales(Rank_2023),
        FOREIGN KEY(Total_Murders) REFERENCES GunLawStrength(Gun_Law_Rank)
        );
    '''
    )

c.execute('''CREATE TABLE IF NOT EXISTS MostGunSales (
        allState TEXT,
        Firearm_Background_Checks_per_Residents_Feb_2023 DECIMAL,
        Firearm_Background_Checks_Feb_2023 REAL,
        Firearm_Background_Checks_per_Residents_Feb_2022 DECIMAL,
        Firearm_Background_Checks_Feb_2022 REAL,
        Population REAL,
        Rank_2023 INTEGER,
        Firearm_Type TEXT,
        PRIMARY KEY(Rank_2023),
        FOREIGN KEY(allState) REFERENCES HomicidesbyState(State),
        FOREIGN KEY(Population) REFERENCES GunLawStrength(Gun_Law_Rank)
        );
    '''
    )
#Send values to SQLite3 tables
GunLawStrength.to_sql('GunLawStrength', db_conn, if_exists='replace', index=False)
HomicidesbyState.to_sql('HomicidesbyState', db_conn, if_exists='replace', index=False)
MostGunSales.to_sql('MostGunSales', db_conn, if_exists='replace', index=False)

#SQLite query to list tables in database with exception handling
try:
    sqliteConnection = sqlite3.connect("data/allFiles.db")
    print("Connected to SQLite")
    sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
    cursor1 = sqliteConnection.cursor()

    cursor1.execute(sql_query)
    print("List of tables\n")
    print(cursor1.fetchall())

except sqlite3.Error as error:
    print("Failed to execute the above query", error)

finally:

    if sqliteConnection:
        sqliteConnection.close()
        print("the sqlite connection is closed")

#Left Join tables MostGunSales and HomicidebyState
print('*********************************')
conn3 = sqlite3.connect("data/allFiles.db")
cursor3 = conn3.cursor()
sql3 = """SELECT allState, Firearm_Background_Checks_per_Residents_Feb_2023, Firearm_Background_Checks_Feb_2023, Firearm_Background_Checks_per_Residents_Feb_2022, Firearm_Background_Checks_Feb_2022, Population, Rank_2023, Firearm_Type  
          FROM MostGunSales
          LEFT JOIN HomicidesbyState
          USING(allState);"""

cursor3.execute(sql3)
result = cursor3.fetchall()
for row in result:
    print(row)

conn3.close()

#Using Matplotlib for Visualization
# Bar chart 

df3 = pd.read_excel('data\GiffordGunLawStrength.xlsx')
plt.rcParams["figure.figsize"] = [14.00, 6.50]
plt.rcParams["figure.autolayout"] = True

df3.plot(y = "Rate_per_Hundred", x = "State_list", kind='bar')
plt.suptitle('States Gun Law Grades')
plt.show()

#Set figure size for Matplotlib
plt.rcParams["figure.figsize"] = [12.00, 6.50]
plt.rcParams["figure.autolayout"] = True


# Make a list of columns needed for data analysis
columns = ['allState','Total_Firearms']
df = pd.read_excel('data\HomicidesbyState.xls', usecols=columns)


# Scatter plot showing Near Earth Asteroids and Mininmum distance in kilometers.
colors = np.random.randint(51, size=(51))
df.plot.scatter(x = 'allState', y = 'Total_Firearms', c=colors, cmap='nipy_spectral')


# Add title and labels to x- and y-axis
plt.suptitle('Homicides by Firearms per State', fontsize = 15)
plt.ylabel('Total Firearm Homicides')
plt.xlabel('States')
plt.xlim(left=-1, right=51)
# rotate x-axis tick labels
plt.xticks(rotation=90) 
plt.show()

#Create a matplotlib pie chart
df_gunlaws = pd.read_excel('data\GiffordGunLawStrength.xlsx')

fig1, ax1 = plt.subplots()
plt.title('State Gun Law Grades', fontsize = 15)

y = np.array([48, 18, 14, 16, 4])
mylabels = ["F", "C", "B", "A", "D"]
myexplode = [0.2, 0, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.legend()
plt.show()

#plt.suptitle('', fontsize = 15)
#ax1.axis('equal')






