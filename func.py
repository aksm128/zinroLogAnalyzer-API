import datetime

# 汎用の関数命令。


def safeCheckOpen(fileName):
	"""
	引数はファイル名、返り値はエラー文。
	エラーがなければ "safe" が出力される。
	正常に読み込めるかチェックする。
	ex) if safeCheckOpen("hoge") == "safe":
	"""
	try:
		with open(fileName,"r") as hoge:
			pass
	except Exception as e:
		error = e
	else:
		error = "safe"
	return error

def inputFile(*errorMsg):
	"""
	引数はエラーが出たときのメッセージ（省略可能）
	返り値は正常と判断されたファイル名。
	正常なファイル名が入力されるまでループする。
	ex) fileName = inputFile(errorMsg = "は？？？？？？？")
	"""
	while 1:
		fileName = input()
		error = safeCheckOpen(fileName)
		if error == "safe":
			break
		else:
			print(error)
			if errorMsg:
				print(errorMsg)
	return fileName


def inputAnswer(ansList):
	"""
	引数は回答（文字列）を入れたリスト。返り値は回答。
	回答が入力されるまでループし、入力された回答を返す。
	ex)
	ans = inputAnswer(["yes","no","forgot"])
	"""
	while True:
		choice = input().lower()
		for ansStr in ansList:
			if choice in [ansStr[0],ansStr]:
				return ansStr

def inputInt():
	"""
	引数はなし。返り値は整数。
	整数が入力されるまでループ。
	ex) max = inputInt()
	"""
	val = 0
	while (val == 0):
		str = input()
		try:
			val = int(str)
		except ValueError as err:
			print(type(err))
			print("不正な入力です。")
		else:
			val = int(str)
	return val


def inputNatural():
	"""
	引数はなし。返り値は自然数。
	自然数が入力されるまでループ。
	ex) apple = inputNatural()
	"""
	val = 0
	while (val < 1):
		val = inputInt()
		if (val < 1):
			print("1以上の整数を入力してください。")
	return val

def tupleInt(tup):
	"""
	引数は文字列のタプル。返り値は整数のタプル。
	文字列が入っているタプルを整数にする。
	例外処理なし。
	ex) a,b,c = tupleInt( ("hoge","piyo","buhi") )
	"""
	readLi = []
	for i in range(len(tup)):
		readLi.append(int(tup[i]))
	return tuple(readLi)

def inputTimedelta():
	"""
	引数はなし。返り値は入力された時刻をtimedelta型で返す。
	H:M:Sで入力。正常な入力がされるまでループ。
	"""
	while 1:
		time = input()
		try:
			hoge = datetime.datetime.strptime(time,"%H:%M:%S")
		except Exception as e:
			print(e)
			print("不正な入力です。")
			continue
			raise
		break
	h, min,sec = tupleInt(tuple(time.split(":")))
	return datetime.timedelta(hours=h,minutes=min,seconds=sec)


def TimestrToTimedelta(str):
	h, min,sec = tupleInt(tuple(str.split(":")))
	return datetime.timedelta(hours=h,minutes=min,seconds=sec)


	return
def gamePrint(id, game):
	"""
	引数はid(ログ番号),game(ログ本体)。
	返り値はなし。
	ゲームの情報を出力する。
	"""
	print("番号：",id,"村名",game["v"])
	print("役職設定：",game["s"])
	print("終了時刻：",game["t"])
	print("突然死有り又は初日終了設定" * game["n"],"勝利陣営：",game["w"])
	print("メンバー：",end="")
	for name in game["m"]:
		print(name,"",end="")
	print("\n")

def waitEnter():
	"""
	引数はなし、返り値もなし。
	inputで入力待機するだけ。
	"""
	input()
