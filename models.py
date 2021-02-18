from utils import StringUtils

class Grid:
	def __init__(self, x: int, y:int):
		self.max_x = x
		self.max_y = y
		self.robots = []

	def generate_robot(self, x: int, y: int, orientation: str):

		# TODO: create restriction for maximum coordinate of 50
		if (x,y) in self.last_positions():
			# TODO: create exception
			print('The robot has been launched on top of another... BOOM!')
			return

		if self.is_outside_grid(x, y):
			# TODO: create exception
			print('Robot cannot be created outside the grid')
			return

		robot = Robot(x, y, orientation)
		self.robots.append(robot)

	def is_outside_grid(self, x: int, y:int):
		return x < 0 or y < 0 or x > self.max_x or y > self.max_y

	def last_positions(self):
		return [
			robot.pos()[:-1]
			for robot in self.robots
		]

	def robot_movement(self, instructions: str):
		if not self.robots:
			return

		instructions = StringUtils.normalize(instructions)
		StringUtils.validate(instructions, 100)

		robot = self.robots[-1]

		for instruction in instructions:
			if instruction not in ['L', 'R', 'F']:
				# TODO: create exception
				print('Unknown instruction has been sent')
				return

			if instruction == 'F':
				robot_position = robot.pos()

				if self.check_collisions(robot_position):
					# TODO: create exception
					print('The robot has crashed with another one')
					return
				robot.move()
			else:
				robot.rotate(instruction)
		print(robot.pos())

	def check_collisions(self, robot_position: tuple):
		robot_direction = robot_position[2]
		direction = Robot.COMPASS.index(robot_direction)

		if direction % 2 == 0:
			final_x = robot_position[0]
			final_y = robot_position[1] + Robot.DIRECTION[direction]
		else:
			final_x = robot_position[0] + Robot.DIRECTION[direction]
			final_y = robot_position[1]

		return (
			self.is_outside_grid(final_x, final_y) 
			or (final_x, final_y) in self.last_positions()
			# TODO: check if there's a scent about this position
		)


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
