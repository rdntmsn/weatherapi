from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route('/')
def home():

    return render_template('home.html')


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = 'data_small/TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # data_no_missing_value = df.loc[df['   TG'] != -9999]
    # df["TG0"] = df['   TG'].mask(df['   TG'] == -9999, np.nan)
    # df["TG"] = df['TG0'] / 10
    # date = data_no_missing_value["    DATE"]
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == '__main__':
    app.run(debug=True)
