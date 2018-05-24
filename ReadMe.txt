
Read Me File on Project 10 SQL queries on "News" database

SQL Queries to external database "News". 

 To run a web service inside the VM which you'll be able to access from your regular browser.
	with the command:  http://localhost:5000/
 Vagrant and VirtualBox to install and manage the VM. The Vagrant interpreter On Windows, is using the Git Bash terminal that
 comes with the Git software. If you don't already have Git installed, download Git from git-scm.com.

-- created files in Brackets and inserted psycopg2 in files. Saved files in project folder, suggested: FSND-Virtual-Machine/ Project.py 

 database and vagrant files should also be kept in same project folder.
After navagating to project folder and installing "Vagrant" input command to call up the virtual environment:
$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
and   You will need a terminal open and logged in to your VM (with vagrant ssh) before continuing on.  when you run the forum code, you should only run it inside the Vagrant virtual machine, i.e. within a terminal window where you've run vagrant ssh to log into the VM.


https://tutorialedge.net/python/python-http-requests-tutorial/
\dt — list all the tables in the database.
\dt+ — list tables plus additional information (notably, how big each table is on disk).
\H — switch between printing tables in plain text vs. HTML.



Install psycopg2 in GitBash:
$ pip install psycopg2

--- Downloaded and installed database: "news"--

--To import the Psycopg2 package into your Python application you insert the following line of code into Brackets file to connect to external database:

#!/usr/bin/python
import psycopg2
conn = psycopg2.connect(database="news")
cur = conn.cursor()

---In GitBash: Call up:  Vagrant up and SSH: when connection is made the response is as follows:

>>  vagrant@vagrant:/vagrant$ ls
catalog  forum  newsdata.sql  project.py  select  tournament  Vagrantfile

>>  vagrant@vagrant:/vagrant$ python project.py

>>>    vagrant@vagrant:/vagrant$ psql -d news  // to connect to “news” database.


>> news=> \dt		// to list database tables in “news” 
          List of relations
 Schema |   Name   | Type  |  Owner
--------+----------+-------+---------
 public | articles | table | vagrant
 public | authors  | table | vagrant
 public | log      | table | vagrant
(3 rows)

Quaries can now be made useing SQL request commands to quary the "news" database.
	
