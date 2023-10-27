# leetspeak
leetspeak翻译小玩具

使用方式打开disk中的leetspeak.exe在命令行中输入
```
leetspeak.exe -m 0 -i "asfdasf"
```
输出结果为：
```
@5fd@5f
```
-m是选择方式，0-编译，1-解译（目前只对win下的0有用）
-i 输出内容

leetspeak.py是小程序原理，替换逻辑也在其中

可直接下列代码直接将Python文件转换为可执行的EXE文件
```
pyinstaller --onefile .\leetspeak.py
```
