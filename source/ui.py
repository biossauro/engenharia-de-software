import tkinter as tk
from source.constants import *


class UserInterface:
    def __init__(self, predict, show_data, get_performance):
        self.root = tk.Tk()
        self.root.title('Tic-Tac-Toe')
        self.root.geometry('600x650')
        self.root.resizable(True, True)
        self.root.configure(background=GRAY)
        self.turn = 'x'
        self.request_prediction = predict
        self.request_data = show_data
        self.request_performance = get_performance
        self.__create_game_buttons()
        self.__create_other_buttons()

    def menu(self):
        self.root.mainloop()

    def __create_game_buttons(self):
        self.buttons = []
        for i in range(9):
            self.buttons.append(tk.Button(self.root, text='', width=10, height=4, font=('Courier', 24, 'bold'), fg=WHITE,
                                          bg=DARK_GRAY, activeforeground=WHITE, activebackground=DARK_GREEN,
                                          command=lambda i=i: self.__button_click(i)))
            self.buttons[i].grid(row=i // 3, column=i % 3)

    def __create_other_buttons(self):
        # breakln
        text = tk.Label(self.root, background=GRAY)
        text.grid(row=4, columnspan=3)
        # Predict
        predict_button = tk.Button(self.root, text='Predict', font=('Courier', 12, 'bold'), fg=WHITE,
                                   bg=DARK_GRAY, activeforeground=WHITE, activebackground=DARK_GREEN,
                                   command=self.__predict)
        predict_button.grid(row=5, column=0)
        # Reset
        reset_button = tk.Button(self.root, text='Reset', font=('Courier', 12, 'bold'), fg=WHITE,
                                 bg=DARK_GRAY, activeforeground=WHITE, activebackground=DARK_GREEN,
                                 command=self.__reset)
        reset_button.grid(row=5, column=1)
        # Quit
        quit_button = tk.Button(self.root, text='Quit', font=('Courier', 12, 'bold'), fg=WHITE,
                                bg=DARK_GRAY, activeforeground=WHITE, activebackground=DARK_GREEN,
                                command=self.__quit)
        quit_button.grid(row=5, column=2)
        # breakln
        text = tk.Label(self.root, background=GRAY)
        text.grid(row=6, columnspan=2)
        # Data
        data_button = tk.Button(self.root, text='Data', font=('Courier', 12, 'bold'), fg=WHITE,
                                bg=DARK_GRAY, activeforeground=WHITE, activebackground=DARK_GREEN,
                                command=self.request_data)
        data_button.grid(row=7, column=0)
        # Performance
        performance_button = tk.Button(self.root, text='Performance', font=('Courier', 12, 'bold'), fg=WHITE,
                                       bg=DARK_GRAY, activeforeground=WHITE, activebackground=DARK_GREEN,
                                       command=self.__show_performance)
        performance_button.grid(row=7, column=1)

    def __button_click(self, index):
        if self.buttons[index].cget('text') == '':
            if self.turn == 'x':
                self.buttons[index].configure(text='x', fg=BLUE, bg=DARK_GRAY,
                                              activeforeground=WHITE, activebackground=DARK_BLUE)
                self.turn = 'o'
            else:
                self.buttons[index].configure(text='o', fg=RED, bg=DARK_GRAY,
                                              activeforeground=WHITE, activebackground=DARK_RED)
                self.turn = 'x'

    def __predict(self):
        data = []
        for button in self.buttons:
            if button.cget('text') == 'x':
                data.append('x')
            elif button.cget('text') == 'o':
                data.append('o')
            else:
                data.append('b')
        results = self.request_prediction(data)
        self.__show_results(results)

    def __show_results(self, results):
        root = tk.Tk()
        root.title('Results')
        root.geometry('400x150')
        root.resizable(False, False)
        root.configure(background=GRAY)
        label = tk.Label(root, font=('Courier', 24, 'bold'), fg=WHITE)
        if results == [1]:
            label.configure(text='According to the AI,\n"X" won!',
                            bg=DARK_BLUE)
        elif results == [-1]:
            label.configure(text='According to the AI, \nit\'s either a tie\nor "O" won!',
                            bg=DARK_RED)
        label.pack()
        ok_button = tk.Button(root, text='OK', font=('Courier', 12, 'bold'), fg=WHITE, bg=DARK_GRAY,
                              activeforeground=WHITE, activebackground=DARK_GREEN,
                              command=root.destroy)
        ok_button.pack()

    def __reset(self):
        for button in self.buttons:
            button.configure(text='', fg=WHITE, bg=DARK_GRAY,
                             activeforeground=WHITE, activebackground=DARK_GREEN)
        self.turn = 'x'

    def __quit(self):
        self.root.destroy()

    def __show_performance(self):
        performance = self.request_performance()
        display_text = 'Performance\n\n' + \
            f'CV: {round(performance["cv"], 2)}\n' + \
            f'R2 Treino: {round(performance["r2_training"], 2)}\n' + \
            f'R2 Teste: {round(performance["r2_testing"], 2)}\n' + \
            f'RMSE: {round(performance["rmse"], 2)}\n'
        root = tk.Tk()
        root.title('Performance')
        root.geometry('400x400')
        root.resizable(False, False)
        root.configure(background=GRAY)
        label = tk.Label(root, font=('Courier', 24, 'bold'), fg=DARK_GRAY)
        label.configure(text=display_text, bg=GRAY)
        label.pack()
        ok_button = tk.Button(root, text='OK', font=('Courier', 12, 'bold'), fg=WHITE, bg=DARK_GRAY,
                              activeforeground=WHITE, activebackground=DARK_GREEN,
                              command=root.destroy)
        ok_button.pack()
