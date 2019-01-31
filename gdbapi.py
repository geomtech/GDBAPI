import sqlite3

class Database:
    def __init__(self):
        self.selectedDatabase = None
        self.name = None

    def Create(self, name):
        if name != ":memory:":
            self.name = name + ".db"
        else:
            self.name = ":memory:"
        sqlite3.connect(self.name).close()

    def Select(self, name):
        self.name = name + ".db"
        self.selectedDatabase = sqlite3.connect(self.name)
        return (self.selectedDatabase.cursor(), self.name, self.selectedDatabase)

    def Commit(self):
        self.selectedDatabase.commit()

class Table:
    def __init__(self, database):
        self.selectedDatabase = database
        self.selectedTable = None

    def Create(self, name, columns):
        request = "CREATE TABLE " + name + str(columns)        
        
        self.selectedDatabase[0].execute(request)
        
        print("[DEBUG]", "request=", request)
        print("[INFO]", "Table", name, "created with", columns, "in", self.selectedDatabase[1], "database")

    def Select(self, name):
        self.selectedTable = name

    def Insert(self, values):
        request = "INSERT INTO " + self.selectedTable + " VALUES " + str(values)
        self.selectedDatabase[0].execute(request)

    def FetchAll(self):
        request = "SELECT * from " + self.selectedTable
        print("[DEBUG]", "request=", request)        

        c = self.selectedDatabase[0]
        c.execute(request)
        
        names = [description[0] for description in self.selectedDatabase[0].description]
        print(names)

        for row in self.selectedDatabase[2].execute(request):
            print(row)
