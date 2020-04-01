# Overview
人狼Onlineのログをスクレイピングしたデータを扱うAPIです。  
URL: https://zinrologanalyzerapi.herokuapp.com/  
~~クソコードクソ設計ガバ英語だけどもう書き直したくないですゆるして~~

# 説明
- ログファイル  
Herokuでは処理時間が30秒超えるとタイムアウトしてしまいます。  
ログを一つのファイルにすると膨大なサイズなので読み込みだけで30秒超えます。  
なので、ログを分割して複数のファイルにしました。これがログファイルです。  
ログファイルには0~numOfLogの番号が割り当てられています。  
これらのログファイルに対してそれぞれ集計したものをAPIで取得していく、という形にしています。  
- names   
戦績サイトでは別名をカンマ区切りで出力となっていますが、それを配列にしたものがnamesです。
- 戦績の連想配列  
戦績を集計する時に使う連想配列です。色々入ってます。  
まずnum: 0で戦績を取得、num: 1~に対してはtmpDataで以前取得した戦績を渡してください。  
ここらへんについては実装見た方が早いかもしれません。
<details>
<summary>戦績の連想配列の型</summary>
<div>

```
{
  "data": {
    // dumpDataで送るのはこの部分
    // いくつかのデータはdumpDataのときに値が入ります
    "winLoseData": {
      "total": {
        // 総合について
        "games": {
          "jobs": {
            "(役職)": (役職)のときの参戦回数,
            ...
          },
          "teams": {
            "total": 全ての役職の参戦回数,
            "村人": 村陣営の参戦回数,
            "人狼": 人狼陣営の参戦回数,
            "妖狐": 同,
            "てるてる": 同
          }
        }, 
        "win": {
          // 勝利回数。構造は上と同じ
          "jobs": {...}
          "teams": {...}
        },
        "winPer": {
          // 勝率。構造は上と同じ
          "jobs": {...}
          "teams": {...}
        }
      },
      // 12A猫について。上と同じ
      "12Acat": {...}
      "12B": {...}
      "11A": {...}
      "8CFO": {...}
      "10A": {...}
      "14Dcat": {...}
    },
    // 途中計算用
    "enterByTime": [(00:00~23:59までの30分区切りの参戦回数)],
    "enterByDate": {"YYYY-MM": 参戦回数, ...},
    "winPerByDate": {"YYYY-MM": 勝利回数, ...},
    "firstLog": [int(id), "村名"],
    "finalLog": [int(id), "村名"],
    "ranking": {
      "friends": ["一位の名前", "二位", ..., "五位"],
      "villeges": ["一位", ..., "五位"]
    },
    // errorには何かあれば入ります
    "error": [{
      "no": エラー番号,
      "LogID": エラーが起きたログの番号,
      "mes": "説明"
    }, ...]
  },
  "friends": {"名前": 同村回数, ...},
  "villeges": {"村名": 参戦回数, ...}
  "winByDate": {"YYYY-MM": 勝利回数, ...}
  "enterByTime": {"hh:mm": 参戦回数, ...}
}
```

</div>
</details>

- ログ情報の連想配列  
ログファイルに保存されているのもこの形です。
<details>
<summary>ログ情報の連想配列の型</summary>
<div>

```
{
    "id": ログ番号(int),
    "v": 村名(str),
    "s": 役職設定(str),
    "t": 終了時刻(str),
    "n": 無効試合か(bool),
    "w": 勝利陣営(str),
    "m": {
        "名前": {
            "l": 最終日に生存しているか("生"or"死")
            "j": 役職(str)
        },
        ...
    },
}
```

</div>
</details>

# APIの仕様
argumentsに連想配列が要求されている場合はapplication/jsonで渡してください。

- /  
テスト用のものです。  
Method: GET  
arguments: (None)  
return: "OK"

- /numOfLog  
ログファイルが現在いくつあるか返します。  
Method: GET  
arguments: (None)  
return: {"numOfLog": int}  

- /inRedList  
本人の要請により戦績の観覧ができないようにしている名前であるかどうかを返します。  
Method: GET, POST  
arguments: {"names": List[str]}  
return: {"inRedList": bool}

- /finalLogDate  
最後に取得したログの日時を返します。  
Method: GET  
arguments: (None)  
return: {"finalLogDate": "YYYY年MM月DD日"}

- /getLog  
指定した番号のログファイルを返します。  
Method: GET, POST  
arguments: {"num": int}  
return: Dict(ログ情報の連想配列)  


- /analyzer/getData  
ログファイルから集計した戦績の連想配列を返します。
Method: GET, POST  
arguments: {"num": int, "names": List[str], "tmpData": Dict}  
return: Dict(戦績の連想配列)  
  
- /analyzer/dumpData  
与えられた戦績の連想配列をもとにサイトで扱えるように加工します。  
Method: GET, POST  
arguments: {"names": List[str], "data": Dict}  
return: Dict(戦績表示用の連想配列)  

- /search/getData  
ログファイルの中で与えられたクエリと一致するログを返します。  
Method: GET, POST  
arguments: {"num": int, "data": dict, "setting": Dict}  
return: List[Dict(ログ情報の連想配列)]  

# 使用例
/analyzer、/searchは汎用的ではないので、結局は/getLogをして自分で処理する方が早いかもです()  
pythonでの例です（requestsは別途pip installしてください）
```python
import requests
import json
url = "https://zinrologanalyzerapi.herokuapp.com/"
log = []
numOfLog = int(requests.get(url + "numOfLog").json()["numOfLog"])
headers = {"Content-Type": "application/json"}
for i in range(0, numOfLog+1):
	sendData = json.dumps({"num": i})
	log += requests.post(url + "getLog", data=sendData, headers=headers).json()
with open("./log.json", "wt") as f:
	json.dump(log, f)
# これでlog.jsonにすべてのログが保存されたぞ！！あとは好きに分析するなりしろ！！！
```