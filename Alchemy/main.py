from sqlalchemy.sql.expression import and_, or_
from sqlalchemy.sql.sqltypes import Integer, String
import model
from db import engine, Base
from sqlalchemy import insert, select,Column, update, and_, or_
from model import User, Address
Base.metadata.create_all(engine)


def insert_one_user():
    stmt=insert(User).values(
        name='Habriel',
        fullname = 'Habriel Sabb',
        age=28,
        sex='M'
    )
    with engine.connect() as conn:
        conn.execute(stmt)

def insert_many_users():
    stmt=insert(User)
    with engine.connect() as conn:
        conn.execute(stmt, values)
values =[
    {'name':'Anna', 'fullname':'Anna Karenina', 'age': 28, 'sex': 'F'  },
    {'name':'Guido', 'fullname':'Guido van Rossum', 'age': 40, 'sex': 'M'},
    {'name':'Henry', 'fullname':'Henry Black', 'age': 60, 'sex': 'M'},
    {'name':'Lui', 'fullname':'Lui Viton ', 'age': 55, 'sex': 'M'},
    {'name':'Hanna', 'fullname':'Hanna Oberg', 'age': 38, 'sex': 'F'},
    {'name':'Hugh', 'fullname':'Hugh Lori', 'age': 62, 'sex': 'M'},
    {'name':'Fred', 'fullname':'Frederik Shopen', 'age': 34, 'sex': 'M'},
]

#insert_many_users()
#insert_one_user()

def select_users():
    stmt=(
       select(User.fullname, User.age, User.sex)
        .where (
            and_(User.sex=='M'),
                or_ (User.name.like('L%') , User.name.like('H%')))
        .limit(3)
        .order_by(User.age.desc()) 
     )
    with engine.connect() as conn:
        return list(conn.execute(stmt))

for row in select_users():
    print (row)



