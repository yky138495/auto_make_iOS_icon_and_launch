# auto_make_iOS_icon_and_launch
生成launch脚本

## 安装Pillow依赖
```
pip install -r requirements.txt
```

## launch_ios.py 

根据个人所需的内容定制此配置文件
```
launch_path = BASE_DIR + '/launch/'#launch所以操作图片路径
txt = '' #设置生成图片上文字内容
app_main_color="#FF0000" #背景图片颜色-程序中随机替换颜色
icon_color_name ='' #icon名字 命名方式 (icon_颜色.png)
fill_color ='white'  #图片文字颜色
font_path = "/System/Library/Fonts/Hiragino Sans GB.ttc" #系统字体路径（以mac为例）
contents_json = "Contents.json" #生成iOS icon使用的json文件
make_gradual_icon=1  #是否生成渐变Img 1生成渐变 0纯色
```

## launch
默认启动图目录，iOS所以启动图位于此目录


## Contents.json

iOS launch使用的json文件
