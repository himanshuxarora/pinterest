import json
def main():
	with open('catlink.json','r')as r:
		cat = json.load(r)
	print(cat.keys())
main()