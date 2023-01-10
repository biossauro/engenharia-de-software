import json
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.tree import DecisionTreeClassifier


class DecisionTree:
    def __init__(self, dataset):
        self.data = dataset
        self.array = dataset.values
        self.x = self.array[:, 0:9]
        self.y = self.array[:, 9]
        self.__train_model()
        self.__check_performance()
        self.__clear_prediction()

    def __train_model(self, max_depth=None):
        results = train_test_split(self.x, self.y, test_size=0.2, shuffle=True,
                                   random_state=22)
        self.x_train, self.x_test, self.y_train, self.y_test = results
        self.regressor = DecisionTreeClassifier(max_depth=max_depth)
        self.regressor.fit(self.x_train, self.y_train)

    def __check_performance(self):
        # Cross-Validation
        cv = cross_val_score(X=self.x_train, y=self.y_train,
                             estimator=self.regressor, cv=10)
        # R2 Treino
        y_pred_train = self.regressor.predict(self.x_train)
        r2_training = r2_score(self.y_train, y_pred_train)
        # R2 Teste
        y_pred_test = self.regressor.predict(self.x_test)
        r2_testing = r2_score(self.y_test, y_pred_test)
        # RMSE
        rmse = (np.sqrt(mean_squared_error(self.y_test, y_pred_test)))
        # Peformance
        self.performance = {
            'cv': cv.mean(),
            'r2_training': r2_training,
            'r2_testing': r2_testing,
            'rmse': rmse
        }
        self.__save_performance()

    def __save_performance(self):
        with open('generated/performance.json', 'w') as file:
            json.dump(self.performance, file)

    def __clear_prediction(self):
        with open('generated/prediction.txt', 'w') as file:
            file.write('')

    def predict(self, matrix):
        prediction = self.regressor.predict(matrix)
        self.__save_prediction(matrix, prediction)
        return prediction

    def __save_prediction(self, matrix, prediction):
        results = np.concatenate(
            (matrix, prediction.reshape(len(prediction), 1)), axis=1)[0]
        with open('generated/prediction.txt', 'a') as file:
            file.write(str(results) + '\n')

    def visualize_data(self):
        # Heat Map
        correlation = self.data.corr()
        figure, axis = plt.subplots(figsize=(10, 10))
        sns.heatmap(correlation, cmap='RdBu', annot=True, fmt='.2f')
        plt.xticks(np.arange(len(correlation.columns)) + 0.5,
                   correlation.columns, ha='center')
        plt.yticks(np.arange(len(correlation.columns)) + 0.5,
                   correlation.columns, va='center')
        plt.savefig('generated/heatmap.png')
        # Correlation
        sns.pairplot(self.data)
        plt.savefig('generated/correlation.png')
        # Show
        plt.show()

    def get_performance(self):
        return self.performance
