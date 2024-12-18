import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuration du thème général
st.set_page_config(
    page_title="Analyse de données", 
    page_icon="📊", 
    layout="wide"
)

# En-tête stylisé
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 36px;
        color: #4CAF50;
        font-weight: bold;
    }
    .sub-title {
        text-align: center;
        font-size: 20px;
        color: #666;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="main-title">Analyse de données avec Streamlit 📊</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Téléchargez vos données, explorez-les et visualisez-les facilement !</div>', unsafe_allow_html=True)

# Étape 1 : Téléchargement des données
st.sidebar.header("Options")
file = st.sidebar.file_uploader("Importer vos données ici", type=["csv"])

if file is not None:
    data = pd.read_csv(file)

    # Conteneur principal
    with st.container():
        # Affichage des données
        st.markdown("### 🗂️ Données importées")
        st.dataframe(data)

        # Statistiques descriptives
        st.markdown("### 📊 Statistiques descriptives")
        st.write(data.describe())

        # Sélection des colonnes numériques
        numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns

        # Visualisations conditionnelles
        if len(numeric_columns) >= 2:
            st.markdown("### 🎨 Visualisation des données")

            # Options pour l'utilisateur
            x_axis = st.selectbox("Sélectionnez l'axe X :", numeric_columns)
            y_axis = st.selectbox("Sélectionnez l'axe Y :", numeric_columns)

            # Graphique en nuage de points
            st.markdown("#### 🔵 Nuage de points")
            fig, ax = plt.subplots()
            sns.scatterplot(data=data, x=x_axis, y=y_axis, ax=ax, color="blue")
            st.pyplot(fig)

            # Histogramme
            st.markdown("#### 📊 Histogramme")
            selected_column = st.selectbox("Sélectionnez une colonne pour l'histogramme :", numeric_columns)
            fig, ax = plt.subplots()
            sns.histplot(data=data, x=selected_column, kde=True, color="green")
            st.pyplot(fig)
        else:
            st.warning("Les colonnes numériques sont nécessaires pour les graphiques.")
else:
    st.sidebar.warning("Veuillez importer un fichier CSV pour commencer.")
    st.markdown("### ❌ Aucun fichier chargé")
    st.info("Téléchargez un fichier CSV via le menu de gauche pour commencer l'analyse.")
