# prep_interviews

## Pyspark setup in Pycharm
1. create a project in pycharm
2. create virtual environment to keep package installation local to the virtual envrionment
  - Create virtual enviornment 
    - "$ python3 -m venv .venv"
  - Activate cirtual envronment 
    - source .venv/bin/activate
3. If you have virtual enviornment already then
   - create the requirment.tx (all package from the old enviornment)
     -  pip freeze > requirements.txt
   - install these packages to current projects venv
     - pip install -r ../<path to requirment.txt>/requirements.txt 