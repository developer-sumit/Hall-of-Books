from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from libs.baseclass.dialog import Item
from kivymd.uix.dialog import BaseDialog
from libs.baseclass.text_field import RoundTextField

KV = '''
#:import KivyLexer kivy.extras.highlight.KivyLexer
#:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer

MDBoxLayout:
	HotReloadViewer:
		path: app.path
		error: True
		errors_text_color: 1,0,0,1
		errors_background_color: app.theme_cls.bg_dark

'''

Window.size = (352, 625)
Window.position = "custom"
Window.left = 1010


class Dialog(BaseDialog):
	pass

class Home(MDScreen):
	pass

class App(MDApp):
	path = "home.kv"

	def build(self):
		return Builder.load_string(KV)


App().run()