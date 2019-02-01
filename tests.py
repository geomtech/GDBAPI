import gdbapi

databasename = "gdbapipoc01"

def DBCreate():
    gdbapi.Database().Create(databasename)
    print("[DEBUG]", databasename, "database created.")

def TableCreate():
    try:
        database = gdbapi.Database()
        db = database.Select(databasename)

        table = gdbapi.Table(db)
        table.Create("Users", ("ID", "Fullname", "Mail", "Type"))

        database.Commit()
    except:
        print("[ERROR]", "Error when creating table, maybe data exists already?")

def InsertData():
    try:
        database = gdbapi.Database()
        db = database.Select(databasename)

        table = gdbapi.Table(db)
        table.Select("Users")
        table.Insert((1, "Alexy DA CRUZ", "Alexy.da-cruz@geomtech.fr", "admin"))
        table.Insert((2, "Jack DA CRUZ", "Jack.da-cruz@geomtech.fr", "standard"))
        table.Insert((3, "Jake DA CRUZ", "Jake.da-cruz@geomtech.fr", "moderator"))

        database.Commit()
    except:
        print("[ERROR]", "Error when inserting data, maybe data exists already?")

def Select():
    database = gdbapi.Database()
    db = database.Select(databasename)

    table = gdbapi.Table(db)

    table.Select("Users")
    for t in table.Fetch():
        print("[DEBUG][NO CONDITION]", t)
    for a in table.Fetch("WHERE ID = 1"):
        print("[DEBUG][WITH CONDITION]", a)

if __name__ == "__main__":
    DBCreate()
    TableCreate()
    InsertData()
    Select()