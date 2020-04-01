
###########################################################################
############################# Log Collecter ###############################
########################## created by 秋雨前線 #############################
###########################################################################
### 人狼のログを収集するプログラム。
### 保存先はlog.json。
### PyQuery,requestsを使用。
### リクエストを送る間隔は3秒。
### robots.txtには対応していない。
##########################################################################
### ログは単純に。読み込んでから解読すればいい。
###########################################################################


###########################################################################
################################################################### IMPORT
###########################################################################
import argparse
from collections import OrderedDict
import requests
from pyquery import PyQuery as pq
import json
import time
import datetime
import ast
import re
# my module
from func import inputFile, inputAnswer, inputTimedelta, inputInt, gamePrint, waitEnter, TimestrToTimedelta
from DriveFileStream import DriveFileStream
###########################################################################
##################################################################### CONST
###########################################################################
REQUESTS_WAIT = 3
LOG_URL = "https://zinro.net/m/log.php?id="
RED_DATA = {
	"id": -1,
	"v": "",
	"s": "",
	"t": "",
	"n": True,
	"w": "",
	"m": {"": {"l": "","j": ""}}
}
LOG_SIZE = 50000
##########################################################################
################################################################# RED LIST
##########################################################################
RED_LIST = [
	19740,
	# 謎のログ連結。何試合も連結して残されていて3年前から現在まで繋がっている。
	# ログが正常に読み取れていないのか、容量がオーバーするのかはわからん。
	# 鯖側で起こっているものなので、レッドリストに追加。
	26000,
	# まだ精査してないけど、同じ現象っぽい。
	# ブラウザで見てみたらメモリ2000MB以上食われてた。
	# 結局ブラウザ落ちたので、詳しいことは調べずにレッドリスト追加。
	142352,
	# ログ欠損により役職情報が正常に取れていない。
	# どちらにしろ罠村だし多少は、ね？
	147756,
	# ブラウザバグ
	162012,
	# 本当によくわからん。なぜかループから抜けて保存待機状態になる
]
# もういいや（）
# try exceptでエラーキャッチしてerrorLogにぶん投げる仕様に変更。

#############################################################################
######################################################## OBJECTS AND FUCTIONS
#############################################################################

class LogData:
	"""
	ログのデータを返す。引数はログid。
	functions: readCheck, title, comments, member
	"""

	def __init__(self, id):
		self.id = id
		self.url = LOG_URL+str(id)
		self.log = pq(requests.get(self.url).text)

	def readCheck(self):
		"""
		引数はなし。返り値はTrue/False
		ログが存在しないor非公開の時に、.aleatクラスが使われる。
		それがあるかどうか取得する。
		"""
		return (self.log.find(".alert").text() != "")

	def title(self):
		"""
		引数はなし。返り値は村名。
		村名-番号の形になる。
		"""
		# ログ観覧(title-num)
		getTitle = self.log.find(".title").text()
		if (getTitle == ""):
			title = "can't_read"
		else:
			title = getTitle[5::][::-1][1::][::-1]
		return title

	def comments(self):
		"""
		引数はなし。返り値は村の発言ログ（辞書型）
		[
			{   'id':'なんかの管理番号？',
				'from_user':'発言者',
				'to_user':'対象（通常はALL）',
				'room_name':'村名',
				'message':'本文（改行は<br \\/>で表記）',
				'created':'YYYY-mm-DD HH:MM:SS',
				'color':'発言色'
			},{},{}....
		]
		"""
		#	 0123456789A		 210
		# ver massege = [{}{}...{}];addMessage(messege);みたいになってる
		getSprict = self.log.find("script").text()
		startCom = getSprict.find("message ")+10
		endCom = getSprict.find("addMessage(message);")-2
		getCom = getSprict[startCom:endCom:]
		if (getCom == ""):
			comments = ""
		else:
			getCom = getCom.replace("\",\"color\":null},{\"id\":\"", "\",\"color\":\"\"},{\"id\":\"")
			try:
				comments = ast.literal_eval(getCom)
			except Exception as e:
				drive = DriveFileStream()
				drive.save_file("errorLog/" + str(self.id) + ".txt", str(e))
				return "error"
			else:
				comments = ast.literal_eval(getCom)
		return comments

	def member(self):
		"""
		引数はなし。返り値は観戦も入れた村メンバー（辞書型）
		{
			{
				"l": "生"/"死"/"観戦者"  # life
				"j": "(役職)"  # job
			},{},{}...
		}
		"""
		# 　1 2 34 56
		# 「名前 状態 NAME1 LIFE1 JOB1 NAME2 LIFE2...」
		getMem = []
		getMemInfo = []
		cnt = 0
		while True:
			getMem.append(self.log.find("tbody td").eq(cnt).text())
			if getMem[int(cnt/2)] == "":
				getMem.pop()
				break
			getMemInfo.append(self.log.find("tbody td").eq(cnt+1).text().split(" "))
			cnt += 2
		member = OrderedDict()
		for name, i in zip(getMem, range(len(getMem))):
			member[name] = {
				"l": getMemInfo[i][0],
				"j": getMemInfo[i][1]
			}
		return dict(member)


def getLog(num):
	"""
	引数はログid。返り値はログデータ（辞書型）
	{
		"t": "村名-番号"  # 村名
		"s": "【役職-人数 役職2-人数 ...】"  # 配役
		"t": "YYYY-mm-DD HH:MM:SS"  # 村が終了した時間
		"n": 1/0  # 突然死、ログ非公開などでゲームができているか
		"w": "勝利陣営"  # 勝利陣営（ログ準拠
		"m": {{"l":,"j":,}{}...}  # 観戦者も入れたメンバー情報
	}
	"""
	log = LogData(num)
	comments = log.comments()
	if comments == "error":
		return "error"

	backFlag = 1
	startFlag = 0
	for msg in comments:
		if msg["from_user"] == "鯖":
			gamesetCheck = re.search("【.*】の勝利です!", msg["message"])
			if (msg["message"] == "ゲームを開始します"):
				startFlag = True
			if (gamesetCheck):
				if startFlag:
					backFlag = 1
				else:
					backFlag = -1
				break
	comments = comments[::backFlag]

	noGameFlag = False
	jobs = ""
	winner = ""
	for msg, i in zip(comments, range(len(comments))):
		if (msg["from_user"] == "鯖"):
			gamesetCheck = re.search("【.*】の勝利です!", msg["message"])
			TTZNdieCheck = re.search(".*さんは時間内に能力を実行しなかったため突然死しました",msg["message"])
			if msg["message"] == "ゲームを開始します":
				noGameFlag = False
				if re.search("役職設定【.*】",comments[i-1]["message"]) != None:
					jobs = comments[i-1]["message"][4:]
				else:
					jobs = comments[i+1]["message"][4:]
			if TTZNdieCheck:
				noGameFlag = True
			if gamesetCheck:
				winner = gamesetCheck.group()[1:][::-1][7::][::-1]
				if winner == "村人チーム":
					winner = "村人"
				elif winner == "人狼チーム":
					winner = "人狼"
				elif winner == "てるてる":
					winner = "てるてる"

	if len(comments) == 0:
		endTime = ""
	else:
		endTime = comments[len(comments)-1]["created"]
	wolf = 0
	human = 0
	member = log.member()
	for name in member:
		if member[name]["j"] == "(人狼)":
			wolf += 1
		elif member[name]["j"] == "()":
			noGameFlag = True
		elif member[name]["j"] not in  ["(妖狐)", "(観戦者)", "(GM)"]:
			human += 1
	if wolf >= human:
		noGameFlag = True
	if jobs == "":
		noGameFlag = True

	data = {
		"id": num,
		"v": log.title(),  # villege
		"s": jobs,  # setting
		"t": endTime,  # time
		"n": noGameFlag * 1,  # boolian -to-> 1 / 0
		"w": winner,  #winner
		"m": log.member(),  # member
		}

	return data

"""---#TESTMAIN
print(getLog(26000))
exit()
#TESTMAIN---"""


def saveLog(log, cnt, collected, finalLogNum):
	drive = DriveFileStream()
	drive.save_file("raw/log%d.json" % finalLogNum, json.dumps(log, ensure_ascii=False))
	drive.save_file("root/finalLogNum.txt", str(finalLogNum))
	year, month, day = log[-1]["t"].split(" ")[0].split("-")
	drive.save_file("root/finalLogDate.txt", "%s年%s月%s日" % (year, month, day))

	print("{} gamelog saved.".format(cnt-collected))
	print("program end.")


###########################################################################
###################################################################### LOAD
###########################################################################
def main():
	drive = DriveFileStream()
	finalLogNum = int(drive.load_file("root/finalLogNum.txt"))
	log = json.loads(drive.load_file("raw/log%d.json" % finalLogNum))

	#####################################################################
	################################################################ MAIN
	#####################################################################

	
	collected = log[-1]["id"]
	cnt = collected
	dt = datetime  # インスタンス
	goal = 0
	OK = False
	limit = dt.datetime.now()  # <class datetime>

	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--mode")
	parser.add_argument("-v", "--value")
	parser.add_argument("-a", "--auto", action='store_true')
	args = parser.parse_args()

	logPage = pq(requests.get("https://zinro.net/m/room_list.php?scene=%E7%B5%82%E4%BA%86").text)
	finalGame = int(re.search(r"(?<=,'log.php\?id=)[0-9]+(?='\))", logPage.find("td").eq(0).attr("onclick")).group())


	print("%s番までログが収集されています" % cnt)
	print("lastLog: " + str(log[-1]))
	print("最新の試合は%d番です" % finalGame)
	print("""
	収集モードを設定してください。[t/n]
	time:終了時間を指定する。
	number:ログ番号で指定。""")

	if args.mode != None :
		mode = args.mode
	else:
		mode = inputAnswer(["time", "number", "final"])
	# mode = "number" # DEBUG
	tMode = (mode == "time")
	# YYYY-MM-DD HH:MM:SS.MICROO
	if tMode:
		print(dt.datetime.now())
		print("どのくらいの間収集しますか？[hh:mm:ss]")
		if args.value != None:
			print(args.value)
			limit = dt.datetime.now() + TimestrToTimedelta(args.value)
		else:
			limit = dt.datetime.now() + inputTimedelta()
	else:
		print("何番まで収集しますか？")
		goal = inputInt()
		# goal = collected + 3 # DEBUG

	nowTime = dt.datetime.now()

	#######################################################################
	############################################################### COLLECT
	#######################################################################

	while ((goal > cnt) and (not tMode)) or ((nowTime < limit) and tMode) and (finalGame > cnt):
		cnt += 1
		print("\tid-{} ".format(cnt))

		if cnt in RED_LIST:
			RED_DATA["id"] = cnt
			log.append(RED_DATA)
			print("レッドリストに登録されたログです。飛ばして次のログを収集します。")
			continue

		try:
			requests.get(LOG_URL+str(cnt))
		except Exception as e:
			print(e)
			print("エラーが発生しました")
			for retry in range(60):
				print("10秒毎に再試行します。[{}/60]".format(retry))
				try:
					requests.get(LOG_URL+str(cnt))
				except Exception as e:
					print(e)
					if retry == 59:
						cnt = cnt - 1
						saveLog(log, cnt, collected, finalLogNum)
						exit()
				else:
					print("接続に成功しました。")
					break
				time.sleep(10)
		data = getLog(cnt)
		if data == "error":
			print("発言ログを正常に読み込めませんでした。飛ばして次のログを収集します。")
			continue
		gamePrint(cnt,data)
		log.append(data)
		nowTime = dt.datetime.now()
		if not tMode:
			print("{}% collected".format(int((cnt-collected)/(goal-collected)*1000)/10))
		else:
			print("It has {} until finish".format(str(limit-nowTime)[:7]))
		if len(log) >= 50000:
			saveLog(log, cnt, collected, finalLogNum)
			finalLogNum += 1
			log = []
		time.sleep(REQUESTS_WAIT)



	print("待機状態 Enterで保存")
	if args.auto == True:
		pass
	else:
		waitEnter()

	###########################################################################
	###################################################################### SAVE
	###########################################################################
	saveLog(log, cnt, collected, finalLogNum)
	

if __name__ == '__main__':
	main()
