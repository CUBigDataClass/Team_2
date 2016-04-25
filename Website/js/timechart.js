var dData = function() {
            return Math.round(Math.random() * 90) + 10
          };
var dData2 = function() {
            return Math.round(Math.random() * 90) + 10
          };
var dData3 = function() {
            return Math.round(Math.random() * 90) + 10
          };
var dData4 = function() {
            return Math.round(Math.random() * 90) + 10
          };
var canvas = document.getElementById('updating-chart'),
    ctx = canvas.getContext('2d'),
    data = {
      labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
      datasets: [
      {
        label: "Bernie Sanders",
        fillColor: "rgba(100,2,220,0)",
        strokeColor: "rgba(41,8,207,1)",
        pointColor: "rgba(41,8,207,1)",
        pointStrokeColor: "#ffff",
        data: [dData(), dData(), dData(), dData(), dData(), dData(), dData()]
      },
      {
        label: "Hillary Clinton",
        fillColor: "rgba(151,187,205,0)",
        strokeColor: "rgba(8,207,183,1)",
        pointColor: "rgba(8,207,183,1)",
        pointStrokeColor: "#fff",
        data: [dData2(), dData2(), dData2(), dData2(), dData2(), dData2(), dData2()]
      },
      {
        label: "Donald Trump",
        fillColor: "rgba(255,0,0,0)",
        strokeColor: "rgba(255,0,0,1)",
        pointColor: "rgba(255,0,0,1)",
        pointStrokeColor: "#fff",
        data: [dData3(), dData3(), dData3(), dData3(), dData3(), dData3(), dData3()]
      },
      {
        label: "Ted Cruz",
        fillColor: "rgba(151,187,205,0)",
        strokeColor: "rgba(153,8,51,1)",
        pointColor: "rgba(153,8,51,1)",
        pointStrokeColor: "#fff",
        data: [dData4(), dData4(), dData4(), dData4(), dData4(), dData4(), dData4()]
      }
      ]
    },
  latestLabel = data.labels[8];
  var options ={
    animationSteps: 15}
// Reduce the animation steps for demo clarity.
var myLiveChart = new Chart(ctx).Line(data, options);
setInterval(function(){
  // Add two random numbers for each dataset
  myLiveChart.addData([[dData()],[dData2()],[dData3()],[dData4()]], ++latestLabel);
  // Remove the first point so we dont just add values forever
  myLiveChart.removeData();
}, 5000);
legend(document.getElementById('placeholder'), data);

