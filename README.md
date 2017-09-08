# Logs Analysis

**by Gedas Gardauskas**

In this project, I was working with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report. I have interacted with a live database both from the command line and from my code. I have explore a large database with over a million rows. And you built and refined complex queries to draw business conclusions from data.

## What it is and it does

This is a Python program which connects to an existing database on a Virtual machine using the psycopg2 module. It executes complex queries to get a meaningful data out of the database and prints it out to the command line in plain text.

## Required Libraries and Dependencies

- Python 2.x is required to run this project. The Python executable should be in your default path, which the Python installer should have set.
- Vagrant
- VirtualBox that is compatible with Vagrant.

## Getting started

### Setup Project:

- Install Vagrant and VirtualBox
Take a look [here](https://drupalize.me/videos/installing-vagrant-and-virtualbox?p=1526) to find more information.
- Download the project .zip file to you computer and unzip the file or clone this repository to your desktop.
- You can download or clone [this](https://github.com/udacity/fullstack-nanodegree-vm) repository with vagrant files.
- Then download [database file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
- Now unzip it and make sure you place `newsdata.sql` file into vagrant folder.

#### This project consists for the following files:
- `news.py` - main python file containing all queries and other stuff doing all the work
- `newsdata.sql` - database file with all records

### Launching the Virtual Machine:

- Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  `$ vagrant up`
- Then Log into this using command:
  `$ vagrant ssh`
- Change directory to /vagrant and look around with ls.

### Setting up the database and Creating Views:

To load the data, use the command `psql -d news -f newsdata.sql`.
Here's what this command does:

- `psql` — the PostgreSQL command line program
- `-d news` — connect to the database named news which has been set up for you
- `-f newsdata.sql` — run the SQL statements in the file newsdata.sql

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

### The database includes three tables:

- The `authors` table includes information about the authors of articles.
- The `articles` table includes the articles themselves.
- The `log table` includes one entry for each time a user has accessed the site.

Use `psql -d news` to connect to database.

### Creating Views:

To create views you first have to connect to the database base using the command from above.
Then just paste the code bellow to create a new view.

```
CREATE VIEW total_errors AS
SELECT DATE(time) as day, COUNT(status) AS errors
FROM log
WHERE status like '4%'
GROUP BY day;
```

```
CREATE VIEW total_visits AS
SELECT DATE(time) AS day, COUNT(status) AS total
FROM log
GROUP BY day;
```
