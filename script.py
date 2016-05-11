#Let's say a firewall is writing a log file with the following format:

#source_IP destination_IP size_of_the_packet_in_bytes

#Example: 
#10.0.0.1 200.0.0.42 34567
#10.0.0.2 200.0.0.43 09876987
#10.0.0.3 200.0.0.42 12345

# Question:
# 1. make a Python function that has the number of bytes received by IP address.
# -> 200.0.0.42 46567
# -> 200.0.0.42 9876987

# 2. make a Python function that has the list of IP address that connected to an destination IP address.


#1.
from collections import defaultdict
count = defaultdict(int)
count2 = defaultdict(list)

for line in open("text.txt"):
	ip_src, ip_dst, byte_string = line.split()
	count[ip_dst] += int(byte_string)
	
	if ip_dst not in count2:
		count2[ip_dst] = ip_src 
if ip_dst in count2:
	count2[ip_dst] = count2[ip_dst] + "  " +ip_src

for k, v in count.items():
	print "->",k,v

print (count2.items())	

	
#2.
# D_IP_address = {}
# for i in open("text.txt"):
# 	if i.split()[1] not in D_IP_address:
# 		D_IP_address[i.split()[1]] = (i.split()[0])
# if i.split()[1] in D_IP_address:
# 	D_IP_address[i.split()[1]] = D_IP_address[i.split()[1]] +"   "+(i.split()[0])
	
# print D_IP_address







		






	
	
