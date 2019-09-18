# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:34:24 2019

@author: daniel.lopez
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML

df = pd.read_csv('9131.csv',sep=';',encoding='latin-1')

current_year = 2018
dff = (df[df['año'].eq(current_year)]
       .sort_values(by='Coste', ascending=True)
       .head(10))
dff

fig, ax = plt.subplots(figsize=(15, 8))
ax.barh(dff['COMUNIDAD'], dff['Coste'])

colors = dict(zip(
    ['Andalucía', 'Aragón', 'Asturias, Principado de', 'Balears,Illes',
     'Canarias', 'Cantabria', 'Castilla y León','Castilla-LaMancha',
     'Cataluña','Comunitat Valenciana','Extremadura','Galicia','Madrid, Comunidad de',
     'Murcia,Región de','Navarra, Comunidad Foral de','País Vasco','Rioja,La'],
    ['#adb0ff', '#ffb3ff', '#90d595', '#e48381',
     '#aafbff', '#f7bb5f', '#eafb50','#909bd5','#db2364','#dbcc23','#66db23',
     '#23d2db','#db6623','#bcdb23','#bf23db','#db236a','#23db8e']
))

group_lk = df.set_index('COMUNIDAD').to_dict()

fig, ax = plt.subplots(figsize=(15, 8))
dff = dff[::-1]   # flip values from top to bottom
# pass colors values to `color=`
ax.barh(dff['COMUNIDAD'], dff['Coste'], color=[colors[i] for i in dff['COMUNIDAD']])

# iterate over the values to plot labels and values (Tokyo, Asia, 38194.2)
for i, (value, name) in enumerate(zip(dff['Coste'], dff['COMUNIDAD'])):
    ax.text(value, i,     name,            ha='right')  # Tokyo: name
#    ax.text(value, i-.25, group_lk[name],  ha='right')  # Asia: group name
    ax.text(value, i,     value,           ha='left')   # 38194.2: value
# Add year right middle portion of canvas
ax.text(1, 0.4, current_year, transform=ax.transAxes, size=46, ha='right')


fig, ax = plt.subplots(figsize=(15, 8))
def draw_barchart(year):
    dff = df[df['año'].eq(year)].sort_values(by='Coste', ascending=True).head(10)
    ax.clear()
    ax.barh(dff['COMUNIDAD'], dff['Coste'],color=[colors[i] for i in dff['COMUNIDAD']])
    dx = dff['Coste'].max() / 200
    for i, (value, name) in enumerate(zip(dff['Coste'], dff['COMUNIDAD'])):
        ax.text(value-dx, i,     name,           size=14, weight=600, ha='right', va='bottom')
        #ax.text(value-dx, i-.25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(value+dx, i,     f'{value:,.0f}',  size=14, ha='left',  va='center')
    # ... polished styles
    ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=30, ha='right', weight=800)
    ax.text(0, 1.06, 'Coste por empleado (euros)', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.12, 'Coste por empleado en las diferentes Comunidades Autonomas',
            transform=ax.transAxes, size=24, weight=600, ha='left')
    ax.text(1, 0, 'by @Nimerya', transform=ax.transAxes, ha='right',
            color='#777777', bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
    plt.box(False)
    
draw_barchart(2018)
x

import matplotlib.animation as animation
from IPython.display import HTML
fig, ax = plt.subplots(figsize=(15, 8))
animator = animation.FuncAnimation(fig, draw_barchart, frames=range(2008, 2019),interval=1000)
animator.to_html5_video(animator.to_jshtml()) 
animator.save('video_to_show.mp4')
animator.to_html5_video()
# or use animator.to_html5_video() or animator.save()
