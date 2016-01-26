from pathlib import Path    
import sqlite3

connPostsDB = sqlite3.connect('posts.db')
crsrPostsDB = connPostsDB.cursor()



def updatePostDir ():
    contentDir = Path ('./static/text/')
    postPaths = []
    for path in contentDir.iterdir():
        if path.is_file() :
            path = str (path)
            postPaths.append (path)

    return postPaths

def updateDB():

    postPaths = updatePostDir()

    for path in postPaths:
        post = open(path, 'r')
        title = post.readline()
        date = post.readline()
        content = post.readlines()


    return
