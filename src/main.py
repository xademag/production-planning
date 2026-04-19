import clr
import sys
import os
from System import Action
from System.Windows import Application
from System.Windows.Markup import XamlReader

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_DIR = os.path.join(BASE_DIR, 'ui')
PAGES_DIR = os.path.join(UI_DIR, 'pages')


def load_xaml_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def load_xaml(path):
    xaml_text = load_xaml_text(path)
    return XamlReader.Parse(xaml_text)


if __name__ == '__main__':
    window_path = os.path.join(UI_DIR, 'main_window.xaml')
    window = load_xaml(window_path)

    def navigate_to(page_file):
        frame = window.FindName('MainFrame')
        page = load_xaml(os.path.join(PAGES_DIR, page_file))
        frame.Navigate(page)

    def on_home(sender, args):
        navigate_to('home_page.xaml')

    def on_data(sender, args):
        # load JSON names into the list on the data page
        navigate_to('data_page.xaml')
        # small delay may be needed; try to find the ListBox and populate
        frame = window.FindName('MainFrame')
        current = frame.Content
        try:
            listbox = current.FindName('DataList')
            data_dir = os.path.join(os.path.dirname(BASE_DIR), 'data')
            if not os.path.exists(data_dir):
                data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
            files = []
            if os.path.exists(data_dir):
                for f in os.listdir(data_dir):
                    if f.lower().endswith('.json'):
                        files.append(f)
            listbox.ItemsSource = files
        except Exception:
            pass

    def on_exit(sender, args):
        app.Shutdown()

    # wire events
    try:
        window.FindName('BtnHome').Click += on_home
        window.FindName('BtnData').Click += on_data
        window.FindName('BtnExit').Click += on_exit
    except Exception:
        pass

    app = Application()
    navigate_to('home_page.xaml')
    app.Run(window)
