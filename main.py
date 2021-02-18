from models import Grid

def main():
	print('*** Welcome to the Mars Robots Guide! ***\n\n')

	# Robot(x=0, y=0, orientation='E').rotate('R')
	# return

	grid_size = input('Enter the upper right corner coordinates: (e.g. 5 3)\n')

	if not grid_size:
		return

	grid_size = grid_size.split(' ')

	grid = Grid(
		x=int(grid_size[0]),
		y=int(grid_size[1]),
	)

	print(grid.max_x)
	print(grid.max_y)

	while True:
		robot_initial_pos = input('Next robot position: (e.g. 1 1 E)\n')

		if not robot_initial_pos:
			break

		print(robot_initial_pos)

		robot_instruction = input('Robot instruction: (e.g RFRFRFRF)\n')
		print(robot_instruction)


if __name__ == '__main__':
	main()
