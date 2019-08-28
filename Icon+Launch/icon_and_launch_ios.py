import requests
import time
import os
import json
import re
#pip3 install pillow
from PIL import Image,ImageDraw,ImageFont
import glob
from math import ceil, floor
from PIL import ImageColor
import random
from biplist import *
from datetime import datetime
import shutil
import chardet
import codecs
import math
 
json_name = '初中生物.json' #DE448F---#133339 ?
# json_name = '证券从业资格.json' #958774---#7C8F37 ?
# json_name = '初中地理.json' #752BD1---#7FE1CB ?
# json_name = '基金从业资格.json' #264A64---#4AFEB5 ？
# json_name = '教师招聘.json' #B88B64---#DEB183
# json_name = '放射医学技术.json' #AB2232---#4CC812
# json_name = '事业单位.json' #311667---#E89B7C
# json_name = '电力安规考试.json' #E85318---#E98FFF
# json_name = '会计职称考试.json' #DD71FE---#CE355F
# json_name = '护师考试.json'  #5636CE---#836F13
# json_name = '初中政治.json' #6A1775---#19D9CD
#json_name = '主管护师.json'  #6D19EB---#4E4E43 ?
# json_name = '司法考试.json' #3B6D42---#A99579
# json_name = '放射医学技士.json' #A9567F---#AED973
# json_name = '社区工作者.json' #66B3DB---#A1EEBC
# json_name = '初中历史.json' #1AC11A---#588755
# json_name = '护士考试.json' #7788F1---#7CADB6 
# json_name = '初中语文.json' #F38662---#8771DD
# json_name = '政法干警.json' #33637E---#DCE71F
# json_name = '银行从业资格.json' #36237D---#93B534
# json_name = '经济师考试.json' #CFA17F---#6F9A5F


db_name = ''

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = BASE_DIR + '/icon_iOS/png/'
plist_path= BASE_DIR + '/../gushiwen/Info.plist'
neigou_plist_path = BASE_DIR + '/../gushiwen/3rd/MKStoreKit/MKStoreKitConfigs.plist'
make_path = BASE_DIR + '/icon_iOS/png/make_image/'
json_path = BASE_DIR + '/icon_iOS/json/'
db_path= BASE_DIR + '/../gushiwen/Resources/db/data.db'

txt = '初  中\n古  诗'
name='初中古诗'
APPLE_ID="1460138250"
TALKING_DATA_ID="C57B008BE91D498785C6C2C89A070230"
UM_DATA_ID="5cb729973fc195b98f00020a"
bundleid='com.suntao.chuzhonggushi'
GADApplicationIdentifier='ca-app-pub-3940256099942544~1458002511'
GADInterstitialIdentifier='ca-app-pub-7710541496651390/2414774184'
GADBannerdentifier='ca-app-pub-7710541496651390/2414774184'

app_make_gradual_icon=0
app_main_color="#FF0000"
color="#FF0000"
has_fenlei="0"
has_attri="0"
DB_COUNT=2000


a = {
    '20':20,
    '29':29,
    '40-1':40,
    '40-2':40,
    '40':40,
    '58-1': 58,
    '58': 58,
    '60': 60,
    '76': 76,
    '80-1': 80,
    '80': 80,
    '87': 87,
    '120-1': 120,
    '120': 120,
    '152': 152,
    '167': 167,
    '180': 180,
    '1024': 1024,
}

def parase_json():
    path = json_path + json_name
    fw=open(path, 'r',encoding='utf-8')
    dic = json.load(fw)
    print(dic)
    global txt
    global name
    global APPLE_ID
    global TALKING_DATA_ID
    global UM_DATA_ID
    global bundleid
    global GADApplicationIdentifier
    global db_name
    global GADInterstitialIdentifier
    global GADBannerdentifier
    global has_fenlei
    global has_attri
    global app_make_gradual_icon
    global DB_COUNT

    txt=dic['txt']
    name=dic['name']
    APPLE_ID=dic['APPLE_ID']
    TALKING_DATA_ID=dic['TALKING_DATA_ID']
    UM_DATA_ID=dic['UM_DATA_ID']
    bundleid=dic['bundleid']
    GADApplicationIdentifier=dic['GADApplicationIdentifier']
    GADInterstitialIdentifier=dic['GADInterstitialIdentifier']
    GADBannerdentifier=dic['GADBannerdentifier']
    has_fenlei=dic['has_fenlei']
    has_attri=dic['has_attri']
    db_name=dic['db_name']
    app_make_gradual_icon=dic['app_make_gradual_icon']
    DB_COUNT=dic['DB_COUNT']

def setup_download_dir(directory):
    """ 设置文件夹，文件夹名为传入的 directory 参数，若不存在会自动创建 """
    print(directory)
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except Exception as e:
            pass
    return True

def make_image_and_bg(str,txt):
    color = ImageColor.getrgb(str)
    img = Image.new("RGBA",(1024,1024),color)
    img.save(path + '1024'+'.png')
    txt = txt
    make_image_text(img,txt)

def make_launch_image_and_bg(str,txt):
    color = ImageColor.getrgb(str)
    icon_l = BASE_DIR + '/icon_iOS/png/launch/'

    for pidImage in glob.glob(icon_l + "/*.[jp][pn]g"):
        url = pidImage
        im = Image.open(url)
        x,y = im.size
        img = Image.new("RGBA",im.size,color)
        img.save(url)
        txt = txt
        make_image_launch_text(img,url,txt)


def make_image_launch_text(img,url,txt):
    x,y = img.size
    #w = 100
    #h = 100
        
    size = math.ceil(x /4.0)
    if x>y:
        size = math.ceil(y /4.0)

    txtl =list(txt)
    #txtl=txt.split("", 1)
    txt = ''
    p=1
    for str1 in txtl:
        if p%2==0:
            txt = txt + str1 + "\n"
        else:
            txt = txt + str1 + "   "
        p=p+1

    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(" /System/Library/Fonts/Hiragino Sans GB.ttc",size = size,encoding='unic')
    #“unic”（Unicode），“symb”（Microsoft Symbol），“ADOB”（Adobe Standard），“ADBE”（Adobe Expert）和“armn”（Apple Roman）
    #fill=(255, 255, 255, 0)
    word_count = math.ceil((p-1) /2.0)
    x_f = abs(ceil((x - 3 * size)/2.0))
    y_f = abs(ceil((y - (word_count * 2 - 1) * size)/2.0))
    w_font,h_font = font.getsize(txt)
    print(str(size) + '----' + str(x)+ '----' + str(y)+ '----' + str(w_font)+ '----' + str(h_font))
    d.text((x_f,y_f), txt, fill='white',font=font ,spacing=size)

    #d.text((abs(x-w_font * 0.6)/2,abs(y-h_font* 0.6)/3), txt, fill='white',font=font ,spacing=size)
    #font是个imagefont实例 spacing字体间距 direction rtl ttb
    img.save(url)
    #img.show()
    img.close()


def make_image_text(img,txt):
    x,y = img.size
    #w = 100
    #h = 100
        
    size = math.ceil(x /4.0)
    if x>y:
        size = math.ceil(y /4.0)

    txtl =list(txt)
    #txtl=txt.split("", 1)
    txt = ''
    p=1
    for str1 in txtl:
        if p%2==0:
            txt = txt + str1 + "\n"
        else:
            txt = txt + str1 + "   "
        p=p+1

    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(" /System/Library/Fonts/Hiragino Sans GB.ttc",size = size,encoding='unic')
    #“unic”（Unicode），“symb”（Microsoft Symbol），“ADOB”（Adobe Standard），“ADBE”（Adobe Expert）和“armn”（Apple Roman）
    #fill=(255, 255, 255, 0)

    word_count = math.ceil((p-1) /2.0)
    x_f = abs(ceil((x - 3 * size)/2.0))
    y_f = abs(ceil((y - (word_count * 2 - 1) * size)/2.0))
    w_font,h_font = font.getsize(txt)
    print(str(size) + '----' + str(x)+ '----' + str(y)+ '----' + str(w_font)+ '----' + str(h_font))
    d.text((x_f,y_f), txt, fill='white',font=font ,spacing=size)

    #font是个imagefont实例 spacing字体间距 direction rtl ttb
    img.save(path + '1024'+'.png')
    #img.show()
    img.close()


#16进制颜色格式颜色转换为RGB格式
def Hex_to_RGB(hex_str):
    r = int(hex_str[1:3],16)
    g = int(hex_str[3:5],16)
    b = int(hex_str[5:7],16)
    rgb = str(r)+','+str(g)+','+str(b)
    return (r,g,b)


def make_image_and_bg_gradual(color1,color2,txt):
    color = ImageColor.getrgb(color1)
    height = 1024
    width = 1024
    img = Image.new("RGBA",size = (1024,1024),color = color)
    bg_1 = Hex_to_RGB(color1)
    bg_2 = Hex_to_RGB(color2)
    draw = ImageDraw.Draw(img)
    strp_r = (bg_2[0] - bg_1[0])/ height
    strp_g = (bg_2[1] - bg_1[1])/ height
    strp_b = (bg_2[2] - bg_1[2])/ height

    for y in range(0,height):
        bg_r = round(bg_1[0] + strp_r * y)
        bg_g = round(bg_1[1] + strp_g * y)
        bg_b = round(bg_1[2] + strp_b * y)
        for x in range(0,width):
            draw.point((x,y),fill=(bg_r,bg_g,bg_b))
    #img.show()
    img.save(path + '1024'+'.png')
    txt = txt
    make_image_text(img,txt)

def make_launch_image_and_bg_gradual(color1,color2,txt):
    color = ImageColor.getrgb(color1)
    icon_l = BASE_DIR + '/icon_iOS/png/launch/'
    for pidImage in glob.glob(icon_l + "/*.[jp][pn]g"):
        url = pidImage
        im = Image.open(url)
        x,y = im.size
        height = y
        width = x
        img = Image.new("RGBA",im.size,color = color)
        bg_1 = Hex_to_RGB(color1)
        bg_2 = Hex_to_RGB(color2)
        draw = ImageDraw.Draw(img)
        strp_r = (bg_2[0] - bg_1[0])/ height
        strp_g = (bg_2[1] - bg_1[1])/ height
        strp_b = (bg_2[2] - bg_1[2])/ height

        for y in range(0,height):
            bg_r = round(bg_1[0] + strp_r * y)
            bg_g = round(bg_1[1] + strp_g * y)
            bg_b = round(bg_1[2] + strp_b * y)
            for x in range(0,width):
                draw.point((x,y),fill=(bg_r,bg_g,bg_b))
        img.save(url)
        txt = txt
        make_image_launch_text(img,url,txt)



def randomcolor():
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return "#"+color

def repalce_bundelid(bundle,name,gad,gBanner,gInterstitial):
    try:
        plist = readPlist(plist_path);
        plist['CFBundleIdentifier']=bundle;
        plist['CFBundleDisplayName']=name;
        plist['GADApplicationIdentifier']=gad;
        plist['GADInterstitialIdentifier']=gInterstitial;
        plist['GADBannerdentifier']=gBanner;
        writePlist(plist,plist_path)
    except InvalidPlistException:
         print("Not a Plist or Plist Invalid:" + e)

def repalce_neigou(bundle):
    try:
        plist = readPlist(neigou_plist_path);
        negou_str = bundle + "neigou"
        list1 = []
        list1.append(negou_str)
        dic2={}
        Consumables = plist['Consumables']
        for key,value in Consumables.items():
            dic1 = value
            dic2 = {negou_str:dic1}

        plist['Non-Consumables']=list1;
        plist['Consumables']=dic2;
        writePlist(plist,neigou_plist_path)
    except InvalidPlistException:
         print("Not a Plist or Plist Invalid:" + e)


def repalce_icon():
    icon_p= path + '1024/'
    app_icon_path= BASE_DIR + '/../gushiwen/Assets.xcassets/AppIcon.appiconset/'
    for pidImage in glob.glob(icon_p + "/*.[jp][pn]g"):
        url = pidImage
        p1 = r'png/1024/(.*)'
        pattern1 = re.compile(p1)  #同样是编译
        matcher1 = re.search(pattern1, url)  #同样是查询
        str1 = matcher1.group(0)
        b = str1.replace('png/1024/', '')
        name = b
        app_name_path = app_icon_path + name
        from_name_path = icon_p + name

        if os.path.exists(app_name_path):
            shutil.copyfile(from_name_path,app_name_path)

def repalce_launch_icon():
    icon_p = BASE_DIR + '/icon_iOS/png/launch/'
    app_icon_path= BASE_DIR + '/../gushiwen/Assets.xcassets/LaunchImage.launchimage/'
    for pidImage in glob.glob(icon_p + "/*.[jp][pn]g"):
        url = pidImage
        p1 = r'png/launch/(.*)'
        pattern1 = re.compile(p1)  #同样是编译
        matcher1 = re.search(pattern1, url)  #同样是查询
        str1 = matcher1.group(0)
        b = str1.replace('png/launch/', '')
        name = b
        app_name_path = app_icon_path + name
        from_name_path = icon_p + name

        if os.path.exists(app_name_path):
            shutil.copyfile(from_name_path,app_name_path)

def repalce_db():
    db_path_to= db_path 
    db_path_from = BASE_DIR + '/icon_iOS/db/' + db_name
    if os.path.exists(db_path_to):
        shutil.copyfile(db_path_from,db_path_to)

      

def repalce_pch():
    pch_path= BASE_DIR + '/../gushiwen/Application/MQ-Prefix.pch'
    result_str = ''
    f=open(pch_path, "r+")
    for line in f.readlines():
        if line.find("#define HAS_FenLei") >= 0:
            has_fenlei_str =  '#define HAS_FenLei  @\"' + has_fenlei + '\"\n'
            result_str = result_str  + has_fenlei_str 
        elif line.find("#define HAS_Attr") >= 0:
            has_attri_str =  '#define HAS_Attr  @\"' + has_attri + '\"\n'
            result_str = result_str  + has_attri_str 
        elif line.find("#define NAVBAR_COLOR") >= 0:
            new_str =  '#define NAVBAR_COLOR  @\"' + app_main_color + '\"\n'
            result_str = result_str  + new_str 
        elif line.find("#define APPLE_ID") >= 0:
            apple_id =  '#define APPLE_ID  @\"' + APPLE_ID  + '\"\n'
            result_str = result_str + apple_id 
        elif line.find("#define TALKING_DATA_ID") >= 0:
            talking_id =  '#define TALKING_DATA_ID  @\"' + TALKING_DATA_ID + '\"\n'
            result_str = result_str + talking_id  
        elif line.find("#define DB_COUNT") >= 0:
            db_count_str =  '#define DB_COUNT  ' + str(DB_COUNT) + '\n'
            result_str = result_str + db_count_str
        elif line.find("#define UM_DATA_ID") >= 0:
            um_id =  '#define UM_DATA_ID  @\"' + UM_DATA_ID + '\"\n'
            result_str = result_str + um_id  
        elif line.find("#define PURCHURE_APP_ID") >= 0:
            pur_id =  '#define PURCHURE_APP_ID  @\"' + bundleid + 'neigou\"\n'
            result_str = result_str + pur_id  

        else:
            result_str = result_str + line 

    f.close()
    fw=open(pch_path, "w")
    fw.write(result_str)
    fw.close()



def repalce_project():
    pch_path= BASE_DIR + '/../gushiwen.xcodeproj/project.pbxproj'
    result_str = ''
    f=open(pch_path, "r+")
    for line in f.readlines():
        if line.find("PRODUCT_BUNDLE_IDENTIFIER") >= 0:
            new_str =  '\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = ' + bundleid + ';\n'
            result_str = result_str  + new_str 
        else:
            result_str = result_str + line 

    f.close()
    fw=open(pch_path, "w")
    fw.write(result_str)
    fw.close()


def make_all_icon():
   for pidImage in glob.glob(path + "/*.[jp][pn]g"):
        url = pidImage
        p1 = r'png/(.*)'
        pattern1 = re.compile(p1)  #同样是编译
        matcher1 = re.search(pattern1, url)  #同样是查询
        str1 = matcher1.group(0)
        b = str1.replace('png/', '')
        b = b.replace('.png', '')
        name = b
        new_path = path + name + '/';

        setup_download_dir(new_path)
        time.sleep(0.3)
        img = Image.open(pidImage)
        (x, y) = img.size  #read image size
        for key, value in a.items():
            out = img.resize((value, value), Image.ANTIALIAS)
            #图片保存
            out.save(new_path + key+'.png')


if __name__ == "__main__":
    parase_json()
    color=''
    color_b=''
    color_e=''
    time.sleep(1)
    if int(app_make_gradual_icon)==0:
        color=randomcolor()
        app_main_color=color
        print(color)
    else:
        color_b=randomcolor()
        color_e=randomcolor()
        app_main_color=color_b
        icon_color_s = color_b.replace('#', '')
        icon_color_e = color_e.replace('#', '')
        icon_color_name = 'icon_' + icon_color_s +'__' + icon_color_e + '.png'
        print(color_b + "---" + color_e)

    repalce_db()
    repalce_pch()
    repalce_project()
    repalce_bundelid(bundleid,name,GADApplicationIdentifier,GADBannerdentifier,GADInterstitialIdentifier)
    repalce_neigou(bundleid)

    if int(app_make_gradual_icon)==0:
        make_image_and_bg(color,txt)
        time.sleep(1)
        make_launch_image_and_bg(color,txt)
    else:
        make_image_and_bg_gradual(color_b,color_e,txt)
        time.sleep(1)
        make_launch_image_and_bg_gradual(color_b,color_e,txt)

    make_all_icon()
    time.sleep(1)
    repalce_icon()
    repalce_launch_icon()
 


