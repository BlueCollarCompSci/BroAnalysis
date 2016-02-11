
class LogReader(object):
	'''
	Reads and parses bro logs
	'''
	def __init__(self):
		self.map = {'count' 	: int,
			    'vector'	: list,
			    'interval' 	: int,
			    'addr'	: ip,
			    'double'	: float,
			    'enum'	: str,
			    'bool'	: bool,
			    'time'	: float,
			    'set'	: set,
			    'port'	: int,
			    'string'	: str,}
