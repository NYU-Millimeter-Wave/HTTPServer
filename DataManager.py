#
# Module For Data Management
# This can be called with:
#
CONST_ARRAY = ["username","password"]

class DataManager:

	json_string = 'Empty'
	parsed_json = 'Empty'
    
	def printData(self):
		print("username =" + self.parsed_json["username"])
		print("password =" + self.parsed_json["password"])

	def refresh(self,json_string,parsed_json):
		for value in CONST_ARRAY:
			if(json_string.find(value) != -1):
				self.parsed_json[value] = parsed_json[value]








