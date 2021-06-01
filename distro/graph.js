let csv_data, rows, cols, choice1, choice2
let previous, previous2, xdata, ydata, x2data, y2data


function init() {
  previous = 0
  previous2 = 0
  xdata = []
  ydata = []
  x2data = []
  y2data = []
}

function preload() {
  csv_data = loadTable('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
}

function setup() {
  noCanvas()

  rows = csv_data.getRowCount()
  cols = csv_data.getColumnCount()
}



function create() {
  choice1=document.querySelector("#state1").value
  choice2=document.querySelector("#state2").value
  init()
  createGraph()
}

function createGraph() {
  for (let i = 0; i < rows; i++) {
    let state = csv_data.getString(i, 1)
    if (state == choice1) {
      xdata.push(csv_data.getString(i, 0))
      ydata.push(parseInt(csv_data.getString(i, 3) - previous))
      previous = parseInt(csv_data.getString(i, 3))
    }
    else if (state == choice2) {
      x2data.push(csv_data.getString(i, 0))
      y2data.push(parseInt(csv_data.getString(i, 3) - previous2))
      previous2 = parseInt(csv_data.getString(i, 3))
    }
  }


  let trace1 = {
    x: xdata,
    y: ydata,
    mode: 'lines',
    name: choice1,
    line: {
      color: 'rgb(219, 64, 82)',
      width: 1
    }
  };

  let trace2 = {
    x: x2data,
    y: y2data,
    name: choice2,
    line: {
      color: 'rgb(55, 128, 191)',
      width: 1
    }
  }

  let layout = {
    // width: windowWidth - 50,
    height: windowHeight - 80
  }


  let data = [trace1, trace2]

  Plotly.newPlot('myDiv', data, layout);
}


