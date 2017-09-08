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

## Running the program:

After you've completed all the steps above you can run the program. You can do this by executing this line of code in your Virtual Machine:
 `python news.py`

## Questions and notes form Udacity

So what are we reporting, anyway?
Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

**1\. What are the most popular three articles of all time?** Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

**Example:**

- "Princess Shellfish Marries Prince Handsome" — 1201 views
- "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
- "Political Scandal Ends In Political Scandal" — 553 views

**2\. Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

**Example:**

- Ursula La Multa — 2304 views
- Rudolf von Treppenwitz — 1985 views
- Markoff Chaney — 1723 views
- Anonymous Contributor — 1023 views

**3\. On which days did more than 1% of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

**Example:**

- July 29, 2016 — 2.5% errors
