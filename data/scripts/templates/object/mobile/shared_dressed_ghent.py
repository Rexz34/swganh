#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/mobile/shared_dressed_ghent.iff"
	is_prototype = False
	
	def create(self, kernel, params):
		result = Creature()
	
		result.template = "object/mobile/shared_dressed_ghent.iff"
		result.attribute_template_id = 9
		result.stfName("obj_n","unknown_creature")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())