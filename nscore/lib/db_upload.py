#!/usr/bin/python

import sqlite3
import sys

#This class models the list input to a formated Dictionary
class TestResultsModel(object):
    def __init__(self, tid, trun, release, version, component, status, category, description):
        self.tid         = tid
        self.trun        = trun
        self.release     = release
        self.version     = version
        self.component   = component
        self.status      = status
        self.category    = category
        self.description = description

    def asDict(self):
        testresults = {
           'tid'         : self.tid,
           'release'     : self.release,
           'trun'        : self.trun,
           'version'     : self.version,
           'component'   : self.component,
           'status'      : self.status,
           'category'    : self.category,
           'description' : self.description
        }
        return testresults

#This class models the list input to a formated Dictionary
class TestResultsModelPerf(object):
    def __init__(self, case, tid, category, release, version, component, trun, cps, hps, tprx, cps_avg, hps_avg, tprx_avg):
        self.case      = case
        self.tid       = tid
        self.category  = category
        self.release   = release
        self.version   = version
        self.component = component
        self.trun      = trun
        self.cps       = cps
        self.hps       = hps
        self.tprx      = tprx
        self.cps_avg   = cps_avg
        self.hps_avg   = hps_avg
        self.tprx_avg  = tprx_avg

    def asDict(self):
        perftestresults = {
           'release'    : self.release,
           'version'    : self.version,
           'component'  : self.component,
           'cps'        : self.cps,
           'hps'        : self.hps,
           'tprx'       : self.tprx,
           'cps_avg'    : self.cps_avg,
           'hps_avg'    : self.hps_avg,
           'tprx_avg'   : self.tprx_avg
        }
        return perftestresults

#This module processes the input file of smoke & regression testsuite
def process(testresultFile):
    '''Returns testresults models as a list'''
    l = []
    with open(testresultFile, 'r') as f:
        for line in f:
            if line.startswith("TestID") or (line.strip() == "") or line.startswith("Failed"):
                continue

            tid, trun, rel, ver, comp, status, category, description = line.strip().split(",")
            l.append(TestResultsModel(tid, trun,  rel, ver, comp, status, category, description).asDict())
    return l

#This module processes the input file of perfomance testsuite
def process_perf(perftestresultsfile):
    '''Returns performance testresults as a list'''
    
    p = []
    try:
        with open(perftestresultsfile, 'r') as f:
            case, tid, category, release, version, component, tr, cps, hps, tprx, cps_avg, hps_avg, tprx_avg = f.readlines()[1].strip().split(",")
            p.append(TestResultsModelPerf(case, tid, category, release, version, component, tr, cps, hps, tprx, cps_avg, hps_avg, tprx_avg).asDict())
    except IndexError:
        print "Splitting error. Returning"
    except IOError:
        print "File not found. Returning"
     
    return p

#This module responsible for upload the processed results of smoke & regression suite and upload to sqlite database 
def upload_to_db(infile, testresults, database):

    DATABASE =  database
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
   
    #Reads input file and gets the release id  from analytics.db for the same release
    with open('%s' %infile) as f:
        line = f.readlines()[1].strip().split(',')
        rel = line[2]
        cursor.execute('SELECT COUNT(*) FROM release WHERE name = "%s"' %rel)
        count = cursor.fetchone()
        if count[0] == 1:
            cursor.execute('SELECT id FROM release where name = "%s"' %rel)
            release_id = cursor.fetchone()
        else:
            cursor.execute('INSERT INTO release VALUES((select max(id) from release)+1, "%s")' %rel)
            cursor.execute('SELECT id FROM release where name = "%s"' %rel)
            release_id = cursor.fetchone()

    #Reads input file and gets component id from analytics.db for the same component 
    with open('%s' %infile) as f1:
        line1 = f1.readlines()[1].strip().split(',')
        comp = line1[4]
        cursor.execute('select id from component where name = "%s"' %comp)
        comp_id = cursor.fetchone()
         
    #Reads input file and gets the category id from analytics.db for the same category of test
    with open('%s' %infile) as f2:
        line2 = f2.readlines()[1].strip().split(',')
        category_id = line2[6]
    
    cursor.execute('SELECT id FROM testcase WHERE id=(SELECT MAX(id) FROM testcase)')
    max_id = cursor.fetchone()
    _id = int(max_id[0]) 
    data = []
    
    for result in testresults:
        data.append((_id + 1,
            result['tid'],
            release_id[0],
            result['version'],
            comp_id[0],
            result['status'],
            category_id,
            result['description'],
            result['trun']))
        _id += 1
    
    #print data
    cursor.executemany('''INSERT INTO 
            testcase 
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)
    connection.commit()
    cursor.close()

#This module responsible for upload the processed results of performance suite and upload to sqlite database 
def upload_perf_data(infile, testresults, database, scripttype):
    DATABASE =  database
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    
    #Reads input file and gets the release id  from analytics.db for the same release
    with open('%s' %infile) as f:
        line1 = f.readlines()[0].strip().split(',')
        rel = line1[3]
        cursor.execute('SELECT COUNT(*) FROM release WHERE name = "%s"' %rel)
        count = cursor.fetchone()
        if count[0] == 1:
            cursor.execute('SELECT id FROM release where name = "%s"' %rel)
            release_id = cursor.fetchone()
        else:
            cursor.execute('INSERT INTO release VALUES((select max(id) from release)+1, "%s")' %rel)
            cursor.execute('SELECT id FROM release where name = "%s"' %rel)
            release_id = cursor.fetchone()

    #Reads input file and gets the component id  from analytics.db for the same component
	cursor.execute("SELECT id FROM component WHERE name = '{}'".format(scripttype))
	comp_id = cursor.fetchone()
    
    #Reads the input file and collects the values of cps, hps, throughput from the respective testcases
    with open('%s' %infile) as f2:
        lines = f2.readlines()
        cps = lines[0].split(',')[10]
        hps = lines[1].split(',')[11]
        throughput = lines[2].split(',')[12] 
    cursor.execute('SELECT id FROM performance WHERE id=(SELECT MAX(id) FROM performance)')
    max_id = cursor.fetchone()
    data = []
    _id = int(max_id[0])
    
    for result in testresults:
        data.append((_id + 1,
            release_id[0],
            comp_id[0],
            result['version'],
            hps,
            cps,
            throughput))
        _id += 1

    cursor.executemany('''INSERT INTO 
            performance 
            VALUES(?, ?, ?, ?, ?, ?, ?)''', data)
    connection.commit()
    cursor.close()

def upload_performance_stats(infile, testresults, database, scripttype):
    DATABASE =  database
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    
    #Reads input file and gets the release id  from analytics.db for the same release
    with open('%s' %infile) as f:
        line1 = f.readlines()[0].strip().split(',')
        rel = line1[3]
        cursor.execute('SELECT COUNT(*) FROM release WHERE name = "%s"' %rel)
        count = cursor.fetchone()
        if count[0] == 1:
            cursor.execute('SELECT id FROM release where name = "%s"' %rel)
            release_id = cursor.fetchone()
        else:
            cursor.execute('INSERT INTO release VALUES((select max(id) from release)+1, "%s")' %rel)
            cursor.execute('SELECT id FROM release where name = "%s"' %rel)
            release_id = cursor.fetchone()

    #Reads input file and gets the component id  from analytics.db for the same component
	cursor.execute("SELECT id FROM component WHERE name = '{}'".format(scripttype))
	comp_id = cursor.fetchone()
    
    #Reads the input file and collects the values of cps, hps, throughput from the respective testcases
    with open('%s' %infile) as f2:
        lines = f2.readlines()
        cps = lines[0].split(',')[10]
        cps_tr = lines[0].split(',')[6].split('R')[1]
        hps = lines[1].split(',')[11]
        hps_tr = lines[1].split(',')[6].split('R')[1]
        throughput = lines[2].split(',')[12] 
        throughput_tr = lines[2].split(',')[6].split('R')[1]
    cursor.execute('SELECT id FROM performance_stats WHERE id=(SELECT MAX(id) FROM performance_stats)')
    max_id = cursor.fetchone()
    print max_id
    data = []
    
    try:
        _id = int(max_id[0]) + 1
    except TypeError:
        _id = 1
    
    data = []
    for result in testresults:
        data.append((_id,
            result['version'],
            release_id[0],
            comp_id[0],
            1,
            cps,
            cps_tr))
        _id += 1

    cursor.executemany('''INSERT INTO 
            performance_stats 
            VALUES(?, ?, ?, ?, ?, ?, ?)''', data)

    data = []
    for result in testresults:
        data.append((_id,
            result['version'],
            release_id[0],
            comp_id[0],
            2,
            hps,
            hps_tr))
        _id += 1

    cursor.executemany('''INSERT INTO 
            performance_stats
            VALUES(?, ?, ?, ?, ?, ?, ?)''', data)

    data = []
    for result in testresults:
        data.append((_id,
            result['version'],
            release_id[0],
            comp_id[0],
            3,
            throughput,
            throughput_tr))
        _id += 1

    cursor.executemany('''INSERT INTO
            performance_stats
            VALUES(?, ?, ?, ?, ?, ?, ?)''', data)
    connection.commit()
    cursor.close()


def main():
    infile = sys.argv[1]
    database = sys.argv[2]
    
    try:
        perf_flag, component_name = sys.argv[3], sys.argv[4]
    except IndexError as e:
        perf_flag, component_name = False, 'NetStorm'

    if perf_flag is False:
        upload_to_db(infile, process(infile), database)
    else:
        upload_perf_data(infile, process_perf(infile), database, component_name)
        upload_performance_stats(infile, process_perf(infile), database, component_name)

if __name__ == "__main__":
    main()
