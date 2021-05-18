#---------get user values------------
def button2(nu):
	global numbers2
	numbers2=nu.get()
#-------Call second function------------
	return funcion()

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




