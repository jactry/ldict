LinDitc--dictionary for Linux!    
====

### 安装

1. 从 GitCafe 获取 ldict：

   `$ git clone git://gitcafe.com/Jactry/ldict.git ~/ldict`    

2. 进入到 ldict 目录，运行安装脚本：

    `$ cd ~/ldict`
	
    `$ python ~/ldict/setup.py`
	
3. 发音选项 `--speak` 需要 **gstreamer0.10-fluendo-mp3** 支持，Debian 和 Ubuntu 用户可以通过以下命令安装：

  `$ sudo apt-get install gstreamer0.10-fluendo-mp3`
  
### 选项说明

* `-a` (`--add`)：添加单词到[有道单词本](http://dict.youdao.com/wordbook/wordlist)，需要网易账号进行登录
* `-c` (`--web-explains`)：显示网络词组
* `-e` (`--example-sentences`)：显示中英双语例句
* `-f` (`--forms`)：查询单词的其他变形
* `-s` (`--speak`)：单词发音

### 截图

![截图](http://gitcafe.com/Jactry/ldict/raw/master/images/ldict.png)


