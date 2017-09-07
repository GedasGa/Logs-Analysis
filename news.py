#!/usr/bin/env python

import psycopg2

DBNAME = "news"

question_1 = "What are the most popular three articles of all time?"
query_1 = """
Select articles.title, count(log.status) as views
from articles join log
on log.path like concat('%', articles.slug)
and log.status like '2%'
group by articles.title
order by views desc, articles.title limit 3;
"""

def get_top_articles(question, query):
  """Find the most popular three articles of all time"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute(query)
  result = c.fetchall()
  db.close()
  print(question)
  for i in results:
      print "%s -- %s views" % (i[0], i[1])

def get_popular_authors():
  """Find the most popular article authors of all time"""

def get_error_percentage():
  """Find on which days did more than 1% of requests lead to errors"""
