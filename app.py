from flask import Flask, request, jsonify, make_response
from Analyzer import getFinalLogDate, getNumOfLogFile, getAnalyzedPartOfData, getDumpAnalyzedData, \
	getSearchedPartOfData, inRedList, getLog
import json
import subprocess
import os

os.environ["RUNNIG_SCHEDULER"] = "OFF"
app = Flask(__name__)


@app.route("/")
def test():
	return "OK."


@app.route("/inRedList", methods=['GET', 'POST'])
def responseInRedList():
	params = request.json
	response = {"inRedList": inRedList(params["names"])}
	return json.dumps(response, ensure_ascii=False)


@app.route("/finalLogDate", methods=['GET'])
def responseFinalLogDate():
	response = {"finalLogDate": getFinalLogDate()}
	return json.dumps(response, ensure_ascii=False)


@app.route("/numOfLog", methods=['GET'])
def responseNumOfLog():
	response = {"numOfLog": getNumOfLogFile()}
	return json.dumps(response, ensure_ascii=False)


@app.route("/analyzer/getData", methods=['GET', 'POST'])
def responseAnalyzedPartOfData():
	params = request.json
	response = getAnalyzedPartOfData(params["num"], params["tmpData"], params["names"])
	return json.dumps(response, ensure_ascii=False)


@app.route("/analyzer/dumpData", methods=['GET', 'POST'])
def responseDumpData():
	params = request.json
	response = getDumpAnalyzedData(params["data"], params["names"])
	return json.dumps(response, ensure_ascii=False)


@app.route("/search/getData", methods=['GET', 'POST'])
def responseSearchedPartOfData():
	params = request.json
	response = getSearchedPartOfData(params["num"], params["data"], *params["setting"])
	return json.dumps(response, ensure_ascii=False)


@app.route("/getLog", methods=['GET', 'POST'])
def responseGetLog():
	params = request.json
	response = getLog(params["num"])
	return json.dumps(response, ensure_ascii=False)


@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
	return response


if __name__ == "__main__":
	# app.run(host="0.0.0.0")
	app.run()
