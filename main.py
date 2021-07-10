import tkinter as tk
import get_time
import time
import icon
import os
import base64

class main(object):
	"""docstring for main"""
	def __init__(self):
		# announce app
		self.app = tk.Tk()
		# title
		self.app.title("Time locker")
		# size
		self.app.geometry('400x100')
		# icon
		with open('tmp.ico','wb') as tmp:
			tmp.write(base64.b64decode(icon.Icon().img))
		self.app.iconbitmap('tmp.ico')
		os.remove('tmp.ico')

		# set frame
		# time frame
		self.div_time = tk.Frame(self.app, width=400, height=10)
		self.div_time.pack(anchor=tk.W)

		# output
		# clock
		self.clock_label = tk.Label(self.div_time, text="")
		self.clock_label.pack()
		self.update_clock()

		# 狀態列
		self.statustext = tk.StringVar()
		self.status = "You open this app on: "+get_time.all_time()
		self.statustext.set(self.status)
		self.statusbar = tk.Label(self.app, textvariable=self.statustext, bd=1, relief=tk.SUNKEN, anchor=tk.W)
		self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)

		# run
		self.app.mainloop()

	def update_clock(self):
		now = "The time on local is: "+time.strftime("%H:%M:%S")
		self.clock_label.configure(text=now)
		self.app.after(200, self.update_clock)


main()