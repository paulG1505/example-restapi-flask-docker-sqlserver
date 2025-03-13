class Config:
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://SA:Passw0rd2021*%23@localhost:1433/mydb?driver=ODBC+Driver+17+for+SQL+Server"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
