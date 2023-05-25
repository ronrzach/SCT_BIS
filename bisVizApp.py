from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from bisviz_interface import bisviz
from kivymd.uix.pickers import MDDatePicker, MDTimePicker

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        layout = BoxLayout(orientation='vertical', padding=20)
        logo = Image(source='UI_Logo_1.png', size_hint=(1, 0.5))
        layout.add_widget(logo)

        start_date_button = Button(text="Choose Start Date")
        start_date_button.bind(on_press=self.show_start_date_picker)
        layout.add_widget(start_date_button)

        end_date_button = Button(text="Choose End Date")
        end_date_button.bind(on_press=self.show_end_date_picker)
        layout.add_widget(end_date_button)

        start_time_button = Button(text="Choose Start Time")
        start_time_button.bind(on_press=self.show_start_time_picker)
        layout.add_widget(start_time_button)

        end_time_button = Button(text="Choose End Time")
        end_time_button.bind(on_press=self.show_end_time_picker)
        layout.add_widget(end_time_button)


        bis_thresh_box = BoxLayout(orientation='horizontal')
        bis_thresh_label = MDLabel(text='Enter BIS Threshold value : ')
        bis_thresh_box.add_widget(bis_thresh_label)
        self.bis_thresh_input = MDTextField()
        bis_thresh_box.add_widget(self.bis_thresh_input)
        layout.add_widget(bis_thresh_box)

        time_thresh_box = BoxLayout(orientation='horizontal')
        time_thresh_label = MDLabel(text='Enter Time Threshold value : ')
        time_thresh_box.add_widget(time_thresh_label)
        self.time_thresh_input = MDTextField()
        time_thresh_box.add_widget(self.time_thresh_input)
        layout.add_widget(time_thresh_box)

        csv_spa_box = BoxLayout(orientation='horizontal')
        csv_spa_label = MDLabel(text='CSV or SPA : ')
        csv_spa_box.add_widget(csv_spa_label)
        self.csv_spa_input = MDTextField()
        csv_spa_box.add_widget(self.csv_spa_input)
        layout.add_widget(csv_spa_box)

        button = Button(text='Choose File')
        button.bind(on_press=self.choose_file)
        layout.add_widget(button)
        self.file_manager = MDFileManager()
        self.file_manager.exit_manager = self.exit_manager
        self.file_manager.select_path = self.select_path

        return layout

    def show_start_date_picker(self, instance):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_start_date_save)
        date_dialog.open()

    def on_start_date_save(self, instance, value, date_range):
        self.start_date = str(value.strftime('%m/%d/%Y'))
        print(str(self.start_date))

    def show_end_date_picker(self, instance):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_end_date_save)
        date_dialog.open()

    def on_end_date_save(self, instance, value, date_range):
        self.end_date = str(value.strftime('%m/%d/%Y'))
        print(str(self.end_date))

    def show_start_time_picker(self, instance):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.on_start_time_save)
        time_dialog.open()

    def on_start_time_save(self, instance, value):
        self.start_time = str(value.strftime('%H:%M'))
        print(str(self.start_time))

    def show_end_time_picker(self, instance):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.on_end_time_save)
        time_dialog.open()

    def on_end_time_save(self, instance, value):
        self.end_time = str(value.strftime('%H:%M'))
        print(str(self.end_time))




    def choose_file(self, instance):
        self.file_manager.show('/')

    def exit_manager(self, *args):
        self.file_manager.close()

    def select_path(self, path):
        self.file_path = path
        bisviz(self.start_date, self.start_time, self.end_date, self.end_time, self.bis_thresh_input.text, self.time_thresh_input.text, self.file_path, self.csv_spa_input.text)
        self.exit_manager()

MyApp().run()