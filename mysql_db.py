import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",                # Localhost for local connection
  user ="root",
  passwd ="Sachin@12345"
)

print(dataBase)
dataBase.close()