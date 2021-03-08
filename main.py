from kivy.app import App
from kivy.core.spelling import Spelling
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.graphics import Color,Rectangle



class MyLayout(BoxLayout):
    def __init__(self,**kwargs):
        super(MyLayout,self).__init__(**kwargs)
        self.s=Spelling()

        #list languages
        #print(self.s.list_languages())

        #select language
        self.s.select_language('en_US')
    
    def check(self,word,*args):
        self.ids.result.canvas.before.clear()
        self.ids.result.text=""
        self.ids.word.text=""
        if word:
            with self.ids.result.canvas.before:
                Color(0,0.7,0.9,1)
                Rectangle(size=self.ids.result.size,pos=self.ids.result.pos)
            if self.s.check(word):
                self.ids.result.text="Correct"
            else:
                self.ids.result.text="Incorrect"

    
    def suggest_words(self,frag,*args):
        self.ids.result.canvas.before.clear()
        self.ids.result.text=""
        self.ids.fragment.text=""
        if frag:
            with self.ids.result.canvas.before:
                Color(0,0.7,0.9,1)
                Rectangle(size=self.ids.result.size,pos=self.ids.result.pos)
            suggestions= self.s.suggest(frag)
            if suggestions:
                string=""
                for i in range(10):
                   string+=suggestions[i]+" "
                self.ids.result.text=string


class SpellApp(App):
    
    def build(self):
        self.title="Spell App By Aniket Thani"
        return MyLayout()

if __name__=="__main__":
    Window.clearcolor=(0.7,0,0,1)
    SpellApp().run()

