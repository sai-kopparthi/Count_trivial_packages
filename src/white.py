import json
import re
import sys
import lizard
import subprocess,shlex
import os
WHITESPACE_RE = re.compile("\s")


def count_whitespace(path):
  print("Counting complexity in file {}".format(path))
#Exclude files that match the pattern. * matches everything, ? matches any single character "./folder/*" exclude everything in the fold recursively
  out = subprocess.Popen([ 'lizard' , path , '-x' , "*/test*"], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
  stdout,stderr = out.communicate()
  m=stdout.splitlines()
  a=m[-1]
  b=a.decode().split()
  result={}
  result["check_id"] = "Complexity"
  result["path"] = path
  result["extra"] = {}
  result["extra"]["NLOC"] = b[0]
  result["extra"]["Average CYclomatic Time Complexity"] = b[2]
  return result
  

all_results = []
all_results.append(count_whitespace(os.getcwd()))


with open("/analysis/output/output.json", "w") as output:
    output.write(json.dumps({"results": all_results}, sort_keys=True, indent=4))
