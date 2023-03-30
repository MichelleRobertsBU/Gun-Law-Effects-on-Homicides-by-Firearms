import pandas as pd
import numpy as np
import sqlite3
import xlrd

#Set up Sqlite
connection = sqlite3.connect("StateGunSafetyLaws.db")
cursor = connection.cursor()

cursor.execute("create table if not exists StateGunSafetyLaws (state text, law_type text, restrictive text, bill_identifier text)")

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
df = pd.DataFrame(sql, columns=["state", "law_type", "restrictive", "bill_identifier"])

print(df)
connection.close()

#Add Excel Dataframes
print('*********************************')
StateGunSafetyLaws = pd.read_excel('data\StateGunSafetyLaws.xlsx', header=0)
GunLawStrength = pd.read_excel('data\GiffordGunLawStrength.xlsx', header=0)
HomicidesbyState = pd.read_excel('data\HomicidesbyState.xls', header=3)
MostGunSales = pd.read_excel('data\StatesWheretheMostPeopleBoughtGunsFebruary2023.xlsx', header =0)

StateGunSafetyLaws.head()
print(StateGunSafetyLaws)
print('*********************************')
GunLawStrength.head()
print(GunLawStrength)
print('*********************************')
HomicidesbyState.head
print(HomicidesbyState)
print('*********************************')
MostGunSales.head
print(MostGunSales)

#Create SQLite Database with excel files
print('*********************************')
db_conn = sqlite3.connect("data/allFiles.db")
c = db_conn.cursor()

c.execute(
    """
    CREATE TABLE StateGunSafetyLaws(
        State TEXT,
        Law Type TEXT,
        Restrictive to Gun Owners TEXT,
        Bill Identifier TEXT,
        PRIMARY KEY(Bill Identifier),
        FOREIGN KEY(State) REFERENCES HomicidesbyState(State),
        FOREIGN KEY(Gun Law Strength(Ranked)) REFERENCES GunLawStrength(Gun Law Strength(Ranked))
        );
    """
    )

c.execute(
    """
    CREATE TABLE GunLawStrength(
        Gun Law Strength(Ranked) INTEGER
        State TEXT,
        Grade TEXT,
        Gun Death Rate(Ranked) INTEGER,
        Gun Death Rate (per 100K) INTEGER,
        PRIMARY KEY(Gun Law Strength(Ranked)),
        FOREIGN KEY(State) REFERENCES HomicidesbyState(State),
        FOREIGN KEY(Rank '2023') REFERENCES MostGunSales(Rank '2023')
        );
    """
    )

c.execute(
    """
    CREATE TABLE HomicidesbyState(
        State TEXT,
        Total Murders INTEGER,
        Total Firearms INTEGER,
        Handguns INTEGER,
        Rifles INTEGER,
        Shotguns INTEGER,
        Type unknown INTEGER,
        Knives or cutting instruments INTEGER,
        Other Weapons INTEGER,
        PRIMARY KEY(State),
        FOREIGN KEY(Rank '2023') REFERENCES MostGunSales(Rank '2023'),
        FOREIGN KEY(Gun Law Strength(Ranked)) REFERENCES GunLawStrength(Gun Law Strength(Ranked))
        );
    """
    )

c.execute(
    """
    CREATE TABLE MostGunSales(
        State TEXT,
        Firearm Background Checks per 1,000 Residents, Feb 2023 DECIMAL,
        Firearm Background Checks, Feb 2023 REAL,
        Firearm Background Checks per 1,000 Residents, Feb 2022 DECIMAL,
        Firearm Background Checks, Feb 2022 REAL,
        '2022' Population REAL,
        Rank '2023' INTEGER,
        Firearm Type TEXT,
        PRIMARY KEY(Rank '2023'),
        FOREIGN KEY(State) REFERENCES HomicidesbyState(State),
        FOREIGN KEY(Gun Law Strength(Ranked)) REFERENCES GunLawStrength(Gun Law Strength(Ranked))
        );
    """
    )

MurderVictimsbyWeapon.to_sql('MurderVictimsbyWeapon', db_conn, if_exists='append', index=False)
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

connection.close()

