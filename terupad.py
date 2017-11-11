#-*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.button import Button

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

from kivy.config import Config
Config.set('graphics', 'width', '340')
Config.set('graphics', 'height', '450')

resource_add_path('./fonts')
LabelBase.register(DEFAULT_FONT, 'GenEiGothicN-SemiBold.otf')

hiragana = ['あいうえお','かきくけこ','さしすせそ','たちつてと','なにぬねの',
            'はひふへほ','まみむめも','やゆよー〜','らりるれろ','わをん、。']
hiragana2 = ['がぎぐげご','ざじずぜぞ','だぢづでど', 'ばびぶべぼ', 'ぱぴぷぺぽ',
              'ぁぃぅぇぉ','ゃゅょ','っ']
katakana = ['アイウエオ','カキクケコ','サシスセソ','タチツテト','ナニヌネノ',
            'ハヒフヘホ','マミムメモ','ヤユヨー〜','ラリルレロ','ワヲン、。']
katakana2 = ['ガギグゲゴ','ザジズゼゾ','ダヂヅデド','バビブベボ','パピプペポ',
              'ァィゥェォ','ャュョ','ッ']

kigou = ['「」！？']

class TeruPadRootLayout(BoxLayout):
    pass

class TeruPadTextViewLayout(BoxLayout):
    pass

class TeruPadModeButtonLayout(BoxLayout):
    pass

class TeruPadKeyScreenManager(ScreenManager):
    pass

def AddKeyPadWidgets(key_letters):
    box_layout = BoxLayout(orientation='vertical')
    for line in key_letters:
        grid_layout = GridLayout(cols=5)
        for letter in list(line):
            button = Button(text=letter)
            button.bind(on_press=App.get_running_app().press_key)
            grid_layout.add_widget(button)
        box_layout.add_widget(grid_layout)
    return box_layout

class TeruPadHiraganaScreen(Screen):
    def __init__(self, **kwargs):
        super(TeruPadHiraganaScreen, self).__init__(**kwargs)
        self.add_widget(AddKeyPadWidgets(hiragana))

class TeruPadHiragana2Screen(Screen):
    def __init__(self, **kwargs):
        super(TeruPadHiragana2Screen, self).__init__(**kwargs)
        self.add_widget(AddKeyPadWidgets(hiragana2))

class TeruPadKatakanaScreen(Screen):
    def __init__(self, **kwargs):
        super(TeruPadKatakanaScreen, self).__init__(**kwargs)
        self.add_widget(AddKeyPadWidgets(katakana))

class TeruPadKatakana2Screen(Screen):
    def __init__(self, **kwargs):
        super(TeruPadKatakana2Screen, self).__init__(**kwargs)
        self.add_widget(AddKeyPadWidgets(katakana2))

class TeruPadKigouScreen(Screen):
    def __init__(self, **kwargs):
        super(TeruPadKigouScreen, self).__init__(**kwargs)
        self.add_widget(AddKeyPadWidgets(kigou))

class TeruPadApp(App):
    def press_hiragana(self):
        if self.root.ids.terupad_sm.current == 'hiragana':
            self.root.ids.terupad_sm.current = 'hiragana2'
        else:
            self.root.ids.terupad_sm.current = 'hiragana'
            
    def press_katakana(self):
        if self.root.ids.terupad_sm.current == 'katakana':
            self.root.ids.terupad_sm.current = 'katakana2'
        else:
            self.root.ids.terupad_sm.current = 'katakana'

    def press_kigou(self):
        self.root.ids.terupad_sm.current = 'kigou'

    def press_key(self, instance):
        self.root.ids.text_view.ids.text_input.insert_text(instance.text)

    def press_copy(self):
        text_input = self.root.ids.text_view.ids.text_input
        text_input.copy(data=text_input.text)

    def press_clear(self):
        text_input = self.root.ids.text_view.ids.text_input
        text_input.text = ""

if __name__ == '__main__':
    TeruPadApp().run()
