import pandas as pd
from source.machine_learning import DecisionTree
from source.ui import UserInterface
from source.utils import *


class AG002:
    def __init__(self):
        dataset = pd.read_csv('source/data/tic-tac-toe.csv')
        dataset_converted = self.__convert_data(dataset)
        dataset_converted.to_csv('source/data/tic-tac-toe-converted.csv',
                                 index=False)
        self.ml_model = DecisionTree(dataset_converted)
        self.ui = UserInterface(self._predict, self._show_data,
                                self._get_performance)

    def start(self):
        self.ui.menu()

    def _predict(self, data):
        data_pandas = self.__convert_data(pd.DataFrame(data))
        data_numpy = [data_pandas.values.flatten()]
        results = self.ml_model.predict(data_numpy)
        return results

    def _show_data(self):
        self.ml_model.visualize_data()

    def _get_performance(self):
        return self.ml_model.get_performance()

    def __convert_data(self, data):
        data.replace(to_replace=['o', 'b', 'x', 'negativo', 'positivo'],
                     value=[-1, 0, 1, -1, 1], inplace=True)
        return data


if __name__ == '__main__':
    clear_console()
    ag002 = AG002()
    ag002.start()
    print('Fim!\n')
