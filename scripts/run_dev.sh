export $(cat environments/dev.env | xargs)
streamlit run src/app.py