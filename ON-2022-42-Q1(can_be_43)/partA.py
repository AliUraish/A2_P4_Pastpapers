# Part A — global 2D structure for jobs and count (adjust size / inner type per the question)
jobs: list[list] = []
number_of_jobs = 0

def Initialise():
    global jobs, number_of_jobs
    for x in range(0,100):
        jobs.append([-1,-1])
    number_of_jobs=0

def AddJob(jobnumber, priority):
    global jobs, number_of_jobs
    if number_of_jobs==100:
        print("Not Added: Array Full")
    else:
        jobs[number_of_jobs]=[jobnumber, priority]
        print("Added")
        Number_of_jobs+=1

Initialise()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)

def insertionsort():
    global jobs, number_of_jobs
    for x in range(1, number_of_jobs):
        job1=jobs[x][0]
        job2=jobs[x][1]
        while x>0 and jobs[x-1][1]<job2:
            jobs[x][0]=jobs[x-1][0]
            jobs[x][1]=jobs[x-1][1]
            x=x-1
        jobs[x][0]=job1
        jobs[x][1]=job2
