from flask import Flask, render_template, jsonify
import requests
import json
def main():
    sc = "en"
    tg = "ja"
    text = "Hello"
    headers = {"context-type":"application/json"}
    res = requests.get('https://script.google.com/macros/s/AKfycbxR4HbOqBxMspDO9bfWTzvyxZCQL07ASyvSFoJ9cc-tudQTy1VKRZmWNU4cd_Q9cj0y/exec?text={0}&source={1}&target={2}'.format(text,sc,tg),headers=headers)
    data = res.json()
    print(data['text'])
if __name__ == '__main__':
    main()