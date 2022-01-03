import os
import requests
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

from tqdm import tqdm
from plotly.subplots import make_subplots

import plotly.io as pio

class Graph:
    
    def folders():
        if not os.path.exists("img"):
            os.mkdir("img")

        if not os.path.exists("html"):
            os.mkdir("html")


    def save_csv_from_response(response, dataset):
        url_content = response.content
        csv_file = open(dataset + '.csv', 'wb')
        csv_file.write(url_content)
        csv_file.close()
        return True

    def pivot_index(df, index):

        pivot = pd.pivot_table(df, 
                                index=[index],
                                columns=['DEPARTAMENTO'],
                                aggfunc=['size'],
                                fill_value=0)
        return pivot

    def date_list(df):
        x = list(df.index)
        return pd.to_datetime(x, format='%Y%m%d')

    def MA(list_MA):
        numbers_series = pd.Series(list_MA)
        moving_averages = round(numbers_series.ewm(
            alpha=0.5, adjust=False).mean(), 7)
        return moving_averages.tolist()
    

    def departamento_plot(departamentos, date_positivos, date_fallecidos, positivos, fallecidos, i):
        
        # Create figure with secondary y-axis
        ciudad = departamentos[i].title()
        y_fallecidos = list(fallecidos["size"][departamentos[i]])
        y_positivos = list(positivos["size"][departamentos[i]])

        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # #fallecidos
        # fig.add_trace(
        #     go.Scatter(
        #         mode='markers',
        #         line_color='blue',
        #         x=date_fallecidos, 
        #         y=y_fallecidos, 
        #         name="Fallecidos"),
                        
        #     secondary_y=True,
        # )
        
        #MA_positivos
        fig.add_trace(
            go.Scatter(x=date_positivos, 
                        y=Graph.MA(y_positivos),
                        line_color='green', 
                        name="Contagios"),
            secondary_y=False,

        )

        #MA_fallecidos
        fig.add_trace(
            go.Scatter(x=date_fallecidos, 
                        y=Graph.MA(y_fallecidos),
                        line_color='blue', 
                        name="Fallecidos"),
            secondary_y=True,
        )


        # #positivos
        # fig.add_trace(
        #     go.Scatter(
        #         mode='markers',
        #         line_color='green',
        #         x=date_positivos, 
        #         y=y_positivos, 
        #         name="Positivos"),
                        
        #     secondary_y=False,
        # )



        # Set y-axes titles
        fig.update_yaxes(title_text="<b>Contagios</b>", secondary_y=False)
        fig.update_yaxes(title_text="<b>Fallecidos</b>", secondary_y=True)

        # #window
        # fig.update_layout(
        #     xaxis=dict(
        #         rangeselector=dict(
        #             buttons=list([
        #                 dict(count=1,
        #                     label="1m",
        #                     step="month",
        #                     stepmode="backward"),
        #                 dict(count=6,
        #                     label="6m",
        #                     step="month",
        #                     stepmode="backward"),
        #                 dict(step="all")
        #             ])
        #         ),
        #         rangeslider=dict(
        #             visible=True
        #         ),
        #         type="date"
        #     )
        # )

        fig.update_layout(
            title = ciudad +': Fallecidos y Contagiados Media Movil 7 dias',
                xaxis_tickformat = '%d %B %Y',

            showlegend=True,
            template="plotly_white",
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01)
            )
        fig.write_image("img/"+ciudad+".png")
        fig.write_html("html/"+ciudad+".html")
                        
        print(ciudad)