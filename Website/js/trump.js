var pie = new d3pie("pieChartTrump", {
  // "size": {
  //    "canvasHeight": 120,
  //    "canvasWidth": 140
  // },
  "header": {
    "title": {
      "text": "Donald Trump Results",
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
    "text": "Total Tweets: 1,584,928",
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
        "value": 697389,
        "color": "#7e3838"
      },
      {
        "value": 887539,
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
