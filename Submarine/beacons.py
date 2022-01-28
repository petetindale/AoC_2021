from math import sqrt
import beacon_tests


class Beacon:
    def __init__(self, x:int, y:int, z:int) -> None:
        self.x = x
        self.y = y
        self.z = z
        pass

    def __str__(self) -> str:
        return f'[{self.x}, {self.y}, {self.z}]'

    @classmethod
    def distance(cls, b1:'Beacon', b2:'Beacon')->float:
        c = (b1.x-b2.x)**2 + (b1.y-b2.y)**2 + (b1.z-b2.z)**2
        return sqrt(c)

    @classmethod
    def beacon_from_str(cls, beaconstr:str) -> 'Beacon':
        x, y, z = beaconstr.split(',')
        return Beacon(int(x), int(y), int(z))

class Scanner:
    def __init__(self, name:str, beacons:list) -> None:
        self.name = name
        self.beacons:list = beacons
        self.distances:dict = Scanner.build_distance_dict(self.beacons)

    def __str__(self) -> str:
        beacons_str = ''
        for bc in self.beacons:
            beacons_str += f'{bc},'

        return f'{self.name}\n{beacons_str}' 
    
    @classmethod
    def build_distance_dict(cls, beacons:list)->dict:
        distances = dict()
        for a in range(len(beacons)):
            for b in range(len(beacons)-a):
                if a != b+a:
                    dist = Beacon.distance(beacons[a], beacons[b+a])
                    if(dist in distances.values()): 
                        print('duplicated')
                    distances[(a,b+a)] = dist
        return distances
    
    @classmethod
    def compare_distances(cls, d1:dict, d2:dict)->int:
        count = 0
        for dist in d1.values():
            if dist in d2.values(): 
                count += 1 
        return count

    @classmethod
    def scanner_from_strs(cls, scanner_strs:list)->'Scanner':
        name = scanner_strs[0].strip()
        beacons = list(map(lambda bstr: Beacon.beacon_from_str(bstr.strip()), scanner_strs[1::]))
        return Scanner(name, beacons)      

class ScannerList:
    def __init__(self, scanners:list) -> None:
        self.scanners = scanners
        pass

    def __str__(self) -> str:
        scanner_str = '===================\n'
        for scanner in self.scanners:
            scanner_str += f'{scanner}\n'
        scanner_str += '==================='
        return scanner_str
    
    def compare_distances(self)->int:
        count = 0
        for a in range(len(self.scanners)):
            for b in range(len(self.scanners)-a):
                if a != b+a:
                    cmp = Scanner.compare_distances(self.scanners[a].distances, self.scanners[b+a].distances)
                    print(f'{a} {b+a} {len(self.scanners[a].distances)} & {cmp}')
                    count += cmp
        return count
    
    @classmethod
    def scanners_from_list(cls, list_of_strings:list)->'ScannerList':
        scanners = list()
        scannerstrs = list()
        for str in list_of_strings:
            if str.strip() == '':
                scanner = Scanner.scanner_from_strs(scannerstrs)
                scanners.append(scanner)
                scannerstrs = list()
            else:
                scannerstrs.append(str)
        scanner = Scanner.scanner_from_strs(scannerstrs)
        scanners.append(scanner)
        return ScannerList(scanners)

def count_beacons(list_of_strings:list)->int:
    sl = ScannerList.scanners_from_list(list_of_strings)
    print(sl.compare_distances())
    #print(sl)
    return len(list_of_strings)


def test_count_beacons():
    #print(f"simple beacons - {count_beacons(beacon_tests.test_simple_beacons)}")
    print(f"complex beacons - {count_beacons(beacon_tests.test_complex_beacons)}")

test_count_beacons()