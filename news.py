#!/usr/bin/env python

import psycopg2

DBNAME = "news"

question_1 = "What are the most popular three articles of all time?"
query_1 = """
SELECT articles.title, COUNT(log.status) AS views
FROM articles
JOIN log ON log.path LIKE concat('%', articles.slug)
AND log.status LIKE '2%'
GROUP BY articles.title
ORDER BY views DESC, articles.title LIMIT 3;
"""

question_2 = "What are the most popular three articles of all time?"
query_2 = """
SELECT authors.name, COUNT(log.status) AS views
FROM authors
JOIN articles ON articles.author = authors.id
JOIN log ON log.path LIKE concat('%', articles.slug)
AND log.status LIKE '2%'
GROUP BY authors.name
ORDER BY views DESC, authors.name;
"""

def get_top_articles(question, query):
  """Find the most popular three articles of all time"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute(query)
  results = c.fetchall()
  db.close()
  print(question) + '\n'
  for i in results:
      print "\"%s\" -- %s views" % (i[0], i[1])

def get_popular_authors(question, query):
  """Find the most popular article authors of all time"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute(query)
  results = c.fetchall()
  db.close()
  print(question) + '\n'
  for i in results:
      print "%s -- %s views" % (i[0], i[1])

def get_error_percentage():
  """Find on which days did more than 1% of requests lead to errors"""

if __name__ == '__main__':
    get_top_articles(question_1, query_1)
    get_popular_authors(question_2, query_2)
