from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivy.properties import ListProperty


Builder.load_string(
"""
<Element>
	elevation: 10
	size_hint_y: None
	height: dp(90)
	ripple_behavior: True
	MDLabel:
		text: root.text[0]
		halign: "center"
		size_hint_x: .5
	MDLabel:
		text: root.text[1]
		halign: "center"
	MDLabel:
		text: root.text[2]
		halign: "center"
		size_hint_x: .8
"""
)



class Element(MDCard):
	"""
	:::Element:::
		...It's what the same suggests: An Elements
		...It contains Name and Episodes of a particular anime
		...Every element has it's own unique key
	"""
	text = ListProperty(["","?","?"])