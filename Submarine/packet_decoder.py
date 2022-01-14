

test_list_of_strings = [
	"D2FE28\n"
	,"38006F45291200\n"
	,"EE00D40C823060\n"
	#,"8A004A801A8002F478\n"
	#,"620080001611562C8802118E34\n"
	#,"C0015000016115A2E0802F182340\n"
	#,"A0016C880162017C3686B18A3D4780\n"
	#,"220D62004EF14266BBC5AB7A824C9C1802B360760094CE7601339D8347E20020264D0804CA95C33E006EA00085C678F31B80010B88319E1A1802D8010D4BC268927FF5EFE7B9C94D0C80281A00552549A7F12239C0892A04C99E1803D280F3819284A801B4CCDDAE6754FC6A7D2F89538510265A3097BDF0530057401394AEA2E33EC127EC3010060529A18B00467B7ABEE992B8DD2BA8D292537006276376799BCFBA4793CFF379D75CA1AA001B11DE6428402693BEBF3CC94A314A73B084A21739B98000010338D0A004CF4DCA4DEC80488F004C0010A83D1D2278803D1722F45F94F9F98029371ED7CFDE0084953B0AD7C633D2FF070C013B004663DA857C4523384F9F5F9495C280050B300660DC3B87040084C2088311C8010C84F1621F080513AC910676A651664698DF62EA401934B0E6003E3396B5BBCCC9921C18034200FC608E9094401C8891A234080330EE31C643004380296998F2DECA6CCC796F65224B5EBBD0003EF3D05A92CE6B1B2B18023E00BCABB4DA84BCC0480302D0056465612919584662F46F3004B401600042E1044D89C200CC4E8B916610B80252B6C2FCCE608860144E99CD244F3C44C983820040E59E654FA6A59A8498025234A471ED629B31D004A4792B54767EBDCD2272A014CC525D21835279FAD49934EDD45802F294ECDAE4BB586207D2C510C8802AC958DA84B400804E314E31080352AA938F13F24E9A8089804B24B53C872E0D24A92D7E0E2019C68061A901706A00720148C404CA08018A0051801000399B00D02A004000A8C402482801E200530058AC010BA8018C00694D4FA2640243CEA7D8028000844648D91A4001088950462BC2E600216607480522B00540010C84914E1E0002111F21143B9BFD6D9513005A4F9FC60AB40109CBB34E5D89C02C82F34413D59EA57279A42958B51006A13E8F60094EF81E66D0E737AE08"
]

def decode_hex(hexstr:str)->int:
	return int(hexstr,16)

def decode_hex_to_bin(hexstr:str)->bin:
	return bin(decode_hex(hexstr))

BinPacket = tuple[int,int] #packet, length

def remove_head(pack:BinPacket,offset:int)->BinPacket:
	bn, bn_ln = pack
	return ((bn & ~((len^2 - 1)<<bn_ln - offset)), bn_ln - offset)

class Packet:
	def __init__(self, packet:str='')->None:
		if packet != '' :
			self.hexstr:str = packet
			self.int_pk:int = decode_hex(self.hexstr)
			self.bin_pk:bin = bin(self.int_pk)
			self.bit_len = len(self.hexstr)*4
			self.pack:BinPacket = (self.int_pk, self.bit_len)
		
	
	def version(self)->int:
		#Get 3 MSBs
		return self.int_pk >> (self.bit_len-3)
	
	def type(self)->int:
		#Get MSB 4-6
		return (self.int_pk >> self.bit_len-6) & 7

	def payload_pack(self)->BinPacket:
		return ((self.int_pk & ~(63<<self.bit_len-6)), self.bit_len - 6)
	
	def value(self)->BinPacket:
		if self.type() == 4:
			pld, pld_len = self.payload_pack()
			original_len = pld_len
			value = 0
			end = False
			while not end :
				value = (value << 4) | ((pld >> pld_len-5)&15)
				end = (pld >> pld_len-1 != 1)
				pld = pld & ~(31<<pld_len-5)
				pld_len -= 5
			return (value, original_len-pld_len)

	def return_excess(self)->BinPacket:
		if self.type() == 4:
			value, value_len = self.value()
			
			
		else:
			return (0,0)


	def subpackets(self)->list:
		if self.type() != 4 :
			pld, pld_len = self.payload_pack()

			if pld >> pld_len-1 == 0 : # Length Type with 15 bits
				length = (pld >> pld_len-16)&((2^15)-1)
				pkts = pld >> 16
				pkts_len = pld_len - 16

			else : #Number of Packets	
				number = (pld >> pld_len-12)&((2^11)-1)
				pkts = pld >> 12
				pkts_len = pld_len - 12




	def __str__(self) -> str:
		return "-------------\n" +\
			f"Hex : {self.hexstr[0:5]}...\n" + \
			f"Binary : {self.bin_pk[0:10]}...\n"+ \
			f"Version : {self.version()}\n" + \
			f"Type : {self.type()}\n" + \
			f"Hex Pld : {self.value()}\n" + \
			"~~~~~~~~~~~~~"

class PacketFromStream(Packet):
	def __init__(self, packets: int, packets_length: int) -> None:
		self.bit_len = packets_length
		self.int_pk = packets
		self.bin_pk = bin(packets)
		self.hexstr = f'{self.int_pk:X}'
	



def decode_packet(list_of_strings:list)->int:
	list_of_packets = list(map(lambda x:Packet(x.strip()),list_of_strings))

	for pack in list_of_packets:
		print(pack)
	return 0
	
def test_decode_packet():
	print(f'Packet Decoded to {decode_packet(test_list_of_strings)}')

test_decode_packet()
