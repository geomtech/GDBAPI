import gdbapi

database = gdbapi.Database()
db = database.Select("test")

table = gdbapi.Table(db)
table.Select("Users")
table.Insert((1,1,1,0))

database.Commit()

