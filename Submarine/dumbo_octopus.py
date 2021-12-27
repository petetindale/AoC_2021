import functools as fn
import numpy as np

test_list_of_strings = [
	"5483143223\n", "2745854711\n", "5264556173\n", "6141336146\n",
	"6357385478\n", "4167524645\n", "2176841721\n", "6882881134\n",
	"4846848554\n", "5283751526\n"
]


def initialise_octopus_map(list_of_strings: list) -> np.array:
	return np.array(
		list(
			map(lambda rows: list(map(lambda chars: int(chars), rows.strip())),
							list_of_strings)), np.short)

def flash_octo(octo_map, I, J):
	for x in range(len(I)):
			top = I[x]-1 if I[x]>0 else 0 
			bottom = I[x]+2 if I[x]+1<10 else 10
			left = J[x]-1 if J[x]>0 else 0 
			right = J[x]+2 if J[x]+1<10 else 10
			#print(f"top {top} bottom {bottom} left {left} right {right}")
			octo_map[top:bottom, left:right] += 1
			new_I,new_J = np.where(octo_map[top:bottom, left:right]==10)
			
			new_I_arr = np.array(new_I)
			new_J_arr = np.array(new_J)
			
			new_I_arr += top
			new_J_arr += left
			flash_octo(octo_map,new_I_arr,new_J_arr)

def count_flashes(list_of_strings: str, count:int) -> int:
	octo_map = initialise_octopus_map(list_of_strings)
	#print(octo_map)
	i = 0
	flashes = 0
	while i < count :
		octo_map += 1
		I, J = np.where(octo_map==10)
		I_arr = np.array(I)
		J_arr = np.array(J)
		flash_octo(octo_map,I_arr,J_arr)
			
		curr_flash = np.count_nonzero(octo_map>9)
		if curr_flash == 100 : return i+1
		flashes += curr_flash
		octo_map[octo_map>9]=0
		#print(octo_map)
		i += 1
		
	return flashes


def test_count_flashes() -> None:
	print(f"Sum of Risk Level = {count_flashes(test_list_of_strings,200)}")
	print("From the script = 204 after 10")
	print("From the script = 1656 after 100")


#test_count_flashes()
#test_find_largest_basins()

