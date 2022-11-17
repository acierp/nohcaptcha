from flask import Flask, request
import threading
import undetected_chromedriver as uc
import httpx
import random
app = Flask(__name__)

hsw_code = httpx.get("https://newassets.hcaptcha.com/c/bed8f9f9/hsw.js").text

@app.route('/hsw', methods=['GET', 'POST'])
def hsw():
    global hsw_code
    request_id = request.form['request_id']
    return driver.execute_script(f"{hsw_code}; return hsw('{request_id}')")


if __name__ == "__main__":
    options = uc.ChromeOptions()
    options.headless=True
    options.add_argument('--headless')
    driver = uc.Chrome(options=options)
    
    app.run(host="0.0.0.0")