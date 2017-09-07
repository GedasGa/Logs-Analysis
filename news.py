#!/usr/bin/env python

import psycopg2

DBNAME = "news"

def get_top_articles(query):
  """Find the most popular three articles of all time"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute(query)
  result = c.fetchall()
  db.close()

  for i in results:
      print "%s -- %s views" % (i[0], i[1])  

def get_popular_authors():
  """Find the most popular article authors of all time"""

def get_error_percentage():
  """Find on which days did more than 1% of requests lead to errors"""
