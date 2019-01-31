import gdbapi

database = gdbapi.Database()
db = database.Select("test")

table = gdbapi.Table(db)

table.Select("Users")
table.FetchAll()