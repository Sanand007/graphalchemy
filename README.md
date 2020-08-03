##Package name - graphalchemy

###Recommended method is to create a virtual env in python3
Install pip using `python3 -m pip install --user --upgrade pip`

Install virtualenv using `python3 -m pip install --user virtualenv`

Create a virtual environment using `python3 -m venv {environment name, say, venv}`


###Install postgresql

###Copy the yaml in yamls dir to `~.etc/config/` dir and both csv in data dir to `~/etc/data/` dir

###Create database `galchemy`

Run `python src/graphalchemy/create_table.py` 
to create and insert data into weighted and directed 
table specified in db_config.yaml.

Run `pip install .` to install the package

Run `pytest` to run the tests in test_orm dir

Public apis available are
 
    1. Get the shortest path between vertex 'a' 
    and 'b' in weighted graph
    
    2. Get the successor of vertex 'a' in directed graph
    
    You can run the available public api after importing
    openapi and calling shortest_path('b', 'f') and 
    successor('b').