#! /usr/bin/python3
import os
import datetime
from dataclasses import dataclass


applications = ["chrome", "firefox", "Postman", "visual studio code",]


@dataclass
class MyPcWrapped():
    appname: str

    
    # get all applications subprocess
    def get_subprocess_ids(self):

        data = os.popen("pidof {}".format(self.appname)).read()
        ids = None
        if data == "":
            pass
        else:
            ids = data.split(" ")
    
        return ids

    # appends the time duration of each subprocess, and return the longest duration
    def get_process_longest_running_duration(self) -> datetime.datetime :
        ts = None
        ts_ls = []
        time_ls = []

        try:
            for i in self.get_subprocess_ids(): #remember when calling tis func ids is to be passed to the func's parameter space
                ts = os.popen("ps -p {0} -o etime".format(int(i))).read()
                try:
                    ts_ls.append(ts.splitlines( )[1].strip())
                except Exception as err:
                    #print(err)
                    pass
        except Exception as err:
            print(err)
            pass

        time = None

        for t in ts_ls:
            if len(t) == 5:            
                time = datetime.datetime.strptime(t, '%M:%S')
                time_ls.append(datetime.datetime.strftime(time, '%M:%S'))
            elif len(t) == 8:
                time = datetime.datetime.strptime(t, '%H:%M:%S')
                time_ls.append(datetime.datetime.strftime(time, '%H:%M:%S'))
            else:
                print("error converting time stamp {0}".format(t))
                continue
        if len(time_ls) < 1:
            return "Application Currently Not Running"
        return time_ls[-1]

    # append memory usage of individual subprocesses and return the total memory used.
    def get_total_process_memory(self) -> int:
        cmd = None
        total_memory_for_PID = []


        try:
            for i in self.get_subprocess_ids():
                cmd = os.popen("pmap {0}".format(int(i))).read()
                try:
                    total_memory_for_PID.append(cmd.splitlines( )[-1].strip())
                except Exception as err:
                    #print(err)
                    pass    
        except Exception as err:
            #print(err)
            pass        


        memory = [i[12:].strip() for i in total_memory_for_PID]
        sum_of_memory_used = 0
        for i in memory:
            sum_of_memory_used += int(i[0:-1])
        return sum_of_memory_used


apps_data = {

}

for i in applications:

    apps_data[i] = {'running_duration': MyPcWrapped(i).get_process_longest_running_duration(), 
        'total_memory_used': MyPcWrapped(i).get_total_process_memory()
    }
#print(apps_data)