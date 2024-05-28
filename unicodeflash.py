import tkinter as tk
from tkinter import filedialog
import pygame
import pygame.mixer
from tkinter import messagebox
import os
import sys
def start():
    def open_file_dialog():
        filename = filedialog.askopenfilename(filetypes=[("字体文件", ("*.ttf", "*.ttc", "*.TTF", "*.otf"))])
        tkb2.config(text=filename)
    button1.destroy()
    frame = tk.Frame(root)
    global tkb2
    global tkb4
    global tkb6
    global tkb8
    global tkb9
    global tkb11
    frame.place(relx=0.5, rely=0.5, anchor="center")  
    tkb0 = tk.Label(frame, text="设置选项")  
    tkb0.grid(row=0, column=2)   
    tkb05 = tk.Label(frame,text="默认黑体，白背景，大小占屏幕一半，帧数为1")
    tkb05.grid(row=1,column=2)
    tkb1 = tk.Label(frame, text="选择字体：")  
    tkb1.grid(row=2, column=1, sticky="ew") 
    tkb2 = tk.Button(frame, text="选择文件",command=open_file_dialog)  
    tkb2.grid(row=2, column=2)
    tkb3 = tk.Label(frame, text="选择背景色：")  
    tkb3.grid(row=3, column=1, sticky="ew")
    tkb4 = tk.Entry(frame, width=7)  
    tkb4.grid(row=3, column=2)
    tkb5 = tk.Label(frame, text="文字大小：")  
    tkb5.grid(row=4, column=1, sticky="ew")
    tkb6 = tk.Entry(frame,width=6)  
    tkb6.grid(row=4, column=2)
    tkb7 = tk.Label(frame, text="字符范畴：")  
    tkb7.grid(row=5, column=1, sticky="ew")
    tkb8 = tk.Entry(frame,width=6)  
    tkb8.grid(row=5, column=2)
    tkb9 = tk.Entry(frame,width=6)  
    tkb9.grid(row=5, column=3)
    tkb10 = tk.Label(frame, text="帧数：")  
    tkb10.grid(row=6, column=1, sticky="ew")
    tkb11 = tk.Entry(frame,width=6)  
    tkb11.grid(row=6, column=2)
    tkb12 = tk.Button(frame, text="开始",command=playing)  
    tkb12.grid(row=7, column=2)
def playing():
    gtkb2 = tkb2["text"]
    gtkb4 = tkb4.get()  
    gtkb6 = tkb6.get()  
    gtkb8 = tkb8.get() 
    gtkb9 = tkb9.get() 
    gtkb11 = tkb11.get()  
    try:  
        start = int(gtkb8, 16)  
        end = int(gtkb9, 16)  
        if start > end:  
            messagebox.showerror("错误", "起始码位必须小于或等于结束码位")  
            return  
        current_dir = os.getcwd()  
        filename = os.path.join(current_dir, "unicode生成.txt")    
        with open(filename, "w", encoding="utf-8") as f:  
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
    char_index=0  
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
        font_path="simhei.ttf"
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
        font = pygame.font.Font(font_path, font_size) 
        if char_index < len(characters):    
            font = pygame.font.Font(font_path, font_size)
            text = characters[char_index]  
            char_index += 1
        else:   
            text = ""
        text_surface = font.render(text, True, (0, 0, 0)) 
        text_rect = text_surface.get_rect() 
        text_rect.center = (width / 2, height / 2)
        screen.blit(text_surface, text_rect) 
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
root.geometry("400x300")
button1 = tk.Button(root, text="初始化设置",command=start)
button1.place(anchor="center",relx=0.5,rely=0.5)
root.mainloop()
