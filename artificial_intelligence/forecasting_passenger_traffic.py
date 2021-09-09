import datetime 
import pandas as pd
import plotly.express as px
from neuralprophet import NeuralProphet

def read_in_hackerrank_data():

    n = int(input())

    dict_for_df = { 'month':[], 
                    'passengers':[]
                    }

    for _ in range(n):

        # change to removing input when not in Hackerrank
        month, passenger_amount = input().split()

        dict_for_df['month'].append(month)
        dict_for_df['passengers'].append(int(passenger_amount))

    df = pd.DataFrame(dict_for_df)

    return df

# example data from hackerrank, using 
if __name__ == '__main__':

    # hackerrank input
    #df = read_in_hackerrank_data()

    path = '/Users/niklastodenhoefer/Downloads/forecasting-passenger-traffic-testcases/input/input00.txt'

    df = pd.read_csv(path, 
                        sep='\t', 
                        names=['ds', 'y']
                        )

    """ plotting with plotly
    print(df.head())

    # some plotting
    fig = px.line(df, 
                    x="ds", 
                    y="y", 
                    title='Amount of Traffic passengers per month')
    fig.show()"""

    num_months = len(df)

    # create 60 days data
    base = datetime.datetime.today()
    date_list = [base + datetime.timedelta(days=x) for x in range(num_months)]
    print(date_list)

    # move dates into df
    df['ds'] = date_list

    print(df.head())

    """
    # getting the train/test split with 45 from 60 data points
    test_length = 45
    df_train = df.iloc[:-test_length]
    df_test = df.iloc[-test_length:]"""

    periods_ahead = 12


    nprophet = NeuralProphet()
    # monthly data
    metrics = nprophet.fit(df, 
    # frequency D is important, as otherwise the model predicts months in advance
                            freq="D"
                            )
    future_df = nprophet.make_future_dataframe(df, 
                                                    periods = periods_ahead,
                                                    n_historic_predictions=len(df)
                                                    )
    preds_df = nprophet.predict(future_df)

    print(preds_df.tail(10))

    # getting the yhat1 column values
    results = preds_df.iloc[-periods_ahead:,2].tolist()

    print(results)

    # results plotting
    res = px.line(preds_df, 
                    x="ds", 
                    y="yhat1", 
                    title='Amount of Traffic passengers per month')
    res.show()