import kivy
import sys
import requests
import serial
import time
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup
from pathlib import Path
from kivy.clock import Clock
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout

##port = '/dev/ttyACM0'
##
##sFA = serial.Serial(port,115200)
##sFA.flushInput()

#constants declaration
x = 100
y = 100
x_size = 200
y_size = 200
step = 20
ApiCall_pos = 'http://10.240.166.254:5000/1,100'
ApiCall_neg = 'http://10.240.166.254:5000/-1,100'
number = 0

def callback(instance):
    global x
    global y
    global x_size
    global y_size
    if instance.text == 'QUIT':
        sys.exit()
    if instance.text == 'MOTOR UP':
        print('hola')
	#sFA.write((str(4)+'\r').encode())
	#sFA.write((str(1)+'\r').encode())
	#sFA.write((str(300)+'\r').encode())
       # r = requests.get(ApiCall_pos)
    if instance.text == 'MOTOR DOWN':
        print('hola')
	#sFA.write((str(4)+'\r').encode())
	#sFA.write((str(-1)+'\r').encode())
	#sFA.write((str(300)+'\r').encode())
        #r = requests.get(ApiCall_neg)

def switchFunction(instance, value):
    global switch_boolean
    if value == True:
        switch_boolean = True
    if value == False:
        switch_boolean = False

class AdjustImage(BoxLayout):
    def __init__(self, **kwargs):
        super(AdjustImage,self).__init__(**kwargs)
        #Main Row
        self.cols = 3

        self.f = FloatLayout()
        self.s = Scatter()
        self.l =  Image(source='chip.png',size=(400,400),allow_stretch=True,keep_data=True)
        print(self.l.pos)

        #b = BoxLayout(orientation='vertical')
        t = Button(text="<-",size_hint=(None,None),size=(75,50),pos_hint= {'left': 1, 'bottom': 1},background_color= (0, 0, 0, 0))
        t.bind(on_press = self.Transition_Back)

        t2 = Button(text="Save",size_hint=(None,None),size=(75,50),pos_hint= {'left': 1, 'bottom': 1},background_color= (0, 0, 0, 0))
        t2.bind(on_press = self.SaveLayout)


        self.f.add_widget(self.s)
        self.s.add_widget(self.l)

        self.add_widget(t)
        self.add_widget(t2)
        self.add_widget(self.f)


    # def on_touch_move(self, touch):
    #     print(touch.pos)
    def SaveLayout(self,instance):
        global x
        global y
        global x_size
        global y_size
        print("POS")
        print(self.s.pos)
        print("SIZE")
        print(self.s.size)
        #print("SCALE")
        #print(self.s.scale)
        print("BBOX")
        print(self.s.bbox)
        print("\n")



    def Transition_Back(self, instance):
        PhonePrinter_App.screen_manager.current = 'Settings'
        PhonePrinter_App.screen_manager.transition.direction = 'right'



class TestMotor(GridLayout):
    def __init__(self, **kwargs):
        super(TestMotor,self).__init__(**kwargs)

        self.rows = 2
        #Back Button
        self.Back_Button = Button(text="BACK")
        self.Back_Button.bind(on_press = self.Transition_Back)
        self.add_widget(self.Back_Button)

        self.buttons = GridLayout(cols=2)

        JButton = Button(text='MOTOR UP',font_size=40)
        JButton.bind(on_press=callback)
        self.buttons.add_widget(JButton)

        NButton = Button(text='MOTOR DOWN',font_size=40)
        NButton.bind(on_press=callback)
        self.buttons.add_widget(NButton)

        self.add_widget(self.buttons)

    def Transition_Back(self, instance):
        PhonePrinter_App.screen_manager.current = 'MainScreen'
        PhonePrinter_App.screen_manager.transition.direction = 'right'

class TestImage(GridLayout):
    def __init__(self, **kwargs):
        super(TestImage,self).__init__(**kwargs)

        self.cols = 1
        self.image = Image(allow_stretch= True,source='slices/out0400.png',size_hint=(x_size,y_size),pos_hint={'center_x': x, 'center_y': y})
        self.image.bind()
        self.add_widget(self.image)

class PrintScreen(GridLayout):
    def __init__(self, **kwargs):
        super(PrintScreen,self).__init__(**kwargs)

        self.cols = 1
        image_file_source = Path('slices/out' + str(0).zfill(4) + '.png')
        self.image = Image(allow_stretch= True,source = str(image_file_source), size_hint = (x_size,y_size), pos_hint = {'center_x': x, 'center_y': y})
        self.image.bind()
        self.add_widget(self.image)
        #HOW MUCH DELAY
        Clock.schedule_interval(self.update_pic,.1)

    def update_pic(self,dt):
        global number
        number += 1
        image_file_source = Path('slices/out' + str(number).zfill(4) + '.png')
        if image_file_source.is_file():
            self.image = Image(allow_stretch= True,source = str(image_file_source), size_hint = (x_size,y_size), pos_hint = {'center_x': x, 'center_y': y})
            self.image.bind()
            self.clear_widgets()
            self.add_widget(self.image)
            #DELAY???
            #r = requests.get(ApiCall_pos)
        else:
            Clock.unschedule(self.update_pic)
            PhonePrinter_App.screen_manager.current = 'MainScreen'

class Settings(GridLayout):
    def __init__(self, **kwargs):
        super(Settings,self).__init__(**kwargs)

        #Main Rows for buttons
        self.rows = 4

        #Back Button
        self.Back_Button = Button(text="BACK")
        self.Back_Button.bind(on_press = self.Transition_Back)
        self.add_widget(self.Back_Button)

        #Adjust Image Button
        self.AdjustImage_Button = Button(text="ADJUST IMAGE")
        self.AdjustImage_Button.bind(on_press = self.Transition_AdjustImage)
        self.add_widget(self.AdjustImage_Button)

        #Test Motor Button
        self.TestMotor_Button = Button(text="TEST MOTORS")
        self.TestMotor_Button.bind(on_press = self.Transition_TestMotor)
        self.add_widget(self.TestMotor_Button)

        #Test Image Button
        self.TestImage_Button = Button(text="TEST IMAGE")
        self.TestImage_Button.bind(on_press = self.Transition_TestImage)
        self.add_widget(self.TestImage_Button)

    def Transition_Back(self, instance):
        PhonePrinter_App.screen_manager.current = 'MainScreen'
        PhonePrinter_App.screen_manager.transition.direction = 'right'

    def Transition_AdjustImage(self, instance):
        PhonePrinter_App.screen_manager.current = 'AdjustImage'
        PhonePrinter_App.screen_manager.transition.direction = 'left'

    def Transition_TestMotor(self, instance):
        PhonePrinter_App.screen_manager.current = 'TestMotor'
        PhonePrinter_App.screen_manager.transition.direction = 'left'

    def Transition_TestImage(self, instance):
        PhonePrinter_App.screen_manager.current = 'TestImage'
        PhonePrinter_App.screen_manager.transition.direction = 'left'


class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen,self).__init__(**kwargs)

        #Main Rows for buttons
        self.rows = 3

        #Print Button
        self.Print_Button = Button(text="PRINT")
        self.Print_Button.bind(on_press = self.Transition_Print)
        self.add_widget(self.Print_Button)

        #Settings Button
        self.Settings_Button = Button(text="SETTINGS")
        self.Settings_Button.bind(on_press = self.Transition_Settings)
        self.add_widget(self.Settings_Button)

        #Quit Button
        self.Quit_Button = Button(text="QUIT")
        self.Quit_Button.bind(on_press = callback)
        self.add_widget(self.Quit_Button)

    def Transition_Print(self, instance):
        PhonePrinter_App.screen_manager.current = 'Print'
        PhonePrinter_App.screen_manager.transition.direction = 'left'

    def Transition_Settings(self, instance):
        PhonePrinter_App.screen_manager.current = 'Settings'
        PhonePrinter_App.screen_manager.transition.direction = 'left'


class PhonePrinter(App):
    def build(self):

        #Declare Screen Manager
        self.screen_manager = ScreenManager()

        #Main Screen
        self.connect_page = MainScreen()
        screen = Screen(name='MainScreen')
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        #Adjust Image Screen
        self.info_page = AdjustImage()
        screen = Screen(name='AdjustImage')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        #Test Motors Screen
        self.info_page = TestMotor()
        screen = Screen(name='TestMotor')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        #Test Image Screen
        self.info_page = TestImage()
        screen = Screen(name='TestImage')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        #Print Screen
        self.info_page = PrintScreen()
        screen = Screen(name='Print')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        #Settings Screen
        self.info_page = Settings()
        screen = Screen(name='Settings')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)


        #Return
        return self.screen_manager


if __name__ == "__main__":
    PhonePrinter_App = PhonePrinter()
    PhonePrinter_App.run()
