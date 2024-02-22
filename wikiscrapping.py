{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMddgsPYp8lB+FLitgwGIx0",
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
        "<a href=\"https://colab.research.google.com/github/kennymaxy/MY-CYBER-SECURITY-PORTFOLIO/blob/main/wikiscrapping.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "MFg6se031flN"
      },
      "outputs": [],
      "source": [
        "import requests\n",
        "\n",
        "from bs4 import BeautifulSoup"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "url = \"https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue\"\n",
        "\n",
        "page = requests.get(url)\n",
        "soup = BeautifulSoup(page.text, 'html')"
      ],
      "metadata": {
        "id": "45etmaH5sFc6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(soup)"
      ],
      "metadata": {
        "id": "b0QcmI6wZqa6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "soup.find_all('table')[1]"
      ],
      "metadata": {
        "id": "dWDvGxMkm08q"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "table = soup.find('table', class_='wikitable sortable')"
      ],
      "metadata": {
        "id": "GA-puM4DtRSr"
      },
      "execution_count": 100,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "world_titles = table.find_all('th')\n",
        "\n",
        "world_titles"
      ],
      "metadata": {
        "id": "qibbAtxsuW_x"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "world_table_titles = [title.text.strip() for title in world_titles]\n",
        "\n",
        "print(world_table_titles)"
      ],
      "metadata": {
        "id": "lXkQjFPcujlE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd"
      ],
      "metadata": {
        "id": "czOnI-FZwCXr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "df = pd.DataFrame(columns = world_table_titles)\n",
        "\n",
        "df"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 89
        },
        "id": "W_8MeEK0aNt3",
        "outputId": "c3757962-688d-4413-fcb0-21c471a88721"
      },
      "execution_count": 103,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Empty DataFrame\n",
              "Columns: [Rank, Name, Industry, Revenue (USD millions), Revenue growth, Employees, Headquarters]\n",
              "Index: []"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-dac061ea-209e-4ff0-9f68-62fb132b13a7\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Rank</th>\n",
              "      <th>Name</th>\n",
              "      <th>Industry</th>\n",
              "      <th>Revenue (USD millions)</th>\n",
              "      <th>Revenue growth</th>\n",
              "      <th>Employees</th>\n",
              "      <th>Headquarters</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-dac061ea-209e-4ff0-9f68-62fb132b13a7')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-dac061ea-209e-4ff0-9f68-62fb132b13a7 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-dac061ea-209e-4ff0-9f68-62fb132b13a7');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "  <div id=\"id_bb6aabda-32e0-42b6-a1fb-0be19b94fc3e\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('df')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_bb6aabda-32e0-42b6-a1fb-0be19b94fc3e button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('df');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "repr_error": "'str' object has no attribute 'empty'"
            }
          },
          "metadata": {},
          "execution_count": 103
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "column_data = soup.find_all('tr')\n"
      ],
      "metadata": {
        "id": "LxL3JSvIwdXP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for row in column_data[1:]:\n",
        "    row_data = row.find_all('td')\n",
        "    individual_row_data = [data.text.strip() for data in row_data]\n",
        "\n",
        "    length = len(df)\n",
        "    df.loc[length] = individual_row_data"
      ],
      "metadata": {
        "id": "8u5LjUz7xk2d"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df"
      ],
      "metadata": {
        "id": "W46X6zvVDroa"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.to_csv(r'C:\\Users\\User\\pyTraining\\Companies.csv', index = False)"
      ],
      "metadata": {
        "id": "kSCbxhTAahUY"
      },
      "execution_count": 109,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "gJTaRVuiBSZc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8defaba5-fb3a-4cfe-b823-96866b4723dd"
      },
      "execution_count": 106,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['98.4 Capital FM', 'Consumer services', 'Broadcasting & entertainment', 'Nairobi', '1996', 'Radio']\n"
          ]
        }
      ]
    }
  ]
}