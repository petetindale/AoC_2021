from typing import Tuple
test_list_of_strings = [
	"target area: x=20..30, y=-10..-5\n"
	,"target area: x=139..187, y=-148..-89"
	]

loc = Tuple[int,int] 

def maxloc(a:loc,b:loc)->loc:
	ax,ay = a
	bx,by = b
	return (max(ax,bx),max(ay,by))

def minloc(a:loc,b:loc)->loc:
	ax,ay = a
	bx,by = b
	return (min(ax,bx),min(ay,by))
	
def eqloc(a:loc,b:loc)->loc:
	ax,ay = a
	bx,by = b
	return ax==bx and ay==by

	

class TargetArea:
	def __init__(self,targetstr:str)->None:
		
		#get information from string
		coord = list(map(lambda str: str.strip()[2::].split('..'), targetstr[13::].split(',')))
		
		#Set Bottom Left location
		self.bl:loc = (int(coord[0][0]),int(coord[1][0]))
		#Set Top Right location
		self.tr:loc = (int(coord[0][1]),int(coord[1][1]))
		
		

	def hit(self, coord:loc)->bool:
		leftx,bottomy = self.bl
		rightx,topy = self.tr
		x,y = coord
		
		if leftx <= x <= rightx and bottomy <= y <= topy:
			return True
		return False
		
	def missed(self, coord:loc) -> bool:
		leftx,bottomy = self.bl
		rightx,topy = self.tr
		x,y = coord
		
		if bottomy > y:
			return True
		return False
		
class Deploy:
	def __init__(self, target:TargetArea)->None:
		self.target = target
		self.reset()
	
	def reset(self, soft:bool=False)->None:
		self.time = 0
		self.pos:loc = (0,0)
		if not soft:
			self.trajectory = [self.pos]
			self.max = (0,0)
			self.min = (0,0)		

	def step(self)->None:
		self.time += 1
		x,y = self.pos
		velx, vely = self.velxy
		x += velx
		y += vely
		vely -= 1
		if velx > 0 : velx -= 1
		elif velx < 0 : velx += 1
		self.pos = (x,y)
		self.max = maxloc(self.max,self.pos)
		self.min = minloc(self.min,self.pos)
		self.velxy = (velx,vely)
		self.trajectory.append(self.pos)
	
	def shoot(self, velocities:loc, soft:bool=True)->None:
		self.reset(soft)
		self.velxy = velocities
		while not self.target.hit(self.pos) and not self.target.missed(self.pos):
			self.step()
		if self.target.hit(self.pos):
			print(f'hit - max y = {self.max[1]}')
		else:
			print('miss')
	
	def draw(self)->None:
		minx,miny = minloc(self.min, self.target.bl)
		maxx,maxy = maxloc(self.max,self.target.bl)
		
		minx,miny = minloc((minx,miny), self.target.tr)
		maxx,maxy = maxloc((maxx,maxy),self.target.tr)
		
		for i in range(maxy-miny+2):
			y = maxy-i
			line = ''
			for j in range(maxx-minx+2):
				x= j+minx
				if x==0 and y==0:
					line+='S'
				elif (x,y) in self.trajectory:
					line += 'X'
				elif self.target.hit((x,y)):
					line += '#'
				else :
					line += '.'
			print(line)	
	
def getmaxheight(list_of_strings:list)->int:
	print('%%%%%%%%%%%%%%%%%%%%%%%%%')
	list_of_targets = list(map(lambda x:TargetArea(x.strip()),list_of_strings))
	shoot = Deploy(list_of_targets[0])
	shoot.shoot((7,4))
	shoot.shoot((6,3))
	shoot.shoot((5,3))
	shoot.draw()
	print('%%%%%%%%%%%%%%%%%%%%%%%%%')
	return 0
	
def test_getmaxheight():
	print(f'Max height to hit target - {getmaxheight(test_list_of_strings)}')

test_getmaxheight()
	


'''

A bit of maths for me.

y = [Distance to Target:min,max] + Vy * time - 1/2 t^2 
dy/dt = Vy - t

x = [Distance to Target:min,max] + Vx * time - 1/2 t^2 (where the last two zero out rather than go negative)
dx/dt = Vx - t (therefore forward motion stops when Vx = t i.e. dx/dt=0)
As the target must be hit in a step.. not partially. Vx must be less than Distance to Target(min,max) i.e. hit directly first go.. 
and Vx must be greater than Vx = d/t Max distance travelled by X is Vx(Vx+1)/2. Therefore Vx = 

x and y speeds are independent. X either makes it or doesnt. 


In order to find the max height, you can calculate the time at which x can be reached.

'''