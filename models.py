class Grid:
	def __init__(self, x: int, y:int):
		self.max_x = x
		self.max_y = y
		self.robots = []

	def generate_robot(self, x: int, y: int, orientation: str):

		if (x,y) in self.last_positions():
			print('The robot has crashed with another one')

		# if self.

	def is_outside_grid(self, x: int, y:int):
		return x < 0 or y < 0 or x > self.max_x or y > self.max_y


	def last_positions(self):
		return [
			robot.pos()[:-1]
			for robot in self.robots
		]


class Robot:
	COMPASS = ['N', 'E', 'S', 'W']
	DIRECTION = [1, 1, -1, -1]

	# TODO: create unknown direction exception

	def __init__(self, x=0, y=0, orientation='N'):
		self.x = x
		self.y = y
		self.orientation = Robot.COMPASS.index(orientation)

	def pos(self):
		return (self.x, self.y, Robot.COMPASS[self.orientation])

	def rotate(self, direction: str):
		if direction not in ['L', 'R']:
			print('Unknown direction')

		delta = 1 if direction == 'R' else -1

		rotation =  self.orientation + delta

		if (rotation >= len(Robot.COMPASS)):
			 rotation = 0
		elif (rotation < 0):
			rotation = len(Robot.COMPASS) - 1

		self.orientation = rotation

	def move(self):
		if not (self.orientation % 2):
			self.y += Robot.DIRECTION[self.orientation]
		else:
			self.x += Robot.DIRECTION[self.orientation]

		return self.pos()
