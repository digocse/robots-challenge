class Grid:
	def __init__(self, x: int, y:int):
		self.max_x = x
		self.max_y = y
		self.robots = []


class Robot:
	COMPASS = ['N', 'E', 'S', 'W']
	DIRECTION = [1, 1, -1, -1]

	def __init__(self, x=0, y=0, orientation='N'):
		self.x = x
		self.y = y
		self.orientation = Robot.COMPASS.index(orientation)

	def pos(self):
		return (self.x, self.y, Robot.COMPASS[self.orientation])
