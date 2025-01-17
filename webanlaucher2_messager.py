from customtkinter import CTkToplevel, CTkLabel, CTkButton, set_appearance_mode
from PIL.ImageTk import PhotoImage as CTkImage

def msg_window(title='WebAnLauncher 2 MessageBox',message='Example', width=500, height=250, textfont=['Open Sans',25],icon='src/iconbitmap/logo.ico', image=None):
    set_appearance_mode('dark')
    des = CTkToplevel()
    des.title(title)
    try:
        des.iconbitmap(icon)
    except:
        pass
    des.resizable(width=False, height=False)
    des.geometry(f'{width}x{height}')
    
    if image == None or image == False:
        pass
    else:
        msg_image=CTkImage(file=image)
        msg_image_label= CTkLabel(des, image=msg_image, text='')
        msg_image_label.place(x=width/5, y=height/2-msg_image.height())

    msg=CTkLabel(des, text=message, wraplength=width-width/5*2.5+width/30, font=(f'{textfont[0]}', textfont[1]))
    msg.place(x=width/5*2, y=height/2-50)
    ok=CTkButton(des, text='OK', font=(f'{textfont[0]}', textfont[1]),corner_radius=0,fg_color='black',hover_color='grey', command=lambda: des.destroy())
    ok.place(x=(width-3*(textfont[1]*len('OK'))), y=height-50)
    des.mainloop()

def choise_window(title='WebAnLauncher 2 MessageBox',message='Example', width=500, height=250, text_choise='OKOK', option_choise=lambda: quit(), textfont=['Open Sans',25], image=None):
    set_appearance_mode('dark')
    des = CTkToplevel()
    des.title(title)
    des.resizable(width=False, height=False)
    des.geometry(f'{width}x{height}')

    if image == None or image == False:
        pass
    else:
        msg_image=CTkImage(file=image)
        msg_image_label= CTkLabel(des, image=msg_image, text='')
        msg_image_label.place(x=width/5*1, y=height/2-msg_image.height())

    msg=CTkLabel(des, text=message, wraplength=width-width/5*2.5+width/30, font=(f'{textfont[0]}', textfont[1]))
    msg.place(x=width/5*2, y=height/2-50)
    ok=CTkButton(des, text='OK', font=(f'{textfont[0]}', textfont[1]),corner_radius=0 ,fg_color='black',hover_color='grey', command=lambda: des.destroy())
    ok.place(x=(width-3*(textfont[1]*len('OK'))), y=height-50)
    choise=CTkButton(des, text=text_choise, font=(f'{textfont[0]}', textfont[1]),corner_radius=0 ,fg_color='black',hover_color='grey',command=option_choise)
    choise.place(x=(width-(textfont[1]*len(text_choise)))/2, y=height-50)
    des.focus_force()
    des.mainloop()