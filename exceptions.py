class CustomExceptions:

	### Grid exceptions:
	class InvalidGridRangeError(Exception):
	    """Exception raised for invalid Grid axis range"""
	    pass

	class InvalidGridCoordinateError(Exception):
	    """Exception raised for invalid Grid coordinate"""
	    pass

	class LaunchRobotCrashError(Exception):
	    """Exception raised when a robot has been launched on top of another"""
	    pass

	class CoordinateDoesntExistError(Exception):
	    """Exception raised while creating robot on invalid coordinate"""
	    pass

	class UnknownInstructionError(Exception):
	    """Exception raised while creating robot on invalid coordinate"""
	    pass
