'''
singlton pattern is responsible of creating one object and only one of class.
Real world example I think of is sqlite . It can handle one process at a time 
so no need to create a new class for connector for each process.
an app (web, mobile) no need to have object for each process only one object can do

'''

import sqlite3

class SingltonMetaType(type):
    _obj = None
    # this can be dictionary {cls : obj} if we expect to use that type for many classes
    # but since we use it for only our class so no need

    def __call__(cls, *args, **kwargs):
        if cls._obj == None:
            cls._obj = super().__call__(*args, **kwargs)
        return cls._obj

class SqliteHandeler(metaclass=SingltonMetaType):
    def __init__(self) -> None:
        self.con = sqlite3.connect('test.db')
        self.cur = self.con.cursor()

    def do_operation(self, operation : str) -> None:
        self.cur.execute(operation)
        self.con.commit()

    def close(self) -> None:
        self.con.close()

if __name__ == '__main__':

    p1 = SqliteHandeler()
    p1.do_operation("CREATE table test (data text)")

    p2 = SqliteHandeler()
    p2.do_operation("INSERT into test VALUES ('hello')")

    p2.close()
    print(p1 is p2)