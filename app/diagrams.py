import numpy as np
import pandas as pd
import kaleido
import plotly
import plotly.graph_objs as go


def plot_bar(txt_path):
    count = np.array([])
    classes = ['дерево', 'стекло', 'пластик', 'металл']
    with open(txt_path, 'r') as file:
        for line in file:
            count = np.append(count, int(line))
    df = pd.DataFrame({'Категория ТБО': classes, 'Кол-во': count})
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df['Категория ТБО'].tolist(), y=df['Кол-во'].tolist(),
                         marker=dict(color=list(range(len(df))))))
    fig.update_layout(
        title='<span style="font-size: 20px;">Общее кол-во ТБО по категориям</span>', title_x=0.5,
        xaxis_title='<span style="font-size: 16px;">Категория ТБО</span>',
        yaxis_title='<span style="font-size: 16px;">Кол-во</span>',
        height=700,
        margin=dict(l=0, r=0, b=0)
    )
    fig.update_xaxes(tickangle=315, tickfont=dict(size=14), gridwidth=2, gridcolor='ivory')
    fig.update_yaxes(tickfont=dict(size=14), gridwidth=2, gridcolor='ivory')
    fig.write_image('templates/assets/img/img_bar.png')


def plot_pie(txt_path):
    count = np.array([])
    classes = ['дерево', 'стекло', 'пластик', 'металл']
    with open(txt_path, 'r') as file:
        for line in file:
            count = np.append(count, int(line))
    df = pd.DataFrame({'Категория ТБО': classes, 'Кол-во': count})
    fig = go.Figure()
    fig.add_trace(go.Pie(labels=df['Категория ТБО'].tolist(), values=df['Кол-во'].tolist(),
                         marker=dict(colors=list(range(len(df))),
                                     line=dict(color='black', width=2)),
                         hole=.4, hoverinfo='label+percent', textfont_size=16,))
    fig.update_layout(
        title='<span style="font-size: 20px;">Общее кол-во ТБО по категориям</span>', title_x=0.5,
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.1, font=dict(size=18)),
        height=700,
        margin=dict(l=0, r=0, b=0)
    )
    fig.update_xaxes(tickangle=315, tickfont=dict(size=14), gridwidth=2, gridcolor='ivory')
    fig.update_yaxes(tickfont=dict(size=14), gridwidth=2, gridcolor='ivory')
    fig.write_image('templates/assets/img/img_pie.png')


