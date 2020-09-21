from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return str(self.id) + '. ' + self.task

    def getdate(self):
        return self.deadline

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

while True:
    print("""
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
    """)
    option = input()
    if option == '1':
        rows = session.query(Task).filter(Task.deadline == datetime.today().date()).all()
        print('Today ' + datetime.today().strftime('%d %b:'))
        if len(rows) > 0:
            for row in rows:
                print(row)
        else:
            print('Nothing to do!')

    elif option == '2':
        for i in range(0,8):
            print((datetime.today() + timedelta(days=i)).strftime('%A %d %b:'))
            rows = session.query(Task)\
                    .filter(Task.deadline == datetime.today().date() + timedelta(days=i))\
                    .all()
            if len(rows) > 0:
                for row in rows:
                    print(row)
                    print("")
            else:
                print('Nothing to do!\n')

    elif option == '3':
        print("All tasks:")
        rows = session.query(Task).order_by(Task.deadline).all()
        for row in rows:
            print(str(row) + '. ' + str(row.getdate().strftime('%#d %b')))

    elif option == '4':
        print("Missed tasks:")
        rows = session.query(Task).filter(Task.deadline < datetime.today().date()).order_by(Task.deadline).all()
        if len(rows) > 0:
            for row in rows:
                print(str(row) + '. ' + str(row.getdate().strftime('%#d %b')))
        else:
            print('Nothing is missed!\n')

    elif option == '5':
        your_task = input("Enter task\n")
        deadline = input("Enter deadline\n")
        new_row = Task(task=your_task, deadline=datetime.strptime(deadline, '%Y-%m-%d'))
        session.add(new_row)
        session.commit()
        print('The task has been deleted!')

    elif option == '6':
        rows = session.query(Task).order_by(Task.deadline).all()
        if len(rows) > 0:
            print('Choose the number of the task you want to delete:\n')
            for row in rows:
                print(str(row) + '. ' + str(row.getdate().strftime('%#d %b')))
            del_option = int(input())
            session.query(Task).filter(Task.id == del_option).delete()
            session.commit()

        else:
            print('Nothing to delete\n')

    elif option == '0':
        print('Bye!')
        break


#rows = session.query(Table).all()
#first_row = rows[0]
#print(first_row.string_field)
#print(first_row.id)
#print(first_row)
