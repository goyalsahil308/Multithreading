import sqlite3
con = sqlite3.connect("employee.db")
c = con.cursor()


def createDb():
    c.execute('''CREATE TABLE employee
      (
          first_name text,
          last_name text,
          salary integar,
          e_id integar ,
          age integar

      )''')


def putValueSingle():

    c.execute('''INSERT INTO employee VALUES ("Sahil","Goyal",1000000,1,22)''')
    c.execute('''INSERT INTO employee VALUES ("Akshdeep","Singh",150000,2,23)''')
              


def putMultivalues(manyval):

    c.executemany('''INSERT INTO employee VALUES (?,?,?,?,?)''', manyval)


def update(sal, id):

    c.execute(f'''UPDATE employee set salary= {sal} WHERE e_id={id}''')


def printSingleValues():
    c.execute('''SELECT rowid,* FROM employee''')
    print(c.fetchone())

def printAllValues():
    c.execute('''SELECT rowid,* FROM employee''')
    print(c.fetchall())
def printManyValue():
    c.execute('''SELECT rowid,* FROM employee''')
    l1 = c.fetchall()
    # for i in range(1,len(c.fetchall())+1):
    #     print(f'''EMPLOYEE {i}''')
    i = 1

    for item in l1:
        print(f'''EMPLOYEE {i}''')

        print(f'''
                           Employee Name  : {item[1]} {item[2]}
                           AGE            : {item[5]}
                           Employee id    : {item[4]}
                           Salary         : {item[3]}
                ''')
        i = i+1


def delete(id):
    c.execute(f'''DELETE FROM employee WHERE e_id={id}''')


createDb()
con.commit()
putValueSingle()
con.commit()
manyval = [("Bhusahn", "Kumar", 10000, 3, 22), ("Ram", "garg", 50000, 4, 25),
           ("tim", "cook", 30000, 5, 35), ("Deepak", "Singh", 100000, 6, 54)]

putMultivalues(manyval)
con.commit()
printManyValue()
con.commit()
delete(5)
con.commit()
update(20000,4)
con.commit()
printManyValue()
con.commit()
con.close()




# printSingleValues()



# printManyValue()



# con.commit()
# printAllValues()
# printManyValue()
