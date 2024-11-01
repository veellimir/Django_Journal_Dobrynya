alert("Раздел статистика в разработке !")
const attendanceData = JSON.parse(document.getElementById('attendance_data').textContent),
      canvas = document.getElementById('attendanceGraph'),
      ctx = canvas.getContext('2d');

function drawGraph(year) {
    if (window.attendanceChart) {window.attendanceChart.destroy();}

    const labels = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'],
          graphData = {labels: labels, datasets: []},
          yearData = attendanceData[year],
          directionNames = new Set();

    Object.values(yearData).forEach(monthData => {
        Object.keys(monthData).forEach(direction => {
            directionNames.add(direction);
        });
    });

    directionNames.forEach((direction, directionIndex) => {
        const directionData = labels.map((_, monthIndex) => {
            const monthData = yearData[monthIndex + 1];
            let totalCount = 0;

            if (monthData && monthData[direction]) {
                Object.values(monthData[direction]).forEach(count => {
                    totalCount += count;
                });
            }
            return totalCount;
        });

        const colors = [
            '#6a5acd', '#ff7f50', '#98fb98', '#87cefa', '#ffa07a', '#d3d3d3', '#32cd32', '#ff6347',
            '#ba55d3', '#ff1493', '#add8e6', '#f0e68c'
        ];

        graphData.datasets.push({
            label: direction,
            data: directionData,
            backgroundColor: colors[directionIndex % colors.length],
            borderColor: colors[directionIndex % colors.length],
            borderWidth: 2,
        });
    });

    const options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: 'Количество посещений'
                },
                ticks: {
                    callback: function(value) {
                        return value % 1 === 0 && value !== 0 ? value : '';
                    }
                }
            },
            x: {
                title: {
                    display: true,
                    text: 'Месяцы'
                }
            }
        },
        plugins: {
            legend: {
                position: 'top',
            },
            tooltip: {
                callbacks: {
                    label: function(tooltipItem) {
                        const datasetIndex = tooltipItem.datasetIndex,
                              monthIndex = tooltipItem.dataIndex,
                              direction = graphData.datasets[datasetIndex].label,
                              monthData = yearData[monthIndex + 1] && yearData[monthIndex + 1][direction];
                        let tooltipText = [`${direction}:`];

                        if (monthData) {
                            Object.entries(monthData).forEach(([profile, count]) => {
                                if (count > 0) {
                                    tooltipText.push(`${profile}: ${Math.round(count)} присутствовал(а)`);
                                }
                            });
                        }
                        return tooltipText.length > 1 ? tooltipText : '';
                    }
                }
            }
        }
    };

    window.attendanceChart = new Chart(ctx, {
        type: 'bar',
        data: graphData,
        options: options
    });
}

function updateYear() {
    const selectedYear = document.getElementById('year-select').value;
    drawGraph(selectedYear);
}

const years = Object.keys(attendanceData),
      initialYear = years[years.length - 1];

drawGraph(initialYear);
