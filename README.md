ATTENTION: C2 is not implemented to work on different machine, yet. Use this on your own device.

SERVER/USER DEPENDANCIES 
install virtual environment\n
activate your virtual environment
python -m pip install -U 'channels[daphne]'  --> install channels and daphne server

We will need a docker container so install docker in your environment
$ python3 -m pip install channels_redis  -->  install this to let channels adapt to redis 
docker run --rm -p 6379:6379 redis:7 --> redis backing store

AGENT CLIENT DEPENDANCIES
Install these utils on the agent's machine:

pip install psutil -_> check ram and memory stats for jittering lookup requests
pip install keyboard --> keylogger
pip install websocket-client --> 


!!! Since im working on a way to set sudo password, some command might not be fully working !!!


QUICK START 
docker run --rm -dp 6379:6379 redis:7 --> run redis container
{path_to_directory}/webapp$ python3 manage.py runserver --> run DAPHNE server
python3 client.py --> run agent

