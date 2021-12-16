
#library used to have access to socket and it's usess 

from socket import AF_INET, SOCK_STREAM, socket

#library that let's pyhton have access to the operating system here is specificaly the getpid functions

from os import getpid


import os

#this module can be used to send mail using smtp protocol 

import smtplib

#module used to determine the type of file or byte stream

import imghdr

#used to obtain network address
import uuid
#module used for emailing
from email.message import EmailMessage

#strting of process id using the system's OS

if __name__ == '__main__':
    print('')
    print('Application started')
    print('')
    print('Os assigned process id: %d' %getpid())
    os_pro_as = getpid()
    print('')
   
    # opening a socket and obtaining it's number
    
    s = socket(AF_INET, SOCK_STREAM)
    print('TCP Socket created')
    print('')
    print('File descriptor assigned by OS:', s.fileno())
    file_descriptor = s.fileno()
    print('')
    
    #binding the socket and giving it a port number
    
    s.bind(('127.0.0.1', 7777))
    print('socket is bound to %s:%d' % s.getsockname())
    print('')
    
    backlog = 0 

    #socket is in listening state waiting for client

    s.listen(backlog)
    print('socket is in listening state to %s:%d' % s.getsockname())
    print('')

    #accepting client connection to server

    client_socket,client_addr = s.accept()
    print('New client connected from %s:%d' % client_addr)
    print('Local end-point socket bound on: %s:%d'% client_socket.getsockname())
    print('')
    recv_buffer_length = 1024
    message = client_socket.recv(recv_buffer_length)
    print('Recieved %d bytes from %s:$%d' % ( (len(message),)+client_addr))
    print('')
    print('Received message: \n%s' %message)
    print('')

    # importing socket module
    import socket
    # getting the hostname 
    hostname = socket.gethostname()
    # getting the IP address using socket
    ip_address = socket.gethostbyname(hostname)
    # printing the client info
    print(f"Hostname: {hostname}")
    print('')
    print(f"IP Address: {ip_address}")
    print('')
    print ("This is your Mac adress", hex(uuid.getnode()))
    print('')

    mac_adr = hex(uuid.getnode())

    

   



# terminating the process
# can also add a timer using date time module before termination

    input('press Enter to terminate....')
    print('')
    print('Closing the TCP socket...')
    
    s.close()

    print('process terminated')
    
    #turning process into SMTP to send mail
    #using gmail as other usually won't work
    

    # here we use the email and password of the sender
    # put the email and password of the email you want to send from 
EMAIL_ADDRESS = 'aliislam4261@gmail.com'
EMAIL_PASSWORD = 'zqezzyijyhspudne'

#commencing connection to gmail using the SMTP protocol

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    #extra ehlo for encryption though not needed, it can be removed based on research 
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
# email subject and body, body is the clients info collected by the server 
    subject = 'client info'
    body = f''' your mac adress is: {mac_adr} 
    your hostname is: {hostname} 
    your adress is: {client_addr}
    File descriptor assigned by OS: {file_descriptor}
    Os assigned process id: {os_pro_as}
    socket: {client_socket}
    message from client: {message}

    '''

    msg = f'subject: {subject}\n\n{body}'

    # here we add email givin by client 
    # put the email address you want to send from first then the email you want to send to

    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

    print('mail sent')