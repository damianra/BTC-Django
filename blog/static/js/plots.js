let xdate = [];
let xclose = [];
let xopen = [];
let xmax = [];
let xmin = [];
let text = []

GetData();

async function GetData() {
    fetch("http://127.0.0.1:8000/api/btchistory/")
    .then(response => response.json())
    .then(data => {
        data["results"].forEach(({date,close,open,max_value,min_value}) => {
                        xdate.push(date)
                        xclose.push(parseFloat(close))
                        xopen.push(parseFloat(open))
                        xmax.push(parseFloat(max_value))
                        xmin.push(parseFloat(min_value))
                        text.push('Date: ' + date + '<br>' + 'Open: ' + open + '<br>' + 'Close: ' + close + '<br>' + 'Min.: ' + min_value + '<br>' + 'Max.: ' + max_value)
                        });
                        ShowPlot();
    });
    
}

function ShowPlot(){

    var trace1 = {
                    x: xdate,
                    y: xclose,
                    mode: 'lines+markers',
                    name: 'Close',
                    text: text
                };


    xdata = [trace1]

    var layout = {
    title: 'BTC History',
    }

    Plotly.newPlot('plot', xdata, layout);

} 
