#UTF-8
'''
感谢：https://bing.ioliu.cn/      https://cn.bing.com/
源码：
禁止商用！
XW的网站:https://xwpython.gitee.io
Copyright © 2021 XW(TigGrak). All rights reserved.
'''




import sys,os,ctypes, sys,requests,argparse,re,shutil,subprocess

#感谢https://my.oschina.net/bluefly/blog/311209提供cmd变色解决方案。
##################################################################
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

# 字体颜色定义 ,关键在于颜色编码，由2位十六进制组成，分别取0~f，前一位指的是背景色，后一位指的是字体色
# 由于该函数的限制，应该是只有这16种，可以前景色与背景色组合。也可以几种颜色通过或运算组合，组合后还是在这16种颜色中

# Windows CMD命令行 字体颜色定义 text colors
FOREGROUND_BLACK = 0x00  # black.
FOREGROUND_DARKBLUE = 0x01  # dark blue.
FOREGROUND_DARKGREEN = 0x02  # dark green.
FOREGROUND_DARKSKYBLUE = 0x03  # dark skyblue.
FOREGROUND_DARKRED = 0x04  # dark red.
FOREGROUND_DARKPINK = 0x05  # dark pink.
FOREGROUND_DARKYELLOW = 0x06  # dark yellow.
FOREGROUND_DARKWHITE = 0x07  # dark white.
FOREGROUND_DARKGRAY = 0x08  # dark gray.
FOREGROUND_BLUE = 0x09  # blue.
FOREGROUND_GREEN = 0x0a  # green.
FOREGROUND_SKYBLUE = 0x0b  # skyblue.
FOREGROUND_RED = 0x0c  # red.
FOREGROUND_PINK = 0x0d  # pink.
FOREGROUND_YELLOW = 0x0e  # yellow.
FOREGROUND_WHITE = 0x0f  # white.

# Windows CMD命令行 背景颜色定义 background colors
BACKGROUND_BLUE = 0x10  # dark blue.
BACKGROUND_GREEN = 0x20  # dark green.
BACKGROUND_DARKSKYBLUE = 0x30  # dark skyblue.
BACKGROUND_DARKRED = 0x40  # dark red.
BACKGROUND_DARKPINK = 0x50  # dark pink.
BACKGROUND_DARKYELLOW = 0x60  # dark yellow.
BACKGROUND_DARKWHITE = 0x70  # dark white.
BACKGROUND_DARKGRAY = 0x80  # dark gray.
BACKGROUND_BLUE = 0x90  # blue.
BACKGROUND_GREEN = 0xa0  # green.
BACKGROUND_SKYBLUE = 0xb0  # skyblue.
BACKGROUND_RED = 0xc0  # red.
BACKGROUND_PINK = 0xd0  # pink.
BACKGROUND_YELLOW = 0xe0  # yellow.
BACKGROUND_WHITE = 0xf0  # white.

# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool


# reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)


###############################################################

# 暗蓝色
# dark blue
def printDarkBlue(mess):
    set_cmd_text_color(FOREGROUND_DARKBLUE)
    sys.stdout.write(mess)
    resetColor()


# 暗绿色
# dark green
def printDarkGreen(mess):
    set_cmd_text_color(FOREGROUND_DARKGREEN)
    sys.stdout.write(mess)
    resetColor()


# 暗天蓝色
# dark sky blue
def printDarkSkyBlue(mess):
    set_cmd_text_color(FOREGROUND_DARKSKYBLUE)
    sys.stdout.write(mess)
    resetColor()


# 暗红色
# dark red
def printDarkRed(mess):
    set_cmd_text_color(FOREGROUND_DARKRED)
    sys.stdout.write(mess)
    resetColor()


# 暗粉红色
# dark pink
def printDarkPink(mess):
    set_cmd_text_color(FOREGROUND_DARKPINK)
    sys.stdout.write(mess)
    resetColor()


# 暗黄色
# dark yellow
def printDarkYellow(mess):
    set_cmd_text_color(FOREGROUND_DARKYELLOW)
    sys.stdout.write(mess)
    resetColor()


# 暗白色
# dark white
def printDarkWhite(mess):
    set_cmd_text_color(FOREGROUND_DARKWHITE)
    sys.stdout.write(mess)
    resetColor()


# 暗灰色
# dark gray
def printDarkGray(mess):
    set_cmd_text_color(FOREGROUND_DARKGRAY)
    sys.stdout.write(mess)
    resetColor()


# 蓝色
# blue
def printBlue(mess):
    set_cmd_text_color(FOREGROUND_BLUE)
    sys.stdout.write(mess)
    resetColor()


# 绿色
# green
def printGreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess)
    resetColor()


# 天蓝色
# sky blue
def printSkyBlue(mess):
    set_cmd_text_color(FOREGROUND_SKYBLUE)
    sys.stdout.write(mess)
    resetColor()


# 红色
# red
def printRed(mess):
    set_cmd_text_color(FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()


# 粉红色
# pink
def printPink(mess):
    set_cmd_text_color(FOREGROUND_PINK)
    sys.stdout.write(mess)
    resetColor()


# 黄色
# yellow
def printYellow(mess):
    set_cmd_text_color(FOREGROUND_YELLOW)
    sys.stdout.write(mess)
    resetColor()


# 白色
# white
def printWhite(mess):
    set_cmd_text_color(FOREGROUND_WHITE)
    sys.stdout.write(mess)
    resetColor()


##################################################

# 白底黑字
# white bkground and black text
def printWhiteBlack(mess):
    set_cmd_text_color(FOREGROUND_BLACK | BACKGROUND_WHITE)
    sys.stdout.write(mess)
    resetColor()


# 白底黑字
# white bkground and black text
def printWhiteBlack_2(mess):
    set_cmd_text_color(0xf0)
    sys.stdout.write(mess)
    resetColor()


# 黄底蓝字
# white bkground and black text
def printYellowRed(mess):
    set_cmd_text_color(BACKGROUND_YELLOW | FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()


'''
if __name__ == '__main__':
    print(sys.path)
    printDarkBlue(u'printDarkBlue:暗蓝色文字\n')
    printDarkGreen(u'printDarkGreen:暗绿色文字\n')
    printDarkSkyBlue(u'printDarkSkyBlue:暗天蓝色文字\n')
    printDarkRed(u'printDarkRed:暗红色文字\n')
    printDarkPink(u'printDarkPink:暗粉红色文字\n')
    printDarkYellow(u'printDarkYellow:暗黄色文字\n')
    printDarkWhite(u'printDarkWhite:暗白色文字\n')
    printDarkGray(u'printDarkGray:暗灰色文字\n')
    printBlue(u'printBlue:蓝色文字\n')
    printGreen(u'printGreen:绿色文字\n')
    printSkyBlue(u'printSkyBlue:天蓝色文字\n')
    printRed(u'printRed:红色文字\n')
    printPink(u'printPink:粉红色文字\n')
    printYellow(u'printYellow:黄色文字\n')
    printWhite(u'printWhite:白色文字\n')

    printWhiteBlack(u'printWhiteBlack:白底黑字输出\n')
    printWhiteBlack_2(u'printWhiteBlack_2:白底黑字输出（直接传入16进制参数）\n')
    printYellowRed('printYellowRed:黄底红字输出\n')
'''
##################################################################






headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
} #其实不要也行的，以防万一吧2333



class Image():
    imageAll = []



class App():
    model='exe'
    verson = 'v2.0.0'
    laVerson = ''
    autoUpgradeLink = ''
    newExeName = ''
    Vcode = 2
    newVcode = None
    mustcode = None
    #checkAppLink = 'http://192.168.2.103:666/info'
    checkAppLink = 'https://xwpython.gitee.io/project/bimage/info'



def getAppInfo():
    #删除upgrade.bat
    if os.path.isfile("upgrade.bat"):
        os.remove("upgrade.bat")
    #获取软件信息
    try:
        response = requests.get(App.checkAppLink, headers=headers).json()
    except:
        printRed('无法获取软件状态，请退出重试。\n')
        input()

    App.autoUpgradeLink = response['update']['autourl']
    App.newExeName = response['update']['exename']
    App.laVerson = response['update']['verson']
    App.newVcode = response['update']['newVcode']
    App.mustcode = response['update']['mustcode']

    #检查可用性
    if response['status']['able'] == "True":
        pass

    else:
        printRed('无法使用,报错:'+response['status']['message']+'  请按回车退出。\n')
        input()
        sys.exit()

    if App.laVerson != App.verson:#对比版本号
        upIntroduce(response['update']['url'], response['update']['message'], response['update']['able'])
        return
    else:
        printGreen('当前是最新版本\n当前版本号：' + App.verson + '\n')
        return


def upIntroduce(url,mess,able):
    printGreen('软件有可用更新！\n')
    printDarkSkyBlue('当前版本：'+App.verson+'\n')
    printSkyBlue('最新版本：'+App.laVerson+'\n')
    printYellow('内容:'+mess+'\n')
    printGreen('以下为下载链接:\n')
    num = 1
    for i in url:
        print(str(num)+'：'+i+'\n')
        num+=1

    if App.newVcode - App.Vcode >= App.mustcode and not (App.mustcode == 0):
        printRed('当前版本过于老旧，将不再允许使用，请手动更新或输入小写y自动更新，（py文件无法自动下载）否则退出。\n')
        answer = input('>>>')
        if answer == 'y':
            updater()
        else:
            sys.exit()

    elif able == 'True':
        printBlue('您可以选择手动更新或输入小写y自动更新。（py文件无法自动下载）\n')
        answer = input('>>>')
        if App.model != 'exe':
            if answer == 'y':
                updater()
            else:
                return
    else:
        printRed('本程序将不再允许使用，请手动更新或输入小写y自动更新，（py文件无法自动下载）否则退出。\n')
        answer = input('>>>')
        if answer == 'y':
            updater()
        else:
            sys.exit()




def writeUpgradeCmd(exe_name,exepath):
    b = open("upgrade.bat",'w')
    TempList = "@echo off\n";   #关闭bat脚本的输出
    TempList += "if not exist "+exepath+" exit \n";    #新文件不存在,退出脚本执行
    TempList += "choice /t 3 /d y /n >nul\n" #3秒后删除旧程序（3秒后程序已运行结束，不延时的话，会提示被占用，无法删除）
    TempList += "del "+ sys.argv[0] + "\n"    #删除当前文件
    TempList += "move "+exepath+' '+os.getcwd()+'\n'
    TempList += "choice /t 1 /d y /n >nul\n"
    TempList += "start " + exe_name     #启动新程序
    b.write(TempList)
    b.close()
    subprocess.Popen("upgrade.bat")
    sys.exit()

def updater():
    #检查更新文件是否存在，没有则创建
    exepath = os.getcwd()+r'\update\BI.exe'
    print(exepath)
    if not os.path.isdir('./update'):
        #shutil.rmtree('./update')
        os.makedirs('./update')
    printYellow('下载更新\n')
    try:
        #下载新程序
        newapp = requests.get(App.autoUpgradeLink, headers=headers)
        with open('./update/BI.exe','wb') as f:
            f.write(newapp.content)

    except:
        printRed('下载更新失败，请关闭软件重试或尝试手动下载。\n')
        input()
    writeUpgradeCmd(App.newExeName, exepath)








def getTodayImageInfo():
    try:
        response = requests.get("https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1").json()  # 请求官方接口
        date = response['images'][0]['enddate']
        url = response['images'][0]['url']
        url = url.split('&')[0]
        url = url.replace('1920x1080','UHD')
        url = "https://cn.bing.com" + url
        info = response['images'][0]['copyright']
        all = [date,url,info]
        return all
    except:
        printRed('获取信息失败,请重试或请联系作者，请按回车退出。\n')
        input()
        sys.exit()


def downloadImage(url,info,date):
    try:
        printYellow('下载中...(文件较大，时间较久，请耐心等待。\n)')

        response = requests.get(url,headers=headers)
        img = response.content
        with open('./'+date+'.jpg', 'wb') as f:
            f.write(img)
        with open('./'+date+'.txt', 'w',encoding='UTF-8') as f:
            f.write('介绍:'+info+'\n'+'图片日期：'+date+'\n'+'图片链接：'+url)
    except:
        print('下载失败,请重试或请联系作者，请按回车退出。')
        input()
        sys.exit()

def getImage():
    printGreen(Image.imageAll[0] + '（日期）的壁纸:' + Image.imageAll[2]+'\n')
    downloadImage(Image.imageAll[1], Image.imageAll[2], Image.imageAll[0])
    printGreen('下载完成！回车退出。\n')
    os.startfile(os.getcwd() + '/' + Image.imageAll[0] + '.txt')
    os.startfile(os.getcwd() + '/' + Image.imageAll[0] + '.jpg')
    input()
    sys.exit()

def getL_NImage(name):
    #获取图片信息
    try:
        response = requests.get("https://bing.ioliu.cn/photo/"+name,headers=headers).text
        info = re.findall(r'<p class="title">(.*)</p><p class="sub">', response)[0]
        # (?<=A).*?(?=B)
        info = info + re.findall(r'<p class="sub">(.*)</p><p class="calendari icon icon-calendar"><em class="t">', response)[0]
        date = re.findall(r'(?<=</p><p class="calendari icon icon-calendar"><em class="t">).*?(?=</em></p><p class=")', response)[0]
        date = date.split('-')
        date = date[0]+date[1]+date[2]
        url = 'https://cn.bing.com/th?id=OHR.'+name+'_UHD.jpg'
        #检查图片可用性
        bad = requests.get('https://cn.bing.com/th?id=OHR.DiwaliRangoli_ZH-_UHD.jpg', headers=headers).content#损坏的图片
        tr = requests.get(url, headers=headers).content#测试图片
        if bad == tr:
            printRed('无法找到高清图片，为您匹配1920x1080分辨率图片。\n')
            url = re.findall(r'(?<=data-progressive=").*?(?="></div>)', response)[0]

        Image.imageAll = [date, url, info]
        getImage()
    except:
        printRed('获取失败，按回车键退出。\n')
        input()
        sys.exit()

def about():
    printYellow('---关于---\n')
    printGreen('当前版本：'+App.verson+'\n')
    printSkyBlue('BI---一款超好用、简便的bing美图解析器\n')
    printPink('项目github:https://github.com/chinaxwredstone/bi\n')
    printYellow('XW的网站:https://xwpython.gitee.io\nCopyright © 2021 XW. All rights reserved.')






if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='感谢https://bing.ioliu.cn/\n\n源码：\n禁止商用！\nXW的网站:https://xwpython.gitee.io\nCopyright © 2021 XW. All rights reserved. ')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-g',action='store_true',help='获取今天的bing壁纸')
    group.add_argument('-l',type=str,dest='link',help='https://bing.ioliu.cn/或官方链接解析成高清，但对古老的美图无效')
    group.add_argument('-n',help='美图id解析成高清，但对古老的美图无效')
    group.add_argument('-ucheck', action='store_true', help='检查更新')
    group.add_argument('-about', action='store_true', help='关于')
    args = parser.parse_args()
    # 打印参数空间中的变量
    # 打印针对这个添加参数模块的使用方法
    # 打印针对这个添加参数模块的使用帮助说明（此处会打印出使用方法）
    Image.imageAll = getTodayImageInfo()
    #printYellow('获取中...\n')

    #printBlue('今天（' + Image.imageAll[0] + ')的壁纸:' + Image.imageAll[2]+'\n\n')

    if args.g:
        getImage()

    elif args.link:
        getAppInfo()
        if args.link[0:28]=='https://bing.ioliu.cn/photo/':
            name = args.link[28:len(args.link)]
            name = name.split('?')[0]
            getL_NImage(name)
        elif args.link[0:30]=='https://cn.bing.com/th?id=OHR.':
            name = args.link.split('&')[0]
            name = name.replace('https://cn.bing.com/th?id=OHR.','')
            name = name.replace('_UHD.jpg','')
            getL_NImage(name)

        else:
            printRed('网址不合法，按回车键退出。\n')
            input()
            sys.exit()
    elif args.n:
        getAppInfo()
        getL_NImage(args.n)

    elif args.about:
        about()

    elif args.ucheck:
        getAppInfo()

    else:
        parser.print_help()
        getAppInfo()
        printBlue('今天（' + Image.imageAll[0] + ')的壁纸:' + Image.imageAll[2] + '\n\n')
        printYellow('添加到path更好用！\n')
        printYellow('输入小写y获取今日壁纸，否则退出。\n')
        answer = input('>>>')
        if answer == 'y':
            getImage()
        else:
            sys.exit()

        #python index.py -l https://bing.ioliu.cn/photo/DiwaliRangoli_ZH-CN0293298599?force=home_1
        #python index.py -l https://cn.bing.com/th?id=OHR.Dromling_ZH-CN0730577626_UHD.jpg&rf=LaDigue_UHD.jpg&pid=hp&w=1920&h=1080&rs=1&c=4
        #python index.py -n DiwaliRangoli_ZH-CN0293298599
        #python index.py -g
        #https://cn.bing.com/th?id=OHR.Dromling_ZH-CN0730577626_UHD.jpg&rf=LaDigue_UHD.jpg&pid=hp&w=1920&h=1080&rs=1&c=4







