const backColor = ['rgba(89, 160, 17, 0.61)', 'rgba(247, 130, 12, 0.45)','rgba(193, 66, 66, 0.45)','rgba(227, 247, 12, 0.45)', 'rgba(12, 247, 235, 0.45)', 'rgba(12, 51, 247, 0.45)', 'rgba(157, 12, 247, 0.45)', 'rgba(243, 12, 247, 0.45)', 'rgba(110, 247, 12, 0.45)', 'rgba(135, 125, 129, 0.45)','rgba(193, 66, 66, 0.45)', 'rgba(247, 130, 12, 0.45)','rgba(227, 247, 12, 0.45)', 'rgba(71, 247, 12, 0.45)', 'rgba(12, 247, 235, 0.45)', 'rgba(12, 51, 247, 0.45)', 'rgba(157, 12, 247, 0.45)', 'rgba(243, 12, 247, 0.45)', 'rgba(110, 247, 12, 0.45)', 'rgba(135, 125, 129, 0.45)', 'rgba(193, 66, 66, 0.45)']

var ctx = document.getElementById("allCountChart").getContext("2d");
var chartData = null;
if(ctx != null){
    chartData = JSON.parse(document.getElementById('chartData').textContent);
}

var myChart = new Chart(ctx, {
	type: "doughnut", 
	data : {
		labels: chartData.label,
		datasets:[
			{
				data: chartData.data,
				label: "Completed Progress",
				backgroundColor: backColor,
				borderWidth: 1,
			}
		]
	},
	options: {
		responsive:false,
	},
});

// code for questionData
var qtx = document.getElementById("allQuestionChart").getContext("2d");
var questionData = null;
if(ctx != null){
    questionData = JSON.parse(document.getElementById('questionData').textContent);
}

var myChart = new Chart(qtx, {
	type: "bar", 
	data : {
		labels: questionData.label,
		datasets:[
			{
				data: questionData.data,
				label: "Questions Type",
				backgroundColor: backColor,
				borderWidth: 1,
			}
		]
	},
	options: {
		responsive:true,
		scales: {
			xAxes: [{
				ticks: {
					autoSkip: false,
					maxRotation: 90,
					minRotation: 90
				}
			}]
		},
		plugins: {
            title: {
                display: true,
                text: 'Distribution of Question',
                padding: {
                    top: 5,
                    bottom:10 
                },
				font: {
					size: 20
				}
            }, 
			legend: {
				display:false,
			}
        }
	},
});