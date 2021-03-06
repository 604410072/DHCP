﻿import argparse, sys, socket, time
from datetime import datetime

MAX_BYTES = 65535
Src = "0.0.0.0"
clientPort = 67
serverPort = 68

class DHCP_client(object):

	def client(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
		sock.bind((Src, serverPort))

		print("\nsend DHCPDISCOVER")
		data = DHCP_client.dhcpdiscover()
		sock.sendto(data,('<broadcast>', clientPort))

		data, address = sock.recvfrom(MAX_BYTES)
		print("\nreceive DHCPOFFER")
		print(data)

		print("\nsend DHCPREQUEST")
		data = DHCP_client.dhcprequest()
		sock.sendto(data,('<broadcast>', clientPort))

		data, address = sock.recvfrom(MAX_BYTES)
		print("\nreceive DHCPACK")
		print(data)
		
	def dhcpdiscover():		
		OP = bytes([0x01])
		HTYPE = bytes([0x01])
		HLEN = bytes([0x06])
		HOPS = bytes([0x00])
		XID = bytes([0x39, 0x03, 0xF3, 0x26])
		SECS = bytes([0x00, 0x00])
		FLAGS = bytes([0x00, 0x00])
		CIADDR = bytes([0x00, 0x00, 0x00, 0x00])
		YIADDR = bytes([0x00, 0x00, 0x00, 0x00])
		SIADDR = bytes([0x00, 0x00, 0x00, 0x00])
		GIADDR = bytes([0x00, 0x00, 0x00, 0x00])
		CHADDR1 = bytes([0x00, 0x0C, 0x29, 0xDD]) 
		CHADDR2 = bytes([0x5C, 0xA7, 0x00, 0x00]) 
		CHADDR3 = bytes([0x00, 0x00, 0x00, 0x00]) 
		CHADDR4 = bytes([0x00, 0x00, 0x00, 0x00]) 
		CHADDR5 = bytes(192)
		MagicCookie = bytes([0x63, 0x82, 0x53, 0x63])
		DHCPOptions1 = bytes([53 , 1 , 1])
		DHCPOptions2 = bytes([50 , 4 , 0xC0, 0xA8, 0x01, 0x64])
		End = bytes([0xff])
		
		package = OP + HTYPE + HLEN + HOPS + XID + SECS + FLAGS + CIADDR +YIADDR + SIADDR + GIADDR + CHADDR1 + CHADDR2 + CHADDR3 + CHADDR4 + CHADDR5 + MagicCookie + DHCPOptions1 + DHCPOptions2 + End
	
		return package
		
	def dhcprequest():		
		OP = bytes([0x01])
		HTYPE = bytes([0x01])
		HLEN = bytes([0x06])
		HOPS = bytes([0x00])
		XID = bytes([0x39, 0x03, 0xF3, 0x26])
		SECS = bytes([0x00, 0x00])
		FLAGS = bytes([0x00, 0x00])
		CIADDR = bytes([0x00, 0x00, 0x00, 0x00])
		YIADDR = bytes([0x00, 0x00, 0x00, 0x00])
		SIADDR = bytes([0x00, 0x00, 0x00, 0x00])
		GIADDR = bytes([0x00, 0x00, 0x00, 0x00])
		CHADDR1 = bytes([0x00, 0x0C, 0x29, 0xDD]) 
		CHADDR2 = bytes([0x5C, 0xA7, 0x00, 0x00])
		CHADDR3 = bytes([0x00, 0x00, 0x00, 0x00]) 
		CHADDR4 = bytes([0x00, 0x00, 0x00, 0x00]) 
		CHADDR5 = bytes(192)
		MagicCookie = bytes([0x63, 0x82, 0x53, 0x63])
		DHCPOptions1 = bytes([53 , 1 , 3])
		DHCPOptions2 = bytes([50 , 4 , 0xC0, 0xA8, 0x01, 0x64])
		DHCPOptions3 = bytes([54 , 4 , 0xC0, 0xA8, 0x01, 0x01])
		End = bytes([0xff])
		
		package = OP + HTYPE + HLEN + HOPS + XID + SECS + FLAGS + CIADDR +YIADDR + SIADDR + GIADDR + CHADDR1 + CHADDR2 + CHADDR3 + CHADDR4 + CHADDR5 + MagicCookie + DHCPOptions1 + DHCPOptions2 +  DHCPOptions3 + End
	
		return package
	
if __name__ == '__main__':
	dhcp_client = DHCP_client()
	dhcp_client.client()
