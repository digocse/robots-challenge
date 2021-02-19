from models import Grid
from exceptions import CustomExceptions

def main():
	print('*** Welcome to the Mars Robots Guide! ***\n')
	print('Here are the computed outputs:\n')

	with open('robots_guide.in.md') as f:
		lines = f.readlines()

	grid_size = lines[0]

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

	updated_lines = lines.pop(0) 		# upper-right coordinates of the rectangular world
	robots_seed_positions = lines[::2]	# Robots initial position
	robots_instructions = lines[1::2]	# Robots instructions

	for position, instruction in zip(robots_seed_positions, robots_instructions):
		robot_initial_pos = position.strip('\n')

		if not robot_initial_pos:
			break

		robot_instruction = instruction

		robot_initial_pos = robot_initial_pos.split(' ')
		grid.generate_robot(
			x=int(robot_initial_pos[0]),
			y=int(robot_initial_pos[1]),
			orientation=robot_initial_pos[2],
		)
		grid.apply_robot_instructions(robot_instruction)
	f.close()

if __name__ == '__main__':
	main()
