import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuration de la page
st.set_page_config(
    page_title="Analyse de données", 
    page_icon="📊", 
    layout="wide"
)

# CSS pour personnaliser le fond et le texte
st.markdown(
    """
    <style>
    body {
        background-color: #f7f3e9; /* Couleur douce */
        color: #333333;
    }
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
    .stApp {
        background: linear-gradient(120deg, #f6d365, #fda085); /* Dégradé élégant */
    }
    </style>
    """, unsafe_allow_html=True
)

# En-tête
st.markdown('<div class="main-title">Analyse de données avec Streamlit 📊</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Téléchargez vos données, explorez-les et visualisez-les facilement !</div>', unsafe_allow_html=True)

# Upload et analyse des données
file = st.sidebar.file_uploader("Importer vos données ici", type=["csv"])

if file is not None:
    data = pd.read_csv(file)

    # Conteneur principal
    with st.container():
        st.markdown("### 🗂️ Données importées")
        st.dataframe(data)

        st.markdown("### 📊 Statistiques descriptives")
        st.write(data.describe())

        numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns

        if len(numeric_columns) >= 2:
            st.markdown("### 🎨 Visualisation des données")
            x_axis = st.selectbox("Sélectionnez l'axe X :", numeric_columns)
            y_axis = st.selectbox("Sélectionnez l'axe Y :", numeric_columns)

            st.markdown("#### 🔵 Nuage de points")
            fig, ax = plt.subplots()
            sns.scatterplot(data=data, x=x_axis, y=y_axis, ax=ax, color="blue")
            st.pyplot(fig)

            st.markdown("#### 📊 Histogramme")
            selected_column = st.selectbox("Sélectionnez une colonne pour l'histogramme :", numeric_columns)
            fig, ax = plt.subplots()
            sns.histplot(data=data, x=selected_column, kde=True, color="green")
            st.pyplot(fig)
else:
    st.sidebar.warning("Veuillez importer un fichier CSV pour commencer.")
    st.markdown("### ❌ Aucun fichier chargé")
    st.info("Téléchargez un fichier CSV via le menu de gauche pour commencer l'analyse.")
