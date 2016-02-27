$(document).ready(function(){
	

	google.charts.load('current', {'packages':['geochart']});
      google.charts.setOnLoadCallback(drawRegionsMap);

      function drawRegionsMap() {

        var data = google.visualization.arrayToDataTable([
          ['Country', 'Popularity', "number of hoes"],
          ['Germany', 200, 5.4],
          ['United States', 300, 10],
          ['Brazil', 400, 89],
          ['Canada', 500,12],
          ['France', 600,33],
          ['RU', 700,1283]
        ]);

        var options = {
          region: '019', // Africa
          colorAxis: {colors: ['#00853f', 'black', '#e31b23']},
          backgroundColor: '#81d4fa',
          datalessRegionColor: '#f8bbd0',
          defaultColor: '#f5f5f5',
        };

        var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

        chart.draw(data, options);
      };

      function consoleLog(){
      	alert("console logged");
      }
      consoleLog();




});