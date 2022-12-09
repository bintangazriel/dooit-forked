const renderChart2 = (data1,data2) => {
    var ctx = document.getElementById("myChart2").getContext("2d");
    const myChart2 = new Chart(ctx, {
        type: 'line',
        data: {
            datasets: [{
                label: 'Pemasukan',
                data: data1,
                // this dataset is drawn below
                order: 2
            }, {
                label: 'Pengeluaran',
                data: data2,
                type: 'line',
                // this dataset is drawn on top
                order: 1
            }],
            labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        },
        options: {
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