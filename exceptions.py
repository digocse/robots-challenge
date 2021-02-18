class CustomExceptions:
	class InvalidGridRangeError(Exception):
	    """Exception raised for invalid Grid axis range"""
	    pass

	class InvalidGridCoordinateError(Exception):
	    """Exception raised for invalid Grid coordinate"""
	    pass
