from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget





class UserInterface(Widget):
    #def __init__(self, **kwargs):
     #   super(UserInterface).__init__(**kwargs)

    
    pass




class NirsUiApp(App):
    def build (self):
        return UserInterface()


         #return FunkyButton(
          #   text="Hellou, Start here",
           #  pos=(100,100),
            # size_hint=(None,None),
            # size=(500,500)
        #)

        # return FunkyButton2(
        #     #  text="nappi2",
        #     #  pos=(400,400),
        #     #  size_hint=(.5,.5)
        #     )
        
            






if __name__ == '__main__':
    NirsUiApp().run()
