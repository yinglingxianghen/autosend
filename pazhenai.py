from selenium import webdriver
import time,os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
url='http://profile.zhenai.com/v2/personal/home.do'
cookies=[]
# cookies=[{'secure': False, 'path': '/', 'httpOnly': False, 'expiry': 1543719575.374465, 'value': '%5E%7Eworkcity%3D10131085%5E%7Esex%3D0%5E%7Emt%3D1%5E%7Enickname%3D%E9%B9%B0%E5%87%8C%E9%A6%99%E7%97%95%5E%7Edby%3D806e5f9efdf4527%5E%7Elh%3D110623950%5E%7Eage%3D25%5E%7E', 'name': 'p', 'domain': '.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'expiry': 1574045975.3752, 'value': '2018-11-18+10%3A50%3A20', 'name': 'preLG_110623950', 'domain': '.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'value': 'uAksjjaQLyeemFCN8F84', 'name': 'sid', 'domain': '.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'expiry': 1574045978, 'value': '1542509978', 'name': 'Hm_lvt_2c8ad67df9e787ad29dbd54ee608f5d2', 'domain': '.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'expiry': 1574045955.836649, 'value': '10131000', 'name': 'ipCityCode', 'domain': 'profile.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'value': '%5E%7Eloginactiontime%3D1542509975335%5E%7E', 'name': 'loginactiontime', 'domain': '.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'expiry': 1543114775.374177, 'value': '86a1af626d905997db4d3a4fa273708d5faaf7ef539ea665f97182448adb7757dbcb4c29375406e007636aff98e54dbc956c086f1283ac9165a7cd574bf4df18', 'name': 'login_health', 'domain': '.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'value': '%5E%7Elogininfo%3D110623950%5E%7E', 'name': 'logininfo', 'domain': '.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'expiry': 3689993622.374325, 'value': '110623950.1542509975335.cbf543cad0dfb48188b6a03b8bd1dfdd', 'name': 'token', 'domain': '.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'value': '%5E%7ElastLoginActionTime%3D1542509975335%5E%7E', 'name': 'isSignOut', 'domain': '.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'value': '%5E%7Emid%3D110623950%5E%7E', 'name': 'mid', 'domain': '.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'expiry': 1542596378.135529, 'value': '1', 'name': 'zxr_index_110623950', 'domain': 'profile.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'value': '%5E%7EinfoValue%3DuserId%253D110623950%2526name%253D110623950%2526memo%253D%5E%7E', 'name': 'live800', 'domain': '.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'expiry': 1574045975.375341, 'value': '0', 'name': 'dgpw', 'domain': '.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'expiry': 1574045975.546117, 'value': '1', 'name': 'isFirstLoadPage', 'domain': 'profile.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'expiry': 1542556798.546249, 'value': 'yes', 'name': 'validate_110623950', 'domain': 'profile.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'expiry': 1542556798.54638, 'value': 'yes', 'name': 'smail_110623950', 'domain': 'profile.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'value': 'abc0vc8XM0IsYcSLLWKCw', 'name': 'JSESSIONID', 'domain': 'profile.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'value': '1542509978', 'name': 'Hm_lpvt_2c8ad67df9e787ad29dbd54ee608f5d2', 'domain': '.zhenai.com'}, {'secure': False, 'path': '/', 'httpOnly': False, 'expiry': 1574045986.050899, 'value': '48760', 'name': 'clientp', 'domain': 'profile.zhenai.com'}]
driver = webdriver.Chrome("./chromedriver.exe")
driver.get(url)
driver.delete_all_cookies()
list=['哈喽姑娘，看了你的资料，我觉得你是那么优秀、绰约多姿、出水芙蓉、温文尔雅、肤如凝脂、衣冠楚楚、姹紫嫣红、风华绝代、天生丽质、小鸟依人、秀色可餐、二八佳人、才子佳人、琪花瑶草、秀外慧中、花信年华、娇小玲珑、夭桃秾李、环肥燕瘦、含苞欲放、明眸皓齿、左家娇女、窈窕淑女、亭亭玉立、一表人才、珠光宝气、眉清目秀、袅袅婷婷、我见犹怜、钟灵毓秀、仪态万方、稚齿婑媠、美如冠玉、小家碧玉、愁眉啼妆、婀娜多姿、冰清玉洁、闭月羞花、香草美人、双瞳剪水、一笑千金、倾国倾城、朱唇皓齿、天生尤物、梨花带雨、姑射神人、娉婷袅娜、国色天香、风姿绰约、眉目如画、冰肌玉骨、楚楚动人、月里嫦娥、花枝招展、金枝玉叶、靡颜腻理、冰雪聪明、貌美如花、螓首蛾眉、绝代佳人、林下风气的美女呀！小生有机会得此一见真是三生有幸！',
      '巧了，而我正是个英俊潇洒、风流倜傥、玉树临风、年少多金、神勇威武、天下无敌、宇内第一、寂寞高手、刀枪不入、唯我独尊、玉面郎君、仁者无敌、勇者无惧、金刚不坏、英明神武、侠义非凡、义薄云天、古往今来、无与伦比、谦虚好学、不耻下问、聪明伶俐、活泼可爱、待友热情、对敌冷酷、对友赴汤蹈火、再所不辞、两肋插刀、枪林弹雨、勇往直前、慷慨大方、头脑精明、仙福永享、寿与天齐、百折不饶、百打不死、侠中豪杰、人中龙凤、有情有义、有胆有色、举世无双、既酷又帅、人之表率、诚实可信、谈吐大方、风度翩翩、气势凌人、气质高贵、单身贵族、貌赛潘安、智胜孔明、勇比子龙、义超关羽、巧越鲁班、至尊至圣、至高无上、华丽绚烂、英勇无比、道德榜样、千杯不醉、坐怀不乱、知识渊博、才高八斗、傲视众生、世外高人、光明磊落、公正无私、震古烁今的帅哥！']
for cookie in cookies:
    driver.add_cookie({
        'name': cookie['name'],
        'path': cookie['path'],
        'domain': cookie['domain'],
        'value': cookie['value'],
        # 'expiry': cookie['expiry'],
        'httpOnly':cookie['httpOnly'],
        'secure':cookie['secure']
    })
# opt = webdriver.FirefoxOptions()
# opt.set_headless()
driver.get(url)
time.sleep(1)
# driver.find_element_by_xpath('//*[@id="jcZAHeader"]/section[2]/div/menu/ul/li[3]/a').click()
WebDriverWait(driver,10,1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="jcZAHeader"]/section[2]/div/menu/ul/li[3]/a'))).click()
# driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/a').click()
# print(driver.find_element_by_xpath('/html/body/div[1]/div/div[5]/a'))
# js="var q=window.document.getElementByclassName('about').scrollTop=1000"
# driver.execute_script(js)
driver.execute_script('window.scrollTo(0,100000);')
time.sleep(2)
# print(driver.find_elements_by_class_name('pin_col masonry-brick').innerText='pin_col masonry-brick')
driver.execute_script('window.scrollTo(0,100000);')
time.sleep(2)
driver.execute_script('window.scrollTo(0,100000);')

for j in list:
    for i in range(15,100,1):
        # driver.find_element_by_xpath('/html/body/div[3]/div['+str(i)+']/div[1]/a[3]/img').click()
        WebDriverWait(driver,10,1).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div['+str(i)+']/div[1]/a[1]/img'))).click()
        # print(driver.window_handles)                                          /html/body/div[3]/div[19]/div[1]/a[1]/img
        # print(driver.current_window_handle)                                  /html/body/div[3]/div[15]/div[1]/a[1]/img  /html/body/div[3]/div[12]/div[1]/a[3]/img
        driver.switch_to_window(driver.window_handles[1])
        WebDriverWait(driver,10,1).until(EC.presence_of_element_located((By.XPATH, '//*[@id = "app"]/div[1]/div[2]/div[1]/div[1]/div[2]/div/a/div'))).click()
        print(driver.window_handles)
        driver.close()
        driver.switch_to_window(driver.window_handles[1])
        # print(driver.find_element_by_xpath('//*[@id="safeDialog"]/div/div[1]/div/p[1]'))
        try:
            WebDriverWait(driver,2,1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="safeDialog"]/div/div[1]/div/p[1]')))
            time.sleep(8)
            WebDriverWait(driver,10,1).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="activeBtn"]'))).click()
        except:
            pass
        print(driver.find_element_by_xpath('//*[@id="mailcontent"]'))
        WebDriverWait(driver,10,1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mailcontent"]'))).send_keys(j)
        driver.find_element_by_xpath('//*[@id="freesendmail2"]').click()
        time.sleep(1)
        driver.close()
        driver.switch_to_window(driver.window_handles[0])