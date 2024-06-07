import tkinter as tk
from tkinter import filedialog,Toplevel
import pygame
import pygame.mixer
from tkinter import messagebox
import os #用于定位文件
import sys #用于确保软件关闭（多加一层保险）
from unicode_charnames import charname#用于显示字符名称，内置库unicodedata最新版本不支持Unicode15.1，得用第三方库
import unidata_blocks #用于显示区块名称，国人做的库，里面还有中文支持
import re #用于解析正则表达式
from fontTools.ttLib import TTFont #用于输出字体内支持的文字
#pygame、unicode_charnames、unidata_blocks需要用pip第三方安装，安装方法上网找教程
#本程序需要python3.10及以上才可以兼容（3.10以下安装库会失败）
def start():
    button1.destroy()
    def limit_text_length(text, max_length):#限制字数，防止选中文字太多导致窗口被占满
        if len(text) > max_length:
            text = text[:max_length-3] + "..."
        return text
    def open_file_dialog():  
        filename = filedialog.askopenfilename(filetypes=[("字体文件", ("*.ttf", "*.ttc", "*.TTF", "*.otf",))])  
        selected_font_path.append(filename)
        tkb2.config(text=filename)
        print(filename)
    def open_file_dialogs():
        global filenames
        filenames = filedialog.askopenfilenames(filetypes=[("字体文件", ("*.ttf", "*.ttc", "*.TTF", "*.otf",))])    
        if filenames: 
            selected_font_paths.extend(filenames)
            tka6.config(text=limit_text_length("已选择字体：" + ", ".join(filenames), 500))
        print(filenames)
    def open_file_dialogx():
        global filenamex
        filenamex = filedialog.askopenfilename(filetypes=[("字体文件", ("*.ttf", "*.ttc", "*.TTF", "*.otf",))])
        tkb8.config(text=filenamex)
        print(filenamex)
    def to_print_support_font(): #中转到print_support_font函数 
        for font_path in selected_font_path:  
            print_support_font(font_path)
    def to_print_support_fonts(): #中转到print_support_font函数 
        for font_path in selected_font_paths:  
            print_support_fonts(font_path)
    def toggle_append_mode():
        global append_mode 
        append_mode = not append_mode  
        print("追加模式:", append_mode) #默认关闭，开启后就会变成在原文本后面再追加内容
    def false_append_mode():
        global append_mode 
        append_mode = False  
        print("追加模式已归位为", append_mode)
    def print_support_font(font_path, start=0, end=0x10FFFF):  #一键输出字体内支持的文字 
        font = TTFont(font_path)
        cmap = font.getBestCmap()  
        supported_chars = set()  
        for code in range(start, end + 1):  
            if code in cmap:  
                supported_chars.add(chr(code))    
        with open('Unicode生成.txt', 'w', encoding='utf-8') as f:  
            for char in sorted(supported_chars):
                if 0xD800 <= code <= 0xDFFF: 
                    continue    
                f.write(char) 
    def print_support_fonts(font_path, start=0, end=0x10FFFF):  #一键输出选定字体内支持的文字并输出为多个文件
        font = TTFont(font_path)  
        cmap = font.getBestCmap()    
        supported_chars = set()    
        for code in range(start, end + 1):    
            if code in cmap:    
                supported_chars.add(chr(code))  
        with open(f'字符输出_{font_path.rsplit("/", 1)[-1].rsplit(".", 1)[0]}.txt', 'w', encoding='utf-8') as f: 
            f.write(font_path+"\n") 
            for char in sorted(supported_chars):    
                f.write(char)
    def delete_fontfiles(): #删除文件以进行下一轮的生成准备
        text_files = [f for f in os.listdir('.') if f.endswith('.txt') and f.startswith('字符输出')]#标识文字，避免误伤单字体用的文件，之后的匹配文字同理
        for file in text_files:
            os.remove(file)
    def unicode_write(): #用于多文本模式挨个生成文件
        gtka11=tka11.get()
        gtka12=tka12.get()
        try:  
            start = int(gtka11, 16)  
            end = int(gtka12, 16)  
            if start > end:  
                messagebox.showerror("错误", "起始码位必须小于或等于结束码位！")  
                return
            try:
                if append_mode == False:
                    with open(f'字符输出_{filenamex.rsplit("/", 1)[-1].rsplit(".", 1)[0]}.txt', "w", encoding="utf-8") as f:  
                        f.write(filenamex+"\n") 
                        for code in range(start, end + 1):  
                            if 0xD800 <= code <= 0xDFFF: 
                                continue  
                            char = chr(code)  
                            f.write(char)
                filename_check = f'字符输出_{filenamex.rsplit("/", 1)[-1].rsplit(".", 1)[0]}.txt'
                if append_mode == True and os.path.exists(filename_check):
                    with open(f'字符输出_{filenamex.rsplit("/", 1)[-1].rsplit(".", 1)[0]}.txt', "a", encoding="utf-8") as f:  
                        for code in range(start, end + 1):  
                            if 0xD800 <= code <= 0xDFFF: 
                                continue  
                            char = chr(code)  
                            f.write(char)
            except NameError:
                messagebox.showerror("错误", "尚未选择文件！")   
        except ValueError:  
            messagebox.showerror("错误", "格式错误！")      
    def fonts(): 
        global tka6,tka11,tka12
        root.withdraw()
        fontsui=Toplevel(root)
        fontsui.title("Unicode快闪懒人版——多字体选项")
        fontsui.iconbitmap('favicon.ico') 
        fontsui.geometry("800x600")
        frame2 = tk.Frame(fontsui)
        frame2.place(relx=0.5, rely=0.5, anchor="center")
        tka1 = tk.Label(frame2, text="选择多个字体设置")
        tka1.grid(row=0,column=1)
        tkas =  tk.Label(frame2,text="一键输出多个字体内的所有字符并在主菜单内通过按钮运行，\n由于部分字体会夹带私用区或重复字符，\n生成后请检查一下重复生成的部分（如数字和字母）和私用区检查，\n如果想要不出现不需要多余的字符，请使用普通的自定义字符范畴。\n在生成文件之前请提前为字体文件用字母或其他方式排序，\n否则很有可能会导致顺序错乱。")
        tkas.grid(row=1,column=1)
        tka2 = tk.Label(frame2,text = "选择多个字体")
        tka2.grid(row=2,column=0)
        tka3 = tk.Button(frame2,text="选择文件",command=open_file_dialogs)
        tka3.grid(row=2, column=1)
        tka4 = tk.Button(frame2,text="一键生成多份字体字符",command=to_print_support_fonts)
        tka4.grid(row=2,column=2)
        tka5 = tk.Button(frame2,text="一键删除所有字体字符",command=delete_fontfiles)
        tka5.grid(row=2,column=3)
        tka6 = tk.Label(frame2,text="未选择文件", wraplength=400)
        tka6.grid(row=3,column=1)
        tka7 = tk.Label(frame2,text="选择单个字体")
        tka7.grid(row=4,column=1)
        tka8 = tk.Button(frame2,text="选择文件",command=open_file_dialogx)
        tka8.grid(row=5,column=1)
        tka9 = tk.Button(frame2,text="生成单个字体字符文件",command=unicode_write)
        tka9.grid(row=5,column=2)
        tka95= tk.Checkbutton(frame2,text="追加模式",command=toggle_append_mode)
        tka95.grid(row=5,column=3)
        tka10 = tk.Label(frame2,text="字符范畴")
        tka10.grid(row=5,column=0)
        tka11 = tk.Entry(frame2,width=6)
        tka11.grid(row=6,column=1)
        tka12 = tk.Entry(frame2,width=6)
        tka12.grid(row=6,column=2)
        fontsui.protocol("WM_DELETE_WINDOW", lambda: (root.deiconify(),fontsui.destroy(),false_append_mode())) 
        fontsui.mainloop
    frame = tk.Frame(root)
    global tkb2,tkb4,tkb6,tkb8,tkb9,tkb11,tkb13,tkbscreena,tkbscreenb
    frame.place(relx=0.5, rely=0.5, anchor="center")  
    tkb0 = tk.Label(frame, text="设置选项")  
    tkb0.grid(row=0, column=2)   
    tkb05 = tk.Label(frame,text="默认黑体，白背景，文字大小占屏幕一半，\n帧数为1，无预留时间，分辨率800x600")
    tkb05.grid(row=1,column=2)
    tkb1 = tk.Label(frame, text="选择字体：")  
    tkb1.grid(row=2, column=1, sticky="e") 
    tkb2 = tk.Button(frame, text="选择文件",command=open_file_dialog)  
    tkb2.grid(row=2, column=2)
    tkb25 = tk.Button(frame,text="一键导入支持字符",command=to_print_support_font)
    tkb25.grid(row=2,column=3)
    tkb3 = tk.Label(frame, text="选择背景色：")  
    tkb3.grid(row=3, column=1, sticky="e")
    tkb4 = tk.Entry(frame, width=7)
    tkb4.grid(row=3,column=2)
    tkbscreen1 = tk.Label(frame,text="屏幕分辨率：")
    tkbscreen1.grid(row=4,column=1)
    tkbscreena = tk.Entry(frame,width=4)
    tkbscreena.grid(row=4,column=2)
    tkbscreenb = tk.Entry(frame,width=4)
    tkbscreenb.grid(row=4,column=3)
    tkb5 = tk.Label(frame, text="文字大小：")  
    tkb5.grid(row=5, column=1, sticky="e")
    tkb6 = tk.Entry(frame,width=6)  
    tkb6.grid(row=5, column=2)
    tkb7 = tk.Label(frame, text="字符范畴：")  
    tkb7.grid(row=6, column=1, sticky="e")
    tkb8 = tk.Entry(frame,width=6)  
    tkb8.grid(row=6, column=2)
    tkb9 = tk.Entry(frame,width=6)  
    tkb9.grid(row=6, column=3)
    tkb95= tk.Checkbutton(frame,text="追加模式",command=toggle_append_mode)
    tkb95.grid(row=6,column=4)
    tkb10 = tk.Label(frame, text="帧数：")  
    tkb10.grid(row=7, column=1, sticky="e")
    tkb11 = tk.Entry(frame,width=6)  
    tkb11.grid(row=7, column=2)
    tkb12 = tk.Label(frame,text = "预留时间：")
    tkb12.grid(row=8,column=1, sticky="e")
    tkb13 = tk.Entry(frame,width=3)
    tkb13.grid(row=8,column=2)
    tkb14 = tk.Button(frame, text="开始（单字体模式）",command=playing1)  
    tkb14.grid(row=9, column=2)
    tkb15 = tk.Button(frame, text="开始（多字体模式）",command=playing2)  
    tkb15.grid(row=9, column=3)
    tkb16 = tk.Button(frame,text="多字体选项",command=fonts)
    tkb16.grid(row=9,column=1)
def playing1():
    gtkb2 = tkb2["text"]
    gtkb4 = tkb4.get()  
    gtkb6 = tkb6.get()  
    gtkb8 = tkb8.get() 
    gtkb9 = tkb9.get() 
    gtkb11 = tkb11.get()
    gtkb13 = tkb13.get()
    gtkbscreenb = tkbscreenb.get()
    gtkbscreena = tkbscreena.get() 
    try:  
        start = int(gtkb8, 16)  
        end = int(gtkb9, 16)  
        if start > end:  
            messagebox.showerror("错误", "起始码位必须小于或等于结束码位")  
            return 
        current_dir = os.getcwd()  
        filename = os.path.join(current_dir, "Unicode生成.txt") 
        mode = "a" if append_mode else "w"     
        with open(filename, mode, encoding="utf-8") as f:  
            for code in range(start, end + 1):  
                if 0xD800 <= code <= 0xDFFF: 
                    continue  
                char = chr(code)  
                f.write(char)   
    except ValueError:  
        pass  #如果格式不对，则按照之前储存的文本显示（如果有）
    try:
        with open('unicode生成.txt', 'r', encoding='utf-8') as file:  
            characters = list(file.read())
    except FileNotFoundError:
        messagebox.showerror("错误", "Unicode生成文件不存在！")
        return
    def hex_to_rgb(hex_color):  
        try:
            hex_color = hex_color.lstrip('#') 
            r = int(hex_color[0:2], 16)  
            g = int(hex_color[2:4], 16)  
            b = int(hex_color[4:6], 16)  
            return r, g, b
        except ValueError:
            messagebox.showerror("错误", "颜色代码必须是6个16进制字符")#因为是写在tkinter和pygame中央的函数，所以这个弹窗报错处理看上去有点磕碜
            sys.exit()#检测到颜色错误直接关闭程序
    root.destroy() 
    pygame.init()  
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")  
    pygame.mixer.music.play()
    icon = pygame.image.load("favicon.ico") 
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    try:
        if gtkb13:
            countdown = int(gtkb13)
        else:
            countdown=-1
    except ValueError:
        countdown=-1 #如果数字不合法则默认没有预留时间
    char_index=0  
    width = 800  
    height = 600
    try:
        if gtkbscreena:
            width = int(gtkbscreena)
        if gtkbscreenb:
            height = int(gtkbscreenb)
    except ValueError:
        width = 800
        height = 600
    screen = pygame.display.set_mode((width, height)) 
    pygame.display.set_caption("Unicode快闪懒人版")
    running = True  
    while running:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                running = False
        hex_color = "#FFFFFF"
        if gtkb4:
            hex_color = gtkb4 
        r, g, b = hex_to_rgb(hex_color)  
        screen.fill((r, g, b))
        font_path=None
        if gtkb2 != '选择文件':
            font_path=gtkb2
        font_size = int(float(min(width/2, height/2)))  #文字是屏幕的一半大小（并居于中央） 
        if gtkb6 :
            try:  
                font_size = int(float(gtkb6)) 
                if font_size <= 0:
                    font_size = int(float(min(width/2, height/2))) 
            except ValueError:  
                pass #如果数字不合法则按照默认大小显示
        font = pygame.font.Font("simhei.ttf", font_size)
        font2 = pygame.font.Font("simhei.ttf", int(width/25))
        font3 = pygame.font.Font("simhei.ttf", int(width/25)) 
        font4 = pygame.font.Font("simhei.ttf", int(width/25))
        while countdown > -1:
            screen.fill((r, g, b))
            text = str(countdown)
            text_surface1 = font.render(text, True, (0, 0, 0))
            text_rect1 = text_surface1.get_rect(center=(width // 2, height // 2))
            screen.blit(text_surface1, text_rect1) #倒计时显示，区分开原本的text防止代码冲突
            countdown -= 1
            pygame.display.flip()
            text_code =""
            text2 = ""
            pygame.time.delay(1000)#不知为何设置倒计时后会出现短暂黑屏，不过无伤大雅，后期剪掉就行，别把开头字符也剪了
        pattern1 = re.compile(r'<reserved-[0-9A-Fa-f]*>') #字符名库内“未定义”的格式
        pattern2 = re.compile(r'<noncharacter-[0-9A-Fa-f]*>') #字符名库内“不是符号”的格式
        if char_index < len(characters):    
            font = pygame.font.Font(font_path, font_size)
            text = characters[char_index]  
            char_index += 1 #循环检索下一个字符
            print(text)
            text_code = f"U+{hex(ord(text))[2:].upper().zfill(4)}" #字符转16进制格式，0x替换为U+
            print(text_code)
            text2 = charname(text) #显示字符名字
            print(text2)
            if pattern1.match(text2) or pattern2.match(text2):
                continue #检测到字符名字为库内未定义或不是符号的格式则跳过
            try:
                text3 = unidata_blocks.get_block_by_chr(text)
                print(text3.name_localized("zh")) #显示字符所在的区块中文译名（如果改为name则为英文）
            #except UnboundLocalError:
            #    text3 =None  #检测到不支持的区块跳过，不过代码改良后似乎没用了，算了放着就放着吧，万一又崩了呢
            except AttributeError:
                continue #检测到未定义的区块跳过
        else:   
            text = None
            text_code = None
            text2 = None
            text3 =None#检索结束将所有数值设为空，配合下面4个if使用
        try:
            text_surface1 = font.render(text, True, (0, 0, 0)) 
        except pygame.error:
            text_surface1 = font.render("", True, (0, 0, 0))  #给零宽字符一点尊严（指啥也不放）
        except ValueError:
            continue
        if text:
            text_rect1 = text_surface1.get_rect(center=(width // 2, height // 2))
            screen.blit(text_surface1, text_rect1) 
        if text_code:
            text_surface2 = font2.render(text_code, True, (0, 0, 0))
            text_rect2 = text_surface2.get_rect(bottomleft=(30, height*0.89))
            screen.blit(text_surface2, text_rect2)
        if text2:
            text_surface3 = font3.render(text2, True, (0, 0, 0))
            text_rect3 = text_surface3.get_rect(bottomleft=(30, height*0.94))
            screen.blit(text_surface3, text_rect3)
        if text3:
            text_surface4 = font4.render(text3.name_localized("zh"), True, (0, 0, 0))
            text_rect4 = text_surface4.get_rect(bottomleft=(30, height))
            screen.blit(text_surface4, text_rect4)
        pygame.display.flip()  
        frame = 1 #默认1帧
        try:  
            frame = int(gtkb11)  
            if frame <= 0: 
                frame = 1   
        except ValueError:  
            pass #如果帧数非法则按默认1帧
        clock.tick(frame)
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()
def playing2():#多字体模式，代码与前者相似，这部分是由ChatGPT和Code Copilot进行编写修改的，感谢这两位救了我的代码
    gtkb4 = tkb4.get()
    gtkb6 = tkb6.get()
    gtkb11 = tkb11.get()
    gtkb13 = tkb13.get()
    gtkbscreenb = tkbscreenb.get()
    gtkbscreena = tkbscreena.get()
    text_files = [f for f in os.listdir('.') if f.endswith('.txt') and f.startswith('字符输出')]#检索对应文件
    font_paths = []#路径
    characters = {}#字符组
    for text_file in text_files:
        with open(text_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if lines:
                font_path = lines[0].strip()
                font_paths.append(font_path)
                characters[font_path] = lines[1].strip()
    def hex_to_rgb(hex_color):
        try:
            hex_color = hex_color.lstrip('#')
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
            return r, g, b
        except ValueError:
            messagebox.showerror("错误", "颜色代码必须是6个16进制字符")
            sys.exit()
    root.destroy()
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()
    icon = pygame.image.load("favicon.ico")
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    try:
        if gtkb13:
            countdown = int(gtkb13)
        else:
            countdown = -1
    except ValueError:
        countdown = -1  # 如果数字不合法则默认没有预留时间
    char_index = 0
    file_index = 0
    width = 800
    height = 600
    try:
        if gtkbscreena:
            width = int(gtkbscreena)
        if gtkbscreenb:
            height = int(gtkbscreenb)
    except ValueError:
        width = 800
        height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Unicode快闪懒人版")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        hex_color = gtkb4 if gtkb4 else "#FFFFFF"
        r, g, b = hex_to_rgb(hex_color)
        screen.fill((r, g, b))
        font_size = int(float(min(width / 2, height / 2)))  # 文字是屏幕的一半大小（并居于中央）
        if gtkb6:
            try:
                font_size = int(float(gtkb6))
                if font_size <= 0:
                    font_size = int(float(min(width / 2, height / 2)))
            except ValueError:
                pass  # 如果数字不合法则按照默认大小显示
        font = pygame.font.Font("simhei.ttf", font_size)
        font2 = pygame.font.Font("simhei.ttf", int(width / 25))
        font3 = pygame.font.Font("simhei.ttf", int(width / 25))
        font4 = pygame.font.Font("simhei.ttf", int(width / 25))
        while countdown > -1:
            screen.fill((r, g, b))
            text = str(countdown)
            text_surface1 = font.render(text, True, (0, 0, 0))
            text_rect1 = text_surface1.get_rect(center=(width // 2, height // 2))
            screen.blit(text_surface1, text_rect1)
            countdown -= 1
            pygame.display.flip()
            text_code = ""
            text2 = ""
            pygame.time.delay(1000)
        pattern1 = re.compile(r'<reserved-[0-9A-Fa-f]*>')  # 字符名库内“未定义”的格式
        pattern2 = re.compile(r'<noncharacter-[0-9A-Fa-f]*>')  # 字符名库内“不是符号”的格式
        if file_index < len(font_paths):
            font_path = font_paths[file_index]
            if char_index < len(characters[font_path]):
                text = characters[font_path][char_index]
                char_index += 1
                print(text)
                text_code = f"U+{hex(ord(text))[2:].upper().zfill(4)}"  # 字符转16进制格式，0x替换为U+
                print(text_code)
                text2 = charname(text)  # 显示字符名字
                print(text2)
                if pattern1.match(text2) or pattern2.match(text2):
                    continue  # 检测到字符名字为库内未定义或不是符号的格式则跳过
                try:
                    text3 = unidata_blocks.get_block_by_chr(text)
                    print(text3.name_localized("zh"))  # 显示字符所在的区块中文译名（如果改为name则为英文）
                except AttributeError:
                    continue  # 检测到未定义的区块跳过
                font = pygame.font.Font(font_path, font_size)
                try:
                    text_surface1 = font.render(text, True, (0, 0, 0))
                except pygame.error:
                    text_surface1 = font.render("", True, (0, 0, 0))  # 给零宽字符一点尊严（指啥也不放）
                except ValueError:
                    continue #防止输出U+0000导致崩溃
                if text:
                    text_rect1 = text_surface1.get_rect(center=(width // 2, height // 2))
                    screen.blit(text_surface1, text_rect1)
                if text_code:
                    text_surface2 = font2.render(text_code, True, (0, 0, 0))
                    text_rect2 = text_surface2.get_rect(bottomleft=(30, height * 0.89))
                    screen.blit(text_surface2, text_rect2)
                if text2:
                    text_surface3 = font3.render(text2, True, (0, 0, 0))
                    text_rect3 = text_surface3.get_rect(bottomleft=(30, height * 0.94))
                    screen.blit(text_surface3, text_rect3)
                if text3:
                    text_surface4 = font4.render(text3.name_localized("zh"), True, (0, 0, 0))
                    text_rect4 = text_surface4.get_rect(bottomleft=(30, height))
                    screen.blit(text_surface4, text_rect4)
                pygame.display.flip()
                frame = 1  # 默认1帧
                try:
                    frame = int(gtkb11)
                    if frame <= 0:
                        frame = 1
                except ValueError:
                    pass  # 如果帧数非法则按默认1帧
                clock.tick(frame)
            else:
                # 当前文件字符显示完，重置字符索引并跳转到下一个文件
                char_index = 0
                file_index += 1
        else:
            text = None
            text_code = None
            text2 = None
            text3 = None  # 检索结束将所有数值设为空
            pygame.display.flip()
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()
root = tk.Tk()
root.title("Unicode快闪懒人版")
root.iconbitmap('favicon.ico') 
root.geometry("800x600")
button1 = tk.Button(root, text="初始化设置",command=start)
button1.place(anchor="center",relx=0.5,rely=0.5)#初始化按钮，理论上可以省掉直接进入设置，但是感觉按下去更有打开设置的感觉
append_mode = False #追加模式默认为False（未开启）
selected_font_path = []
selected_font_paths = [] 
root.mainloop()