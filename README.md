<div align="center">
    <h1>Genshin_Gacha_XY</h1>
    <h2>一个HoshinoBot的原神模拟抽卡插件</h2>
</div>
部分源码和资源文件参考和使用了 egenshin的资源
https://github.com/pcrbot/erinilis-modules/

## 安装
到`/hoshino/modules`目录下`git clone https://github.com/CMHopeSunshine/Genshin_Gacha_XY`
并在`/hoshino/config/__bot__.py`的`MODULES_ON`处添加`Genshin_Gacha_XY`开启模块

## 指令
```
1.抽n十连xx
n不写默认为1，xx不写默认为角色1池
如：抽十连、抽2十连角色池、抽5十连武器池

2.查看抽卡记录
查看已抽多少发，出货率、UP率等信息

3.查看抽卡记录 角色\武器
查看抽到的角色\武器

```

武器定轨还没写
用json用于存储模拟抽卡记录，为什么不用数据库呢？因为我懒、菜...
字体路径好像写得有点问题，自己解决吧，可以改成绝对路径

