#coding = utf-8
#running in python3.6

from tkinter import *
from tkinter import messagebox
import qrcode  #使用python的pip安装器安装，pip3 install qrcode
from PIL import ImageTk as IK #使用python的pip安装器安装，pip3 install Pillow
from PIL import Image as IM

class TkinterUtil(object):
#Tkinter主界面布局
    def __init__(self):
        object.__init__(self)

    @staticmethod
    def get_screen_size(window):
        return window.winfo_screenwidth(), window.winfo_screenheight()

    @staticmethod
    def get_window_size(window):
        return window.winfo_reqwidth(), window.winfo_reqheight()

    @staticmethod
    def center_window(root, width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(size)

class ConfigFrom(object):
    def __init__(self,save_paths=''):
        object.__init__(self)
        self.save_paths = save_paths
        self.root = Tk()
        self.root.title(u'QR图生成器')
        TkinterUtil.center_window(self.root,800,430)#主界面大小

        self.sp_input_val = StringVar()

        self.pd = None #生成按钮承载变量
        self.imgs = None #生成QR图承载变量
        self.create_button = None #生成按钮变量
        self.save_button = None #保存按钮变量
        self.save_path()

        self._text = None
        self.html_init()

        self.picture_display_init()

        self.root.update()

        self.root.mainloop()

    def save_path(self): #保存地址输入框布局
        sk_frm = Frame(self.root)
        opt_frm = Frame(self.root)

        Label(
            sk_frm, text=u"保存地址", font=('Aria', 12)
        ).grid(row=0, column=0)
        self.sk_entry = Entry(sk_frm, textvariable=self.sp_input_val)
        self.sp_input_val.set(self.save_paths)
        self.sk_entry.grid(row=0, column=1, sticky=W + E + N + S)
        sk_frm.grid(row=0, column=0)

        self.create_button = Button(opt_frm, text=u"生成", width=6, height=2, command=self.create_qr)
        self.create_button.grid(row=0, column=1, sticky=W + E + N + S)

        self.save_button = Button(opt_frm, text=u"保存", width=6, height=2, command=self.save_qr)
        self.save_button.grid(row=0, column=0, sticky=W + E + N + S)

        opt_frm.grid(row=0, column=1)
        pass

    def html_init(self): #网址输入框布局
        Label(
            self.root,
            text=u"HTML", font=('Aria', 12)
        ).grid(row=1, column=0)
        self.html_text = Text(self.root, fg="white", bg="dimgray", width=56)
        self.html_text.grid(row=2, column=0)
        pass

    def picture_display_init(self): #二维码显示区域布局
        Label(
            self.root,
            text=u"QR图", font=('Aria', 12)
        ).grid(row=1, column=1)
        self.display_canvas =Canvas(self.root,width=394,height=360,bg="dimgray") #Label(self.root, fg="white", bg="dimgray",width=43,height=22)
        #
        print(1)
        self.display_canvas.grid(row=2, column=1)
        pass

    def make_qr(self): #二维码生成函数

        data = self.html_text.get(0.0, END)
        print(data)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=4
        )
        '''version：值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）。 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。
        error_correction：控制二维码的错误纠正功能。可取值下列4个常量。
        ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
        ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
        ROR_CORRECT_H：大约30%或更少的错误能被纠正。
        box_size：控制二维码中每个小格子包含的像素数。
        border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）'''

        qr.add_data(data)
        qr.make(fit=True)
        self.imgs = qr.make_image(fill_color='black', back_color='white')
        return self.imgs



    def create_qr(self): #生成显示方法
        #global pd
        make_qr_images = self.make_qr()
        self.pd = IK.PhotoImage(make_qr_images)
        self.display_canvas.create_image(196,180,image=self.pd)
        #self.display_canvas.image = pd
        print(2)
        #self.root.update()
        #self.display_canvas.grid(row=2, column=1)

        #self.root.after(2000)
        #pass

    def save_qr(self): #保存二维码图片方法
        path = self.sk_entry.get()
        #print(self.html_text.get(0.0, END))
        save_image = self.imgs
        try:
            save_image.save(path)
            IM.open(path).show()
            #print(self.make_qr)
        except Exception as e :
            messagebox.showinfo(title="Tips", message=u"保存失败，未有图片生成")
            print(e)

        pass


if __name__== "__main__":
    form = ConfigFrom('tmp.png')

#code by 摩托






