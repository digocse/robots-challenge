from utils import StringUtils
from exceptions import CustomExceptions

class Grid:
	"""Class that controls the Grid, robots and their instructions"""
	def __init__(self, x: int, y:int):
		self.max_x = x
		self.max_y = y
		self.robots = []
		self.legacyScent = []

	def generate_robot(self, x: int, y: int, orientation: str):
		"""
		Receives the coordinates and orientation to build a new robot on the Grid
		Validates if the launch position is the same of a previous one.
		"""
		if (x > 50 or y > 50):
			raise CustomExceptions.InvalidGridCoordinateError(x, y)

		if (x,y) in self.last_positions():
			print('The robot has been launched on top of another... BOOM!')
			raise CustomExceptions.LaunchRobotCrashError(x, y, orientation)

		if self.is_outside_grid(x, y):
			print('Robot cannot be created outside the grid')
			raise CustomExceptions.CoordinateDoesntExistError(x, y, orientation)

		robot = Robot(x, y, orientation)
		self.robots.append(robot)

	def is_outside_grid(self, x: int, y:int):
		return x < 0 or y < 0 or x > self.max_x or y > self.max_y

	def last_positions(self):
		return [
			robot.pos()[:-1]
			for robot in self.robots
		]

	def apply_robot_instructions(self, instructions: str):
		"""
		Apply robot instructions to rotate and/or move forward on the specified direction
		Check Grid edges and leave a "Robot's scent" of a dangerous position and direction

		Notice:
		1) Mars robots might be very expensive so instead of crashing them with another I've 
		decided to also skip this instruction if its the case.
		2) A Robot scent (x, y) position is not a prohibited coordinate if it is going on a different direction!
		"""
		if not self.robots:
			return

		instructions = StringUtils.normalize(instructions)
		StringUtils.validate(instructions, 100)

		robot = self.robots[-1]

		for instruction in instructions:
			if instruction not in ['L', 'R', 'F']:
				raise CustomExceptions.UnknownInstructionError(instruction)

			if instruction == 'F':
				robot_position = robot.pos()

				if not self.is_safe_position(robot_position):
					continue

				final_x, final_y = self.calculate_next_positions(robot_position)

				if self.check_collisions(final_x, final_y):
					# This approach skips the dangerous instruction. This intentionally changes the route
					print('ALERT: Robot would have crashed with another. Instruction skipped!')
					continue

				"""
				if the next position is outside the grid but there was none legacyScent
				the robot should leave one for posterity
				"""
				if self.is_outside_grid(final_x, final_y):
					self.legacyScent.append(robot_position)
					print(str(robot_position) + ' LOST')
					robot.move()
					return

				robot.move()
			else:
				robot.rotate(instruction)
		print(robot.pos())


	def check_collisions(self, final_x: int, final_y: int):
		return (final_x, final_y) in self.last_positions()

	def is_safe_position(self, position):
		return False if position in self.legacyScent else True

	def calculate_next_positions(self, robot_position: tuple):
		robot_direction = robot_position[2]
		direction = Robot.COMPASS.index(robot_direction)

		# Even indexes represent y-axis and odd indexes x-axis direction changes
		if direction % 2 == 0:
			final_x = robot_position[0]
			final_y = robot_position[1] + Robot.DIRECTION[direction]
		else:
			final_x = robot_position[0] + Robot.DIRECTION[direction]
			final_y = robot_position[1]
		return final_x, final_y


class Robot:
	"""Class that models a Robot"""
	COMPASS = ['N', 'E', 'S', 'W']
	DIRECTION = [1, 1, -1, -1]

	def __init__(self, x=0, y=0, orientation='N'):
		self.x = x
		self.y = y
		self.orientation = Robot.COMPASS.index(orientation)

	def pos(self):
		return (self.x, self.y, Robot.COMPASS[self.orientation])

	def rotate(self, direction: str):
		if direction not in ['L', 'R']:
			raise CustomExceptions.UnknownInstructionError(direction)

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
