# GDBAPI
Database management with sqlite3 using python.

``import gdbapi``
Don't forget to import GDBAPI!

## How to use GDBAPI?
Create a database :
```python
gdbapi.Database().Create("DATABASENAME")
```

Create a table in a database :
```python
db = gdbapi.Database().Select("DATABASENAME")
gdbapi.Table(db).Create("Users", ("ID", "Fullname", "Username", "Mail"))
```

Insert data in a table :
```python
db = gdbapi.Database().Select("DATABASENAME")

table = gdbapi.Table(db)
table.Select("Users")

values = ("1", "Alexy DA CRUZ", "geomtech", "alexy.da-cruz@geomtech.fr")
table.Insert(values)
```