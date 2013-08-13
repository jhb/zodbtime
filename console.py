import cPickle, time, uuid, sys
import pygraph,transaction
from ZODB.FileStorage import FileStorage
from ZODB.DB import DB
import testlib

storage = FileStorage('Data.fs')
db = DB(storage)
connection = db.open()
root = connection.root()
g=root['graphdb']
x = None 

def timeit():
    global x
    start = time.time()
    x = list(g.edges.values())
    delta = time.time()-start
    print delta

def extract():
    global x
    start = time.time()
    y = [e[3] for e in x]
    delta = time.time()-start
    print delta
