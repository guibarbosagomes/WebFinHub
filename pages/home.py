import streamlit as st
import streamlit_authenticator as stauth
from st_pages import Page, Section, add_page_title, show_pages


import yaml
from yaml.loader import SafeLoader

from pathlib import Path


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
    
    with st.echo("below"):

        "## Declaring the pages in your app:"

        show_pages(
            [
                Page("pages/home.py", "Home", "🏠"),
                # Can use :<icon-name>: or the actual icon
                Page("pages/example_one.py", "Example One", ":books:"),
                # The pages appear in the order you pass them
                Page("pages/example_four.py", "Example Four", "📖"),
                Page("pages/example_two.py", "Example Two", "✏️"),
                # Will use the default icon and name based on the filename if you don't
                # pass them
                Page("pages/example_three.py")
            ]
        )

        add_page_title()  # Optional method to add title and icon to current page
        
        # authenticator.logout('Sair', 'sidebar', key='unique_key')

elif authentication_status is False:
    st.error('Usuário ou senha esta incorreto')

elif authentication_status is None:
    st.warning('Por favor informe seu usuário e senha.')