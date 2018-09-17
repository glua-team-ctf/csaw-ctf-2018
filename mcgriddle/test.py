#!/bin/env python3

from scapy.all import *
from lxml import html
from IPython import embed
from urllib.parse import unquote
import email
import pprint

writedir = "./files"
packets = rdpcap('final.pcap')
sessions = packets.sessions()
for s in sessions: # Iterate over sessions
    #print("\nSESSION START")
    for p in sessions[s]: # Iterate over packets in session
        if p.haslayer(DNS):
            print("")
        if p.haslayer(TCP) and p.haslayer(Raw):
            data = p.load.decode('utf-8')
            method, mime = data.split('\r\n', 1) # Split HTTP method out
            msg = email.message_from_string(mime)

            if (msg):
                print(method)
                if (msg.is_multipart()):
                    # This is a SVG
                    for part in msg.walk():
                        filename = part.get_filename()
                        if (filename):
                            print(filename)
                            file = open(writedir + "/" + filename, "w")
                            file.write(part.get_payload())
                            file.close()
                else:
                    # Regular HTTP
                    print(unquote(msg.get_payload()))

#embed()
