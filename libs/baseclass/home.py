from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from libs.baseclass.dialog import Dialog, Item
from libs.baseclass.text_field import RoundTextField


Builder.load_string(
"""
#:import Admin libs.baseclass.dialog.Admin

<Home>
	name: "home"

"""
)


class Home(MDScreen):
	"""
	:::Home Screen:::
		...Shows the available data files
	"""
	pass
