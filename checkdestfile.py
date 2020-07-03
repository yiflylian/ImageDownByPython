import  os
'输出目标目录下所有文件 默认当前目录'
def getdestdirallfile(destidr='.'):
    return os.listdir('.')

def checkdestdir(destdir,currdir='.'):
    if not destdir in os.listdir(currdir):
        os.mkdir(os.path.join(currdir,destdir))

