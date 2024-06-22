import tkinter as tk

from MovingText import MovingText
from UserEntry import UserEntry
from Timer import Timer
from RetryButton import RetryButton
from StatsFrame import StatsFrame
from WidgetModel import WidgetModel


class MainFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):   # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outermost frame
        self.parent = parent
        self.parent.title("The Ultimate Typing Test")
        self.pack(anchor=tk.CENTER)
        self.parent.config(bg='lightseagreen')
        self.parent.minsize(960, 340)

        # get the data and create an instance of WidgetModel (that holds all persistent data)
        self.widgetModel = WidgetModel()
        self.typingFont = "Raleway"

        # configure the frames
        self.timer = Timer(self)
        self.timer.pack(anchor=tk.CENTER, pady=(10, 10))
        
        self.movingText = MovingText(self)
        self.movingText.pack(anchor=tk.CENTER)
        self.movingText.grid_propagate(0)

        self.entry = UserEntry(self)
        self.entry.pack(anchor=tk.CENTER, pady=(30, 0))

        self.retryButton = RetryButton(self)
        self.retryButton.pack(anchor=tk.CENTER, pady=(10, 65))

        self.statsFrame = StatsFrame(self)
        self.statsFrame.place(relx=1.0, rely=1.0, x=0, y=-159, anchor="ne")

    def totalReset(self):
        self.widgetModel.reset()
        self.movingText.reset()
        self.entry.reset()
        self.timer.reset()

    def newTopicReset(self, new_words):
        self.widgetModel.reset(new_words)
        self.movingText.reset()
        self.entry.reset()
        self.timer.reset()


if __name__ == "__main__":
    root = tk.Tk()
    MainFrame(root)
    root.mainloop()
