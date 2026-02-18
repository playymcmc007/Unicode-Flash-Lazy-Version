import tkinter as tk
from tkinter import ttk, filedialog, Toplevel, messagebox
import pygame
import pygame.mixer
import os #用于定位文件
import sys #用于确保软件关闭（多加一层保险）
from unicodedata2 import name #用于显示字符名称，内置库unicodedata最新版本随python一起更新，得用第三方库，名字没有高亮属于正常现象，无视即可
from unicode_charnames import charname #用于显示字符名称，备用防止报错，unicodedata2没有对特殊字符做处理，遇到就报错
from unidata_blocks import get_blocks,get_block_by_chr #用于显示区块名称和获取各区块范围，国人做的库，里面还有中文支持
import re #用于解析正则表达式
from fontTools.ttLib import TTFont #用于输出字体内支持的文字
from easyfont import getfont  #用于使用NotoSansSC字体
import base64 #用于图标base64解码
from tempfile import NamedTemporaryFile #用于清除图标缓存
from io import BytesIO #用于提前为pygame加载图标
#pygame、unicodedata2、unicode_charnames、unidata_blocks、easyfont需要用pip第三方安装，安装方法上网找教程
#本程序需要python3.10及以上才可以兼容（3.10以下安装库会失败）
unicode_icon_base64="""AAABAAIAEBAAAAEAIABoBAAAJgAAACAgAAABACAAqBAAAI4EAAAoAAAAEAAAACAAAAABACAAAAAAAAAEAAATCwAAEwsAAAAAAAAAAAAA/1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1ZW//9XV///Vlb//1ZW//9XV///Vlb//1VV//9VVf//VVX//1VV//9XV///V1f//1VV//9VVf//VVX//1ZW//9UVP//Skr//05O//9PT///SUn//1FR//9WVv//VVX//1VV//9UVP//TEz//01N//9TU///VVX//1ZW//9TU///WVn//56e///Ozv//1NT//7Gx//9oaP//UFD//1dX//9UVP//WVn//7Ky//++vv//aGj//1FR//9WVv//UVH//8bG////////4+P//9TU////////6ur//2Zm//9UVP//TEz//5iY/////////f3//3d3//9OTv//Tk7//3R0////////x8f//1BQ//9JSf//h4f///////+pqf//R0f//2Fh///p6f///f3///j4//91df//T0///0tL//+Li////////5GR//9JSf//Vlb//1hY///9/f//xcX//0JC//+srP///////8DA///8/P//dnb//05O//9LS///jIz///////+Rkf//TEz//1VV//9bW////f3//8HB//9eXv///////8TE//+QkP///////3R0//9OTv//S0v//4yM////////kpL//0tL//9VVf//W1v///7+//+6uv//rKz///////9tbf//kpL///////90dP//Tk7//0tL//+MjP///////5GR//9LS///VVX//1xc///39///29v///j4///IyP//QkL//5WV///4+P//cnL//09P//9KSv//jIz///////+Rkf//S0v//1VV//9dXf//8fH////////4+P//cHD//05O//9cXP//b2///1ZW//9VVf//S0v//4uL////////kZH//0tL//9VVf//XV3//+/v////////sLD//05O//9LS///oKD///////9+fv//TU3//1NT//9hYf//fX3//2Ji//9TU///VVX//1ZW//93d///fHz//1xc//9VVf//Tk7//4OD///Ozv//bGz//1BQ//9VVf//U1P//05O//9TU///VVX//1VV//9VVf//T0///05O//9UVP//VVX//1ZW//9QUP//TU3//1FR//9WVv//VVX//1VV//9XV///Vlb//1VV//9VVf//VVX//1ZW//9XV///VVX//1VV//9VVf//Vlb//1ZW//9WVv//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAIAAAAEAAAAABACAAAAAAAAAQAAATCwAAEwsAAAAAAAAAAAAA/1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9iYv//iYn//5yc//+iov//lpb//3l5//9XV///VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//21t//+AgP//gID//4CA//9fX///VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9oaP//xMT///39/////////////////////////////+3t//+bm///Vlb//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9gYP//9PT//////////////////4qK//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//bGz///Dw//////////////////////////////////////////////////+/v///VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//66u////////////////////////ior//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV///U1P//////////////////4OD//6io//+Xl///ra3//+vr//////////////////+QkP//VVX//1VV//9VVf//VVX//1VV//9nZ///+vr///////////////////////+Kiv//VVX//1VV//9VVf//VVX//1VV//9VVf//dnb//////////////////8jI//9XV///VVX//1VV//9VVf//Xl7//97e/////////////+Li//9VVf//VVX//1VV//9VVf//VVX//7+//////////////////////////////4qK//9VVf//VVX//1VV//9VVf//VVX//1VV//+kpP/////////////7+///Y2P//1VV//9VVf//VVX//1VV//9VVf//g4P//////////////////2ho//9VVf//VVX//1VV//90dP///v7/////////////6Oj/////////////ior//1VV//9VVf//VVX//1VV//9VVf//VVX//7m5/////////////9ra//9VVf//VVX//1VV//9VVf//VVX//1VV//9ZWf///f3/////////////f3///1VV//9VVf//VVX//8/P/////////////9XV///Kyv////////////+Kiv//VVX//1VV//9VVf//VVX//1VV//9VVf//wMD/////////////ysr//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV///19f////////////+Kiv//VVX//1VV//+Cgv//////////////////f3///8rK/////////////4qK//9VVf//VVX//1VV//9VVf//VVX//1VV///AwP/////////////Kyv//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX///X1/////////////4qK//9VVf//Vlb//93d/////////////9DQ//9VVf//z8//////////////ior//1VV//9VVf//VVX//1VV//9VVf//VVX//8DA/////////////8rK//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//9fX/////////////ior//1VV//+Njf//////////////////d3f//1VV///V1f////////////+Kiv//VVX//1VV//9VVf//VVX//1VV//9VVf//wMD/////////////ysr//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV///19f////////////+Kiv//WFj//+bm/////////////8bG//9VVf//VVX//9XV/////////////4qK//9VVf//VVX//1VV//9VVf//VVX//1VV///AwP/////////////Kyv//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX///X1/////////////4qK//+Vlf/////////////8/P//bW3//1VV//9VVf//1dX/////////////ior//1VV//9VVf//VVX//1VV//9VVf//VVX//8DA/////////////8rK//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//9fX/////////////jo7//+jo/////////////7i4//9VVf//VVX//1VV///V1f////////////+Kiv//VVX//1VV//9VVf//VVX//1VV//9VVf//wMD/////////////ysr//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV///19f/////////////Nzf/////////////39///ZGT//1VV//9VVf//VVX//9PT/////////////4qK//9VVf//VVX//1VV//9VVf//VVX//1VV///AwP/////////////Kyv//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX///X1/////////////////////////////6io//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//8DA/////////////8rK//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//9fX////////////////////////u7v//XFz//1VV//9VVf//VVX//1VV//9WVv//eHj//2dn//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//wMD/////////////ysr//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV///19f///////////////////////5eX//9VVf//VVX//1VV//9VVf//VVX//8jI////////+/v//4WF//9VVf//VVX//1VV//9VVf//VVX//1VV///AwP/////////////Kyv//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX///X1///////////////////i4v//Vlb//1VV//9VVf//VVX//1VV//9dXf//////////////////wMD//1VV//9VVf//VVX//1VV//9VVf//VVX//3x8//+Vlf//lZX//4CA//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//jo7//5WV//+Vlf//lZX//3Jy//9VVf//VVX//1VV//9VVf//VVX//1VV///i4v////////////+bm///VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//2Nj//+goP//ior//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV//9VVf//VVX//1VV/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"""
class EmbeddedIcon: #将图标优化到base64代码里
    def __init__(self, base64_str):
        self.base64_str = base64_str
        self._temp_file = None
    def get_tk(self): #tkinter临时图标
        self._temp_file = NamedTemporaryFile(suffix='.ico', delete=False)
        self._temp_file.write(base64.b64decode(self.base64_str))
        self._temp_file.close()
        return self._temp_file.name   
    def get_pygame(self): #pygame图标
        img_io = BytesIO(base64.b64decode(self.base64_str))
        return pygame.image.load(img_io)    
    def cleanup(self): #清除临时图标文件
        if self._temp_file and os.path.exists(self._temp_file.name):
            os.unlink(self._temp_file.name)
icon = EmbeddedIcon(unicode_icon_base64)# 创建全局图标对象
def get_all_blocks():
    blocks = []
    try:
        all_blocks = get_blocks() #获取Unicode区块信息，unidata_blocks立大功
        for block in all_blocks:
            zh_name = block.name_localized('zh')
            display_name = zh_name if zh_name else block.name
            start_hex = f"{block.code_start:04X}"
            end_hex = f"{block.code_end:04X}"
            display_text = f"{display_name} ({start_hex}-{end_hex})"
            blocks.append({
                'display': display_text,'start': start_hex,'end': end_hex,'start_int': block.code_start,'end_int': block.code_end,'name': display_name,'en_name': block.name,'capacity': block.capacity
            })
    except Exception as e:
        print(f"获取区块失败: {e}")
        blocks = [
            {'display': '获取区块失败', 'start': '100000', 'end': '10FFFF', 'start_int': 0x100000, 'end_int': 0x10FFFF, 'name': '获取区块失败', 'en_name': 'Error'},
        ]
    blocks.sort(key=lambda x: x['start_int'])
    return blocks
ALL_BLOCKS = get_all_blocks()
def get_screen_size():#获取屏幕大小（自动适配屏幕放大选项）
    import tkinter as tk
    temp_root = tk.Tk()
    temp_root.withdraw()
    width = temp_root.winfo_screenwidth()
    height = temp_root.winfo_screenheight()
    temp_root.destroy()
    return width, height
def start():
    button1.destroy()
    def limit_text_length(text, max_length):#限制字数，防止选中文字太多导致窗口被占满
        if len(text) > max_length:
            text = text[:max_length-3] + "..."
        return text
    def on_block_selected(block_combo, start_entry, end_entry):
        selection = block_combo.get()#选择区块时自动填入起始和结束码位
        if not selection:
            return
        for block in ALL_BLOCKS:
            if block['display'] == selection:
                start_entry.delete(0, tk.END)
                start_entry.insert(0, block['start'])
                end_entry.delete(0, tk.END)
                end_entry.insert(0, block['end'])
                break
    def open_file_dialog():  
        filename = filedialog.askopenfilename(filetypes=[("字体文件", ("*.ttf", "*.TTF", "*.otf",))])  #由于ttc文件处理工序太过繁琐故将其移除，下面同理
        selected_font_path.append(filename)
        tkb2.config(text=filename)
        print(filename)
    def open_file_dialogs():
        global filenames
        filenames = filedialog.askopenfilenames(filetypes=[("字体文件", ("*.ttf", "*.TTF", "*.otf",))])    
        if filenames: 
            selected_font_paths.extend(filenames)
            tka6.config(text=limit_text_length("已选择字体：" + ", ".join(filenames), 500))
        print(filenames)
    def open_file_dialogx():
        global filenamex
        filenamex = filedialog.askopenfilename(filetypes=[("字体文件", ("*.ttf", "*.TTF", "*.otf",))])
        tkb8.config(text=filenamex)
        print(filenamex)
    def to_print_support_font(): #中转到print_support_font函数 
        for font_path in selected_font_path:  
            print_support_font(font_path)
    def to_print_support_fonts(): #中转到print_support_font函数 
        for font_path in selected_font_paths:  
            print_support_fonts(font_path)
    def print_support_font(font_path, start=0, end=0x10FFFF):  #一键输出字体内支持的文字
        try:
            font = TTFont(font_path)
        except Exception as e:
            messagebox.showerror("错误", f"无法读取字体文件：\n{font_path}\n\n仅支持TTF/OTF格式")
            return
        cmap = font.getBestCmap()  
        supported_chars = set()  
        for code in range(start, end + 1):  
            if code in cmap:  
                if 0xD800 <= code <= 0xDFFF:
                    continue
                supported_chars.add(chr(code))    
        with open('Unicode生成.txt', 'w', encoding='utf-8') as f:  
            for char in sorted(supported_chars):
                f.write(char)
        messagebox.showinfo("完成", "已生成 Unicode生成.txt") 
    def print_support_fonts(font_path, start=0, end=0x10FFFF):  #一键输出选定字体内支持的文字并输出为多个文件
        try:
            font = TTFont(font_path)
        except Exception as e:
            messagebox.showerror("错误", f"无法读取字体文件：\n{font_path}\n\n仅支持ttf/otf格式")
            return
        cmap = font.getBestCmap()    
        supported_chars = set()    
        for code in range(start, end + 1):    
            if code in cmap:    
                if 0xD800 <= code <= 0xDFFF:
                    continue
                supported_chars.add(chr(code))
        filename = f'字符输出_{font_path.rsplit("/", 1)[-1].rsplit(".", 1)[0]}.txt'
        with open(filename, 'w', encoding='utf-8') as out_file:
            out_file.write(font_path + "\n") 
            for char in sorted(supported_chars):    
                out_file.write(char)
        messagebox.showinfo("完成", f"已生成 {filename}")
    def delete_fontfiles(): #删除文件以进行下一轮的生成准备
        text_files = [f for f in os.listdir('.') if f.endswith('.txt') and f.startswith('字符输出')]
        for file in text_files:
            os.remove(file)
        messagebox.showinfo("完成", "已删除所有字体字符文件")
    def write_unicode_file():#写入系统
        gtkb8 = tkb8.get() 
        gtkb9 = tkb9.get()
        try:  
            start = int(gtkb8, 16)  
            end = int(gtkb9, 16)  
            if start > end:  
                messagebox.showerror("错误", "起始码位必须小于或等于结束码位")  
                return 
            filename = os.path.join(os.getcwd(), "Unicode生成.txt")
            with open(filename, "w", encoding="utf-8") as f:  
                for code in range(start, end + 1):  
                    if 0xD800 <= code <= 0xDFFF: 
                        continue  
                    char = chr(code)  
                    f.write(char)
            messagebox.showinfo("完成", "已生成 Unicode生成.txt")
        except ValueError:  
            messagebox.showerror("错误", "请输入有效的十六进制码位")
    def append_playing1():#追加系统
        gtkb8 = tkb8.get() 
        gtkb9 = tkb9.get()
        try:  
            start = int(gtkb8, 16)  
            end = int(gtkb9, 16)  
            if start > end:  
                messagebox.showerror("错误", "起始码位必须小于或等于结束码位")  
                return 
            filename = os.path.join(os.getcwd(), "Unicode生成.txt")
            if not os.path.exists(filename):
                result = messagebox.askyesno("文件不存在", "Unicode生成.txt 不存在，是否创建新文件？")
                if not result:
                    return
                with open(filename, "w", encoding="utf-8") as f:
                    f.write("")
            with open(filename, "a", encoding="utf-8") as f:  
                for code in range(start, end + 1):  
                    if 0xD800 <= code <= 0xDFFF: 
                        continue  
                    char = chr(code)  
                    f.write(char)
            messagebox.showinfo("完成", "已追加字符到 Unicode生成.txt")
        except ValueError:  
            messagebox.showerror("错误", "请输入有效的十六进制码位")
    def append_unicode_write():#追加系统
        gtka11 = tka11.get()
        gtka12 = tka12.get()
        try:  
            start = int(gtka11, 16)  
            end = int(gtka12, 16)  
            if start > end:  
                messagebox.showerror("错误", "起始码位必须小于或等于结束码位！")  
                return
            try:
                filename = f'字符输出_{filenamex.rsplit("/", 1)[-1].rsplit(".", 1)[0]}.txt'
                if not os.path.exists(filename):
                    result = messagebox.askyesno("文件不存在", f"{filename} 不存在，是否创建新文件？")
                    if not result:
                        return
                    mode = "w"
                    with open(filename, mode, encoding="utf-8") as f:
                        f.write(filenamex + "\n")
                else:
                    mode = "a"
                with open(filename, mode, encoding="utf-8") as f:  
                    for code in range(start, end + 1):  
                        if 0xD800 <= code <= 0xDFFF: 
                            continue  
                        char = chr(code)  
                        f.write(char)
            except NameError:
                messagebox.showerror("错误", "尚未选择文件！")   
        except ValueError:  
            messagebox.showerror("错误", "格式错误！")
    def auto_fit_screen():
        screen_width, screen_height = get_screen_size()
        
        tkbscreena.delete(0, tk.END)
        tkbscreena.insert(0, str(screen_width))
        
        tkbscreenb.delete(0, tk.END)
        tkbscreenb.insert(0, str(screen_height))
    def fonts(): 
        global tka6, tka11, tka12, tka_block
        root.withdraw()
        fontsui = Toplevel(root)
        fontsui.title("Unicode快闪懒人版——多字体选项")
        icon_path = icon.get_tk()
        fontsui.iconbitmap(icon_path)
        # fontsui.iconbitmap("favicon.ico")
        fontsui.geometry("850x600")
        frame2 = tk.Frame(fontsui)
        frame2.place(relx=0.5, rely=0.5, anchor="center")
        tka1 = tk.Label(frame2, text="选择多个字体设置")
        tka1.grid(row=0, column=1, columnspan=4)
        tkas = tk.Label(frame2, text="一键输出多个字体内的所有字符并在主菜单内通过按钮运行，\n由于部分字体会夹带私用区或重复字符，\n生成后请检查一下重复生成的部分（如数字和字母）和私用区检查，\n如果想要不出现不需要多余的字符，请使用普通的自定义字符范畴。\n在生成文件之前请提前为字体文件用字母或其他方式排序，\n否则很有可能会导致顺序错乱。\n生成字符表示直接覆盖原有文本生成字符\n追加字符表示在原有字符基础上继续追加")
        tkas.grid(row=1, column=1, columnspan=4)
        tka2 = tk.Label(frame2, text="选择多个字体")
        tka2.grid(row=2, column=0)
        tka3 = tk.Button(frame2, text="选择文件", command=open_file_dialogs)
        tka3.grid(row=2, column=1)
        tka4 = tk.Button(frame2, text="一键生成多份字体字符", command=to_print_support_fonts)
        tka4.grid(row=2, column=2)
        tka5 = tk.Button(frame2, text="一键删除所有字体字符", command=delete_fontfiles)
        tka5.grid(row=2, column=3)
        tka6 = tk.Label(frame2, text="未选择文件", wraplength=400)
        tka6.grid(row=3, column=1, columnspan=3)
        tka7 = tk.Label(frame2, text="选择单个字体")
        tka7.grid(row=4, column=2)
        tka8 = tk.Button(frame2, text="选择文件", command=open_file_dialogx)
        tka8.grid(row=5, column=1)
        tka9 = tk.Button(frame2, text="生成字符文件", command=unicode_write)
        tka9.grid(row=5, column=2)
        tka9_append = tk.Button(frame2, text="追加字符", command=append_unicode_write, width=10)
        tka9_append.grid(row=5, column=3)
        tka10 = tk.Label(frame2, text="字符范畴")
        tka10.grid(row=6, column=0)
        tka11 = tk.Entry(frame2, width=6)
        tka11.grid(row=6, column=1)
        tka12 = tk.Entry(frame2, width=6)
        tka12.grid(row=6, column=2)
        tka_block_label = tk.Label(frame2, text="快捷选择区块:")
        tka_block_label.grid(row=7, column=0, columnspan=2, pady=(10,0))
        block_values = [block['display'] for block in ALL_BLOCKS]
        tka_block = ttk.Combobox(frame2, values=block_values, width=40, state="readonly")
        tka_block.grid(row=7, column=2, columnspan=5, pady=(5,0))
        tka_block.set("请选择Unicode区块")
        def on_block_selected_wrapper(event):
            on_block_selected(tka_block, tka11, tka12)
        tka_block.bind('<<ComboboxSelected>>', on_block_selected_wrapper)
        fontsui.protocol("WM_DELETE_WINDOW", lambda: (root.deiconify(), fontsui.destroy())) 
        fontsui.mainloop()
    frame = tk.Frame(root)
    global tkb2, tkb4, tkb6, tkb8, tkb9, tkb11, tkb13, tkbscreena, tkbscreenb, tkb_block
    frame.place(relx=0.5, rely=0.5, anchor="center")  
    tkb0 = tk.Label(frame, text="设置选项")  
    tkb0.grid(row=0, column=2, columnspan=4)   
    tkb05 = tk.Label(frame, text="显示字体为NotoSansSC，白背景，文字大小占屏幕一半，\n帧数为1，无预留时间，分辨率800x600\n生成字符表示直接覆盖原有文本生成字符\n追加字符表示在原有字符基础上继续追加")
    tkb05.grid(row=1, column=2, columnspan=4)
    tkb1 = tk.Label(frame, text="选择字体：")  
    tkb1.grid(row=2, column=1, sticky="e") 
    tkb2 = tk.Button(frame, text="选择文件", command=open_file_dialog)  
    tkb2.grid(row=2, column=2)
    tkb25 = tk.Button(frame, text="一键导入支持字符", command=to_print_support_font)
    tkb25.grid(row=2, column=3)
    tkb3 = tk.Label(frame, text="选择背景色：")  
    tkb3.grid(row=3, column=1, sticky="e")
    tkb4 = tk.Entry(frame, width=7)
    tkb4.grid(row=3, column=2)
    tkbscreen1 = tk.Label(frame, text="屏幕分辨率：")
    tkbscreen1.grid(row=4, column=1)
    tkbscreena = tk.Entry(frame, width=4)
    tkbscreena.grid(row=4, column=2)
    tkbscreenb = tk.Entry(frame, width=4)
    tkbscreenb.grid(row=4, column=3)
    tkbscreenc = tk.Button(frame, text="自动适配全屏", command=auto_fit_screen, width=10)
    tkbscreenc.grid(row=4, column=4, padx=(5,0))
    tkb5 = tk.Label(frame, text="文字大小：")  
    tkb5.grid(row=5, column=1, sticky="e")
    tkb6 = tk.Entry(frame, width=6)  
    tkb6.grid(row=5, column=2)
    tkb7 = tk.Label(frame, text="字符范畴：")  
    tkb7.grid(row=6, column=1, sticky="e")
    tkb8 = tk.Entry(frame, width=6)  
    tkb8.grid(row=6, column=2)
    tkb9 = tk.Entry(frame, width=6)  
    tkb9.grid(row=6, column=3)
    tkb_write = tk.Button(frame, text="生成字符", command=write_unicode_file, width=8)
    tkb_write.grid(row=6, column=4)
    tkb_append = tk.Button(frame, text="追加字符", command=append_playing1, width=8)
    tkb_append.grid(row=6, column=5)
    tkb_block_label = tk.Label(frame, text="快捷选择区块:")
    tkb_block_label.grid(row=7, column=0, columnspan=2, pady=(10,0), sticky="e")
    block_values = [block['display'] for block in ALL_BLOCKS]
    tkb_block = ttk.Combobox(frame, values=block_values, width=40, state="readonly")
    tkb_block.grid(row=7, column=2, columnspan=5, pady=(5,10))
    tkb_block.set("请选择Unicode区块")
    def on_block_selected_main(event):
        on_block_selected(tkb_block, tkb8, tkb9)
    tkb_block.bind('<<ComboboxSelected>>', on_block_selected_main)
    tkb10 = tk.Label(frame, text="帧数：")  
    tkb10.grid(row=8, column=1, sticky="e")
    tkb11 = tk.Entry(frame, width=6)  
    tkb11.grid(row=8, column=2)
    tkb12 = tk.Label(frame, text="预留时间：")
    tkb12.grid(row=9, column=1, sticky="e")
    tkb13 = tk.Entry(frame, width=3)
    tkb13.grid(row=9, column=2)
    tkb14 = tk.Button(frame, text="开始（单字体模式）", command=playing1)  
    tkb14.grid(row=10, column=2)
    tkb15 = tk.Button(frame, text="开始（多字体模式）", command=playing2)  
    tkb15.grid(row=10, column=3)
    tkb16 = tk.Button(frame, text="多字体选项", command=fonts)
    tkb16.grid(row=10, column=4)
def unicode_write():#覆盖系统
    gtka11 = tka11.get()
    gtka12 = tka12.get()
    try:  
        start = int(gtka11, 16)  
        end = int(gtka12, 16)  
        if start > end:  
            messagebox.showerror("错误", "起始码位必须小于或等于结束码位！")  
            return
        try:
            filename = f'字符输出_{filenamex.rsplit("/", 1)[-1].rsplit(".", 1)[0]}.txt'
            with open(filename, "w", encoding="utf-8") as f:  
                f.write(filenamex + "\n") 
                for code in range(start, end + 1):  
                    if 0xD800 <= code <= 0xDFFF: 
                        continue  
                    char = chr(code)  
                    f.write(char)
            messagebox.showinfo("完成", f"已生成文件 {filename}")
        except NameError:
            messagebox.showerror("错误", "尚未选择文件！")   
    except ValueError:  
        messagebox.showerror("错误", "格式错误！")
def playing1():#单字体模式
    gtkb2 = tkb2["text"]
    gtkb4 = tkb4.get()  
    gtkb6 = tkb6.get()  
    gtkb11 = tkb11.get()
    gtkb13 = tkb13.get()
    gtkbscreenb = tkbscreenb.get()
    gtkbscreena = tkbscreena.get() 
    try:
        with open('Unicode生成.txt', 'r', encoding='utf-8') as file:  
            characters = list(file.read())
    except FileNotFoundError:
        messagebox.showerror("错误", "Unicode生成.txt 不存在！\n请先使用「生成字符」或「追加字符」按钮创建文件。")
        return
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
    pygame.mixer.music.load("music.ogg")  
    pygame.display.set_icon(icon.get_pygame()) 
    # icon = pygame.image.load("favicon.ico")
    # pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    try:
        if gtkb13:
            countdown = int(gtkb13)
        else:
            countdown = -1
    except ValueError:
        countdown = -1
    char_index = 0  
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
    font_path = None
    if gtkb2 != '选择文件':
        font_path = gtkb2
    font_size = int(float(min(width/2, height/2)))
    if gtkb6:
        try:  
            font_size = int(float(gtkb6)) 
            if font_size <= 0:
                font_size = int(float(min(width/2, height/2))) 
        except ValueError:  
            pass
    default_font=getfont() #改用NotoSansSC字体
    font = pygame.font.Font(default_font, font_size)
    hex_color = "#FFFFFF" if not gtkb4 else gtkb4
    r, g, b = hex_to_rgb(hex_color)
    font2 = pygame.font.Font(default_font, int(width/25))
    font3 = pygame.font.Font(default_font, int(width/25)) 
    font4 = pygame.font.Font(default_font, int(width/25))
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
    pygame.mixer.music.play()
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
        pattern1 = re.compile(r'<reserved-[0-9A-Fa-f]*>') #字符名库内“未定义”的格式
        pattern2 = re.compile(r'<noncharacter-[0-9A-Fa-f]*>') #字符名库内“不是符号”的格式
        if char_index < len(characters):    
            font = pygame.font.Font(font_path, font_size)
            text = characters[char_index]  
            char_index += 1
            print(text)
            text_code = f"U+{hex(ord(text))[2:].upper().zfill(4)}" #字符转16进制格式，0x替换为U+
            print(text_code)
            try:
                text2 = name(text) #显示字符名字
            except ValueError:
                text2 = charname(text) #备用显示字符名字
            print(text2)
            if pattern1.match(text2) or pattern2.match(text2):
                continue  # 检测到字符名字为库内未定义或不是符号的格式则跳过
            try:
                text3 = get_block_by_chr(text)
                print(text3.name_localized("zh")) #显示字符所在的区块中文译名
            except AttributeError:
                continue #检测到未定义的区块跳过
        else:   
            text = None
            text_code = None
            text2 = None
            text3 = None
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
def playing2():#多字体模式
    gtkb4 = tkb4.get()
    gtkb6 = tkb6.get()
    gtkb11 = tkb11.get()
    gtkb13 = tkb13.get()
    gtkbscreenb = tkbscreenb.get()
    gtkbscreena = tkbscreena.get()
    text_files = [f for f in os.listdir('.') if f.endswith('.txt') and f.startswith('字符输出')]
    if not text_files:
        messagebox.showerror("错误", "没有找到字符文件！\n请先使用「生成字符文件」按钮创建文件。")
        return
    font_paths = []
    characters = {}
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
    pygame.mixer.music.load("music.ogg")
    pygame.display.set_icon(icon.get_pygame())
    # icon = pygame.image.load("favicon.ico")
    # pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    try:
        if gtkb13:
            countdown = int(gtkb13)
        else:
            countdown = -1
    except ValueError:
        countdown = -1
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
    font_size = int(float(min(width / 2, height / 2)))
    if gtkb6:
        try:
            font_size = int(float(gtkb6))
            if font_size <= 0:
                font_size = int(float(min(width / 2, height / 2)))
        except ValueError:
            pass
    default_font=getfont() #改用NotoSansSC字体
    font = pygame.font.Font(default_font, font_size)
    hex_color = gtkb4 if gtkb4 else "#FFFFFF"
    r, g, b = hex_to_rgb(hex_color)
    font2 = pygame.font.Font(default_font, int(width/25))
    font3 = pygame.font.Font(default_font, int(width/25)) 
    font4 = pygame.font.Font(default_font, int(width/25))
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
    pygame.mixer.music.play(-1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        hex_color = gtkb4 if gtkb4 else "#FFFFFF"
        r, g, b = hex_to_rgb(hex_color)
        screen.fill((r, g, b))
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
                try:
                    text2 = name(text) #显示字符名字
                except ValueError:
                    text2 = charname(text) #备用显示字符名字
                print(text2)
                if pattern1.match(text2) or pattern2.match(text2):
                    continue  # 检测到字符名字为库内未定义或不是符号的格式则跳过
                try:
                    text3 = get_block_by_chr(text)
                    print(text3.name_localized("zh"))  # 显示字符所在的区块中文译名
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
                frame = 1
                try:
                    frame = int(gtkb11)
                    if frame <= 0:
                        frame = 1
                except ValueError:
                    pass
                clock.tick(frame)
            else:
                char_index = 0
                file_index += 1
        else:
            text = None
            text_code = None
            text2 = None
            text3 = None
            pygame.display.flip()
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()
root = tk.Tk()
root.title("Unicode快闪懒人版")
icon_path = icon.get_tk()
root.iconbitmap(icon_path)
# fontsui.iconbitmap("favicon.ico")  
root.geometry("1000x650")
button1 = tk.Button(root, text="初始化设置", command=start)
button1.place(anchor="center", relx=0.5, rely=0.5)
selected_font_path = []
selected_font_paths = [] 
root.mainloop()