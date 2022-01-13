test_list_of_strings = [
	"D2FE28\n"
]

def decode_hex(hexstr:str)->int:
		return int(hexstr,16)
				

class Packet:
	def __init__(self, packet:str)->None:
		self.hexstr = packet
		self.int_pk = decode_hex(self.hexstr)
		print(self.int_pk)
		
	

def decode_packet(list_of_strings:list)->int:
	list_of_packets = list(map(lambda x:Packet(x.strip()),list_of_strings))
	return 0
	
def test_decode_packet():
	print(f'Packet Decoded to {decode_packet(test_list_of_strings)}')

test_decode_packet()
