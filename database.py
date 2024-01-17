from sqlalchemy import Column, create_engine, Integer, Text, Date  #importing Column data types in SQL
from sqlalchemy.orm import declarative_base, sessionmaker


db_url = "sqlite:///userta.db"   #you can specify the database you would like to use "".py has url for different database
engine = create_engine(db_url)
 
base = declarative_base()

class databaseserver(base):
    __tablename__ = "classmanagementsystem"  #This will be name of the table in the database
    id = Column(Integer, autoincrement=True, primary_key=True)
    student_name = Column(Text)
    registration_number = Column(Text, nullable=False)
    admission_date = Column(Date)

session = sessionmaker(bind=engine)
Session = session()
base.metadata.create_all(engine)




