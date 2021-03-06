var pie = new d3pie("pieChartHillary", {
  // "size": {
  //    "canvasHeight": 120,
  //    "canvasWidth": 140
  // },
  "header": {
    "title": {
      "text": "Hillary Clinton Results",
      "fontSize": 32,
      "font": "open sans"
    },
    "subtitle": {
      "text": "Data Taken from 04/05/16-04/22/16",
      "color": "#999999",
      "fontSize": 15,
      "font": "open sans"
    },
    "titleSubtitlePadding": 20
  },
  "footer": {
    "text": "Total Tweets: 545,019",
    "color": "#777777",
    "fontSize": 20,
    "font": "verdana",
    "location": "bottom-center"
  },
  "misc": {
    "gradient": {
      "enabled": true,
      "percentage": 100
    },
    "canvasPadding": {
      "top": 25,
      "left": 5
    }
  },
  "data": {
    "content": [
      {
        "value": 303419,
        "color": "#7e3838"
      },
      {
        "value": 241600,
        "color": "#587e38"
      }
    ]
  },
  "labels": {
    "outer": {
      "pieDistance": 0
    },
    "mainLabel": {
      "fontSize": 17
    },
    "percentage": {
        "color": "#ffffff",
        "fontSize": 15,
        "decimalPlaces": 0
    }
  }
}
);
