# Hello!

from tkinter import Variable
from winreg import DeleteValue
import time
import httpx, urllib, json,datetime
from undetected_chromedriver import Chrome, ChromeOptions

db = open("./db.txt", "r+").read()

def _MotionData():
    return "{\"st\":1662999253604,\"dct\":1662999253604,\"mm\":[[249,206,1662999326866],[234,163,1662999326894],[221,142,1662999326920],[214,139,1662999326946],[209,141,1662999326974],[202,149,1662999327000],[194,157,1662999327026],[189,160,1662999327053],[187,160,1662999327080],[185,159,1662999327106],[181,151,1662999327134],[177,140,1662999327160],[175,131,1662999327186],[174,127,1662999327214],[173,124,1662999327265],[172,125,1662999327634],[170,127,1662999327653],[168,129,1662999327680],[166,130,1662999327707],[164,130,1662999327746],[164,131,1662999327854],[163,133,1662999327880],[162,135,1662999327907],[162,138,1662999327934],[162,141,1662999327960],[163,144,1662999327987],[165,147,1662999328014],[170,151,1662999328040],[179,157,1662999328067],[190,161,1662999328094],[198,165,1662999328120],[205,167,1662999328147],[209,167,1662999328174],[212,167,1662999328200],[214,167,1662999328228],[215,166,1662999328253],[218,166,1662999328280],[220,165,1662999328307],[222,165,1662999328334],[225,165,1662999328360],[229,166,1662999328388],[236,170,1662999328414],[244,175,1662999328440],[249,178,1662999328467],[251,178,1662999328494],[251,177,1662999328736],[249,174,1662999328761],[246,170,1662999328787],[242,166,1662999328813],[238,161,1662999328841],[234,156,1662999328867],[231,154,1662999328893],[229,151,1662999328920],[226,147,1662999328947],[221,141,1662999328974],[214,134,1662999329001],[208,128,1662999329027],[204,124,1662999329054],[201,122,1662999329081],[202,122,1662999329343],[207,125,1662999329361],[219,131,1662999329387],[234,139,1662999329414],[248,147,1662999329440],[258,153,1662999329468],[260,155,1662999329494],[261,156,1662999329520],[261,159,1662999329548],[262,161,1662999329574],[262,162,1662999329601],[262,163,1662999329702],[262,164,1662999329721],[262,166,1662999329748],[263,169,1662999329788],[263,171,1662999329851],[264,172,1662999329881],[265,174,1662999329921],[266,175,1662999329948],[267,176,1662999329975],[269,178,1662999330001],[270,179,1662999330025],[269,179,1662999330255],[266,178,1662999330281],[262,177,1662999330307],[259,175,1662999330334],[255,173,1662999330361],[249,168,1662999330388],[243,162,1662999330414],[238,156,1662999330441],[235,152,1662999330467],[234,151,1662999330495],[235,151,1662999330593],[238,151,1662999330614],[247,154,1662999330641],[254,158,1662999330668],[261,162,1662999330694],[265,165,1662999330721],[266,168,1662999330748],[268,171,1662999330775],[269,174,1662999330802],[272,176,1662999330828],[273,178,1662999330854],[275,178,1662999330931]],\"mm-mp\":22.28095238095237,\"md\":[[173,124,1662999327280],[251,178,1662999328537],[270,179,1662999330025],[275,178,1662999330990]],\"md-mp\":1236.6666666666667,\"mu\":[[173,124,1662999327413],[251,178,1662999328655],[270,179,1662999330166],[275,178,1662999331088]],\"mu-mp\":1225,\"kd\":[[83,1662999327818],[65,1662999327841],[68,1662999327963],[68,1662999329203],[65,1662999329359],[68,1662999329572],[68,1662999330532],[65,1662999330621],[83,1662999330643]],\"kd-mp\":313.8888888888889,\"ku\":[[83,1662999328019],[68,1662999328243],[68,1662999329449],[65,1662999329584],[83,1662999329605],[68,1662999329772],[68,1662999330823],[65,1662999330867]],\"ku-mp\":317.6666666666667,\"topLevel\":{\"st\":1662999246905,\"sc\":{\"availWidth\":1920,\"availHeight\":1050,\"width\":1920,\"height\":1080,\"colorDepth\":24,\"pixelDepth\":24,\"top\":0,\"left\":0,\"availTop\":0,\"availLeft\":0,\"mozOrientation\":\"landscape-primary\",\"onmozorientationchange\":null},\"nv\":{\"permissions\":{},\"pdfViewerEnabled\":true,\"doNotTrack\":\"1\",\"maxTouchPoints\":0,\"mediaCapabilities\":{},\"oscpu\":\"Windows NT 10.0; Win64; x64\",\"vendor\":\"\",\"vendorSub\":\"\",\"productSub\":\"20100101\",\"cookieEnabled\":true,\"buildID\":\"20181001000000\",\"mediaDevices\":{},\"serviceWorker\":{},\"credentials\":{},\"clipboard\":{},\"mediaSession\":{},\"webdriver\":false,\"hardwareConcurrency\":12,\"geolocation\":{},\"appCodeName\":\"Mozilla\",\"appName\":\"Netscape\",\"appVersion\":\"5.0 (Windows)\",\"platform\":\"Win32\",\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0\",\"product\":\"Gecko\",\"language\":\"en-US\",\"languages\":[\"en-US\",\"en\"],\"locks\":{},\"onLine\":true,\"storage\":{},\"plugins\":[\"internal-pdf-viewer\",\"internal-pdf-viewer\",\"internal-pdf-viewer\",\"internal-pdf-viewer\",\"internal-pdf-viewer\"]},\"dr\":\"\",\"inv\":false,\"exec\":false,\"wn\":[],\"wn-mp\":450.51612903225805,\"xy\":[],\"xy-mp\":0,\"mm\":[[568,779,1662999326734],[517,755,1662999326760],[468,720,1662999326787],[428,674,1662999326813],[400,627,1662999326840],[385,577,1662999326864]],\"mm-mp\":82.32692307692308},\"v\":1}".replace('1662739', str(round(datetime.datetime.now().timestamp()))[:7])
    
objectData = {  #add calfs 
    'buffalo': ['roam', 'battle', 'forest', 'food','walk', 'kill', 'animal', 'drink', 'cell', 'face', 'body', 'real', 'hair', 'mammal', 'life', 'live',  "move", "organism", "living", "head", "alive", 'body part', 'eat', 'warm', 'amniote', 'survive', 'vertebrate', 'mate', 'head', 'defend', 'bone', 'find', 'die','exist'],
    'buffalos': ['roam', 'battle', 'forest', 'food','walk', 'kill', 'animal', 'drink', 'cell', 'face', 'body', 'real', 'hair', 'mammal', 'life', 'live', "move", "organism", "living", "head", "alive", 'body part', 'eat', 'warm', 'amniote', 'survive', 'vertebrate', 'mate', 'head', 'defend', 'bone', 'find', 'die','exist'],
    'buffaloes': ['roam', 'battle', 'forest', 'food','walk','kill', 'animal', 'drink', 'cell', 'face', 'body', 'real', 'hair', 'mammal', 'life', 'live', "move", "organism", "living", "head", "alive", 'body part', 'eat', 'warm', 'amniote', 'survive', 'vertebrate', 'mate', 'head', 'defend', 'bone', 'find', 'die','exist'],
    'bull': ['roam', 'battle', 'forest', 'food','walk','kill', 'animal', 'drink', 'cell', 'face', 'body', 'real', 'hair', 'mammal', 'life', 'live', "move", "organism", "living", "head", "alive", 'body part', 'eat', 'warm', 'amniote', 'survive', 'vertebrate', 'mate', 'head', 'defend', 'bone', 'find', 'die','exist'],
    'bulls': ['roam', 'battle', 'forest', 'food','walk','kill', 'animal', 'drink', 'cell', 'face', 'body', 'real', 'hair', 'mammal', 'life', 'live', "move", "organism", "living", "head", "alive", 'body part', 'eat', 'warm', 'amniote', 'survive', 'vertebrate', 'mate', 'head', 'defend', 'bone', 'find', 'die','exist'],
    'calf': ['roam', 'battle', 'forest', 'food','walk','kill', 'animal', 'drink', 'cell', 'face', 'body', 'real', 'hair', 'mammal', 'life', 'live', "move", "organism", "living", "head", "alive", 'body part', 'eat', 'warm', 'amniote', 'survive', 'vertebrate', 'mate', 'head', 'defend', 'bone', 'find', 'die','exist'],
    'calfs': ['roam', 'battle', 'forest', 'fight','food','walk','kill', 'animal', 'drink', 'cell', 'face', 'body', 'real', 'hair', 'mammal', 'life', 'live',"move", "organism", "living", "head", "alive", 'body part', 'eat', 'warm', 'amniote', 'survive', 'vertebrate', 'mate', 'head', 'defend', 'bone', 'find', 'die','exist'],
    'calves': ['roam', 'battle', 'forest', 'fight','food','walk','kill', 'animal', 'drink', 'cell', 'face', 'body', 'real', 'hair', 'mammal', 'life', 'live',  "move", "organism", "living", "head", "alive", 'body part', 'eat', 'warm', 'amniote', 'survive', 'vertebrate', 'mate', 'head', 'defend', 'bone', 'find', 'die','exist'],
    'baboon': ['roam', 'battle', 'forest', 'fight','food','walk','kill', 'animal', 'drink', 'cell', 'face', 'body', 'real', 'hair', 'mammal', 'life', 'live',  "move", "organism", "living", "head", "alive", 'body part', 'eat', 'warm', 'amniote', 'survive', 'vertebrate', 'mate', 'head', 'defend', 'bone', 'find', 'die','exist'],
    'baboons': ['roam', 'battle', 'forest', 'fight','food','walk','kill', 'animal', 'drink', 'cell', 'face', 'body', 'real', 'hair', 'mammal', 'life', 'live', "move", "organism", "living", "head", "alive", 'body part', 'eat', 'warm', 'amniote', 'survive', 'vertebrate', 'mate', 'head', 'defend', 'bone', 'find', 'die','exist'],
    'monkey': ['roam', 'battle', 'forest', 'fight','food','walk','kill', 'animal', 'drink', 'cell', 'face', 'body', 'real', 'hair', 'mammal', 'life', 'live', "move", "organism", "living", "head", "alive", 'body part', 'eat', 'warm', 'amniote', 'survive', 'vertebrate', 'mate', 'head', 'defend', 'bone', 'find', 'die','exist'],
    'monkeys': ['roam', 'battle', 'forest', 'fight','food','walk','kill', 'animal', 'drink', 'cell', 'face', 'body', 'real', 'hair', 'mammal', 'life', 'live',"move", "organism", "living", "head", "alive", 'body part', 'eat', 'warm', 'amniote', 'survive', 'vertebrate', 'mate', 'head', 'defend', 'bone', 'find', 'die','exist'],
    'camel': ['roam', 'battle', 'forest', 'fight','food','walk','kill', 'animal', 'drink', 'cell', 'face', 'body', 'real', 'hair', 'mammal', 'life', 'live', "move", "organism", "living", "head", "alive", 'body part', 'eat', 'warm', 'amniote', 'survive', 'vertebrate', 'mate', 'head', 'defend', 'bone', 'find', 'die','exist'],
    'camels': ['roam', 'battle', 'forest', 'fight','food','walk','kill', 'animal', 'drink', 'cell', 'face', 'body', 'real', 'hair', 'mammal', 'life', 'live', "move", "organism", "living", "head", "alive", 'body part', 'eat', 'warm', 'amniote', 'survive', 'vertebrate', 'mate', 'head', 'defend', 'bone', 'find', 'die','exist'],
    'carp': ['body', 'roam', 'battle', 'scale', 'fight','light', 'live', 'shiny', 'ocean', 'sea', 'fresh', 'river', 'tail', 'fin', 'gill', 'mammal', 'food', 'fresh', 'face', 'life', 'swim', 'kill', 'animal', "tail", "lake", "aqua", "pond", "carp", "move", 'water', 'swim', 'organism', 'living', 'alive', 'eat', 'cold', 'survive', 'mate', 'fish', 'head', 'defend', 'bone', 'find', 'die','exist', 'vertebrate'],
    'carps': ['body', 'roam', 'battle', 'scale', 'fight','light', 'live', 'shiny', 'ocean','sea', 'fresh', 'river', 'tail','fin', 'gill', 'mammal','food', 'cell', 'fresh', 'face', 'life', 'swim', 'kill', 'animal', "tail", "lake", "aqua", "pond", "carp", "move", 'water', 'swim', 'organism', 'living', 'alive', 'eat', 'cold', 'survive', 'mate', 'fish', 'head', 'defend', 'bone', 'find', 'die','exist', 'vertebrate'],
    'fish': ['body', 'roam', 'battle', 'scale', 'fight','light', 'live', 'shiny', 'ocean','sea', 'fresh', 'river', 'tail','fin', 'gill', 'mammal','food', 'cell', 'fresh', 'face', 'life', 'swim', 'kill', 'animal', "tail", "lake", "aqua", "pond", "carp", "move", 'water', 'swim', 'organism', 'living', 'alive', 'eat', 'cold', 'survive', 'mate', 'fish', 'head', 'defend', 'bone', 'find', 'die','exist', 'vertebrate'],
    'carnivores': ['body', 'roam', 'battle', 'forest', 'fight','live', 'mammal', 'food', 'body part', 'kill', 'animal', 'face', 'drink', 'cell', 'live', 'life', 'living', 'alive', 'living', 'move', 'real', 'survive', 'body part', 'eat',  'head', 'mate', 'organism', 'defend', 'bone', 'find', 'die','exist', 'vertebrate'],
    'carnivore': ['body', 'roam', 'battle', 'forest', 'fight','live', 'mammal', 'food', 'body part', 'life', 'live', 'kill', 'animal', 'face', 'drink', 'cell', 'alive', 'living', 'move', 'real', 'survive', 'body part', 'eat',  'head', 'mate', 'organism','defend', 'bone', 'find', 'die','exist', 'vertebrate']
}
antiobjectData = ["invertebrate", "soda", "body of", "die more", "plastic", "country", "disease"]

#add battle


# add support for INvertebrate, drink SODA, exist, body OF .. (water), die, die MORE than once, real COUNTRY

def analyze(text):
    if "_really" in text:
        text = text.replace("_really", "") # accuracy improvements
    text = text.replace("?", "")
    animal = None
    for antiobject in antiobjectData:
        if antiobject in text.replace("_", ""):
            print(f'guessing no for {text} (anti object)'); return 'no'
    for word in text.split("_"):
        if len(word) >= 4 and str(word) in objectData:
            animal = str(word)
    if animal:
        if text.split("_").count(str(animal)) > 1:
            print(f'guessing yes for {text} (animal >1)');return 'yes'
        for word in text.replace(f'_{animal}', "").replace("?", "").split("_"):
            if any(n in word for n in objectData[animal]): 
                print(f'guessing yes for {text} (crtiteria matched)');return 'yes'
        print(f'guessing no for {text} (criteria not matched)');return 'no'
    else:
        print(f'animal was not found in {text}, guessing no');return 'no'

base_header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-type': 'application/x-www-form-urlencoded', #'text/plain'
            'Origin': 'https://newassets.hcaptcha.com',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Alt-Used': 'hcaptcha.com',
            'Connection': 'keep-alive',
            'Referer': 'https://newassets.hcaptcha.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'TE': 'trailers'
        }

class solver:
    def __init__(_self, site_key: str = '4c672d35-0701-42b2-88c3-78380b0db560', siteurl: str = 'discord.com', proxy: str = ''):
        _self.site_key = site_key
        _self.website = siteurl
        _self.base_header = base_header
        _self.proxy = proxy
        
        #_self.chrome_opts = ChromeOptions()
       # _self.chrome_opts.headless = True
        #_self.driver = Chrome(options=_self.chrome_opts)
        _self.v = _self._Get_v()

    def _Get_v(_self):
        respone = httpx.get("https://hcaptcha.com/1/api.js").text
        s = respone.find("https://newassets.hcaptcha.com/captcha/") + 42
        f = respone[s:].find("/") + s
        return respone[s:f]
        
    def _HSW(_self, req_id: str):
        #hsw_code = httpx.get("https://newassets.hcaptcha.com/c/bed8f9f9/hsw.js").text
        with httpx.Client() as client:
            response = client.post('http://192.168.1.18:5000/hsw', data={'request_id': req_id}, timeout=30)
            return response.text
        #return _self.driver.execute_script(f"{hsw_code}; return hsw('{req_id}')")

    def _Get_Task(_self):
        payload = {
            'v': _self.v,
            'host': _self.website,
            'sitekey': _self.site_key,
            'sc': '1',
            'swa': '1',
        }

        payload = urllib.parse.urlencode(payload)
        _self.base_header['Content-Type'] = 'application/x-www-form-urlencoded'
        _self.base_header['Content-Length'] = str(len(payload))

        with httpx.Client(headers= _self.base_header, proxies=_self.proxy) as client:
            response = client.post(f"https://hcaptcha.com/checksiteconfig?v=1f7dc62&host={_self.website}&sitekey={_self.site_key}&sc=1&swa=1", data=payload).json()
            return response['c']

    def _Get_Captcha(_self, n: str, c: dict):
        payload = {
            'v': _self.v,
            'sitekey': _self.site_key,
            'host': _self.website,
            'hl': 'en',
            'motionData': _MotionData(),
            'n': n,
            'c': json.dumps(c)
        }

        payload = urllib.parse.urlencode(payload)
        _self.base_header['Content-Type'] = 'application/x-www-form-urlencoded'
        _self.base_header['Content-Length'] = str(len(payload))

        with httpx.Client(headers=_self.base_header, proxies=_self.proxy) as client:
            response = client.post(f"https://hcaptcha.com/getcaptcha?s={_self.site_key}", data=payload).json()
            return response

    def _Get_Text_Captcha(_self,captcha_task):
        n = _self._HSW(captcha_task['c']['req'])
        c = captcha_task['c']
        payload = {
            'v': _self.v,
            'sitekey': _self.site_key,
            'host': _self.website,
            'hl': 'en',
            'a11y_tfe': 'true',
            'action': 'challenge-refresh',
            'extraData': captcha_task,
            'motionData': _MotionData(),
            'n': n,
            'c': json.dumps(c)
        }

        payload = urllib.parse.urlencode(payload)
        _self.base_header['Content-Type'] = 'application/x-www-form-urlencoded'
        _self.base_header['Content-Length'] = str(len(payload))

        with httpx.Client(headers=_self.base_header, proxies=_self.proxy) as client:
            response = client.post(f"https://hcaptcha.com/getcaptcha?s={_self.site_key}", data=payload)
            if response.status_code == 429:
                raise Exception("too many requests sir")
            #print(response.status_code)
            return response.json()

    def _Slove_Text(_self, text: str):
        try: 
            gg = db.split(f'{text} || ')[1].split("\n")[0].strip()
            print(f'answering {gg} for {text}')
            return {'text': gg}
        except:
            # t = text.replace("_", " ")
            # r = input(f"(?) {t}")
            # if r.lower() == "yes":
            #     ff = "yes"#بله
            # else:
            #     ff = "no"#خیر
            # if not r.lower() == "idk":
            #     with open("./db.txt","a") as f:
            #         f.write(f"{text} || {ff}\n")
            # return {'text': ff}
            guess = analyze(text)
            return {'text': guess}

    def Solve_Task(_self, task: dict):
        n = _self._HSW(task['c']['req'])
        if "key" not in task:print("bad", task)
        task_key = task['key']
        c = task['c']
        tasklist = task['tasklist']
        solved_task = {}
        for i in tasklist:
            time.sleep(1.5)
            solved_task[i['task_key']] = _self._Slove_Text(i['task_key'])
        with httpx.Client(headers=_self.base_header, proxies=_self.proxy) as client:
            payload = {
                'v': _self.v,
                'job_mode': 'text_free_entry',
                'answers': solved_task,
                'serverdomain': _self.website,
                'sitekey': _self.site_key,
                'motionData': _MotionData(),
                'n': n,
                'c': json.dumps(c),
            }

            client.headers['Content-Length'] = str(len(json.dumps(payload)))
            client.headers['Content-Type'] = 'application/json;charset=UTF-8'

            response = client.post(f'https://hcaptcha.com/checkcaptcha/{task_key}?s={_self.site_key}', json=payload).json()

            if 'pass' in str(response):
                if response['pass']:
                    return response['generated_pass_UUID']
            else:
                print("failed converting to text", response)
                pass

    def solve(_self):
        task = _self._Get_Task()
        _N = _self._HSW(task['req'])
        _CT = _self._Get_Captcha(_N, task)
        Text_Captcha = _self._Get_Text_Captcha(captcha_task=_CT)
        return _self.Solve_Task(Text_Captcha)