# 实战Scrapy加Splash爬取js加载网站(天眼查)

## 目标
- 获取某个企业在天眼查上展示的文本信息

## 环境
- mac or linux(mint)
- python3 or python2
- docker and splash
- mongodb
- scrapy,其它库
## 原理
- splash具有处理js的能力(依赖docker)，实际上类似webkit。并且使用Twisted框架实现，故与scrapy结合很好(`都是异步非阻塞`)，哪怕是分布式扩展方面。利用html解析库beautiful4进行解析出结构化数据，并通过scrapy框架的pipeline将数据存入mongodb。

## 过程
- 安装mongodb
	- ubuntu
	
	<pre>
	$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
	$ deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen
	$ sudo apt-get update  # 更新仓库源
	$ sudo apt-get install mongodb-10gen  # 安装
	$ sudo mkdir -p /data/db  # mongodb数据文件默认使用的文件夹
	$ sudo chmod -R 777 /data/db # 并递归设置文件的全部权限可用(不建议直接这么粗鲁)
	
	$ sudo service mongodb start
	$ sudo service mongodb stop
	$ sudo service mongodb restart
	$ mongo
	</pre>
	
- 安装 docker 及 splash
	- [ubuntu install docker](https://store.docker.com/editions/community/docker-ce-server-ubuntu)
	
	<pre>
	$ sudo apt-get -y install apt-transport-https ca-certificates curl
	$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
	$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs)    stable"
	$ sudo apt-get update
	$ sudo apt-get -y install docker-ce
	</pre>
	
	- [ubuntu install splash](http://splash.readthedocs.io/en/latest/install.html)
	
	<pre>
	$ sudo docker pull scrapinghub/splash
	$ sudo docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash #可以访问 http://localhost:8050/
	</pre>
	
	- [OS X + Docker + splash](https://docs.docker.com/docker-for-mac/)

	<pre>
	download Docker for mac [Docker.dmg](https://download.docker.com/mac/stable/Docker.dmg)
	$ docker-machine create default
	$ docker-machine start default
	$ eval “$(docker-machine env default)”
	
	$ docker pull scrapinghub/splash
	$ docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash #可以访问 http://localhost:8050/
	
	$ docker-machine ip default # 还得运行splash的IP地址，端口默认为8050,这个地址:端口在配置文件setting.py里会使用到。
	</pre>
- 使用virtualenv安装python3

	<pre>
	$ pip install virtualenv # 安装第三方库
	$ virtualenv -h # 查看帮助
	$ virtualenv -p /usr/bin/python3 py3env #指定为python3,mac上也得先下载python3.dmg然后指定python3的路径
	$ source py3env/bin/activate  # 激活虚拟环境
	$ pip install anything # 在虚拟环境安装各种第三方库，还不需要sudo权限
	$ deactivate # 直到某时刻不再需要使用虚拟环境
	</pre>

- 安装scrapy，其他第三方库
	<pre>
	$ sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
	$ sudo apt-get install python3 python3-dev
	$ pip install scrapy
	$ pip install scrapy-splash # scrapy扩展splash用到的库
	$ pip install pymongo	# 结构后数据入库到 mongodb
	$ pip install beautifulsoup4  # 解析html库
	$ pip install -r requirements.txt # 或者直接一次性安装python第三方库
	</pre>
	
## 运行项目
- 项目地址[https://github.com/haijunt/tianyancha_example](https://github.com/haijunt/tianyancha_example)
- 安装 mongodb,docker,virtualenv,spalsh,scrapy,requirements.txt
- 启动splash: `sudo docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash`
- 启动虚拟环境 `source py3env/bin/activate` 并进行项目目录
- 开始爬取 `scrapy crawl tianyancha_spider -s LOG_FILE=scrapy.log`
- 查看scrapy.log日志，mongodb数据



