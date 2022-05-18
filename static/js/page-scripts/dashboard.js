(function ($) {
  $(document).ready(function () {


    // Main Toggle Line Chart

    fetch("static/js/data.json")
      .then(res => res.json())
      .then(data => {
        console.log("2", data);
        var toggleData = {
          revenue: {
            label: 'Sequenced',
            data: [1200, 940, 1340, 1440, 2420, 1100, 4545]
          },
          users: {
            label: 'Projects',
            data: [3, 1, 4, 2, 5, 2, 2]
          },
          ctr: {
            label: 'Samples',
            data: [18, 50, 42, 20, 14, 22, 24]
          }
        };
        var ctx = $("#main-toggle-line-chart");
        var myLineChart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: ["November", "December", "January", "February", "March", "April", "May"],
            datasets: [{
              label: toggleData['revenue'].label,
              data: toggleData['revenue'].data,
              lineTension: 0,
              fill: 0
            }]
          },
          options: {
            hover: {
              mode: 'index',
              intersect: false
            },
            maintainAspectRatio: false,
          }
        });

        $("#main-toggle-line-chart")
          .closest('.card').find('.card-metrics')
          .on('click', '.card-metric', function (e) {
            e.stopPropagation();
            var card = $(this).closest('.card');
            var cardChart = card.find($('.card-chart'));

            if (cardChart.length) {
              var chart = chartExists(cardChart);
              var metric = $(this).attr('data-metric');

              if (!!chart && toggleData.hasOwnProperty(metric)) {
                $(this).siblings().removeClass('active');
                $(this).addClass('active');
                var index = $(this).index();
                var isActive = $(this).hasClass('active');

                chart.data.datasets[0].data = toggleData[metric].data;
                chart.data.datasets[0].label = toggleData[metric].label;
                chart.update();
              }
            }
          });
      })

    // Mini Flush Charts
    var $flushAreaChartBlue = $('#flush-area-chart-blue');
    if ($flushAreaChartBlue.length) {
      var blueData = {
        labels: ['one', 'two', 'three', 'four', 'five'],
        datasets: [{
          backgroundColor: chartColorBlue,
          borderColor: chartColorBlue,
          data: [2, 4, 7, 3, 8],
          label: 'Number'
        }]
      };
      var flushAreaChartBlue = new Chart($flushAreaChartBlue, {
        type: 'line',
        data: blueData,
        options: flushChartOptions
      });
    }

    var $flushAreaChartYellow = $('#flush-area-chart-yellow');
    if ($flushAreaChartYellow.length) {
      var yellowData = {
        labels: ['one', 'two', 'three', 'four', 'five'],
        datasets: [{
          backgroundColor: chartColorYellow,
          borderColor: chartColorYellow,
          data: [5, 6, 3, 3, 9],
          label: 'Number'
        }]
      };
      var flushAreaChartYellow = new Chart($flushAreaChartYellow, {
        type: 'line',
        data: yellowData,
        options: flushChartOptions
      });
    }

    var $flushAreaChartPink = $('#flush-area-chart-pink');
    if ($flushAreaChartPink.length) {
      var pinkData = {
        labels: ['one', 'two', 'three', 'four', 'five'],
        datasets: [{
          backgroundColor: chartColorPink,
          borderColor: chartColorPink,
          data: [7, 5, 3, 6, 6],
          label: 'Number'
        }]
      };
      var flushAreaChartPink = new Chart($flushAreaChartPink, {
        type: 'line',
        data: pinkData,
        options: flushChartOptions
      });
    }

    var $flushAreaChartGreen = $('#flush-area-chart-green');
    if ($flushAreaChartGreen.length) {
      var greenData = {
        labels: ['one', 'two', 'three', 'four', 'five'],
        datasets: [{
          backgroundColor: chartColorGreen,
          borderColor: chartColorGreen,
          data: [9, 3, 7, 5, 4],
          label: 'Number'
        }]
      };
      var flushAreaChartGreen = new Chart($flushAreaChartGreen, {
        type: 'line',
        data: greenData,
        options: flushChartOptions
      });
    }


    // Doughnut chart
    //var doughnutTooltip = Object.assign({}, tooltipsOpts);
    //doughnutTooltip.intersect = true;
    //doughnutTooltip.callbacks = { footer: percentageFooterCallback };
    //delete doughnutTooltip.mode;
    var d = fetch("history_line_data")
      .then(res => res.json())
      .then(data => {
        console.log("history_line_data yes, ", data[0]["a"]);
      })
      .catch(err => console.log("Fetch history_line_data failed"))


    var doughnutChart = $('#doughnut-chart');
    if (doughnutChart.length) {
      var doughnutChartJS = new Chart(doughnutChart, {
        type: 'doughnut',
        data: {
          labels: ["pre-seq", "bcl", "mkfastq", "count", "delivery"],
          datasets: [{
            label: 'dataset 1',
            data: [12, 19, 4, 15, 22],
            backgroundColor: [chartColorPink, chartColorBlue, chartColorYellow, chartColorGreen, chartColorPurple],
            borderWidth: 0
          }],
        },
        options: {
          //tooltips: doughnutTooltip,
          legendCallback: doughnutLegendCallback,
          cutoutPercentage: 80
        }
      });
      doughnutChart.closest('.card-content').find('.chart-legend-wrapper').append($(doughnutChartJS.generateLegend()));
    }

  });
}(jQuery));
