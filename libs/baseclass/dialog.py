
__all__ = ("Item", "Dialog", "Admin", "Loading")

from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import BaseDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import (
		StringProperty,
		ListProperty,
	)


Builder.load_string(
"""
<Info>
	text: root.text
	pos_hint: {"center_y":.5}
	halign: "left"
	markup: True

<Loading>
	MDCard:
		elevation: 10
		size_hint: None, None
		width: dp(200)
		height: dp(60)
		padding: 10
		pos_hint: {"center_x":.5, "center_y":.5}
		MDLabel:
			text: "Loading"
			bold: True

<Admin>
	MDCard:
		elevation: 10
		radius: [15]
		orientation: "vertical"
		size_hint: None, None
		width: dp(320)
		height: dp(300)
		padding: 10
		pos_hint: {"center_x":.5, "center_y":.5}
		MDFloatLayout:
			size_hint_y: .2
			pos_hint: {"center_x":.5, "center_y":1}
			MDLabel:
				text: root.title
				font_style: "H6"
				size_hint_y: .2
				halign: "center"
				pos_hint: {"center_y":.5, "center_x":.5}
			MDIconButton:
				icon: "close"
				pos_hint: {"center_y":.5, "center_x":.9}
				on_press: app.root.get_screen("watch").remove_widget(root)
		MDBoxLayout:
			padding: 10
			spacing: 10
			Image:
				source: "assets/admin.jpg"
			MDBoxLayout:
				id: info_container
				spacing: 10
				orientation: "vertical"
				pos_hint: {"center_y":.5}

<Dialog>
	MDCard:
		elevation: 10
		radius: [15]
		orientation: "vertical"
		size_hint: None, None
		width: dp(280)
		height: dp(300)
		padding: 10
		pos_hint: {"center_x":.5, "center_y":.5}
		MDLabel:
			text: root.title
			font_style: "H6"
			size_hint_y: .2
			halign: "center"
		MDBoxLayout:
			id: item_container
			orientation: "vertical"
			padding: 10
			size_hint_y: .5
			# ITEMS WILL BE ADDED HERE

		MDBoxLayout:
			spacing: 50
			size_hint: .5,.2
			pos_hint: {"center_x":.5}
			MDIconButton:
				icon: "close"
				md_bg_color: 0,1,1,1
				on_press: app.root.get_screen("watch").remove_widget(root)
			MDIconButton:
				icon: "check"
				md_bg_color: 0,1,1,1
				on_press: app.threadpool()

<Item>
	spacing: 10
	# padding: 10
	MDLabel:
		text: root.text
		size_hint_x: .5
		adaptive_height: True
		pos_hint: {"center_y":.5}
	RoundTextField:
		id: container
		hint_text: root.hint_text
		pos_hint: {"center_y":.5}
		md_bg_color: 1,1,1,.7
"""
)

class Info(MDLabel):
	"""
	:::Info:::
		...Label for entries in "INFORMATON DIALOG"
	"""
	text = StringProperty()



class Item(MDBoxLayout):
	"""
	:::Item:::
		...Object for Dialog Class
		...It's a layout which contains a label and a text field
		...User can't change text of the label but that will be possible in future update
	"""
	text = StringProperty()
	hint_text = StringProperty()


class Dialog(BaseDialog):
	"""
	:::Dialog Box:::
		...User Interactive dialog box
		...Only two Item classes are present at the moment
		...User can add more Item classes in future updates
	"""
	title = StringProperty()
	items = ListProperty()

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		for item in self.items:
			self.ids["item_container"].add_widget(item)



class Admin(BaseDialog):
	""" App Info Dialog Box """
	title = StringProperty("DEVELOPER")
	details = [	"[b]Developer:[/b] Sumit",
				"[b]Software:[/b] Hall of Books",
				"[b]Version:[/b] 2022.1.0",
				"[b]Package:[/b] com.sumit.hall_of_books",
			]
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		for info in self.details:
			self.ids["info_container"].add_widget(
					Info(
						text = info
					)
				)


class Loading(BaseDialog):
	"""Loading Dialog"""
	pass