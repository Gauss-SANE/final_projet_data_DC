# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd

##############################

import pandas as pd
from requests import get # alows us to get the content  (html) of webpage
from bs4 import BeautifulSoup as bs # store the content in beautifulsoup objet and sparse the code

############  url_1 #################

def scrape_nombre_page_url_1(nombre_page): # Le nombre de pages disponibles est de 2772
    df = pd.DataFrame()
    for index in range(1, nombre_page + 1):
        url = f'https://dakar-auto.com/senegal/voitures-4?&page={index}'
        res = get(url)
        soup = bs(res.content, 'html.parser')
        containers = soup.find_all('div', class_ = 'listing-card__content p-2')
        data = []
        for container in containers:
            try:
                # Marque
                gen_inf_1 = container.find('h2', 'listing-card__header__title mb-md-2 mb-0').a.text.strip().split() # Pour la marque et l'année...
                brand = ""
                for i in range(len(gen_inf_1) - 1):
                    brand += gen_inf_1[i]
                    brand += " "
                brand = brand.strip()
                #Année
                year = gen_inf[-1]
                
                # Prix
                price = "".join(container.find('h3', "listing-card__header__price font-weight-bold text-uppercase mb-0").text.strip().split()).replace('FCFA', '')
                
                # Adresse
                gen_inf_2 = container.find('div', "col-12 entry-zone-address").text.split() # pour l'addresse...
                address = ""
                for i in range(len(gen_inf_2)):
                    address += gen_inf_2[i]
                    address += " "
                address = address.strip()
                address
                # Nombre de Km
                gen_inf_3 = container.find('div', "col-12 listing-card__properties d-none d-sm-block").text.split()
                kilometerage = gen_inf_3[2]
                # boîte de vitesses
                gearbox = gen_inf_3[4]
                # carburant
                fuel = gen_inf_3[5]
                # propriétaire
                owner = container.find('p', "time-author m-0").text.strip()
        
                dictionnaire = {'brand': brand, 'price': price, 'year': year,
                                'address': address, 'kilometerage': kilometerage, 
                                'gearbox': gearbox, 'fuel': fuel, 'owner': owner}
                data.append(dictionnaire)
            except:
                pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0).reset_index(drop = True)
        df = df.drop_duplicates()
        #df.year = df.year.astype('int64')
        #df.price = df.price.astype('int64')
        #df.kilometerage = df.kilometerage.astype('float64')        
    return df


############  url_2 #################

def scrape_nombre_page_url_2(nombre_page): # Le nombre de pages disponibles est de 55https://dakar-auto.com/senegal/location-de-voitures-19?&page=1
    df = pd.DataFrame()
    for index in range(1, nombre_page + 1):
        url = f'https://dakar-auto.com/senegal/motos-and-scooters-3?&page={index}'
        res = get(url)
        soup = bs(res.content, 'html.parser')
        containers = soup.find_all('div', class_ = 'listing-card__content p-2')
        data = []
        for container in containers:
            try:
                # Marque
                gen_inf_1 = container.find('h2', 'listing-card__header__title mb-md-2 mb-0').text.strip().split()
                brand = ""
                for i in range(len(gen_inf_1) - 1):
                    brand += gen_inf_1[i]
                    brand += " "
                brand = brand.strip()
                # Année
                year = gen_inf_1[-1]
                # Prix
                price = "".join(container.find('h3', 'listing-card__header__price font-weight-bold text-uppercase mb-0').text.strip().split()).replace('FCFA', '')
                # Adresse 
                gen_inf_2 = container.find('div', 'col-12 entry-zone-address').text.split()
                address = ""
                for i in range(len(gen_inf_2)):
                    address += gen_inf_2[i]
                    address += " "
                address = address.strip()
                # Nombre de Kilomètre
                kilometerage = container.find('li', 'listing-card__attribute list-inline-item').text.strip().split()[1]
                # Propriétaire
                owner = " ".join(container.find('p', 'time-author m-0').text.strip().split()[1:])
                dictionnaire = {'brand': brand, 'year': year, 'price': price, 
                                'address': address, 'kilometerage': kilometerage, 
                                'owner': owner}
                data.append(dictionnaire)
            except:
                pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0).reset_index(drop = True)
        df = df.drop_duplicates()
        df.year = df.year.astype('int64')
        df.price = df.price.astype('int64')
    return df


############  url_3 #################

def scrape_nombre_page_url_3(nombre_page): # Le nombre de pages disponibles est de 9
    df = pd.DataFrame()
    for index in range(1, nombre_page + 1):
        url = f'https://dakar-auto.com/senegal/location-de-voitures-19?&page={index}'
        res = get(url)
        soup = bs(res.content, 'html.parser')
        containers = soup.find_all('div', class_ = 'listing-card__content p-2')
        data = []
        for container in containers:
            try:
                # Marque
                gen_inf_1 = container.find('h2', 'listing-card__header__title mb-md-2 mb-0').text.strip().split()
                brand = ""
                for i in range(len(gen_inf_1) - 1):
                    brand += gen_inf_1[i]
                    brand += " "
                brand = brand.strip()
                # Année
                year = gen_inf_1[-1]
                # Prix
                price = "".join(container.find('h3', 'listing-card__header__price font-weight-bold text-uppercase mb-0').text.strip().split()).replace('FCFA', '')
                # Adresse 
                gen_inf_2 = container.find('div', 'col-12 entry-zone-address').text.split()
                address = ""
                for i in range(len(gen_inf_2)):
                    address += gen_inf_2[i]
                    address += " "
                address = address.strip()
                # Nombre de Kilomètre
                kilometerage = container.find('li', 'listing-card__attribute list-inline-item').text.strip().split()[1]
                # Propriétaire
                owner = " ".join(container.find('p', 'time-author m-0').text.strip().split()[1:])
                dictionnaire = {'brand': brand, 'year': year, 'price': price, 
                                'address': address, 'owner': owner}
                data.append(dictionnaire)
            except:
                pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0).reset_index(drop = True)
        df = df.drop_duplicates()
        df['price'] = pd.to_numeric(df['price'], errors = "coerce").astype('int')
        df.fillna(df.price.mean(), inplace = True)
        df['year'] = pd.to_numeric(df['year'], errors = "coerce").astype('int')
        df.fillna(df.year.mode(), inplace = True)
    return df


################ Mon programme #####################


####################################################
st.markdown("<h1 style='text-align: center; color: black;'>AIMS-APP</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: blue;'>J'aime AIMS</h2>", unsafe_allow_html=True)

st.markdown("""
This application allows you to download data retrieved from cars, motorcycles, and scooters from dakar-auto. 
* **Python libraries:** base64, pandas, streamlit, BeautifulSoup
* **Data source:** [Dakar-Auto](https://dakar-auto.com/).""")



# Function for loading the data
def load_(dataframe, title, key) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    
    if st.button(title,key):
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)


# define some styles rely to the box
st.markdown('''<style> .stButton>button {
    font-size: 12px;
    height: 4em;
    width: 25em;
}</style>''', unsafe_allow_html=True)



################################ Scraper des données avec WebScraper ###########################

st.markdown("<h2 style='text-align: center; color: red;'>Scraper des données avec WebScraper</h2>", unsafe_allow_html=True)

# Voitures
st.markdown("<h3 style='text-align: center; color: black;'>Voitures</h3>", unsafe_allow_html=True)
load_(pd.DataFrame(pd.read_csv("data/Dakar_auto_WebScraper.csv")), 'Voir tableau voitures', '4')
# Partie téléchargement du ficheir Dakar_auto_WebScraper.csv
df_1 = pd.DataFrame(pd.read_csv("data/Dakar_auto_WebScraper.csv"))
csv_data_1 = df_1.to_csv(index=False, encoding='utf-8')
st.download_button(
    label="Download as CSV",
    data=csv_data_1,
    file_name='Dakar_auto_WebScraper.csv',
    mime='text/csv',
)

# Motos and Scooters
st.markdown("<h3 style='text-align: center; color: black;'>Motos and Scooters</h3>", unsafe_allow_html=True)
load_(pd.DataFrame(pd.read_csv("data/Motos_and_Scooters_WebScraper.csv")), 'Voir tableau Motos and Scooters', '5')
# Partie téléchargement du ficheir Motos_and_Scooters_WebScraper.csv
df_2 = pd.DataFrame(pd.read_csv("data/Motos_and_Scooters_WebScraper.csv"))
csv_data_2 = df_2.to_csv(index=False, encoding='utf-8')
st.download_button(
    label="Download as CSV",
    data=csv_data_2,
    file_name='Motos_and_Scooters_WebScraper.csv',
    mime='text/csv',
)


#location de voitures
st.markdown("<h3 style='text-align: center; color: black;'>location de voitures</h3>", unsafe_allow_html=True)
load_(pd.DataFrame(pd.read_csv("data/Location_voitures_WebScraper.csv")), 'Voir tableau location de voitures', '6')
# Partie téléchargement du ficheir Location_voitures_WebScraper.csv
df_3 = pd.DataFrame(pd.read_csv("data/Location_voitures_WebScraper.csv"))
csv_data_3 = df_3.to_csv(index=False, encoding='utf-8')
st.download_button(
    label="Download as CSV",
    data=csv_data_3,
    file_name='Location_voitures_WebScraper.csv',
    mime='text/csv',
)

################################  Scraper des données avec BeautifulSoup #########################

st.markdown("<h2 style='text-align: center; color: red;'>Scraper des données avec BeautifulSoup</h2>", unsafe_allow_html=True)

##############  url 1 ##############

st.markdown("<h3 style='text-align: center; color: black;'>Voitures</h3>", unsafe_allow_html=True)
nombre_page_1 = st.number_input("Donner le nombre de pages à scrapper et tapper sur entrer", min_value=1, max_value=5, value=1)
load_(pd.DataFrame(scrape_nombre_page_url_1(nombre_page_1)), 'Voir tableau voitures', '1')


##############  url 2 ##############

st.markdown("<h3 style='text-align: center; color: black;'>Motos and Scooters</h3>", unsafe_allow_html=True)
nombre_page_2 = st.number_input("Donner le nombre de pages à scrapper et tapper sur entrer", min_value=1, max_value=5, value=2)
load_(pd.DataFrame(scrape_nombre_page_url_2(nombre_page_2)), 'Voir tableau Motos and Scooters', '2')

# Partie téléchargement du ficheir Motos_and_Scooters_BeautifulSoup.csv
df_5 = pd.DataFrame(scrape_nombre_page_url_2(nombre_page_2))
csv_data_5 = df_5.to_csv(index=False, encoding='utf-8')
st.download_button(
    label="Download as CSV",
    data=csv_data_5,
    file_name='Motos_and_Scooters_BeautifulSoup.csv',
    mime='text/csv',
)
##############  url 3 ##############

st.markdown("<h3 style='text-align: center; color: black;'>Location de voitures</h3>", unsafe_allow_html=True)
nombre_page_3 = st.number_input("Donner le nombre de pages à scrapper et tapper sur entrer", min_value=1, max_value=5, value=3)
load_(pd.DataFrame(scrape_nombre_page_url_3(nombre_page_3)), 'Voir tableau location de voitures', '3')

# Partie téléchargement du ficheir Location_voitures_BeautifulSoup.csv
df_6 = pd.DataFrame(scrape_nombre_page_url_3(nombre_page_3))
csv_data_6 = df_6.to_csv(index=False, encoding='utf-8')
st.download_button(
    label="Download as CSV",
    data=csv_data_6,
    file_name='Location_voitures_BeautifulSoup.csv',
    mime='text/csv',
)
#####################  Les formulaires  #########################

st.markdown("<h3 style='text-align: center'>Give your Feedback</h3>", unsafe_allow_html=True)

# centrer les deux boutons
col1, col2 = st.columns(2)

# Formulaire Kobo
with col1:
    st.link_button("Kobo Evaluation Form", url = "https://ee.kobotoolbox.org/x/Sx6Lf6Jw")

# Formulaire Google Form
with col2:
    st.link_button("Google Forms Evaluation"\
                   , url="https://docs.google.com/forms/d/e/1FAIpQLSeBwlY1vaL4GOthBCvTZ23ml1S1Xe20wXX7yY2-M7kD4ark3w/viewform?usp=dialog")
    
