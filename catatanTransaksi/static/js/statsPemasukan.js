const renderChart2 = (data1,data2) => {
    var ctx = document.getElementById("myChart2").getContext("2d");
    let gradient = ctx.createLinearGradient(0,0,0,400);
    gradient.addColorStop(0,"rgba(58,123,213,1)")
    gradient.addColorStop(1,"rgba(0,210,255,0.3)")
    const myChart2 = new Chart(ctx, {
        type: 'line',
        data: {
            datasets: [{
                label: 'Pemasukan',
                data: data1,
                // this dataset is drawn below
                backgroundColor: [
                    "rgba(255, 99, 132, 0.2)",
                    "rgba(54, 162, 235, 0.2)",
                    "rgba(255, 206, 86, 0.2)",
                    "rgba(75, 192, 192, 0.2)",
                    "rgba(153, 102, 255, 0.2)",
                    "rgba(255, 159, 64, 0.2)",
                  ],
                  borderColor: [
                    "rgba(255, 99, 132, 1)",
                    "rgba(54, 162, 235, 1)",
                    "rgba(255, 206, 86, 1)",
                    "rgba(75, 192, 192, 1)",
                    "rgba(153, 102, 255, 1)",
                    "rgba(255, 159, 64, 1)",
                  ],
                order: 2,
            }, {
                label: 'Pengeluaran',
                data: data2,
                backgroundColor: [
                    "rgba(255, 99, 132, 0.2)",
                    "rgba(54, 162, 235, 0.2)",
                    "rgba(255, 206, 86, 0.2)",
                    "rgba(75, 192, 192, 0.2)",
                    "rgba(153, 102, 255, 0.2)",
                    "rgba(255, 159, 64, 0.2)",
                  ],
                  borderColor: [
                    "rgba(255, 99, 132, 1)",
                    "rgba(54, 162, 235, 1)",
                    "rgba(255, 206, 86, 1)",
                    "rgba(75, 192, 192, 1)",
                    "rgba(153, 102, 255, 1)",
                    "rgba(255, 159, 64, 1)",
                  ],
                type: 'line',
                order: 1
            }],
            labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        },
        options: {
            responsive: true,
            title: {
              display: true,
              text: "Expenses per category",
            },
          },
     });
  };
  
  const getChartData2 = () => {
    console.log("fetching");
    fetch("get_vis_pemasukan_pengeluaran_by_waktu")
      .then((res) => res.json())
      .then((results) => {
        console.log("results", results);
        const rdata1 = results.income_time_data;
        const rdata2 = results.expense_time_data;
        const [data1,data2] = [
          Object.values(rdata1),
          Object.values(rdata2),
        ];
  
        renderChart2(data1,data2);
      });
  };
  
  document.onload = getChartData2();