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