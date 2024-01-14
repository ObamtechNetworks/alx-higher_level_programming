# Project: Python - Object-relational mapping
### Introduction
This project focuses on bridging the realms of databases and Python through the utilization of Object-Relational Mapping (ORM). Two key modules, MySQLdb and SQLAlchemy, will be explored to connect to a MySQL database and execute SQL queries seamlessly. ORM abstracts storage details, allowing developers to focus on manipulating objects in Python without delving into the intricacies of database storage.

### Prerequisites
Before diving into the project, ensure your MySQL server is in version 8.0. Here's how to install MySQL 8.0 in Ubuntu 20.04:

```bash
sudo apt-get install python3.8-venv
python3 -m venv venv
source venv/bin/activate
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient
```

### Overview
- Part 1: MySQLdb
In the initial phase, we'll use MySQLdb to connect to a MySQL database and execute SQL queries. This involves writing SQL queries in Python, which can be powerful but requires knowledge of SQL syntax.

Example without ORM:


```python
Copy code
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

### Part 2: SQLAlchemy
In the second part, we introduce SQLAlchemy as an ORM. This allows us to interact with the database using Python objects instead of direct SQL queries. The focus shifts from "How is this object stored?" to "What can I do with my objects?"

Example with ORM:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
```

### Resources
- Object-relational mappers
- mysqlclient/MySQLdb documentation
- SQLAlchemy tutorial
- SQLAlchemy ORM Tutorial for Python Developers
- Python Virtual Environments: A primer

### Learning Objectives
By the end of this project, you should be able to:

- Connect to a MySQL database from a Python script using MySQLdb.
- Execute SELECT, INSERT, and other SQL operations in Python using MySQLdb.
- Understand the concept of ORM and its advantages.
- Map a Python class to a MySQL table using SQLAlchemy.
- Create a Python Virtual Environment for project-specific dependencies.

### Instructions
- Clone this repository.
- Install the required dependencies in your virtual environment.
- Follow the provided examples and documentation to complete the tasks.
- Ensure your code adheres to the specified requirements.
- Create a detailed README.md at the root of the project folder.
