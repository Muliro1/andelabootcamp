def add_skill():
	skill_status = {}
	skill_limit = 10
	for i in range(skill_limit):
		skill = input('please enter a skill, type stop to end: ')
		if skill == 'stop':
			break
		else:
			skill_status[skill] = 'incomplete'
			print(skill_status)
	return skill_status 

add_skill()
