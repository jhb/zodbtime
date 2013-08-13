zodbtime
========

Measurements on zodb and persistent objects

All the code creates 100k nodes and 1m edge objects. Whats differing is the format of the edges, or their content.

Some extract from the code is:

    g=root['graphdb']
    g.nodes=IOBTree()
    g.edges=IOBTree()

    
    for j in range(1,1000001):
        edge = [[j,random.randint(1,100000),random.randint(1,100000),{}]
        g.edges[j]=edge


The differences between the files


    Test            edge              node refs      data
    ====            ====              =========      ====

    testid:         list              int            empty dict
    testplist:      PersistentList    int            empty dict
    testref:        list              object ref     empty dict
    testpref:       PersistentList    object ref     empty dict
    testdatatuple:  list              int            tuple 
    testdataplist:  list              int            PersistentList 
    testdatadict:   list              int            dict 
    testdatapmap:   list              int            PersistentMapping
    testdataclass:  list              int            'normal' class instance
    testdatapclass: list              int            Persistence inheriting class instance




    Test           Data.fs (MB)  Init RAM (MB)   load time(s)    loaded RAM(MB)    extract time(s)    extracted RAM (MB)    
    ====           ============  =============   ============    ==============    ===============    ==================

    testid                   30      181    21           2.28        692    531               0.09            693    533
    testplist               133      189    29          3.593        432    271               28.3           1239   1100
    testref                  38      181    21          3.349       1081    920               0.13           1082    921
    testpref                141      189    29          3.583        432    271              30.69           1726   1500
    testdatatuple            30      181    21          1.883        422    261               0.04            423    262
    testdataplist           148      189    29          4.697        636    476               0.06            652    483
    testdatadict             35      181    21          2.388        694    533               0.09            695    534
    testpmap                153      189    29          4.617        636    474               0.06            650    483
    testdataclass            49      181    21          3.994        756    595               0.08            757    596
    testdatapclass          121      189    29          4.409        636    476               0.06            652    483


The order of steps was the following:

- create Data with `python <test>.py`
- ls -alh Data.fs                                                                     Data.fs (MB)
- open console with `ipython -i console.py`      
- look in `top` to see ram values                                                     Init RAM (MB)
- execute `timeit()` in console (this loads all the edges)                            load time(s)
- look in `top` to see ram values                                                     loaded RAM(MB)
- execute `extract()` in console (this accesses the last data element in the edges)   extract time(s)
- look in `top` to see ram values                                                     extracted RAM (MB)
