console.log("sanity check!")


// let ctx = document.getElementById('myChart').getContext('2d');
let ctx2 = document.getElementById('mixedChart').getContext('2d');
// let myChart = new Chart(ctx, {
//     type: 'doughnut',
//     data: {
//         labels: ['Utility', 'Transportation', 'Shopping', 'dinner', 'bar', 'groceries'],
//         datasets: [{
//             data: [12, 19, 3, 5, 2, 3],
//             backgroundColor: [
//                 'rgba(255, 99, 132, 0.2)',
//                 'rgba(54, 162, 235, 0.2)',
//                 'rgba(255, 206, 86, 0.2)',
//                 'rgba(75, 192, 192, 0.2)',
//                 'rgba(153, 102, 255, 0.2)',
//                 'rgba(255, 159, 64, 0.2)'
//             ],
//             borderColor: [
//                 'rgba(255, 99, 132, 1)',
//                 'rgba(54, 162, 235, 1)',
//                 'rgba(255, 206, 86, 1)',
//                 'rgba(75, 192, 192, 1)',
//                 'rgba(153, 102, 255, 1)',
//                 'rgba(255, 159, 64, 1)'
//             ],
//             borderWidth: 1
//         }]
//     },

// });

fetch('http://localhost:8000/api/user/1/budget/4')
    .then((response) => {
        return response.json()
    })
    .then((data) => {

        render(data)
        console.log(data)
    })

const render = (data) => {
    let mixedChart = new Chart(ctx2, {
        type: 'bar',
        data: {
            datasets: [{
                label: data.budget_name,
                data: [data.budget_total],
                backgroundColor: 'rgba(255, 99, 132)',

            }, {
                label: 'Currently',
                data: [data.expense_total],
                backgroundColor: 'rgba(255, 99, 132, 0.8',
                type: 'bar'
            }],
            labels: ['Budget1']
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });

}
