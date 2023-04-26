from flask import Flask, render_template
import pandas as pd

# create app
app = Flask(__name__)

# read data file and select columns for view
stations = pd.read_csv('data_small/stations.txt', skiprows=17)
stations = stations[['STAID', 'STANAME                                 ']]


# define home page
@app.route('/')
def home():

    return render_template('home.html', data=stations.to_html())


# define api url for station and date
@app.route("/api/v1/<station>/<date>")
def station_date(station, date):
    # filename with zfill format.
    filename = 'data_small/TG_STAID' + str(station).zfill(6) + '.txt'
    # parce the date from the data
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # squeeze temperature according to date
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    return {"station": station,
            "date": date,
            "temperature": temperature}


@app.route("/api/v1/<station>")
def all_station_data(station):
    # filename with zfill format.
    filename = 'data_small/TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient='records')
    return result


@app.route("/api/v1/yearly/<station>/<year>")
def single_year_data(station, year):
    # filename with zfill format.
    filename = 'data_small/TG_STAID' + str(station).zfill(6) + '.txt'
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient='records')
    return result


if __name__ == '__main__':
    app.run(debug=True)
