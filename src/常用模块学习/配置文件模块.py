# 用于生成和修改常见配置文档，当前模块的名称在 python 3.x 版本中变更为 configparser
import configparser

config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {"user":'hg'}
config['topsecret.server.com'] = {}
config['topsecret.server.com']={'Host Port':'50022',
                                'ForwardX11':'no'
                                }
config['DEFAULT']['ForwardX11'] = 'yes'

with open('example.ini', 'w') as configfile:
    config.write(configfile)

config.read('example.ini') #读取配置文件
print(config.sections()) #查看配置文件除默认值default以外的章节
print(config.defaults())#查看配置文件默认值default内容
print(config["bitbucket.org"]["user"])

for value in config: #有哪几个模块
    print(value)

for value in config['bitbucket.org']:
    print(value) #包含默认值

config.remove_section('bitbucket.org') #删除模块
config.remove_option("DEFAULT","Compression") #删除键值对
config.set("DEFAULT",'CompressionLevel','2') #把其中一个模块的键值对的值改变
print(config.has_section('bitbucket.org')) #判断是否还有该模块
config.write(open("changeee.ini","w")) #其实都是覆盖写的过程

