import tkinter as tk
from tkinter import ttk


class UserInterface(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title('Timer Simulator')
        self.pack(fill=tk.BOTH, expand=True)
        self.__create_widgets()
        self.controller = None

    def __create_widgets(self):
        # Stop Button
        self.stop_button = ttk.Button(self, text='Stop')
        self.stop_button.config(command=self.stop_button_clicked)
        self.stop_button.pack(side=tk.BOTTOM, fill=tk.X)
        # Timer Value (Input)
        self.timer_value = tk.StringVar()
        self.timer_value.set('15')
        self.timer_value_entry = ttk.Entry(self)
        self.timer_value_entry.config(textvariable=self.timer_value)
        self.timer_value_entry.pack(side=tk.BOTTOM, fill=tk.X)
        # Semaphore Checkbox (Input)
        self.semaphore_checkbox = tk.IntVar()
        self.semaphore_checkbox.set(0)
        self.semaphore_checkbutton = ttk.Checkbutton(self, text='Semaphore')
        self.semaphore_checkbutton.config(variable=self.semaphore_checkbox)
        self.semaphore_checkbutton.pack(side=tk.BOTTOM, fill=tk.X)
        # Timer Button
        self.timer_button = ttk.Button(self, text='Start Timer')
        def timer(): return int(self.timer_value.get())
        def use_semaphore(): return self.semaphore_checkbox.get()
        def command(): return self.timer_button_clicked(timer(), use_semaphore())
        self.timer_button.config(command=command)
        self.timer_button.pack(side=tk.BOTTOM, fill=tk.X)
        # Error Message
        self.error_message = tk.StringVar()
        self.error_message.set('')
        self.error_message_label = ttk.Label(self)
        self.error_message_label.config(textvariable=self.error_message)
        self.error_message_label.pack(side=tk.BOTTOM, fill=tk.X)
        # Checks if the timer value is a valid integer
        self.timer_value_entry.config(validate='key')
        args = (self.register(self.validate_timer_value), '%d', '%i', '%P')
        self.timer_value_entry.config(validatecommand=args)

    def set_controller(self, controller):
        self.controller = controller

    def stop_button_clicked(self):
        self.controller.stop()

    def timer_button_clicked(self, time, use_semaphore):
        self.controller.new_timer(time, use_semaphore)

    def set_error_message(self, message):
        self.error_message.set(message)
        self.after(1000, lambda: self.error_message.set(''))

    def validate_timer_value(self, action, index, value):
        if value == '':
            self.timer_value.set('0')
            return True
        try:
            int(value)
        except ValueError:
            self.set_error_message('Timer value must be an integer')
            return False
        return True
