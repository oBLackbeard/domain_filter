import threading


class Attak(object):
    def __init__(self, view):
        super().__init__()
        self.view = view

    def launch(self, mailliste_file):
        lau = Start(self.view, mailliste_file)
        lau.start()


class Start(threading.Thread):
    def __init__(self, view, mailliste_file):
        threading.Thread.__init__(self)

        self.threadID = 1
        self.name = "AttackThread"
        self.view = view
        self.mailliste_file = mailliste_file

    def run(self):
        self.view.clear_output()
        self._open_file()

    def _open_file(self):
        with open((self.mailliste_file), errors='ignore') as (f):
            lines = f.read().split('\n')
            for line in lines:
                try:
                    if line.count('.fr') == 1:
                        self.view.display_output(line, update_task=True)
                    else:
                        pass
                except:
                    pass
