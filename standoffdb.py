from pathlib import Path    
import sqlite3

connPostsDB = sqlite3.connect('posts.db')
crsrPostsDB = connPostsDB.cursor()



def postDir ():
    contentDir = Path ('./static/text/')
    postPaths = []

    for path in contentDir.iterdir():
        if path.is_file() :
            path = str (path)
            postPaths.append (path)

    return postPaths


def updateDB():
    initDB()
    postPaths = postDir()

    for path in postPaths:
        postFile = open(path, 'r')
        h = postFile.readline()
        d = postFile.readline()
        t = ""

        for line in postFile.readlines():
            t += line

        postuple = (h, d, t)

        crsrPostsDB.execute("insert or ignore into posts values (?,?,?)", postuple)

    connPostsDB.commit()

def getPosts():
    crsrPostsDB.execute("select * from posts")
    connPostsDB.commit()

    return crsrPostsDB.fetchall()


def initDB():
    crsrPostsDB.execute("create table if not exists posts (title PRIMARY KEY, date, content)")
    connPostsDB.commit()

