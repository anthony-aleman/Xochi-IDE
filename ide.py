import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.splitter import Splitter


# '''
#
#
# TODO:  figure out how to assemble this tree dictionary using the OS module to organize the files within the current
# TODO: directory being edited. Node id is the file name with extension it will only have children if
#  '''

def initialize_tree(root_dir):
    pass


tree = {'node_id': '1',
        'children': [{'node_id': '1.1',
                      'children': [{'node_id': '1.1.1',
                                    'children': [{'node_id': '1.1.1.1',
                                                  'children': []}]},
                                   {'node_id': '1.1.2',
                                    'children': []},
                                   {'node_id': '1.1.3',
                                    'children': []}]},
                     {'node_id': '1.2',
                      'children': []}]}


def populate_treeview(treeview, parent, node):
    if parent is None:
        tree_node = treeview.add_node(TreeViewLabel(text=node['node_id'],
                                                    is_open=True))
    else:
        tree_node = treeview.add_node(TreeViewLabel(text=node['node_id'],
                                                    is_open=True), parent)

    for child_node in node['children']:
        populate_treeview(treeview, tree_node, child_node)


class MyIDE(GridLayout):
    # initialize with as many keywords
    def __init__(self, **kwargs):
        # constructor
        super(MyIDE, self).__init__(**kwargs)

        # setting the columns
        self.cols = 2

        # setting the file structure
        self.files = TreeView(root_options=dict(text='Files'), size_hint_x=None, width=200)
        populate_treeview(self.files, None, tree)


        # setting the text editor
        self.text_editor = GridLayout()
        self.text_editor.cols = 1
        self.text_editor.add_widget(TextInput(multiline=True, size_hint_y=None, height=500))

        # adding splitters
        self.splitter_top = Splitter()
        self.splitter_top.sizable_from = 'left'
        self.splitter_top.add_widget(self.text_editor)

        # adding the text editor the window
        self.add_widget(self.files)
        self.add_widget(self.splitter_top)



class MyApp(App):
    def build(self):
        return MyIDE()


if __name__ == '__main__':
    MyApp().run()
