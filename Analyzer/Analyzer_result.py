import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine


###################################
# EDIT THESE CONSTANTS
###################################

GROUP = "ecs260-31"
DB_PASSWORD = "phrasing-litany-guttural-invest"
ANALYZER_NAME = "ecs260-31/cyclo5"
ANALYZER_VERSION = "0.0.1"
CORPUS_NAME = "r2c-1000"

###################################
# END EDIT SECTION
###################################

# Canonical SQL query to get job-specific results back.
JOB_QUERY = """
SELECT * 
FROM   result, 
       commit_corpus 
WHERE  result.commit_hash = commit_corpus.commit_hash 
       AND analyzer_name = %(analyzer_name)s 
       AND analyzer_version = %(analyzer_version)s
       AND corpus_name = %(corpus_name)s
"""

QUERY_PARAMS = {
    "corpus_name": CORPUS_NAME,
    "analyzer_name": ANALYZER_NAME,
    "analyzer_version": ANALYZER_VERSION
}

# Connect to PostgreSQL host and query for job-specific results
engine = create_engine(f'postgresql://notebook_user:{DB_PASSWORD}@{GROUP}-db.massive.ret2.co/postgres')
job_df = pd.read_sql(JOB_QUERY, engine, params=QUERY_PARAMS)

# Print pandas dataframe to stdout for debugging
print("Total percent of trivial packages after removing test files and folders:")


count =0 

for i in job_df[1:].extra:
	if ( (float(i['Average CYclomatic Time Complexity'])<=10) and (float (i['NLOC'])<=35)):
		count=count+1


print((count/job_df.shape[0])*100)
