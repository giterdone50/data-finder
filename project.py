#!/usr/bin/python
import psycopg2

conn = psycopg2.connect(database="news")

cur = conn.cursor()

#question 1    // 3 most popular ARTICLES, list in desending order.
print("Processing first query ...\n")
cur.execute('''
            SELECT title, count(articles.time)
            AS ArticleViews 
            FROM log, articles 
            WHERE path like concat('%', slug) 
            GROUP BY title 
            ORDER BY ArticleViews 
            DESC 
            LIMIT 3;
            ''')
rows = cur.fetchall()
print("Here is solution to question 1:")
for i in rows:
    print('"' + i[0] + '"' +" - "+ str(int(i[1])) + " views")

    
#question 2      //Which AUTHORS has the most PAGE VIEWS, list in desending order.
print("\n\nProcessing second query ...\n")
cur.execute('''
        SELECT name, count(log.time) 
        FROM log, articles, authors 
        WHERE log.status='200 OK' 
        AND log.path like concat('%', articles.slug) 
        AND articles.author = authors.id 
        GROUP BY authors.name 
        ORDER BY count(log.time) desc 
        LIMIT 4;
''')
rows = cur.fetchall()
print("Here is solution to question 2:")
for i in rows:
    print('"%s" - %s views' % (i[0], i[1]))
    
#question 3    // number of DAYS http STATUS CODE > then 1% errors.
#cur.execute("select * from articles;")
#data=cur.fetchall()
#print("\n\n")
#
#for each in data:
#    print(each)

print("\n\n")
conn.commit()
print("Records fetched successfully");
conn.close()