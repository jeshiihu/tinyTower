import csv

def parseMissions(missions):

	store = []

	with open("TinyTowerMissions.csv") as csvfile:
		reader = csv.DictReader(csvfile)

		for line in reader:
			store = line['Items'].split(';')
			line = [line['Name'], store]
			missions.append(line)

	csvfile.close()
	return missions

def parseFloors(floors):
	with open('TinyTowerFloors.csv') as csvfile:
		reader = csv.DictReader(csvfile)

		for line in reader:
			floors.append(line['Floors'])
	
	csvfile.close()
	return floors

def checkAvailableMissions(floor, missions):
	noMissions = True
	for mission in missions:
		size = len(mission[1])
		i = 0

		for store in mission[1]:
			if store in floor:
				i += 1
		if i == size:
			print("mission:", mission[0])
			print("   stores:", mission[1])
			noMissions = False
	return noMissions


def main():
	floors = []
	missions = []
	floors = parseFloors(floors)
	missions = parseMissions(missions)
	if(checkAvailableMissions(floors, missions)):
		print("No available missions")

if __name__ == "__main__":
	main()
