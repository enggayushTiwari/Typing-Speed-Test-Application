import tkinter as tk
from tkinter import ttk


class StatsFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # parent is the root
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # configurations for the outer-most frame
        self.parent = parent
        self.widgetModel = self.parent.widgetModel

        self.config(bg='black', relief=tk.RAISED, bd=4)

        # create stats elements
        self.lastRunLabel, self.lastRunDivider = None, None
        self.wpmScoreLabel = None
        self.accuracyScoreLabel = None
        self.divider, self.divider2 = None, None

        self.createLabels()
        self.update_self()
        
    def createLabels(self):
        self.lastRunLabel = tk.Label(self, text="Last Run", font=(self.parent.typingFont, 14), bg="black",
                                       fg='white')
        self.lastRunLabel.grid(row=0, column=0, pady=(2, 0))
        self.lastRunDivider = ttk.Separator(self, orient='horizontal')
        self.lastRunDivider.grid(row=1, column=0, ipadx=65)
        self.wpmScoreLabel = tk.Label(self, text="Wpm: 0", font=(self.parent.typingFont, 14), bg="black",
                                      fg='white')
        self.wpmScoreLabel.grid(row=2, column=0)
        self.accuracyScoreLabel = tk.Label(self, text="Acc: 0%", font=(self.parent.typingFont, 14), bg="black",
                                      fg='white')
        self.accuracyScoreLabel.grid(row=3, column=0)

    def createHighscoreLabels(self):
        self.divider = ttk.Separator(self, orient='vertical')
        self.divider.grid(row=0, column=1, rowspan=5, sticky='e', ipady=75)

        self.divider2 = ttk.Separator(self, orient='horizontal')
        self.divider2.grid(row=1, column=2, sticky='e', ipadx=65)


    def calculateWpm(self):
        num_of_words = (self.widgetModel.char_count / 5.0)
        wpm = round(num_of_words - self.widgetModel.mistyped_word_count, 2)
        if wpm < 0:
            wpm = 0
        return wpm

    def calculateAccuracy(self):
        total_correct_char = self.widgetModel.char_count
        total_char = (self.widgetModel.char_count + self.widgetModel.mistyped_char_count)
        if total_char == 0:
            return 0.0
        return round((total_correct_char / float(total_char)) * 100.0, 2)
    
    def update_self(self):
        if self.widgetModel.started and self.widgetModel.ended:
            # update the words per minute stat
            new_wpm = self.calculateWpm()
            self.wpmScoreLabel.config(text="Wpm: {}".format(str(new_wpm)))
            self.accuracyScoreLabel.config(text="Acc: {}%".format(str(self.calculateAccuracy())))
        self.parent.parent.after(100, self.update_self)