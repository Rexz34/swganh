#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *

class Template(BaseTemplate):
	name = "object/weapon/melee/knife/base/shared_knife_base.iff"
	is_prototype = False
	
	def create(self, kernel, params):
		result = Weapon()
	
		result.template = "object/weapon/melee/knife/base/shared_knife_base.iff"
		result.attribute_template_id = 10
		result.stfName("obj_n","unknown_weapon")		
		
		#### BEGIN MODIFICATIONS ####
		####  END MODIFICATIONS  ####
		
		return result

def loadTemplates(addTemplate):
	addTemplate(Template())