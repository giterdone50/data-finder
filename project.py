#!/usr/bin/python
import psycopg2

conn = psycopg2.connect(database="news")

cur = conn.cursor()

#question 1    // 3 most popular ARTICLES, list in desending order.
cur.execute("select title, count(articles.time) as ArticleViews from log, articles where path like concat('%', slug, '%') group by title order by ArticleViews desc limit 3;")
rows = cur.fetchall()

print("Here is solution to question 1:")
for i in rows:
    print('"' + i[0] + '"' +" - "+ str(int(i[1])) + " views")

    
#question 2      //Which AUTHORS has the most PAGE VIEWS, list in desending order.
cur.execute("select * from authors;")
rows = cur.fetchall()

print("\n\n")
for i in rows:
    print(i)
    
#question 3    // number of DAYS http STATUS CODE > then 1% errors.
cur.execute("select * from articles;")
data=cur.fetchall()
print("\n\n")
for each in data:
    print(each)

conn.commit()
print("Records fetched successfully");
conn.close()