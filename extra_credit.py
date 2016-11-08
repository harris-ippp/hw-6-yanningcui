import requests
import pandas as pd

def plot_replican_share(county):
    years = []
    for line in open("ELECTION_ID"):
        year, el_id = tuple(line.split())
        years.append(year)

    all_lst = []
    for year in years:
        header = pd.read_csv(str(year)+".csv", nrows = 1).dropna(axis = 1)
        d = header.iloc[0].to_dict()

        df = pd.read_csv(str(year)+".csv", index_col = 0, \
                         thousands = ",", skiprows = [1])
        df.rename(inplace = True, columns = d) # rename to democrat/republican
        df.dropna(inplace = True, axis = 1)    # drop empty columns
        df["Year"] = year
        df = df[["Democratic", "Republican", "Total Votes Cast", "Year"]]
        all_lst.append(df)

        election_df = pd.concat(all_lst)
        election_df["Republican%"] = election_df["Republican"]/\
                                     election_df["Total Votes Cast"] * 100
        selected_county = election_df[election_df.index == county]
        selected_county_plot = selected_county.plot(x = "Year", y = "Republican%", \
                                                    title = str(county))
        selected_county_plot.get_figure().savefig(county+".png")
