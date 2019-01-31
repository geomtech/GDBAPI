import gdbapi

database = gdbapi.Database()
db = database.Select("test")

table = gdbapi.Table(db)
table.Create("Users", ("Alexy", "Guillaume", "William", "Cyril"))

database.Commit()

