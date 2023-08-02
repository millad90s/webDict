  $(function () {
    var interactive_plot = $.plot('#bar-chart', 
      {
        grid: {
          borderColor: '#f3f3f3',
          borderWidth: 1,
          tickColor: '#f3f3f3'
        },
        series: {
          color: '#3c8dbc',
          lines: {
            show: true,
            fill: true,
          },
        },
        yaxis: {
          min: 0,
          max: 50,
          show: true
        },
        xaxis: {
          show: true
        }
      }
    )
    var bar_data = {
      data : [[1,10], [2,8], [3,30], [4,13], [5,17], [6,9]],
      bars: { show: true }
    }
    $.plot('#bar-chart', [bar_data], {
      grid  : {
        borderWidth: 1,
        borderColor: '#f3f3f3',
        tickColor  : '#f3f3f3'
      },
      series: {
         bars: {
          show: true, barWidth: 0.25, align: 'center',
        },
      },
      colors: ['#3c8dbc'],
      xaxis : {
        ticks: 
        [[1,'O1'], [2,'O2'], [3,'O3'],
        [4,'O4'], [5,'O5'], [6,'O6']]
      }
    })
  })
