QUICK START 

SERVER/USER DEPENDANCIES 
install virtual environment
activate your virtual environment
python -m pip install -U 'channels[daphne]'  --> install channels and daphne server

We will need a docker container so install docker in your environment
$ python3 -m pip install channels_redis  -->  install this to let channels adapt to redis 
docker run --rm -p 6379:6379 redis:7 --> redis backing store



AGENT CLIENT DEPENDANCIES
Install these utils on the agent machine

pip install psutil # controllare le stat del pc
pip install keyboard #keylogger
pip install websocket-client


Since im working on a way to set sudo password, some command might not be fully working





