
//3.14159265

$(document).ready(function(){
	$(".button").click(function(){
    $("#timeline").html("something else");
  
});
// Add the tiles to the map, and initialise the view in the middle of Europe

	 google.charts.load('current', {'packages':['geochart']});
      google.charts.setOnLoadCallback(drawVisualization);
      var fa = [
    // ['State', 'Race distrubution', "median income "], //max is 3 x 3. TODO: Use interactive tutorial
    // ['US-IL\nRace distribution: Whatever ', 200, 1],
    // ['US-IN', 300, 22],
    // ['US-IA', 20,456],
    // ['US-RI', 150,0]

    ['State', 'median income '],
['US-AL',42278],
['US-AK',67629],
['US-AZ',49254],
['US-AR',44922],
['US-CA',60487],
['US-CO',60940],
['US-CT',70161],
['US-DE',57522],
['US-FL',46140],
['US-GA',49555],
['US-HI',71223],
['US-ID',53438],
['US-IL',54916],
['US-IN',48060],
['US-IA',57810],
['US-KS',53444],
['US-KY',42786],
['US-LA',42406],
['US-ME',51710],
['US-MD',76165],
['US-MA',63151],
['US-MI',52005],
['US-MN',67244],
['US-MS',35521],
['US-MO',56630],
['US-MT',51102],
['US-NE',56870],
['US-NV',49875],
['US-NH',73397],
['US-NJ',65243],
['US-NM',46686],
['US-NY',54310],
['US-NC',46784],
['US-ND',60730],
['US-OH',49644],
['US-OK',47199],
['US-OR',58875],
['US-PA',55173],
['US-RI',58633],
['US-SC',44929],
['US-SD',53053],
['US-TN',43716],
['US-TX',53875],
['US-UT',63383],
['US-VT',60708],
['US-VA',66155],
['US-WA',59068],
['US-WV',39552],
['US-WI',58080],
['US-WY',55690]
  ]
      function drawVisualization() {
  var data = google.visualization.arrayToDataTable(fa);
        var chart = new google.visualization.GeoChart(document.getElementById('geochart-colors'));
        //chart.draw(data, options);
          chart.draw(data, {width: 700, height: 700, region: "US", resolution: "provinces", background:"gray"});

      };
});
