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
        "4-Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.\n",
        "The STATION table is described as follows:\n",
        "\n",
        "SELECT DISTINCT CITY FROM STATION WHERE MOD(ID,2)=0 ;"
      ]
    }
  ]
}