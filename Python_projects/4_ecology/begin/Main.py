from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Rys import Rys
from Organisms.Antylopa import Antylopa
import os


if __name__ == '__main__':
	pyWorld = World(10, 10)

	newOrg = Grass(position=Position(xPosition=9, yPosition=9), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Grass(position=Position(xPosition=1, yPosition=1), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Sheep(position=Position(xPosition=2, yPosition=2), world=pyWorld)
	pyWorld.addOrganism(newOrg)


	newOrg = Rys(position=Position(xPosition=3, yPosition=3), world=pyWorld)
	pyWorld.addOrganism(newOrg)


	print(pyWorld) 
	

	for _ in range(0, 50):
		option = input("Wybierz P - tryb Plaga / Wybierz O - dodaj organizm").lower()
		if (option == 'p'):
			os.system('cls')
			pyWorld.plague(option)
			pyWorld.makeTurn()
			print(pyWorld)
		elif(option == 'o'):
			zwierze = input("Wybierz organizm: G - grass / S - sheep / R - rys / A - antylopa: ").lower()
			if (zwierze == 'g'):
				zwierze = Grass
			elif (zwierze == 's'):
				zwierze = Sheep
			elif (zwierze == 'r'):
				zwierze = Rys
			elif (zwierze == 'a'):
				zwierze = Antylopa
			pozycja_x = int(input('Wprowadz pozycję x: '))
			pozycja_y = int(input('Wprowadz pozycję y: '))
			os.system('cls')
			newOrgy = zwierze(position=Position(xPosition=pozycja_x, yPosition=pozycja_y), world=pyWorld)
			pyWorld.addOrganism(newOrgy)
			
			print(pyWorld)
		else:
			os.system('cls')
			pyWorld.makeTurn()
			print(pyWorld)

		

	
