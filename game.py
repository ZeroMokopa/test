class KillerofThreeKingdoms(object):
	"""docstring for KillerofThreeKingdoms"""
	def __init__(self,num):
		super(KillerofThreeKingdoms, self).__init__()
		self.hp = 4
		self.kill_able = 1
		self.dodge_able = 1
		self.kill = 0
		self.dodge = 0
		if(num == 1):
			self.name = "张飞"
			self.skill = "咆哮(无限出杀)"
		if (num == 2):
			self.name = "黄忠"
			self.skill = "烈弓(使用杀，目标不能出闪)"

	def Set_pai(self,sha,shan):
		self.kill = sha
		self.dodge = shan
		print("Name:",self.name)
		print("HP:",self.hp," Kill:",self.kill," Dodge:",self.dodge," Skill:",self.skill)

	def kills(self,my_obj): 
		print(self.name,"对",my_obj.name,"使用‘杀’")
		self.kill = self.kill-1
		if(self.name == "张飞"):
			self.kill_able = 1000
			print(self.name,"发动技能‘咆哮’（持续出‘杀’）")
		if(self.kill_able > 0):
			self.kill_able = self.kill_able - 1

			if(self.name == "黄忠"):
				my_obj.dodge_able = 0
				print(self.name,"发动技能‘烈弓’（",my_obj.name,"）不能出牌‘闪’")
			if(my_obj.dodge_able == 1):
				if(my_obj.dodge>0):
					my_obj.dodge = my_obj.dodge - 1
					print("抵挡伤害，闪-1")
				else:
					my_obj.hp = my_obj.hp - 1
					print("造成伤害，生命值-1")
			else:
				my_obj.hp = my_obj.hp - 1
				print("造成伤害，生命值-1")
		else:
			print("本轮不能继续出杀")
			self.kill = self.kill+1
	
	def show(self):
		print(self.name,"(HP:",self.hp," Kill:",self.kill," Dodge:",self.dodge,")")
		
if __name__ =='__main__':		
	h1 = KillerofThreeKingdoms(1)
	h2 = KillerofThreeKingdoms(2)

	h1.Set_pai(3,1)
	h2.Set_pai(2,2)

	print("\n第一回合:")
	h2.kills(h1)  #第一回合
	h1.show()
	h2.show()

	print("\n第一回合:")
	h2.kills(h1)  #第一回合
	h1.show()
	h2.show()

	print("\n第二回合:")
	h1.kills(h2)  #第二回合
	h1.show()
	h2.show()

	print("\n第二回合:")
	h1.kills(h2)  #第二回合
	h1.show()
	h2.show()
