let labelsArray = []
let colorArray = []
let borderArray = []
let dataArray = []

let ctx = document.getElementById('myChart').getContext('2d');
let ctx2 = document.getElementById('mixedChart').getContext('2d');

let budgetTitle = document.query
let budgets_select = document.querySelectorAll('#budgets a')
budgets_select.forEach(budget => budget.addEventListener('click', renderGraph))


const getRandomColor = () => {
    color = "rgba("
    for (i = 0; i < 3; i++) {
        color += Math.floor(Math.random() * (255)) + 0 + ', '
    }
    color += '1)'
    return color    
}


function renderGraph(event) {
    event.preventDefault()
    renderHelper(event.target.getAttribute('value') ,event.target.id)
}


function renderHelper(user_id, budget_id) {
    fetch('http://localhost:8000/api/user/' + user_id + '/budget/' + budget_id)
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            render(data)
        })
}

const render = (data) => {
    labelsArray.length = 0 
    colorArray.length = 0
    borderArray.length = 0
    dataArray.length = 0
    data.categories.forEach(e => labelsArray.push(e.name))
    data.categories.forEach(e => dataArray.push(e.total))
    data.categories.forEach(e => colorArray.push(getRandomColor()))
    data.categories.forEach(e => borderArray.push(getRandomColor()))

    let myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labelsArray,
            datasets: [{
                data: dataArray,
                backgroundColor: colorArray,
                borderColor: borderArray,
                borderWidth: 1
            }]
        },
    });

    let mixedChart = new Chart(ctx2, {
        type: 'bar',
        data: {
            datasets: [{
                label: data.budget_name,
                data: [data.budget_total],
                backgroundColor: 'rgba(216, 28, 28)',

            }, {
                label: 'Currently',
                data: [data.expense_total],
                backgroundColor: 'rgba(28, 144, 216, 0.8',
                type: 'bar'
            }],
            labels: [data.budget_name]
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
