export $(cat environments/prod.env | xargs)
streamlit run src/app.py