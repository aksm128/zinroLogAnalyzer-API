import json
import re
import datetime as dt
from DriveFileStream import DriveFileStream


class Player():
    """docstring for player."""

    def __init__(self, names):
        self.names = names
        self.data = {
            "winLoseData": {
                "total": {
                    "games": {
                        "jobs": {
                            "(占い師)": 0,
                            "(霊能者)": 0,
                            "(狩人)": 0,
                            "(猫又)": 0,
                            "(共有者)": 0,
                            "(村人)": 0,
                            "(人狼)": 0,
                            "(狂人)": 0,
                            "(狂信者)": 0,
                            "(妖狐)": 0,
                            "(背徳者)": 0,
                            "(怪盗)": 0,
                            "(てるてる)": 0,
                            "(狼憑き)": 0,
                            "(役人)": 0,
                            "(ものまね)": 0,
                            "(観戦者)": 0,
                            "(GM)": 0,
                        },
                        "teams": {
                            "total": 0,
                            "村人": 0,
                            "人狼": 0,
                            "妖狐": 0,
                            "てるてる": 0
                        }
                    },
                    "win": {
                        "jobs": {
                            "(占い師)": 0,
                            "(霊能者)": 0,
                            "(狩人)": 0,
                            "(猫又)": 0,
                            "(共有者)": 0,
                            "(村人)": 0,
                            "(人狼)": 0,
                            "(狂人)": 0,
                            "(狂信者)": 0,
                            "(妖狐)": 0,
                            "(背徳者)": 0,
                            "(怪盗)": 0,
                            "(てるてる)": 0,
                            "(狼憑き)": 0,
                            "(役人)": 0,
                            "(ものまね)": 0,
                            "(観戦者)": 0,
                            "(GM)": 0,
                        },
                        "teams": {
                            "total": 0,
                            "total": 0,
                            "村人": 0,
                            "人狼": 0,
                            "妖狐": 0,
                            "てるてる": 0
                        }
                    },
                    "winPer": {
                        "jobs": {
                            "(占い師)": -1,
                            "(霊能者)": -1,
                            "(狩人)": -1,
                            "(猫又)": -1,
                            "(共有者)": -1,
                            "(村人)": -1,
                            "(人狼)": -1,
                            "(狂人)": -1,
                            "(狂信者)": -1,
                            "(妖狐)": -1,
                            "(背徳者)": -1,
                            "(怪盗)": -1,
                            "(てるてる)": -1,
                            "(狼憑き)": -1,
                            "(役人)": -1,
                            "(ものまね)": -1,
                            "(観戦者)": -1,
                            "(GM)": -1,
                        },
                        "teams": {
                            "total": -1,
                            "村人": -1,
                            "人狼": -1,
                            "妖狐": -1,
                            "てるてる": -1
                        }
                    }
                },
                "12Acat": {
                    "games": {
                        "jobs": {
                            "(占い師)": 0,
                            "(霊能者)": 0,
                            "(狩人)": 0,
                            "(猫又)": 0,
                            "(村人)": 0,
                            "(人狼)": 0,
                            "(狂人)": 0
                        },
                        "teams": {
                            "total": 0,
                            "村人": 0,
                            "人狼": 0
                        }
                    },
                    "win": {
                        "jobs": {
                            "(占い師)": 0,
                            "(霊能者)": 0,
                            "(狩人)": 0,
                            "(猫又)": 0,
                            "(村人)": 0,
                            "(人狼)": 0,
                            "(狂人)": 0
                        },
                        "teams": {
                            "total": 0,
                            "村人": 0,
                            "人狼": 0
                        }
                    },
                    "winPer": {
                        "jobs": {
                            "(占い師)": -1,
                            "(霊能者)": -1,
                            "(狩人)": -1,
                            "(猫又)": -1,
                            "(村人)": -1,
                            "(人狼)": -1,
                            "(狂人)": -1
                        },
                        "teams": {
                            "total": -1,
                            "村人": -1,
                            "人狼": -1
                        }
                    }
                },
                "11A": {
                    "games": {
                        "jobs": {
                            "(占い師)": 0,
                            "(霊能者)": 0,
                            "(狩人)": 0,
                            "(村人)": 0,
                            "(人狼)": 0,
                            "(狂人)": 0
                        },
                        "teams": {
                            "total": 0,
                            "村人": 0,
                            "人狼": 0
                        }
                    },
                    "win": {
                        "jobs": {
                            "(占い師)": 0,
                            "(霊能者)": 0,
                            "(狩人)": 0,
                            "(村人)": 0,
                            "(人狼)": 0,
                            "(狂人)": 0
                        },
                        "teams": {
                            "total": 0,
                            "村人": 0,
                            "人狼": 0
                        }
                    },
                    "winPer": {
                        "jobs": {
                            "(占い師)": -1,
                            "(霊能者)": -1,
                            "(狩人)": -1,
                            "(村人)": -1,
                            "(人狼)": -1,
                            "(狂人)": -1
                        },
                        "teams": {
                            "total": -1,
                            "村人": -1,
                            "人狼": -1
                        }
                    }
                },
                "12B": {
                    "games": {
                        "jobs": {
                            "(占い師)": 0,
                            "(霊能者)": 0,
                            "(狩人)": 0,
                            "(村人)": 0,
                            "(人狼)": 0,
                            "(狂人)": 0,
                            "(妖狐)": 0
                        },
                        "teams": {
                            "total": 0,
                            "村人": 0,
                            "人狼": 0,
                            "妖狐": 0
                        }
                    },
                    "win": {
                        "jobs": {
                            "(占い師)": 0,
                            "(霊能者)": 0,
                            "(狩人)": 0,
                            "(村人)": 0,
                            "(人狼)": 0,
                            "(狂人)": 0,
                            "(妖狐)": 0
                        },
                        "teams": {
                            "total": 0,
                            "村人": 0,
                            "人狼": 0,
                            "妖狐": 0
                        }
                    },
                    "winPer": {
                        "jobs": {
                            "(占い師)": -1,
                            "(霊能者)": -1,
                            "(狩人)": -1,
                            "(村人)": -1,
                            "(人狼)": -1,
                            "(狂人)": -1,
                            "(妖狐)": -1
                        },
                        "teams": {
                            "total": -1,
                            "村人": -1,
                            "人狼": -1,
                            "妖狐": -1
                        }
                    }
                },
                "8CFO": {
                    "games": {
                        "jobs": {
                            "(占い師)": 0,
                            "(霊能者)": 0,
                            "(共有者)": 0,
                            "(村人)": 0,
                            "(人狼)": 0,
                            "(狂人)": 0
                        },
                        "teams": {
                            "total": 0,
                            "村人": 0,
                            "人狼": 0
                        }
                    },
                    "win": {
                        "jobs": {
                            "(占い師)": 0,
                            "(霊能者)": 0,
                            "(共有者)": 0,
                            "(村人)": 0,
                            "(人狼)": 0,
                            "(狂人)": 0
                        },
                        "teams": {
                            "total": 0,
                            "村人": 0,
                            "人狼": 0
                        }
                    },
                    "winPer": {
                        "jobs": {
                            "(占い師)": -1,
                            "(霊能者)": -1,
                            "(共有者)": -1,
                            "(村人)": -1,
                            "(人狼)": -1,
                            "(狂人)": -1
                        },
                        "teams": {
                            "total": -1,
                            "村人": -1,
                            "人狼": -1
                        }
                    }
                },
                "10A": {
                    "games": {
                        "jobs": {
                            "(占い師)": 0,
                            "(霊能者)": 0,
                            "(狩人)": 0,
                            "(村人)": 0,
                            "(人狼)": 0,
                            "(狂人)": 0
                        },
                        "teams": {
                            "total": 0,
                            "村人": 0,
                            "人狼": 0
                        }
                    },
                    "win": {
                        "jobs": {
                            "(占い師)": 0,
                            "(霊能者)": 0,
                            "(狩人)": 0,
                            "(村人)": 0,
                            "(人狼)": 0,
                            "(狂人)": 0
                        },
                        "teams": {
                            "total": 0,
                            "村人": 0,
                            "人狼": 0
                        }
                    },
                    "winPer": {
                        "jobs": {
                            "(占い師)": -1,
                            "(霊能者)": -1,
                            "(狩人)": -1,
                            "(村人)": -1,
                            "(人狼)": -1,
                            "(狂人)": -1
                        },
                        "teams": {
                            "total": -1,
                            "村人": -1,
                            "人狼": -1
                        }
                    }
                },
                "14Dcat": {
                    "games": {
                        "jobs": {
                            "(占い師)": 0,
                            "(霊能者)": 0,
                            "(狩人)": 0,
                            "(猫又)": 0,
                            "(共有者)": 0,
                            "(村人)": 0,
                            "(人狼)": 0,
                            "(狂信者)": 0,
                            "(妖狐)": 0,
                            "(背徳者)": 0
                        },
                        "teams": {
                            "total": 0,
                            "村人": 0,
                            "人狼": 0,
                            "妖狐": 0
                        }
                    },
                    "win": {
                        "jobs": {
                            "(占い師)": 0,
                            "(霊能者)": 0,
                            "(狩人)": 0,
                            "(猫又)": 0,
                            "(共有者)": 0,
                            "(村人)": 0,
                            "(人狼)": 0,
                            "(狂信者)": 0,
                            "(妖狐)": 0,
                            "(背徳者)": 0
                        },
                        "teams": {
                            "total": 0,
                            "村人": 0,
                            "人狼": 0,
                            "妖狐": 0
                        }
                    },
                    "winPer": {
                        "jobs": {
                            "(占い師)": -1,
                            "(霊能者)": -1,
                            "(狩人)": -1,
                            "(猫又)": -1,
                            "(共有者)": -1,
                            "(村人)": -1,
                            "(人狼)": -1,
                            "(狂信者)": -1,
                            "(妖狐)": -1,
                            "(背徳者)": -1
                        },
                        "teams": {
                            "total": -1,
                            "村人": -1,
                            "人狼": -1,
                            "妖狐": -1
                        }
                    }
                }
            },
            "enterByTime": [],
            "enterByDate": {},
            "winPerByDate": {},
            "firstLog": [0, ""],
            "finalLog": [0, ""],
            "ranking": {
                "friends": [],
                "villeges": []
            },
            "error": []
        }
        self.friends = {}
        self.villeges = {}
        self.winByDate = {}
        self.enterByTime = {}
        for h in range(24):
            for m in range(60):
                self.enterByTime["%02d:%02d" % (h, m)] = 0

    def errorPush(self, id, errorNum, mes):
        self.data["error"].append({
            "no": errorNum,
            "LogID": id,
            "mes": mes
        })

    def load(self, sendData):
        self.data = sendData["data"]
        self.friends = sendData["friends"]
        self.villeges = sendData["villeges"]
        self.winByDate = sendData["winByDate"]
        self.enterByTime = sendData["enterByTime"]

    def dumpData(self):
        # 破壊的
        for setting in self.data["winLoseData"]:
            for job in self.data["winLoseData"][setting]["games"]["jobs"]:
                if self.data["winLoseData"][setting]["games"]["jobs"][job] != 0:
                    self.data["winLoseData"][setting]["winPer"]["jobs"][job] = int(
                        self.data["winLoseData"][setting]["win"]["jobs"][job]
                        / self.data["winLoseData"][setting]["games"]["jobs"][job]
                        * 10000
                    ) / 100
            for team in self.data["winLoseData"][setting]["games"]["teams"]:
                if self.data["winLoseData"][setting]["games"]["teams"][team] != 0:
                    self.data["winLoseData"][setting]["winPer"]["teams"][team] = int(
                        self.data["winLoseData"][setting]["win"]["teams"][team]
                        / self.data["winLoseData"][setting]["games"]["teams"][team]
                        * 10000
                    ) / 100
        if not "初日犠牲者" in self.names:
            self.data["ranking"]["friends"] = sorted(self.friends.items(), key=lambda x: x[1], reverse=True)[1:6]
        else:
            self.data["ranking"]["friends"] = sorted(self.friends.items(), key=lambda x: x[1], reverse=True)[:5]
        self.data["ranking"]["villeges"] = sorted(self.villeges.items(), key=lambda x: x[1], reverse=True)[:5]
        cnt30m = 0
        for i, time in zip(range(len(self.enterByTime)), self.enterByTime):
            cnt30m += self.enterByTime[time]
            # 0~29 30~59
            if i % 30 == 29:
                self.data["enterByTime"].append(cnt30m)
                cnt30m = 0
        for month in sorted(self.winByDate.keys()):
            self.data["winPerByDate"][month] = int(
                self.winByDate[month]
                / self.data["enterByDate"][month]
                * 10000
            ) / 100
        if len(self.data["ranking"]["villeges"]) == 0:
            self.errorPush(-1, 2, "ログが存在しません。")
        return self.data

    def dumpSendData(self):
        return {
            "data": self.data,
            "friends": self.friends,
            "villeges": self.villeges,
            "winByDate": self.winByDate,
            "enterByTime": self.enterByTime
        }

    def addData(self, gamedata):
        game = Game(gamedata)
        id = game.id
        name = game.searchName(self.names)
        title, villegeNum = game.ParsedTitle(numDelete=True)
        setting = game.settingName()
        job = game.game["m"][name]["j"]
        team = game.thisJobTeam(job)
        didWin = game.didThisJobWin(job)
        isNoGame = game.isNoGame()
        if isNoGame:
            return None

        self.data["winLoseData"]["total"]["games"]["jobs"][job] = self.data["winLoseData"]["total"]["games"][
                                                                      "jobs"].get(job, 0) + 1
        # 参戦していないならtotalにしか代入しない
        if team == "no team":
            return None
        self.data["winLoseData"]["total"]["games"]["teams"]["total"] += 1
        self.data["winLoseData"]["total"]["games"]["teams"][team] = self.data["winLoseData"]["total"]["games"][
                                                                        "teams"].get(team, 0) + 1
        if didWin:
            self.data["winLoseData"]["total"]["win"]["teams"]["total"] += 1
            self.data["winLoseData"]["total"]["win"]["jobs"][job] = self.data["winLoseData"]["total"]["win"][
                                                                        "jobs"].get(job, 0) + 1
            self.data["winLoseData"]["total"]["win"]["teams"][team] = self.data["winLoseData"]["total"]["win"][
                                                                          "teams"].get(team, 0) + 1
            self.winByDate[game.game["t"][:7]] = self.winByDate.get(game.game["t"][:7], 0) + 1

        if setting != "undefined":
            if job in self.data["winLoseData"][setting]["games"]["jobs"].keys():
                self.data["winLoseData"][setting]["games"]["teams"]["total"] += 1
                self.data["winLoseData"][setting]["games"]["jobs"][job] = self.data["winLoseData"][setting]["games"][
                                                                              "jobs"].get(job, 0) + 1
                self.data["winLoseData"][setting]["games"]["teams"][team] = self.data["winLoseData"][setting]["games"][
                                                                                "teams"].get(team, 0) + 1
                if didWin:
                    self.data["winLoseData"][setting]["win"]["teams"]["total"] += 1
                    self.data["winLoseData"][setting]["win"]["jobs"][job] = self.data["winLoseData"][setting]["win"][
                                                                                "jobs"].get(job, 0) + 1
                    self.data["winLoseData"][setting]["win"]["teams"][team] = self.data["winLoseData"][setting]["win"][
                                                                                  "teams"].get(team, 0) + 1
            else:
                self.errorPush(id, 1, "認識された配役と職業が一致しません。")

        self.enterByTime[game.game["t"][11:-3]] = self.enterByTime.get(game.game["t"][11:-3], 0) + 1
        self.data["enterByDate"][game.game["t"][:7]] = self.data["enterByDate"].get(game.game["t"][:7], 0) + 1

        for friendName in game.game["m"].keys():
            if friendName == name or game.thisJobTeam(game.game["m"][friendName]["j"]) == "no team":
                continue
            self.friends[friendName] = self.friends.get(friendName, 0) + 1
        self.villeges[title] = self.villeges.get(title, 0) + 1
        if self.data["firstLog"][0] > game.id or self.data["firstLog"][1] == "":
            self.data["firstLog"][0] = game.id
            self.data["firstLog"][1] = game.ParsedTitle(numDelete=False)[0]
        if self.data["finalLog"][0] < game.id or self.data["finalLog"][1] == "":
            self.data["finalLog"][0] = game.id
            self.data["finalLog"][1] = game.ParsedTitle(numDelete=False)[0]


class Game():
    def __init__(self, gameLog):
        self.game = gameLog
        self.id = self.game["id"]
        self.villegeTeam = ["(占い師)", "(霊能者)", "(狩人)", "(猫又)", "(共有者)", "(村人)", "(怪盗)", "(狼憑き)", "(役人)", "(ものまね)"]
        self.wolfTeam = ["(人狼)", "(狂人)", "(狂信者)"]
        self.foxTeam = ["(妖狐)", "(背徳者)"]
        self.teruteruTeam = ["(てるてる)"]

    def searchName(self, names, escapeAtMark=False):
        for mem in self.game["m"]:
            if escapeAtMark:
                if mem.split("@")[0] in names:
                    return mem
            else:
                if mem in names:
                    return mem
        return "not in"

    def ParsedTitle(self, numDelete=False):
        isNumberingDefined = False
        tmp = self.game["v"].split("-")
        if isNumberingDefined == True:
            num = int(tmp.pop())
        else:
            num = -1
        villege = "-".join(tmp)
        if numDelete:
            deleteCharacter = list("0123456789０１２３４５６７８９一二三四五六七八九十百壱弐参肆伍陸漆捌玖拾佰")
            villege = "".join(list(map(lambda x: x * (not x in deleteCharacter), list(villege))))
        return (villege, num)

    def canShonikiBejob(self):
        # ex.) 役職設定【人狼-3,占い師-1,狩人-1,霊能者-1,狂人-1,猫又-1,村人-4,役欠け:あり】
        return self.game["s"][5:][::-1][1:][::-1].split(",").pop() == "役欠け:あり"

    def normalizedSetting(self):
        """
        【人狼-2,占い師-1,狩人-1,霊能者-1,狂人-1,狂信者-0,妖狐-1,背徳者-0,てるてる-0,猫又-0...ものまね-0,村人-5,役欠け:あり】
        みたいなのから
        【人狼-2,占い師-1,狩人-1,霊能者-1,狂人-1,妖狐-1,村人-5,役欠け:あり】
        にする
        """
        jobList = self.game["s"][1:-1].split(",")
        yakukake = jobList.pop()
        normalJobStr = ""
        for jobInfo in jobList:
            jobName, jobNum = tuple(jobInfo.split("-"))
            if jobNum == "0" and jobName != "村人":
                continue
            normalJobStr += jobName + "-" + jobNum + ","
        return "【" + normalJobStr + yakukake + "】"

    def didThisJobWin(self, job):
        winner = self.game["w"]
        return (
                (winner == "村人" and job in self.villegeTeam) or
                (winner == "人狼" and job in self.wolfTeam) or
                (winner == "妖狐" and job in self.foxTeam) or
                (winner == "てるてる" and job in self.teruteruTeam)
        )

    def thisJobTeam(self, job):
        if job in self.villegeTeam:
            return "村人"
        elif job in self.wolfTeam:
            return "人狼"
        elif job in self.foxTeam:
            return "妖狐"
        elif job in self.teruteruTeam:
            return "てるてる"
        else:
            return "no team"

    def settingName(self):
        jobStr = self.normalizedSetting()
        if jobStr == "【人狼-3,占い師-1,狩人-1,霊能者-1,狂人-1,猫又-1,村人-4,役欠け:あり】":
            settingName = "12Acat"
        elif jobStr == "【人狼-2,占い師-1,狩人-1,霊能者-1,狂人-1,村人-5,役欠け:あり】":
            settingName = "11A"
        elif jobStr == "【人狼-2,占い師-1,狩人-1,霊能者-1,狂人-1,妖狐-1,村人-5,役欠け:あり】":
            settingName = "12B"
        elif jobStr == "【人狼-2,占い師-1,霊能者-1,狂人-1,共有者-2,村人-1,役欠け:あり】":
            settingName = "8CFO"
        elif jobStr == "【人狼-2,占い師-1,狩人-1,霊能者-1,狂人-1,村人-4,役欠け:あり】":
            settingName = "10A"
        elif jobStr == "【人狼-3,占い師-1,狩人-1,霊能者-1,狂信者-1,妖狐-1,背徳者-1,猫又-1,共有者-2,村人-2,役欠け:あり】":
            settingName = "14Dcat"
        else:
            settingName = "undefined"
        return settingName

    def isNoGame(self):
        return self.game["n"]

    def matchQuery(self,
                   playersNames=[[""]],
                   jobs=[""],
                   villegeNames=[""],
                   settings=[""],
                   duringPairs=[[""]],
                   escapeAtMark=False,
                   ignoreNoGame=False,
                   ignoreWatcher=False):
        match = True
        if playersNames != [[""]]:
            playersName = []
            for playerNames in playersNames:
                playerName = self.searchName(playerNames, escapeAtMark=escapeAtMark)
                if playerName == "not in":
                    match = False
                playersName.append(playerName)
            if match and jobs != [""]:
                for i, playerName in enumerate(playersName):
                    if self.game["m"][playerName]["j"] != jobs[i]:
                        match = False
            if match and ignoreWatcher:
                for i, playerName in enumerate(playersName):
                    if self.game["m"][playerName]["j"] in ["(観戦者)", "(GM)"]:
                        match = False
        if villegeNames != [""]:
            villegeMatch = False
            for villegeName in villegeNames:
                if re.search(villegeName, self.game["v"]):
                    villegeMatch = True
            if not villegeMatch:
                match = False
        if settings != [""]:
            if not self.settingName() in settings:
                match = False
        if duringPairs != [[""]]:
            timeMatch = False
            for duringPair in duringPairs:
                startTime = dt.datetime.strptime(duringPair[0], "%Y-%m-%d %H:%M:%S")
                endTime = dt.datetime.strptime(duringPair[1], "%Y-%m-%d %H:%M:%S")
                gameTime = dt.datetime.strptime(self.game["t"], "%Y-%m-%d %H:%M:%S")
                if startTime <= gameTime <= endTime:
                    timeMatch = True
            if not timeMatch:
                match = False
        if ignoreNoGame:
            if self.game["n"]:
                match = False
        return match


def getNumOfLogFile():
    drive = DriveFileStream()
    finalLogNum = int(drive.load_file("root/finalLogNum.txt"))
    return finalLogNum


def getAnalyzedPartOfData(num, data, names):
    player = Player(names)
    drive = DriveFileStream()
    log = json.loads(drive.load_file("minify/log%d.json" % num))
    if inRedList(names):
        player.errorPush(-1, 3, "exist red list")
        return player.dumpSendData()
    if num != 0:
        player.load(data)
    for i in range(len(log)):
        for name in names:
            if name in log[i]["m"].keys():
                player.addData(log[i])
    return player.dumpSendData()


def getDumpAnalyzedData(data, names):
    player = Player(names)
    player.load(data)
    return player.dumpData()


def getSearchedPartOfData(num, data, playersNames, jobs, villegeNames, settings, duringPairs, escapeAtMark,
                          ignoreNoGame, ignoreWatcher):
    drive = DriveFileStream()
    log = json.loads(drive.load_file("minify/log%d.json" % num))
    matchedList = []
    if num != 0:
        matchedList = data
    for i in range(len(log)):
        game = Game(log[i])
        if game.matchQuery(playersNames, jobs, villegeNames, settings, duringPairs, escapeAtMark, ignoreNoGame,
                           ignoreWatcher):
            matchedList.append(log[i])
    return matchedList


def getFinalLogDate():
    drive = DriveFileStream()
    finalLogDate = drive.load_file("root/finalLogDate.txt")
    return finalLogDate

def inRedList(names):
    drive = DriveFileStream()
    red_list = json.loads(drive.load_file("root/red_list.json"))
    in_red_list = False
    for name in names:
        if name in red_list:
            in_red_list = True
    return in_red_list

def getLog(num):
    drive = DriveFileStream()
    log = json.loads(drive.load_file("raw/log{}.json".format(num)))
    return log
