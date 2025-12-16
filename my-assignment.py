{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOAO2Fy1yhgqdFrZZa9UQef",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Sandeept1986-web/python-first-tutorial-practise/blob/main/my-assignment.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vukXTqEOJ3T2"
      },
      "outputs": [],
      "source": [
        "# file.py\n",
        "\n",
        "fo=open(\"sample.txt\",\"r+\")\n",
        "print(fo.tell())\n",
        "fo.read(10)\n",
        "fo.close()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# sample_func1.py\n",
        "\n",
        "def func1(*args):\n",
        "    \"\"\"Accepts variable length arguments and prints their values.\"\"\"\n",
        "    print(\"Received arguments:\")\n",
        "    for arg in args:\n",
        "        print(arg)\n",
        "\n",
        "\n",
        "func1(10, 20, 30)\n",
        "func1(\"apple\", \"banana\", \"cherry\")\n",
        "func1(1, \"mixed\", 3.14, True)"
      ],
      "metadata": {
        "id": "uFajKEWvJ5fl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# delete_keys.py\n",
        "\n",
        "sample_dict = {\n",
        "    \"name\": \"Sandeep\",\n",
        "    \"role\": \"Engineer\",\n",
        "    \"location\": \"Hyderabad\",\n",
        "    \"company\": \"Movate\"\n",
        "}\n",
        "\n",
        "keys_to_delete = [\"location\", \"company\"]\n",
        "\n",
        "# One-liner to remove keys\n",
        "updated_dict = {k: v for k, v in sample_dict.items() if k not in keys_to_delete}\n",
        "\n",
        "print(\"Updated dictionary:\", updated_dict)"
      ],
      "metadata": {
        "id": "xj7BBo7OKAdS"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}