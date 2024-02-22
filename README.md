ATTENTION: C2 is not implemented to work on different machine, yet. Use this on your own device.<br>

SERVER/USER DEPENDANCIES <br>
install virtual environment<br>
activate your virtual environment<br>
python -m pip install -U 'channels[daphne]'  --> install channels and daphne server<br>

We will need a docker container so install docker in your environment<br>
$ python3 -m pip install channels_redis  -->  install this to let channels adapt to redis <br>
docker run --rm -p 6379:6379 redis:7 --> redis backing store<br>

AGENT CLIENT DEPENDANCIES<br>
Install these utils on the agent's machine:<br>

pip install psutil -_> check ram and memory stats for jittering lookup requests<br>
pip install keyboard --> keylogger<br>
pip install websocket-client --> to handle communication with server<br>


!!! Since im working on a way to set sudo password, some command might not be fully working !!!<br>


QUICK START <br>
docker run --rm -dp 6379:6379 redis:7 --> run redis container<br>
{path_to_directory}/webapp$ python3 manage.py runserver --> run DAPHNE server<br>
python3 client.py --> run agent<br>

Create you admin running "python manage.py createsuperuser"<br>
You will need to login as administrator inside http://localhost:8000/admin/<br>
Add a user specifying username and password <br>
http://localhost:8000/ --> login --> select device test 2<br>
Run python3 client.py<br>
Send commands in chat <br>

