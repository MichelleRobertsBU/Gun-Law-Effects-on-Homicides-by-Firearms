import pandas as pd
import numpy as np
import sqlite3
import xlrd

#Add Excel Dataframes
print('*********************************')
StateGunSafetyLaws = pd.read_excel('data\StateGunSafetyLaws.xlsx', header=0)
GunLawStrength = pd.read_excel('data\GiffordGunLawStrength.xlsx', header=0)
HomicidesbyState = pd.read_excel('data\HomicidesbyState.xls', header=0)
MostGunSales = pd.read_excel('data\StatesWheretheMostPeopleBoughtGunsFebruary2023.xlsx', header =0)

StateGunSafetyLaws.head()
print(StateGunSafetyLaws)
print('*********************************')
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

c.execute('''CREATE TABLE IF NOT EXISTS StateGunSafetyLaws (
        id INTEGER NOT NULL,
        state TEXT NOT NULL,
        law type TEXT,
        restrictive gun law TEXT,
        Bill Identifier TEXT,
        PRIMARY KEY(id),
        FOREIGN KEY(state) REFERENCES HomicidesbyState(State_ID)
        );
    '''
    )

c.execute('''CREATE TABLE IF NOT EXISTS GunLawStrength (
        Gun_Law_Rank INTEGER,
        State_list TEXT,
        Grade TEXT,
        Death_Rank INTEGER,
        Rate_per_100K INTEGER,
        PRIMARY KEY(Gun_Law_Rank),
        FOREIGN KEY(State_list) REFERENCES HomicidesbyState(State_ID),
        FOREIGN KEY(Death_Rank) REFERENCES MostGunSales(Rank_2023)
        );
    '''
    )

c.execute('''CREATE TABLE IF NOT EXISTS HomicidesbyState (
        State_ID TEXT,
        Total_Murders INTEGER,
        Total_Firearms INTEGER,
        Handguns INTEGER,
        Rifles INTEGER,
        Shotguns INTEGER,
        Type_unknown INTEGER,
        Cutting_instruments INTEGER,
        Other_Weapons INTEGER,
        PRIMARY KEY(State_ID),
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
        FOREIGN KEY(allState) REFERENCES HomicidesbyState(State_ID),
        FOREIGN KEY(Firearm_Background_Checks_Feb_2023) REFERENCES StateGunSafetyLaws(state),
        FOREIGN KEY(Population) REFERENCES GunLawStrength(Gun_Law_Rank)
        );
    '''
    )

StateGunSafetyLaws.to_sql('StateSafetyLaws', db_conn, if_exists='append', index=False)
GunLawStrength.to_sql('GunLawStrength', db_conn, if_exists='append', index=False)
HomicidesbyState.to_sql('HomicidesbyState', db_conn, if_exists='append', index=False)
MostGunSales.to_sql('MostGunSales', db_conn, if_exists='append', index=False)


#print specific Gun Laws
print('*********************************')
#cursor.execute("create table LawType1 (state text, law_type text)")
#law_type1 = ('select law_type from StateGunSafetyLaws where law_type like "%Community Violence Intervention%"');
#cursor.executemany("insert into LawType1 values (?,?)", law_type1)
#for row in cursor.execute("select * from LawType1"):
    #print(row)



