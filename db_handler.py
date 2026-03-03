from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Date


engine = create_engine('sqlite:///todo.db?check_same_thread=False', echo=True)
Base = declarative_base()

class Task(Base):
    __tablename__ = 'Task'

    id = Column(Integer, primary_key=True)
    task = Column(String(255))
    deadline = Column(Date, default=datetime.today())


Base.metadata.create_all(engine)