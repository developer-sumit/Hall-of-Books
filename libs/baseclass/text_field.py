
__all__ = ("RoundTextField",)


from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty


Builder.load_string(
"""
<RoundTextField>
	elevation: 15
	radius: [10]
	size_hint_y: None
	height: dp(40)
	TextInput:
		id: text_input
		halign: "center"
		multiline: False
		hint_text: root.hint_text
		background_color: (0,0,0,0)

"""
)


class RoundTextField(MDCard):
	"""
	:::RoundTextField:::
		...Custom Text Field
		...Height in dp (in short fixed, won't change according to device)
	"""

	hint_text = StringProperty()
	"""
	A blur text which gives the user a hint about
	what to type in the given field

	:::Example:::
		...py...
		element = RoundTextField()
		element.hint_text = "e.g.devil001@gmail.com"
		
		...kv...
		RoundTextField:
			hint_text: "e.g.devil001@gmail.com"
	"""
