#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/intangible/data_item/shared_data_item.iff"
	is_prototype = False
	
	def create(self, kernel, params):
		result = Intangible()
	
		result.template = "object/intangible/data_item/shared_data_item.iff"
		result.attribute_template_id = -1
		result.stfName("item_n","data_item_unknown")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())