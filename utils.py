class StringUtils:
	class InvalidInstructionError(Exception):
	    """Exception raised for invalid instructions"""
	    pass

	@staticmethod
	def normalize(inputString: str):
		updatedString = inputString.replace(" ", "")
		return updatedString.strip().upper()

	@staticmethod
	def validate(inputString: str, exceedLimit: int):
		if len(inputString) >= exceedLimit:
			raise StringUtils.InvalidInstructionError(inputString)
			print('These instructions exceed the maximum of ' + str(exceedLimit) + ' characters')
