# Unicode快闪懒人版
Unicode快闪，但是懒人版！<br/>

受到[Losketch](https://github.com/Losketch/Unicode-Flash-Mob)的[Unicode快闪生成器](https://github.com/Losketch/Unicode-Flash-Mob) 启发制作的Python代码，由学过基础Python的我，聪明的文心一言、和擅长补救的ChatGPT和Copy Copilot编写而成<br/>
相比于Losketch佬和[涂蜡锈蚀双切制铜台阶](https://space.bilibili.com/2004298532)的[Unicode快闪生成器](https://gitee.com/golllllll/unicode-flash-generator)，本代码更注重于简单粗暴轻量化，只需**一个**py文件和一些点缀的文件（图标、音乐和字体）<del>以及几个前置库</del>组成，内有用Tkinter库制作的UI界面方便设置参数，前面两者使用的快闪生成器均采用图片自动拼接的方式制作视频，而本代码使用的是<del>万能的</del>Pygame库直接在页面上以指定的帧数显示字符，你所需要的只是一个简单的60帧录屏软件（如OBS）设置好倒计时，等倒计时结束，快闪就会开始实时生成。
<br/>
## 当前版本运行环境:
- Python3.10<br/>
## 主要的<del>前置模组</del>前置库：
- tkinker————内置库，用于显示UI；
- fonttools————用于一键生成字符；
- pygame————代码核心，用于生成快闪的界面；
- [unicode_charnames](https://github.com/mlodewijck/unicode_charnames)————用于显示这个字符在Unicode中的英文名称；
- [unidata_blocks](https://github.com/TakWolf/unidata-blocks)————用于显示字符所在区块，由国人制作，自带中文（赞）；<br/>
其中pygame、unicode_charnames、unidata_blocks需要使用pip安装第三方库，如需打包成exe，请手动把unicode_charnames和unidata_blocks打包到exe里。
## 上传版本须知：
由于Github本身有一定的限制，所以有关当前版本和上传版本的内容会和百度网盘版有所偏差：
- <del>快闪小曲音质为40kbps，百度网盘的音质为128kbps，这是因为Github无法上传太大的文件，源文件的音乐大小高达70MB，塞不了，被迫压缩，后面会想办法使用外置音乐播放（多此一举了属于是）</del>
- 已使用Gitbush上传正常音质的另外打包了一份，如果使用旧版请手动下载音乐文件，不想再重新打包一遍了_(:з」∠)_
## 当前支持的可视化选项：
- ttf、ttc、otf文件选择
- 字体文件一键输出（部分字体文件有夹带字母符号或私用区，可能导致排序混乱）
- 背景色（6位16进制编码）
- 屏幕分辨率
- 文字大小
- 字符范畴（和追加模式，用于跨区块显示）
- 帧数（B站60帧要开大会员才能看的咧）
- 预留时间（防止录屏软件没反应过来漏露了几个字符）
- 多字体模式（支持一键生成字符和自定义范畴，带追加模式）
## 接下来的计划
- 增加快捷填写特定区块范畴的功能（可能又得借助某些库的力量）
- 在程序内打开生成的文本文件，无需在外面点开文件
## 其他
如有出现小bug的情况请在我的b站账号上反馈，如果有推荐的py第三方库（可在Pypi官网正常安装的那种）请在这里反馈。
百度网盘链接：https://pan.baidu.com/s/1W9U2GM8Io1oEPGDBCabbQg，提取码：code
