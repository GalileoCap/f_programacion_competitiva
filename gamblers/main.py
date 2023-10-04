import numpy as np
import plotly.graph_objects as go
from random import randint

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

def scatter(data, color):
  return go.Scatter(
    x = np.arange(len(data)),
    y = data,
    line = {'color': color}
  )

def plotMean(mean):
  fig = go.Figure(scatter(mean, 'blue'))

  fig.update_layout(
    xaxis_title = 'Tirada',
    yaxis_title = 'Riqueza Promedio ($)',
  )

  fig.write_image('mean.png')

def plotPaths(data, n):
  fig = go.Figure()
  for path in data[:n]:
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

  fig.write_image('paths.png')

def plotLogPaths(data, mean, median, n):
  fig = go.Figure()
  for path in data[:n]:
    fig.add_trace(scatter(path, 'pink'))
  fig.add_trace(scatter(mean, 'blue'))
  fig.add_trace(scatter(median, 'red'))

  fig.add_hline( # Horizontal line at breaking even
    y = data[0][0],
    line = {'color': 'gray'}
  )

  fig.update_layout(
    xaxis_title = 'Tirada',
    yaxis_title = 'Riqueza (log, $)',
    showlegend = False,
  )
  fig.update_yaxes(type = 'log')

  fig.write_image('logPaths.png')

def plot(numberOfPlayers, throws):
  data = simulate(numberOfPlayers, throws)
  transposed = [[x[t] for x in data] for t in range(throws)]
  mean = [np.mean(x) for x in transposed]
  median = [np.median(x) for x in transposed]

  plotMean(mean)
  plotPaths(data, 20)
  plotLogPaths(data, mean, median, 20)

plot(10000, 100)
# plot(3, 4)
