import numpy as np
import plotly.graph_objects as go
from random import randint
import time

def simulateThrow(currentCash):
  side = randint(0, 1) # 0: Heads, 1: Tails
  return currentCash * (1.5 if side == 0 else 0.6)

def simulatePlayer(throws):
  data = [100]
  for _ in range(throws):
    data.append(simulateThrow(data[-1]))
  return data

def simulate(numberOfPlayers, throws):
  return [simulatePlayer(throws) for _ in range(numberOfPlayers)]

def scatter(data, color, name = '', showlegend = True):
  return go.Scatter(
    x = np.arange(len(data)),
    y = data,
    name = name,
    showlegend = showlegend,
    line = {'color': color}
  )

def writeImage(fig, name):
  fig.write_image(f'{name}.pdf')
  time.sleep(1)
  fig.write_image(f'{name}.pdf') # NOTE: Fixes "Loading [MathJax]/extensions/MathMenu.js" showing in other pdf plots

def plotMean(mean):
  fig = go.Figure(scatter(mean, 'blue'))

  fig.update_layout(
    xaxis_title = 'Tirada',
    yaxis_title = 'Riqueza Promedio ($)',
    showlegend = False,
  )

  writeImage(fig, 'mean')

def plotPaths(data):
  fig = go.Figure()
  for path in data:
    fig.add_trace(scatter(path, 'red'))

  fig.add_hline( # Horizontal line at breaking even
    y = data[0][0],
    line = {'color': 'gray'}
  )

  fig.update_layout(
    xaxis_title = 'Tirada',
    yaxis_title = 'Riqueza ($)',
    showlegend = False,
  )

  writeImage(fig, 'paths')

def plotLogPaths(data, mean, median):
  fig = go.Figure()
  for i in range(len(data)):
    fig.add_trace(scatter(data[i], 'pink', 'Riqueza Individual', i == 0))
  fig.add_trace(scatter(mean, 'blue', 'Riqueza Promedio'))
  fig.add_trace(scatter(median, 'red', 'Riqueza Mediana'))

  fig.add_hline( # Horizontal line at breaking even
    y = data[0][0],
    line = {'color': 'gray'}
  )

  fig.update_layout(
    xaxis_title = 'Tirada',
    yaxis_title = 'Riqueza (log, $)',
    showlegend = True,
  )
  fig.update_yaxes(type = 'log')

  writeImage(fig, 'logPaths')

def plot(numberOfPlayers, throws):
  data = simulate(numberOfPlayers, throws)
  transposed = [[x[t] for x in data] for t in range(throws)]
  mean = [np.mean(x) for x in transposed]
  median = [np.median(x) for x in transposed]

  selected = data.copy()
  np.random.shuffle(selected)
  selected = selected[:20]

  plotMean(mean)
  plotPaths(selected)
  plotLogPaths(selected, mean, median)

plot(10000, 100)
# plot(3, 4)
