$(document).ready(function(){

	$(".button").click(function(){
    $("#timeline").html("yay");
});

	google.charts.load('current', {'packages':['geochart']});
      google.charts.setOnLoadCallback(drawRegionsMap);

      function drawRegionsMap() {

        var data = google.visualization.arrayToDataTable([
          ['country', 'Popularity', "number of hoes"],
          ['united states', 200, 5.4],
          ['Canada', 300, 10],
          ['Germany', 400, 89],
          ['India', 500,12],
          ['China', 600,33],
          ['South Africa', 700,1283]
        ]);

        var options = {
         // region: '019', 
         // colorAxis: {colors: ['#00853f', 'black', '#e31b23']},
         // backgroundColor: '#81d4fa',
          //datalessRegionColor: '#f8bbd0',
          //defaultColor: '#f5f5f5',
        };

        var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

        chart.draw(data, options);
      };

      function consoleLog(){
      	alert("console logged");
      }
      consoleLog();




});