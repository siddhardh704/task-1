import pandas as pd
df = pd.read_csv("C:\\Users\\siddh\\OneDrive\\Desktop\\siddhardh\\customer_details.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print("Missing Values:\n", df.isnull().sum())
df = df.dropna()
df = df.drop_duplicates()
if 'gender' in df.columns:
    df['gender'] = df['gender'].str.lower()
    df['gender'] = df['gender'].replace({
        'MALE': 'male',
        'FEMALE': 'female'
    })
if 'age' in df.columns:
    df['age'] = df['age'].astype(int)
if 'review_rating' in df.columns:
    df['review_rating'] = df['review_rating'].astype(float)
if 'previous_purchases' in df.columns:
    df['previous_purchases'] = df['previous_purchases'].astype(int)
if 'season' in df.columns:
    df['season'] = df['season'].str.capitalize()
if 'category' in df.columns:
    df['category'] = df['category'].str.capitalize()
df.to_csv("C:\\Users\\siddh\\OneDrive\\Desktop\\siddhardh\\customer_details.csv", index=False)
print(df.head(10))
print("finally the data is cleaned")