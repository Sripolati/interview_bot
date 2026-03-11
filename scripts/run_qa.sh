export $(cat environments/qa.env | xargs)
streamlit run src/app.py