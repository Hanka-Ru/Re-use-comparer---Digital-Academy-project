import streamlit as st
import pandas as pd
from datetime import datetime

# Load data with caching
@st.cache_data
def load_data():
    # Replace this path with the correct file path
    data_path = "/data/in/tables/UNION_TO_APP_CORR_SIZES.csv"
    return pd.read_csv(data_path)

# CSS for styling
st.markdown(
    """
    <style>
    /* Fancy header styling */
    .header-frame {
    background: linear-gradient(135deg, #18b4a4, #a8e6cf);
    border: 3px solid #18b4a4; /* Subtle green border */
    border-radius: 15px; /* Smooth, rounded corners */
    padding: 30px 20px; /* Spacious padding */
    text-align: center; /* Center-align content */
    box-shadow: 0 6px 15px rgba(24, 180, 164, 0.3); /* Soft drop shadow */
    margin-bottom: 30px; /* Add spacing below the header */
    position: relative;
    overflow: hidden;
}

		.header-frame:before {
    	content: '';
    	position: absolute;
   		top: -50%;
    	left: -50%;
    	width: 200%;
    	height: 200%;
    	background: radial-gradient(circle, rgba(255, 255, 255, 0.2), rgba(0, 0, 0, 0));
    	transform: rotate(30deg);
    	z-index: 0;
		}

		.header-title {
    	font-size: 2.8rem; /* Slightly larger font */
    	color: #18b4a4; /* Main green color */
    	font-family: 'Montserrat', sans-serif; /* Modern font */
    	font-weight: 700; /* Bold */
    	margin-bottom: 10px; /* Spacing below title */
    	text-transform: none;
    	letter-spacing: 3px; /* Add spacing between letters */
    	z-index: 1;
    	position: relative;
    	background: linear-gradient(90deg, #18b4a4, #11998e); /* Gradient text */
    	-webkit-background-clip: text;
    	-webkit-text-fill-color: transparent;
    	text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Soft text shadow */
		}

    /* Bold green labels */
    label {
        font-weight: bold;
        color: #18b4a4; /* Green color for labels */
        font-size: 16px;
    }

    /* Green slider styling */
    .stSlider {
        background-color: rgba(24, 180, 164, 0.1); /* Light green background for slider row */
        border-radius: 10px;
        padding: 10px;
    }
    .stSlider > div {
        color: #18b4a4; /* Green slider labels */
    }
    .stSlider > div [role='slider'] {
        background-color: #18b4a4; /* Green slider knob */
    }
    .stSlider > div .stNumberInput {
        background-color: transparent;
        color: #18b4a4; /* Green numbers */
    }

    /* Green button styling */
    div.stButton > button {
        background-color: #18b4a4; /* Green button */
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 20px;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #16a193; /* Slightly darker green on hover */
    }

    /* Table header and content styling */
    table {
        width: 100%;
        border-collapse: collapse;
    }
    th {
        background-color: #18b4a4; /* Green header */
        color: white;
        padding: 10px;
        text-align: left;
    }
    td {
        color: #18b4a4; /* Green table text */
        padding: 10px;
        text-align: left;
        border: 1px solid #18b4a4;
    }
    tr:nth-child(even) {
        background-color: rgba(24, 180, 164, 0.1); /* Light green for alternate rows */
    }
    a {
        color: #e5a51b; /* Orange for hyperlinks */
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add the link below your header or any other section
st.markdown(
    f"""
    <style>
    @keyframes blink {{
        0% {{ border-color: #18b4a4; background-color: white; }}
        50% {{ border-color: #18b4a4; background-color: #d9fdfc; }}
        100% {{ border-color: #18b4a4; background-color: white; }}
    }}

    .blinking-button {{
        color: #18b4a4;
        background-color: white;
        border: 2px solid #18b4a4;
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 5px;
        font-weight: bold;
        font-size: 18px;
        display: inline-block;
        animation: blink 1.5s infinite;
        text-align: center;
    }}
    .blinking-button:hover {{
        color: orange;
    }}
    </style>
    <p style="text-align: center; font-size: 15px; color: #77807e; font-weight: bold; margin-bottom: 20px;">
        PROJEKT HANKY RŮŽIČKOVÉ A PAVLÍNY LUKEŠOVÉ PRO DIGITÁLNÍ AKADEMII CZECHITAS PODZIM 2024
     		DEMO APLIKACE PRO POROVNÁNÍ NABÍDEK RE-USE OBLEČENÍ
    </p>    
    <div class="header-frame">
        <h1 class="header-title">♻️ reuse.it</h1>
    </div>
    <p style="text-align: center; font-size: 18px; color: #18b4a4; font-weight: bold;">
        Chceš zjistit, zda je nakupování re-use oblečení opravdu výhodné? Klikni na tlačítko a ponoř se do Tableau Public analýzy, která ti ukáže benefity nákupu z druhé ruky! 🌿👕 
        Uvidíš, že můžeš šetřit nejen peníze, ale i naši planetu. 🌍✨
    </p>
    <p style="text-align: center;">
        <a href="https://public.tableau.com/app/profile/pavl.na.luke.ov./viz/reuse_it/reuse_it" target="_blank" class="blinking-button" style="color: orange;">
        KOUKNI SEM
        </a>
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p style='text-align: center; color: #18b4a4; font-size: 18px; font-weight: bold; margin-top: 40px;'>
        ♻️🆕 Hledáš nový kousek oblečení? Vyber si, co hledáš, a zobraz si nabídku z dnešního dne. Rozhodni se, jestli chceš nové nebo re-use. ♻️🆕
    </p>
    """,
    unsafe_allow_html=True
)

# Load the dataset
data = load_data()

# Product, Brand, Gender filters with green bold labels
product = st.selectbox("Vyberte produkt", options=[""] + data["product"].unique().tolist())
brand = st.selectbox("Vyberte značku", options=[""] + data["brand"].unique().tolist())
gender = st.selectbox("Vyberte pohlaví", options=[""] + data["gender"].unique().tolist())

# Dynamically filter sizes based on the selected gender
if gender:
    filtered_sizes = sorted(data[data["gender"] == gender]["size"].unique())
else:
    filtered_sizes = sorted(data["size"].unique())  # Default: all sizes if no gender is selected

    # Change to a multiple selection filter for size
sizes = st.multiselect("Vyberte velikost", options=filtered_sizes)
    
# Horizontal slider for price range with green labels
price_min, price_max = st.slider(
    "Rozsah ceny (Minimální cena - Maximální cena):",
    min_value=0,
    max_value=5000,
    value=(0, 5000),
    step=100,
    label_visibility="visible",  # Ensures labels are styled by custom CSS
)
    
# Get the current date
current_date = datetime.now().strftime("%d.%m.%Y")  # Format as DD.MM.YYYY

# Green button to display results
if st.button("Zobrazit výsledky"):
    # Apply filters
    filtered_data = data.copy()

    # Apply product, brand, and gender filters
    if product:
        filtered_data = filtered_data[filtered_data["product"] == product]
    if brand:
        filtered_data = filtered_data[filtered_data["brand"] == brand]
    if gender:
        filtered_data = filtered_data[filtered_data["gender"] == gender]
    if sizes:  # Kontrola, zda uživatel vybral velikosti
        filtered_data = filtered_data[filtered_data["size"].isin(sizes)]

    # Apply price range filter
    filtered_data = filtered_data[
        (filtered_data["price"] >= price_min) & (filtered_data["price"] <= price_max)
    ]

    # Sort data by price
    filtered_data = filtered_data.sort_values(by="price", ascending=True)

    # Rename columns for display
    filtered_data = filtered_data.rename(
        columns={
            "e_shop": "E-shop",
            "name": "Název",
            "size": "Velikost",
            "condition": "Stav",
            "price": "Cena",
            "url": "Odkaz",
        }
    )

    # Add the text "Nabídka z [current_date]" above the displayed data
    st.markdown(
        f'<p style="text-align: left; font-size: 14px; color: #18b4a4; font-weight: bold;">Nabídka z {current_date}</p>',
        unsafe_allow_html=True,
    )

    if not filtered_data.empty:
        # Create clickable links in orange
        filtered_data["Odkaz"] = filtered_data["Odkaz"].apply(
            lambda x: f'<a href="{x}" target="_blank" style="color: #e5a51b;">Odkaz</a>'
        )

        # Display filtered table with green styling
        st.markdown(
            filtered_data[["E-shop", "Název", "Velikost", "Stav", "Cena", "Odkaz"]]
            .to_html(index=False, escape=False),
            unsafe_allow_html=True,
        )
    else:
        st.warning("Pro dané parametry nebyla nalezena žádná data.")
