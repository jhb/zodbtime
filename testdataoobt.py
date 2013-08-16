import cPickle, time, uuid, sys, random
import transaction
from ZODB.FileStorage import FileStorage
from ZODB.DB import DB
from BTrees.IOBTree import IOBTree
from BTrees.IIBTree import IIBTree
from BTrees.OOBTree import OOBTree
import testlib

storage = FileStorage('Data.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

root['graphdb']=testlib.gdb()

g=root['graphdb']
g.nodes=IOBTree()
g.edges=IOBTree()

for i in range(1,100001):
    node = [i,{}]
    g.nodes[i]=node

for j in range(1,1000001):
    edge = [j,random.randint(1,100000),random.randint(1,100000),OOBTree({'foo':'bar'})]
    g.edges[j]=edge
transaction.commit()
connection.close()
db.close()

