# Gun-Law-Effects-on-Homicides-by-Firearms\


The following is my final project for Data Analysis 2 (March 2023) with Code Louisville. 
It is a Data Analysis of Gun Law Effects on Homicides by Firearms. My datasets include
an FBI table on Murders by state and the method of injury, information gathered from the
2023 Giffords: Courage to Fight Gun Violence Website, data on firearm Homicides for a 5 year
period, and a list of states where the most firearms were purchased from a 24 Wall St.LLC 
special report. My theory is that there will be more gun violence in the states with lax 
gun laws. I will use database comparisons and graphic visualizations to demonstrate the 
connections. The conclusions I have discovered is that though there is a clear impact from
states with the worst gun laws having higher firearm homocides, it is not as clear cut as
I had originally thought. Population and overall crime rates also play a significant factor.



Listed below are the requirements for the project.


I have uploaded Gun Law Effects on Homocides by Firearms into my GitHub repository greater
than the required 5 times.
This README file has been included and includes a description of my project. Relevant
packages to be installed and instructions to run are listed below. 
The project contains 4 original datasets. Three datasets are Excel files loaded into an
SQLite3 database. (Requirement 1) The other dataset is a local dataset built into SQLite3.
(Requirement 2) I Left Joined two tables in my SQLite3 database and combined a column with 
pandas on an Excel file. (Requirement 3) I created 3
visualizations with Matplotlib. (Requirement 4)

Project was written with Python in Visual Studio. You will run the program on GunLawEffects.py.
The following imports are needed.
import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
All Datasets are in the project, including StateGunSafetyLaws.db which is generated during the program.
When you run the program, all the data will be generated and you will have to scroll up 
to review. The graphs will need to be closed out before the next one appears. 
