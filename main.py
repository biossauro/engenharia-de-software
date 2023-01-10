import tkinter as tk
import sys
from source.scheduling.fcfs import FCFS
from source.scheduling.round_robin import RoundRobin
from source.utils.cli import cls
from source.utils.palette import *
from source.utils.settings import RESOLUTION


class CRUD:
    def __init__(self):
        cls()
        self._ready_queue = None
        self._queueing = False

    def main_menu(self):
        root = tk.Tk()
        root.title("Simulador de Fila de Prontos")
        root.geometry(RESOLUTION)
        root.resizable(False, False)
        root.configure(background=GRAY)
        label = tk.Label(root, text="Simulador de Ready Queue",
                         fg=BLACK, bg=GRAY, font=("Helvetica", 16))
        label.pack()
        button1 = tk.Button(root, text="Iniciar Fila de Prontos",
                            fg=WHITE, bg=BLACK,
                            command=self._start_ready_queue)
        button1.pack()
        button2 = tk.Button(root, text="Novo Processo",
                            fg=WHITE, bg=BLACK,
                            command=self._get_burst_time)
        button2.pack()
        button3 = tk.Button(root, text="Parar Fila de Prontos",
                            fg=WHITE, bg=BLACK,
                            command=self._stop_ready_queue)
        button3.pack()
        button4 = tk.Button(root, text="Sair",
                            fg=WHITE, bg=BLACK,
                            command=self._exit)
        button4.pack()
        root.mainloop()

    def _show_warning(self, message):
        root = tk.Tk()
        root.title("AVISO")
        root.geometry(RESOLUTION)
        root.resizable(False, False)
        root.configure(background=GRAY)
        label = tk.Label(root, text=message,
                         fg=BLACK, bg=GRAY,
                         font=("Helvetica", 12))
        label.pack()
        button = tk.Button(root, text="OK",
                           fg=WHITE, bg=BLACK,
                           command=root.destroy)
        button.pack()
        root.mainloop()

    def _start_ready_queue(self):
        if not self._queueing:
            root = tk.Tk()
            root.title("Tipo de Fila")
            root.geometry(RESOLUTION)
            root.resizable(False, False)
            root.configure(background=GRAY)
            label = tk.Label(root, text="Tipo de Fila",
                             fg=BLACK, bg=GRAY,
                             font=("Helvetica", 20))
            label.pack()
            button1 = tk.Button(root, text="FCFS",
                                fg=WHITE, bg=BLACK,
                                command=lambda: self._fcfs_queue(root))
            button1.pack()
            button2 = tk.Button(root, text="Round Robin",
                                fg=WHITE, bg=BLACK,
                                command=lambda: self._get_quantum_time(root))
            button2.pack()
            root.mainloop()
        else:
            self._show_warning("Fila de Prontos já em execução!")

    def _fcfs_queue(self, parent):
        self._ready_queue = FCFS()
        self._queueing = True
        parent.destroy()
        self._show_warning("Fila 'FCFS' foi iniciada!")

    def _get_quantum_time(self, parent):
        root = tk.Tk()
        root.title("Quantum Time")
        root.geometry(RESOLUTION)
        root.resizable(False, False)
        root.configure(background=GRAY)
        label = tk.Label(root, text="Quantum Time:",
                         fg=BLACK, bg=GRAY,
                         font=("Helvetica", 20))
        label.pack()
        text = tk.Entry(root, width=10,
                        font=("Helvetica", 20))
        text.pack()
        button = tk.Button(root, text="Adicionar",
                           fg=WHITE, bg=BLACK,
                           command=lambda: self._round_robin_queue(text.get(), root, parent))
        button.pack()
        root.mainloop()

    def _round_robin_queue(self, quantum, parent, grandparent):
        if quantum.isdigit():
            self._ready_queue = RoundRobin(float(quantum))
            self._queueing = True
            parent.destroy()
            grandparent.destroy()
            self._show_warning("Fila 'Round Robin' foi iniciada!")
        else:
            self._show_warning("Não é número!")

    def _get_burst_time(self):
        if self._queueing:
            root = tk.Tk()
            root.title("Novo Processo")
            root.geometry(RESOLUTION)
            root.resizable(False, False)
            root.configure(background=GRAY)
            label = tk.Label(root, text="Burst Time:",
                             fg=BLACK, bg=GRAY,
                             font=("Helvetica", 20))
            label.pack()
            text = tk.Entry(root, width=10,
                            font=("Helvetica", 20))
            text.pack()
            button = tk.Button(root, text="Adicionar",
                               fg=WHITE, bg=BLACK,
                               command=lambda: self._new_process(text.get(), root))
            button.pack()
            root.mainloop()
        else:
            self._show_warning("Fila de Prontos não está em execução!")

    def _new_process(self, burst_time, parent):
        if burst_time.isdigit():
            self._ready_queue.add_process(float(burst_time))
            parent.destroy()
            self._show_warning("Processo adicionado com sucesso!")
        else:
            self._show_warning("Não é número!")

    def _stop_ready_queue(self):
        if self._queueing:
            self._ready_queue.stop()
            self._queueing = False
            self._show_warning("Fila de Prontos foi parada!")
        else:
            self._show_warning("Fila de Prontos não está em execução!")

    def _exit(self):
        if self._queueing:
            self._ready_queue.stop()
        cls()
        print("Fim!\n")
        sys.exit()


if __name__ == "__main__":
    crud = CRUD()
    crud.main_menu()
