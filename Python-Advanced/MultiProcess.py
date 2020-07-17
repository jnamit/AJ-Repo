import multiprocessing

# Refer https://pymotw.com/2/multiprocessing/basics.html
# Refer https://stackabuse.com/python-async-await-tutorial/
def worker(num):
    """thread worker function"""
    print ('Worker:', num)
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i+1,))
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
        print ('%s.exitcode = %s' % (j.name, j.exitcode))