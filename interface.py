#!/usr/bin/env python
# coding: UTF-8
#
## @package interface
#  GUI
#  @author Wellington Oliveira
#  @since 23/02/2018
# import os

from tkinter import *

from tkinter import filedialog, messagebox

from river import River


class Application(Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("800x600")
        self.title("River Simulator")
        self.resizable(0, 0)
        self.configure(bg='#F5FFFA', relief="sunken", bd=1)
        self.wm_iconbitmap("imagens/ico.ico")

        # frames
        self.f_title = Frame(self, width=780, height=100, bd=1, relief="sunken", pady=20, bg="#FFE4C4")
        self.f_title.pack(pady=3)
        self.f_option = Frame(self, width=145, height=490, bd=1, relief="sunken", bg="#F0F8FF")
        self.f_option.place(x=10, y=105)
        self.f_saida = Frame(self, width=631, height=490, bd=1, relief="sunken", bg="#F8F8FF")
        self.f_saida.place(x=158, y=105)
        self.nc = LabelFrame(self.f_option, width=130, text="Number of Cycles", fg="#191970", padx=15,
                             height=100, bg="#F0F8FF")
        self.nc.place(x=5, y=35)
        self.river_opt = LabelFrame(self.f_option, width=130, text="River type", fg="#191970", padx=15,
                                    height=250, bg="#F0F8FF")
        self.river_opt.place(x=5, y=135)
        self.seed_opt = LabelFrame(self.f_option, width=130, text="Seed option", fg="#191970", padx=15,
                                   height=95, bg="#F0F8FF")
        self.seed_opt.place(x=5, y=390)

        # variables
        self.option_seed = StringVar()
        self.option = StringVar()
        self.trial = 0
        self.rio = None
        self.seed = None

        # image
        self.img = PhotoImage(file="imagens/button.png")
        self.img_del = PhotoImage(file="imagens/Delete-.png")
        self.fileimg = PhotoImage(file="imagens/file.png")
        self.imgreset = PhotoImage(file="imagens/reset.png")
        self.imgsave = PhotoImage(file="imagens/save.png")
        self.img_bear = PhotoImage(file="imagens/bear.png")

        # labels
        self.header = Label(self.f_title, fg="#4B0082", text="River Simulator", font=("Colonna MT", 40, "bold"),
                            bg="#FFE4C4")
        self.header.place(x=230, y=0)
        self.lb_trial = Label(self.f_saida, text="TRIAL:", font=("Constantia", 15), bg="#F8F8FF", fg="#191970")
        self.lb_trial.place(x=220, y=10)
        self.lb_trial_c = Label(self.f_saida, text=str(self.trial), font=("Arial", 15), fg="#191970", bg="#F8F8FF")
        self.lb_trial_c.place(x=290, y=10)
        self.random_lb1 = Label(self.river_opt, text="Length", bg="#F0F8FF")
        self.random_lb1.place(x=12, y=30)
        self.optlb = Label(self.f_option, text="Options", font=("Constantia", 15), bg="#F0F8FF", fg="#191970")
        self.optlb.place(x=25, y=0)
        self.bear_lb = Label(self.f_title, image=self.img_bear, bg="#FFE4C4")
        self.bear_lb.place(x=40)

        # radios button
        self.random_rb = Radiobutton(self.river_opt, text="Random river", variable=self.option, value=1,
                                     command=self.radioRandom, bg="#F0F8FF", font=("Constantia", 10),
                                     width=10, fg="#191970", cursor="hand2")
        self.random_rb.place(x=-10, y=10)
        self.file_rb = Radiobutton(self.river_opt, text="File input", variable=self.option, value=2, cursor="hand2",
                                   command=self.radioFile, bg="#F0F8FF", font=("Constantia", 10), fg="#191970")
        self.file_rb.place(x=-5, y=110)

        self.seed_rby = Radiobutton(self.seed_opt, text="Yes", variable=self.option_seed, value=1,
                                    command=self.radioSeedYes, bg="#F0F8FF", font=("Constantia", 10),
                                    width=2, fg="#191970", cursor="hand2")
        self.seed_rby.place(x=-10, y=5)

        self.seed_rbn = Radiobutton(self.seed_opt, text="No", variable=self.option_seed, value=2,
                                    command=self.radioSeedNo,
                                    bg="#F0F8FF", font=("Constantia", 10), width=2, fg="#191970", cursor="hand2")
        self.seed_rbn.place(x=-10, y=40)

        # scale
        self.len = Scale(self.river_opt, from_=1, to=25, width=10, state='disabled', orient="horizontal",
                         bg="#F0F8FF", cursor="hand2")
        self.len.place(x=-5, y=50)

        # spinbox
        self.ncycl = Spinbox(self.nc, from_=1, to=20, width=5, font=("Arial", 12))
        self.ncycl.place(x=20, y=30)
        self.valueseed = Spinbox(self.seed_opt, from_=0, to=40, width=3, font=("Arial", 10), state="disabled")
        self.valueseed.place(x=40, y=8)

        # buttons
        self.openfile = Button(self.river_opt, text="Open", state='disabled', command=self.fileOpen, relief="flat",
                               bg="#F0F8FF", cursor="hand2")
        self.openfile.configure(image=self.fileimg)
        self.openfile.place(x=20, y=170)
        self.bt_play = Button(self.f_saida, text="Play", command=self.play, bg="#F8F8FF", relief="flat",
                              cursor="hand2")
        self.bt_play.configure(image=self.img)
        self.bt_play.place(x=150, y=400)
        self.bt_exit = Button(self.f_saida, text="Exit", image=self.img_del, command=self.exit, bg="#F8F8FF",
                              relief="flat", cursor="hand2")
        self.bt_exit.place(x=290, y=400)
        self.bt_reset = Button(self.f_saida, text="reset", image=self.imgreset, command=self.reset, relief="flat",
                               bg="#F8F8FF", cursor="hand2")
        self.bt_reset.place(x=220, y=400)
        self.bt_save = Button(self.f_saida, text="Save", command=self.save, bg="#F8F8FF", image=self.imgsave,
                              relief="flat", state="disabled", cursor="hand2")
        self.bt_save.place(x=360, y=400)

        # scrollbar
        self.sb_y = Scrollbar(self.f_saida)
        self.sb_y.place(x=610, y=45)

        # listbox
        self.lb = Listbox(self.river_opt, width=18, height=2, state="disabled")
        self.lb.place(x=-10, y=140)
        self.box = Listbox(self.f_saida, width=100, height=20, bg="#87CEFA", bd=2, relief="ridge")
        self.box.place(x=5, y=45)
        self.box.config(yscrollcommand=self.sb_y.set)
        self.sb_y.config(command=self.box.yview)

    # Methods
    def radioRandom(self):
        """Enables the option that randomly generates a river"""
        self.lb.delete(0, 0)
        self.len.configure(state="normal")
        self.openfile.configure(state="disabled")
        self.lb.configure(state="disabled")

    def radioFile(self):
        """Enables the generation of a river through a file"""
        self.len.configure(state="disabled")
        self.openfile.configure(state="normal")
        self.lb.configure(state="normal")

    def radioSeedYes(self):
        """Enable seed"""
        self.valueseed.configure(state="normal")

    def radioSeedNo(self):
        """Disabled seed"""
        self.seed = None
        self.valueseed.configure(state="disabled")

    def exit(self):
        """Closes the application"""
        self.destroy()

    def save(self):
        """Saves the river displayed on the screen in a text file"""
        try:
            arq = filedialog.asksaveasfile(mode='w', filetypes=(("Arquivo", "*.txt"), ("All files", "*.*")))
            with arq:
                arq.write("Trial: " + str(self.trial) + "\n")
                for line in self.box.get(0, END):
                    arq.write(line + "\n")
                arq.write("\n")
                arq.write("Length: " + str(self.len.get()) + "\n")
                arq.write("Cycles: " + self.ncycl.get() + "\n")
                arq.write("Seed  : " + str(self.seed))
        except AttributeError:
            pass

    def fileOpen(self):
        """Opens the text file that will generate the river"""
        self.lb.delete(0, 0)
        filename = filedialog.askopenfilename(filetypes=(("File", "*.txt"), ("All files", "*.*")))
        self.lb.insert(END, filename)

    def reset(self):
        """reset trial counter"""
        self.trial = 0
        self.lb_trial_c.configure(text=str(self.trial))
        self.box.delete(0, END)
        self.bt_save.configure(state="disabled")

    def riverOutPut(self):
        """iterates over the river and shows the update every cycle"""
        for i in range(int(self.ncycl.get())):
            self.rio.updateRiver()
            self.box.insert(END, "After cycle: {}".format(i + 1))
            self.box.insert(END, self.rio)
        self.box.insert(END, "Final River")
        self.box.insert(END, self.rio)
        self.trial += 1
        self.lb_trial_c.configure(text=str(self.trial))
        self.bt_save.configure(state="normal")

    def play(self):
        self.box.delete(0, END)
        if self.option_seed.get() == "1":
            self.seed = int(self.valueseed.get())
        if self.option.get() == "":
            msg = "{:^180}".format("Invalid option!!")
            self.box.insert(END, msg)
        elif self.option.get() == "1":
            self.box.insert(END, "Random River")
            self.box.insert(END, "Initial river:")
            self.rio = River(int(self.len.get()), self.seed)
            self.box.insert(END, self.rio)
            self.riverOutPut()
        elif self.option.get() == "2":
            arg = self.lb.get(0)
            seed = self.seed
            if arg.endswith(".txt"):
                self.rio = River(arg, seed)
                self.box.insert(END, "File input")
                self.box.insert(END, "Initial river:")
                self.box.insert(END, self.rio)
                self.riverOutPut()
            else:
                msg = messagebox.showinfo("Invalid file format", "Please enter a valid txt file")
                return msg
