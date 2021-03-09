{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "# -*- coding: utf-8 -*-\n",
    "\"\"\"\n",
    "Created on Mon Mar  8 20:56:12 2021\n",
    "\n",
    "@author: Sourya\n",
    "\"\"\"\n",
    "#import flask\n",
    "from flask import Flask, request\n",
    "import numpy as np\n",
    "import pickle\n",
    "import pandas as pd\n",
    "import flasgger\n",
    "from flasgger import Swagger\n",
    "\n",
    "app=Flask(__name__)\n",
    "Swagger(app)\n",
    "\n",
    "pickle_in = open(\"classifier.pkl\",\"rb\")\n",
    "classifier=pickle.load(pickle_in)\n",
    "\n",
    "@app.route('/')\n",
    "def welcome():\n",
    "    return \"Welcome All\"\n",
    "\n",
    "@app.route('/predict',methods=[\"Get\"])\n",
    "def predict_note_authentication():\n",
    "    \"\"\"Let's Authenticate the Banks Note \n",
    "    This is using docstrings for specifications.\n",
    "    ---\n",
    "    parameters:  \n",
    "      - name: variance\n",
    "        in: query\n",
    "        type: number\n",
    "        required: true\n",
    "      - name: skewness\n",
    "        in: query\n",
    "        type: number\n",
    "        required: true\n",
    "      - name: curtosis\n",
    "        in: query\n",
    "        type: number\n",
    "        required: true\n",
    "      - name: entropy\n",
    "        in: query\n",
    "        type: number\n",
    "        required: true\n",
    "    responses:\n",
    "        200:\n",
    "            description: The output values\n",
    "        \n",
    "    \"\"\"\n",
    "    variance=request.args.get(\"variance\")\n",
    "    skewness=request.args.get(\"skewness\")\n",
    "    curtosis=request.args.get(\"curtosis\")\n",
    "    entropy=request.args.get(\"entropy\")\n",
    "    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])\n",
    "    print(prediction)\n",
    "    return \"Hello The answer is\"+str(prediction)\n",
    "\n",
    "@app.route('/predict_file',methods=[\"POST\"])\n",
    "def predict_note_file():\n",
    "    \"\"\"Let's Authenticate the Banks Note \n",
    "    This is using docstrings for specifications.\n",
    "    ---\n",
    "    parameters:\n",
    "      - name: file\n",
    "        in: formData\n",
    "        type: file\n",
    "        required: true\n",
    "      \n",
    "    responses:\n",
    "        200:\n",
    "            description: The output values\n",
    "        \n",
    "    \"\"\"\n",
    "    df_test=pd.read_csv(request.files.get(\"file\"))\n",
    "    print(df_test.head())\n",
    "    prediction=classifier.predict(df_test)\n",
    "    \n",
    "    return str(list(prediction))\n",
    "\n",
    "if __name__=='__main__':\n",
    "    app.run(debug = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
