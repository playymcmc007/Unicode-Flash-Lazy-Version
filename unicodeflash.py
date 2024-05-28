import tkinter as tk
from tkinter import filedialog
import pygame
import pygame.mixer
from tkinter import messagebox
import os
import sys
import time
import unicodedata
def start():
    def open_file_dialog():
        filename = filedialog.askopenfilenames(filetypes=[("字体文件", ("*.ttf", "*.ttc", "*.TTF", "*.otf"))])
        tkb2.config(text=filename)
    button1.destroy()
    def toggle_append_mode():
        global append_mode 
        append_mode = not append_mode  
        print("追加模式:", append_mode)
    frame = tk.Frame(root)
    global tkb2
    global tkb4
    global tkb6
    global tkb8
    global tkb9
    global tkb11
    global tkb13
    global tkbscreena
    global tkbscreenb
    frame.place(relx=0.5, rely=0.5, anchor="center")  
    tkb0 = tk.Label(frame, text="设置选项")  
    tkb0.grid(row=0, column=2)   
    tkb05 = tk.Label(frame,text="默认黑体，白背景，文字大小占屏幕一半，\n帧数为1，无预留时间，分辨率800x600")
    tkb05.grid(row=1,column=2)
    tkb1 = tk.Label(frame, text="选择字体：")  
    tkb1.grid(row=2, column=1, sticky="e") 
    tkb2 = tk.Button(frame, text="选择文件",command=open_file_dialog)  
    tkb2.grid(row=2, column=2)
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
    tkb14 = tk.Button(frame, text="开始",command=playing)  
    tkb14.grid(row=9, column=2)
def playing():
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
        filename = os.path.join(current_dir, "unicode生成.txt") 
        mode = "a" if append_mode else "w"     
        with open(filename, mode, encoding="utf-8") as f:  
            for code in range(start, end + 1):  
                if 0xD800 <= code <= 0xDFFF: 
                    continue  
                char = chr(code)  
                f.write(char)   
    except ValueError:  
        pass  
    root.destroy() 
    with open('unicode生成.txt', 'r', encoding='utf-8') as file:  
        characters = list(file.read())
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
    pygame.init()  
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")  
    pygame.mixer.music.play()
    icon = pygame.image.load("favicon.ico") 
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    try:
        if gtkb13:
            countdown = int(gtkb13)
        else:
            countdown=-1
    except ValueError:
        countdown=-1
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
        font_size = int(float(min(width/2, height/2)))   
        if gtkb6 :
            try:  
                font_size = int(float(gtkb6)) 
                if font_size <= 0:
                    font_size = int(float(min(width/2, height/2))) 
            except ValueError:  
                pass
        font = pygame.font.Font("simhei.ttf", font_size)
        font2 = pygame.font.Font("simhei.ttf", 25)
        font3 = pygame.font.Font("simhei.ttf", 25) 
        if countdown > -1:
            text = str(countdown)
            text_code =""
            text2 = ""
            countdown -= 1
            time.sleep(1)
            #这里用tick暂停不准，得用time.sleep
            #不知为何设置倒计时后会出现短暂黑屏，不过无伤大雅，后期剪掉就行，别把开头字符也剪了
        else:
            try:
                if char_index < len(characters):    
                    font = pygame.font.Font(font_path, font_size)
                    text = characters[char_index]  
                    char_index += 1
                    text_code = f"U+{hex(ord(text))[2:].upper().zfill(4)}"
                    text2 = unicodedata.name(text)
                    print(text)
                    print(text_code)
                    print(text2)
                else:   
                    text = ""
            except ValueError:
                errortext = text
                text = "不存在"
                text2 = "不存在或python版本不支持（暂不支持CJK扩展I区）"
                text_code = f"U+{hex(ord(errortext))[2:].upper().zfill(4)}"
                print(text)
                print(text_code)
                print(text2)


                text_surface1 = font.render(text, True, (0, 0, 0))
                text_rect1 = text_surface1.get_rect(center=(width // 2, height // 2))
                text_surface2 = font2.render(text_code, True, (0, 0, 0))
                text_rect2 = text_surface2.get_rect(bottomleft=(40, height - 40))
                text_surface3 = font3.render(text2, True, (0, 0, 0))
                text_rect3 = text_surface3.get_rect(bottomleft=(40, height))
                screen.blit(text_surface1, text_rect1) 
                screen.blit(text_surface2, text_rect2)
                screen.blit(text_surface3, text_rect3)
                pass
        try:
            text_surface1 = font.render(text, True, (0, 0, 0)) 
        except pygame.error:
            pass
        text_rect1 = text_surface1.get_rect(center=(width // 2, height // 2))
        text_surface2 = font2.render(text_code, True, (0, 0, 0))
        text_rect2 = text_surface2.get_rect(bottomleft=(40, height - 40))
        text_surface3 = font3.render(text2, True, (0, 0, 0))
        text_rect3 = text_surface3.get_rect(bottomleft=(40, height))
        screen.blit(text_surface1, text_rect1) 
        screen.blit(text_surface2, text_rect2)
        screen.blit(text_surface3, text_rect3)
        pygame.display.flip()  
        frame = 1
        try:  
            frame = int(gtkb11)  
            if frame <= 0: 
                frame = 1   
        except ValueError:  
            pass
        clock.tick(frame)
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()
root = tk.Tk()
root.title("Unicode快闪懒人版")
root.iconbitmap('favicon.ico') 
root.geometry("800x600")
button1 = tk.Button(root, text="初始化设置",command=start)
button1.place(anchor="center",relx=0.5,rely=0.5)
append_mode = False 
root.mainloop()
