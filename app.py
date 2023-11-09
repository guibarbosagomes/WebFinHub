import streamlit as st
import streamlit_authenticator as stauth
from st_pages import Page, Section, add_page_title, show_pages

import yaml
from yaml.loader import SafeLoader

def graficos():

    st.write(f'Bem vindo *{name}*')
    st.title('Outro Conteudo')


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Sair', 'sidebar', key='unique_key')

    # Either this or add_indentation() MUST be called on each page in your
    # app to add indendation in the sidebar
    add_page_title()

    # Specify what pages should be shown in the sidebar, and what their titles and icons
    # should be
    show_pages(
        [
            Page("streamlit_app.py", "Home", "🏠"),
            Page("other_pages/page2.py", "Page 2", ":books:"),
            Section("My section", icon="🎈️"),
            # Pages after a section will be indented
            Page("Another page", icon="💪"),
            # Unless you explicitly say in_section=False
            Page("Not in a section", in_section=False)
        ]
    )
elif authentication_status is False:
    st.error('Usuário ou senha esta incorreto')

elif authentication_status is None:
    st.warning('Por favor informe seu usuário e senha.')



