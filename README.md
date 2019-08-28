# auto_make_iOS_icon_and_launch
生成iOS launch 和 icon脚本

## 安装Pillow依赖
```
pip install -r requirements.txt
```

## Icon目录
自动生成纯色或者渐变色iOS icon 

使用方法（记得安装Pillow依赖）
```
cd Icon
python3  icon_ios.py
```

## launch目录
自动修改默认启动图为纯色或者渐变色+文案

使用方法（记得安装Pillow依赖）
```
cd Launch
python3  launch_ios.py
```

## Icon+Launch目录
自动生成纯色或者渐变色icon 
自动修改默认启动图为纯色或者渐变色+文案

使用方法（记得安装Pillow依赖）
```
cd Icon+Launch
python3  icon_and_launch_ios.py
```

