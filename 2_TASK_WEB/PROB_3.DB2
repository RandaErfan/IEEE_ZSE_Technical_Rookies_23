{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "uICNdkdQp-wx"
      },
      "outputs": [],
      "source": [
        "3-Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.\n",
        "\n",
        "The CITY table is described as follows:\n",
        " \n",
        " SELECT NAME FROM CITY WHERE COUNTRYCODE = 'USA' AND POPULATION >120000;"
      ]
    }
  ]
}