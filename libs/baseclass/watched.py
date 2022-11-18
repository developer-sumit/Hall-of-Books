from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from libs.baseclass.dialog import Dialog, Item
from libs.baseclass.text_field import RoundTextField


Builder.load_string(
"""
#:import Admin libs.baseclass.dialog.Admin

<WatchList>
	name: "watch"
	MDBoxLayout:
		orientation: 'vertical'

		MDCard:
			elevation: 10
			size_hint_y: None
			height: dp(100)
			md_bg_color: 0,1,1,1
			spacing: 10
			orientation: "vertical"
			MDBoxLayout:
				padding: 10
				spacing: 5
				MDIconButton:
					icon: "assets/icon.png"
					pos_hint: {"center_y":.5}
					on_press: app.root.get_screen("watch").add_widget(Admin())
				MDLabel:
					text: app.title
					font_style: "H5"
					pos_hint: {"center_y":.5}
				MDIconButton:
					icon: "magnify"
					pos_hint: {"center_y":.5}
			MDBoxLayout:
				MDLabel:
					text: "#"
					halign: "center"
					size_hint_x: .5
				MDLabel:
					text: app.fields[0]
					halign: "center"
				MDLabel:
					text: app.fields[1]
					halign: "center"
					size_hint_x: .8
		MDSeparator:

		ScrollView:
			do_scroll: False, True
			MDBoxLayout:
				id: element_container
				orientation: "vertical"
				size_hint_y: None
				height: self.minimum_height
				

	MDFloatingActionButton:
		id: floating_button
		icon: "plus"
		pos_hint: {'center_x': .85, "center_y":.1}
		on_press: app.show_dialog()

"""
)


class WatchList(MDScreen):
	"""
	:::WatchList:::
		...Only those anime will be added which are watched by the user
		...To add the anime he wants to watch will be added in other MDScreen: WishList
	"""
	pass