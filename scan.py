import os
import re


def execCmd(cmd):  
    r = os.popen(cmd)  
    text = r.read()  
    r.close()  
    return text  


error_keywords = ["ERROR SUMMARY", "Conditional jump or move depends", "uninitialised value", "Invalid"]


process = execCmd("ps -ux | grep xxx_server | grep valgrind")

regex = re.compile(r"--log-file=(.*?) \./gamesvr\.dbg -g /home/deke/(.*?)/bin")
result = regex.findall(process)
if result:
    log_path = "~/%s/bin/work/game1/bin/%s" % (result[0][1], result[0][0])
    print log_path
    for item in error_keywords:
        os.system('cat %s | grep "%s"' % (log_path, item))
    
