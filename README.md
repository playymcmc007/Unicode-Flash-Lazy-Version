# Unicode快闪懒人版
Unicode快闪，但是懒人版<br/>
页面施工中……刚开始用Github<br/>
受到[Losketch](https://github.com/Losketch/Unicode-Flash-Mob)的[Unicode快闪生成器](https://github.com/Losketch/Unicode-Flash-Mob) 启发制作的Python代码，由学过基础Python的我，聪明的文心一言、和擅长补救的ChatGPT和Copy Copilot编写而成<br/>
相比于Losketch佬和[涂蜡锈蚀双切制铜台阶](https://space.bilibili.com/2004298532)的[Unicode快闪生成器](https://gitee.com/golllllll/unicode-flash-generator)，本代码更注重于简单粗暴轻量化，只需**一个**py文件和一些点缀的文件（图标、音乐和字体）<del>以及几个前置库</del>组成，内有用Tkinter库制作的UI界面方便设置参数，前面两者使用的快闪生成器均采用图片自动拼接的方式制作视频，而本代码使用的是<del>万能的</del>Pygame库直接在页面上以指定的帧数显示字符，你所需要的只是一个简单的60帧录屏软件（如OBS屏）设置好倒计时，等倒计时结束，快闪就会开始实时生成。
<br/>
## 当前版本运行环境:
- Python3.10<br/>
## 主要的<del>前置模组</del>前置库：
- tkinker————内置库，用于显示UI
- pygame————代码核心，用于生成快闪的界面
- [unicode_charnames](https://github.com/mlodewijck/unicode_charnames)————用于显示这个字符在Unicode中的英文名称
- [unidata_blocks](https://github.com/TakWolf/unidata-blocks)————用于显示字符所在区块，由国人制作，自带中文（赞）
其中pygame、unicode_charnames、unidata_blocks需要使用pip安装第三方库

当你看到这段话的时候说明这个项目还没上传完（
