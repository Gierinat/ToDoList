from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, Date


engine = create_engine('sqlite:///todo.db?check_same_thread=False', echo=False)
Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    task = Column(String())
    deadline = Column(Date, default=datetime.today())


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def save_task(task):
    session = Session()
    session.add(task)
    session.commit()


def get_tasks(mode):
    session = Session()

    if mode == 'all':
        rows = session.query(Task).order_by(Task.deadline).all()
    elif mode == 'week':
        next_week = datetime.today() + timedelta(days=7)
        rows = session.query(Task).filter(Task.deadline >= datetime.today().date(),
                                          Task.deadline < next_week.date()).order_by(Task.deadline).all()
    elif mode == 'today':
        rows = session.query(Task).filter(Task.deadline == datetime.today().date()).all()
    else:
        rows = None

    return rows