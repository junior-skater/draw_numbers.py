#---------get user values------------
def button2(nu):
	global numbers2
	numbers2=nu.get()
#----check if is digit------
	if numbers2.isdigit():
#-------Call second function------------
		return funcion() 
	else:
		return "no"
	

def funcion():
	global numbers2
	nums=["###\n#   #\n#   #\n#   #\n###", "#\n#\n#\n#\n#", "###\n    #\n###\n#    \n###", "###\n    #\n###\n    #\n###",
		"#   #\n#   #\n###\n    #\n    #", "###\n#     \n###\n    #\n###", "###\n#     \n###\n#  #\n###", "###\n    #\n    #\n    #\n    #",
		"###\n#   #\n###\n#   #\n###", "###\n#   #\n###\n    #\n    #"]	
	
	draw_list=[]
#---------choosing numbers drawings---------
	for x in range(len(numbers2)):

		num=numbers2[x]
		draw_list.append(nums[int(num)])
	return draw_list




