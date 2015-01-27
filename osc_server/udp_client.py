import socket


"""
script to send data to unity
"""
UDP_IP = "127.0.0.1"
UDP_PORT = 8052
MESSAGE = "alpha_norm:0.0"

print "UDP target IP: ", UDP_IP
print "UDP target port: ", UDP_PORT
print "message: ", MESSAGE
value = 0.0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mellon_msg = "mellon:1"
concen_msg = "concentration:0"
while True:
    # value = value + 0.1
    # MESSAGE = "alpha_norm:" + str(value)
    sock.sendto(mellon_msg, (UDP_IP, UDP_PORT))