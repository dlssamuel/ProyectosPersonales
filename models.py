{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "42541021-345b-47a9-a168-26cb5acd01db",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import accuracy_score, classification_report, confusion_matrix\n",
    "\n",
    "class SimpleClassifier:\n",
    "    def __init__(self, model_type=\"lr\", **kwargs):\n",
    "        if model_type == \"lr\":\n",
    "            self.model = LogisticRegression(**kwargs)\n",
    "        elif model_type == \"rf\":\n",
    "            self.model = RandomForestClassifier(**kwargs)\n",
    "        else:\n",
    "            raise ValueError(\"Tipo de modelo no soportado. Use 'lr' o 'rf'.\")\n",
    "\n",
    "    def fit(self, X, y):\n",
    "        self.model.fit(X, y)\n",
    "\n",
    "    def predict(self, X):\n",
    "        return self.model.predict(X)\n",
    "\n",
    "    def evaluate(self, X, y):\n",
    "        y_pred = self.predict(X)\n",
    "        return {\n",
    "            \"accuracy\": accuracy_score(y, y_pred),\n",
    "            \"confusion_matrix\": confusion_matrix(y, y_pred),\n",
    "            \"report\": classification_report(y, y_pred, zero_division=0)\n",
    "        }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "212f6110-df52-4b51-94b6-7e1265a3cef6",
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
