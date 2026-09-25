from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Intent = autoclass('android.content.Intent')
    VpnService = autoclass('android.net.VpnService')

class TigerBlockUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        self.label = Label(
            text="TigerBlock\nجدار الحماية بدون Root", 
            font_size='20sp',
            halign='center'
        )
        self.add_widget(self.label)

        btn_start = Button(
            text="تفعيل حظر المنافذ والتطبيقات", 
            size_hint=(1, 0.3)
        )
        btn_start.bind(on_press=self.start_vpn)
        self.add_widget(btn_start)

    def start_vpn(self, instance):
        if platform == 'android':
            activity = PythonActivity.mActivity
            intent = VpnService.prepare(activity)
            
            if intent is not None:
                activity.startActivityForResult(intent, 0)
                self.label.text = "يرجى منح إذن الـ VPN للتطبيق"
            else:
                self.run_vpn_service(activity)
        else:
            self.label.text = "التطبيق يعمل فقط على أجهزة أندرويد"

    def run_vpn_service(self, activity):
        service_intent = Intent(activity, autoclass('org.tigerblock.BlockVpnService'))
        activity.startService(service_intent)
        self.label.text = "تم تفعيل حظر المنافذ بنجاح!"

class TigerBlockApp(App):
    def build(self):
        return TigerBlockUI()

if __name__ == '__main__':
    TigerBlockApp().run()