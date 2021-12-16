from socket import AF_INET, SOCK_STREAM, socket
from time import sleep
from os import getpid

# here is where we start the client process by assigning a process id 
if __name__ == '__main__':
    print('Application started')
    print('Os assigned process id: %d' %getpid())
    
    # opening and binding the clients socket with the server
    
    s = socket(AF_INET, SOCK_STREAM)
    print('TCP Socket created')
    print('File descriptor assigned by OS:', s.fileno())
    server_address = ('127.0.0.1',7777)
    s.connect(server_address)
    print('socket is connected to %s:%d' % s.getpeername())
    print('Local end-point is bound to %s:%d' % s.getsockname())

    #here we take message or client's mail adress so the server can use it to send mail'
    message = input("Please provide email to send infromation: ")
    if s.sendall(message.encode()) == None:
        print('Send %d bytes to %s:%d' % ((len(message),)+s.getpeername()))
    input('press Enter to terminate....')
    #here we terminate process 
    wait_secs = 3   
    print('Waiting %d seconds before termination ...' %wait_secs) 
    sleep(wait_secs)
    print('Closing the TCP socket...')
    s.close()
    print('terminating....')

