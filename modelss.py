{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "320fed75-8035-446b-bf0e-ba46b8556b89",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "import numpy as np\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import mean_squared_error, r2_score\n",
    "\n",
    "\n",
    "class HousingPriceModel:\n",
    "    def __init__(self):\n",
    "        \"\"\"Inicializa el modelo de regresión lineal\"\"\"\n",
    "        self.model = LinearRegression()\n",
    "\n",
    "    def fit(self, X_train, y_train):\n",
    "        \"\"\"Entrena el modelo con los datos de entrenamiento\"\"\"\n",
    "        self.model.fit(X_train, y_train)\n",
    "\n",
    "    def predict(self, X_test):\n",
    "        \"\"\"Genera predicciones\"\"\"\n",
    "        return self.model.predict(X_test)\n",
    "\n",
    "    def evaluate(self, X_test, y_test):\n",
    "        \"\"\"Evalúa el modelo con métricas de regresión\"\"\"\n",
    "        y_pred = self.predict(X_test)\n",
    "        metrics = {\n",
    "            \"MSE\": mean_squared_error(y_test, y_pred),\n",
    "            \"R2\": r2_score(y_test, y_pred)\n",
    "        }\n",
    "        return metrics\n",
    "\n",
    "    def save_model(self, filepath=\"regression_model.pkl\"):\n",
    "        \"\"\"Guarda el modelo entrenado en un archivo .pkl\"\"\"\n",
    "        with open(filepath, \"wb\") as f:\n",
    "            pickle.dump(self.model, f)\n",
    "\n",
    "    def load_model(self, filepath=\"regression_model.pkl\"):\n",
    "        \"\"\"Carga un modelo previamente guardado\"\"\"\n",
    "        with open(filepath, \"rb\") as f:\n",
    "            self.model = pickle.load(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25774fc1-61c8-4aa7-9991-7f1e35c4f42b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
