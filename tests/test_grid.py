import pytest

from models import Grid
from exceptions import CustomExceptions


class TestGrid:
    def test_generate_robot(self):
        grid = Grid(3, 3)

        grid.generate_robot(0, 0, 'N')

        assert len(grid.robots) > 0
        assert grid.robots[0].pos() == (0, 0, 'N')

    def test_should_not_generate_robot_at_same_coordinate(self):
        grid = Grid(3, 3)
        grid.generate_robot(1, 1, 'E')

        with pytest.raises(CustomExceptions.LaunchRobotCrashError) as exc:
            grid.generate_robot(1, 1, 'E')

        assert str(exc.value) == str((1, 1, 'E'))

    def test_should_not_generate_robot_at_invalid_coordinate(self):
        grid = Grid(3, 3)

        with pytest.raises(CustomExceptions.CoordinateDoesntExistError) as exc:
            grid.generate_robot(4, 1, 'E')

        assert str(exc.value) == str((4, 1, 'E'))


    @pytest.mark.parametrize(
        'robots, expected',
        [
            ([], []),
            ([(0, 0, 'N')], [(0, 0)]),
            ([(0, 0, 'N'), (0, 1, 'E')], [(0, 0), (0, 1)]),
        ],
        ids=['empty_grid', 'one_robot_grid', 'two_robots_grid']
    )
    def test_last_positions(self, robots, expected):
        grid = Grid(5, 5)
        for robot in robots:
            grid.generate_robot(*robot)

        final = grid.last_positions()

        assert len(final) == len(expected)
        assert final == expected


    @pytest.mark.parametrize(
        'robot_position, expected',
        [
            ((-1, 0), True),
            ((0, -1), True),
            ((2, 0), True),
            ((-1, 2), True),
            ((0, 0), False),
            ((1, 1), False),
            ((1, 0), False),
        ]
    )
    def test_is_outside_grid(self, robot_position, expected):
        grid = Grid(1, 1)

        value = grid.is_outside_grid(*robot_position)

        assert value == expected

    def test_apply_robot_instructions_with_empty_grid(self):
        grid = Grid(5, 5)

        grid.apply_robot_instructions('')

        assert not grid.robots

    @pytest.mark.parametrize(
        'robot_position, instructions, final',
        [
            ((1, 1, 'E'), '', (1, 1, 'E')),
            ((1, 1, 'E'), 'FFF', (4, 1, 'E')),
            ((1, 1, 'E'), 'RRRR', (1, 1, 'E')),
            ((1, 1, 'E'), 'FLFRFLFRF', (4, 3, 'E')),
        ],
        ids=[
            'without_instructions',
            'move_foward',
            'rotating',
            'diagonal',
        ]
    )
    def test_apply_robot_instructions(
        self,
        robot_position,
        instructions,
        final,
    ):
        grid = Grid(5, 5)
        grid.generate_robot(*robot_position)

        grid.apply_robot_instructions(instructions)

        assert grid.robots[0].pos() == final
