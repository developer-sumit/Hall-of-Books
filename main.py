"""		■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
		¦			HALL OF BOOKS			¦
		¦		  	  2022.1.0				¦
		¦		  Developed by Sumit		¦
		■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

======================
		INFO
======================
	...Developed by Sumit

	...Version: 2022.1.0
	
	...Libraries Used: csv, kivy, kivyMD

======================
	  OBJECTIVE
======================
	...Store the data with an user-friendly look

	...Learn how to create an app which stores user data

======================
		PROS
======================
	...Data is saved in a csv file (a beautiful way of presentation)

======================
	   PROBLEMS
======================

	<<< Version 2022.1.0 >>>
		...Only one thread

		...No delete option

		...One element can be added multiple times

		...Not in an organised order (ascending or descending)

		...Object cannot be changed, once added to the list (manually it's possible)

		...Added object cannot be searched (user has to find that element one by one)

======================
	FUTURE UPDATES
======================
	...New App name

	...Search not available

	...Name change functionality

	...Python to Java conversion

	...Addition of long press event

	...Complex but user-friendly design

	...Change of storage file format (csv --> sql)

	...Create objects using own custom txt,csv,sql files

	...Addition of widgets: Menu, Tabs, TapTargetView, FileManager,
							Screen, RefreshLayout, Chips, Carousel

	...DSA Concept: Binary Search, Stacks, Queues (might include Trees)

"""


__author__ = "Developer Sumit"
__version__ = "2022.1.0"


'''----------------------------------IMPORTS------------------------------------------'''
from kivy.config import Config
Config.set("graphics", "resizable",0)

#### BUILT-IN MODULES ####
import os
import csv
import time
import numpy
import concurrent.futures

#### THIRD PARTY MODULES ####
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
from kivy.core.window import Window
from kivy.animation import Animation
from kivymd.uix.card import MDSeparator
from kivy.clock import mainthread, Clock
from kivy.uix.screenmanager import ScreenManager

#### CUSTOM MODULES ####
from libs.baseclass.dialog import Dialog, Admin, Item, Loading
from libs.baseclass.text_field import RoundTextField
from libs.baseclass.watched import WatchList
from libs.baseclass.list import Element
from libs.baseclass.home import Home
'''-----------------------------------------------------------------------------------'''


Window.size = (417, 625)


########################################## APP CLASS STARTS #################################################

class App(MDApp):
	title = "Hall of Books"
	key = 1
	fields = ["Name", "Price"]

	'''-----------------------------------------------------------------------------------'''
	def build(self):
		global screen_manager, _screen_list
		screen_manager = ScreenManager()
		SCREENS = [
			WatchList(),
			Home()
		]
		for screen in SCREENS:
			screen_manager.add_widget(screen)
		_screen_list = []
		return screen_manager
	'''-----------------------------------------------------------------------------------'''

	'''-----------------------------------------------------------------------------------'''
	@mainthread
	def on_start(self):
		"""
		:::App:- on_start():::
			...App will call this function every time it starts
			...It will create a "data.csv" if not exists
			...If exists then it will just create the cards using that csv data
			...If file is not empty then alert the user that it's loading
				and create cards using the given value
		"""
		if not os.path.isfile("data.csv"):
			with open("data.csv", "x") as file:
				file.close()
		with open("data.csv", newline="") as file:
			reader = csv.reader(file)
			for column in reader:
				if column !="":
					toast("Loading...")
					Clock.schedule_once(self.create_card, 1)
	'''-----------------------------------------------------------------------------------'''

	'''-----------------------------------------------------------------------------------'''
	@mainthread
	def show_dialog(self):
		"""
		:::App:- show_dialog():::
			...Pops up the dialog box
		"""
		global dialog_box, dialog_elements
		dialog_elements = []
		ITEMS = {self.fields[0]: "e.g.Solo Leveling", self.fields[1]: "e.g."}
		for text, hint_text in ITEMS.items():
			item = Item(
						text = text,
						hint_text = hint_text
					)
			dialog_elements.append(item)
		dialog_box = Dialog(
				title ="BOOK DETAILS",
				items = dialog_elements,
			)
		screen_manager.get_screen("watch").add_widget(dialog_box)
	'''-----------------------------------------------------------------------------------'''

	'''-----------------------------------------------------------------------------------'''
	def key_increment(self):
		"""
		:::App:- key_increment():::
			...Checks the last key value in csv file
			...Then increments the key every time this function is called
			...Stores that incremented key in a class variable
		"""
		with open("data.csv", newline="") as file:
			reader = csv.reader(file)
			for column in reader:
				if column!=[]:
					self.key = int(column[0])+1
	'''-----------------------------------------------------------------------------------'''

	'''-----------------------------------------------------------------------------------'''
	@mainthread
	def write_data(self):
		global name
		"""
		:::App:- write_data():::
			...Capitalizes every first letter of the word
			...Saves the user entered value in a csv file
		"""
		self.key_increment()
		name = dialog_elements[0].ids["container"].ids["text_input"].text.title()
		episodes = dialog_elements[1].ids["container"].ids["text_input"].text
		with open("data.csv", "a") as file:
			writer = csv.writer(file)
			if name=="":
				toast("No Name!")
			else:
				writer.writerow([self.key, name, episodes])
				self.clear_input()
			file.close()
			toast(f"{name} added")
			screen_manager.get_screen("watch").remove_widget(dialog_box)
			self.create_card()
	'''-----------------------------------------------------------------------------------'''

	'''-----------------------------------------------------------------------------------'''
	@mainthread
	def clear_input(self):
		"""
		:::App:- clear_input():::
			...Change the text-field text to default: ""
		"""
		for element in dialog_elements:
			element.ids["container"].ids["text_input"].text = ""
	'''-----------------------------------------------------------------------------------'''

	'''-----------------------------------------------------------------------------------'''
	def threadpool(self):
		with concurrent.futures.ThreadPoolExecutor() as executor:
			thread1 = executor.submit(self.write_data)
			thread1.result()
	'''-----------------------------------------------------------------------------------'''

	'''-----------------------------------------------------------------------------------'''
	@mainthread
	def check_elements(self):
		NAMES = []
		with open("data.csv", newline="") as file:
			reader = csv.reader(file)
			for column in reader:
				if column!=[]:
					NAMES.append(column)
		element = screen_manager.get_screen("watch").ids["element_container"]

	'''-----------------------------------------------------------------------------------'''

	'''-----------------------------------------------------------------------------------'''
	@mainthread
	def create_card(self, *args):
		"""
		:::App:- create_card():::
			...Fetches the values from the csv file
			...Creates a element card using those values
			...Adds a separator after every element
		
		:::Bugs:::
			...Removes all elements every time the function is called
			...Adds those elements again with a new element
			...Removing and adding those same elements takes a lot of time

		:::Solution:::
			...Using multi-threads
			...Only add those elements which aren't already there
		"""
		global widget
		screen_manager.get_screen("watch").ids["element_container"].clear_widgets()
		ELEMENTS = []
		with open("data.csv", newline="") as file:
			reader = csv.reader(file)
			for column in reader:
				if column!=[]:
					if column[1]!="":
						widget = Element()
						if column[2]=="":
							widget.text = [column[0],column[1],"?"]
						else:
							widget.text = [column[0],column[1],column[2]]
						screen_manager.get_screen("watch").ids["element_container"].add_widget(widget)
						screen_manager.get_screen("watch").ids["element_container"].add_widget(MDSeparator())
	'''-----------------------------------------------------------------------------------'''

############################################ APP CLASS ENDS #################################################



if __name__ == "__main__":
	app = App()
	app.run()