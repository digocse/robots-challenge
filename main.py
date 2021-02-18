from models import Grid
from exceptions import CustomExceptions

def main():
	print('*** Welcome to the Mars Robots Guide! ***\n\n')
	grid_size = input('Enter the upper right corner coordinates: (e.g. 5 3)\n')

	if not grid_size:
		return

	grid_size = grid_size.split(' ')

	max_x_axis = int(grid_size[0])
	max_y_axis = int(grid_size[1])

	if max_x_axis > 50 or max_y_axis > 50:
		raise CustomExceptions.InvalidGridRangeError(max_x_axis, max_y_axis)

	grid = Grid(
		x=max_x_axis,
		y=max_y_axis,
	)

	while True:
		robot_initial_pos = input('Next robot position: (e.g. 1 1 E)\n')

		if not robot_initial_pos:
			break

		robot_instruction = input('Robot instruction: (e.g RFRFRFRF)\n')

		robot_initial_pos = robot_initial_pos.split(' ')
		grid.generate_robot(
			x=int(robot_initial_pos[0]),
			y=int(robot_initial_pos[1]),
			orientation=robot_initial_pos[2],
		)
		grid.apply_robot_instructions(robot_instruction)


if __name__ == '__main__':
	main()
