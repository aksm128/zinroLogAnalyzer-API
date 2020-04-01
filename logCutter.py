import json
from DriveFileStream import DriveFileStream
drive = DriveFileStream()
finalLogNum = int(drive.load_file("root/finalLogNum.txt"))
for i in range(finalLogNum+1):
	drive = DriveFileStream()
	log = json.loads(drive.load_file("raw/log%d.json" % i))
	newLog = []
	for j in range(len(log)):
		if log[j]["t"] in ["","RED_VILLEGE"]:
			continue
		newLog.append(log[j])

	newFile = json.dumps(newLog, ensure_ascii = False)
	print("minify/log%d.json", i)
	drive.save_file("minify/log%d.json" % i, newFile)
print("OK")
