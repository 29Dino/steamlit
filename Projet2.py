import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Analyse de données avec Streamlit")

# Étape 1 : Téléchargement des données via le file uploader
file = st.file_uploader("Importer vos données ici", type=["csv"])

# Vérification que le fichier a été chargé
if file is not None:
    # Charger les données dans un DataFrame pandas
    data = pd.read_csv(file)

    # Étape 2 : Afficher les données
    st.header("Données importées")
    st.write(data)

    # Étape 3 : Statistiques descriptives
    st.header("Statistiques descriptives")
    st.write(data.describe())

    # Étape 4 : Graphiques interactifs
    st.header("Visualisation des données")

    # Sélectionner les colonnes numériques
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns

    if len(numeric_columns) >= 2:
        # Sélection de colonnes pour les axes
        x_axis = st.selectbox("Sélectionnez l'axe X", numeric_columns)
        y_axis = st.selectbox("Sélectionnez l'axe Y", numeric_columns)

        # Graphique en nuage de points
        fig, ax = plt.subplots()
        sns.scatterplot(data=data, x=x_axis, y=y_axis)
        st.pyplot(fig)
    else:
        st.warning("Les colonnes numériques sont nécessaires pour les graphiques.")

    # Histogramme
    st.subheader("Histogramme")
    selected_column = st.selectbox("Sélectionnez une colonne pour l'histogramme", numeric_columns)
    fig, ax = plt.subplots()
    sns.histplot(data=data, x=selected_column, kde=True)
    st.pyplot(fig)

else:
    st.warning("Veuillez importer un fichier CSV pour commencer.")
