const DASHBOARD_API =
    "https://d8cl4m3i62.execute-api.us-east-1.amazonaws.com/dashboard";

const REPORT_API =
    "https://d8cl4m3i62.execute-api.us-east-1.amazonaws.com/report";


async function loadDashboard() {

    const response =
        await fetch(DASHBOARD_API);

    const data =
        await response.json();

    document.getElementById(
        "latestSavings"
    ).innerText =
        `₹ ${data.latest_estimated_savings}`;

    document.getElementById(
        "historicalSavings"
    ).innerText =
        `₹ ${data.historical_total_savings}`;

    document.getElementById(
        "resources"
    ).innerText =
        data.resources_analyzed;

    document.getElementById(
        "candidates"
    ).innerText =
        data.optimization_candidates;

    createChart(
        data.latest_estimated_savings,
        data.historical_total_savings
    );
}


function createChart(latest, historical) {

    new Chart(

        document.getElementById(
            "savingsChart"
        ),

        {

            type: "bar",

            data: {

                labels: [
                    "Latest",
                    "Historical"
                ],

                datasets: [

                    {

                        label: "Savings",

                        data: [
                            latest,
                            historical
                        ]
                    }
                ]
            }
        }
    );
}


async function loadReport() {

    const response =
        await fetch(REPORT_API);

    const data =
        await response.json();

    let html =
        `<h2>Latest Optimization Report</h2>`;

    data.findings.forEach(item => {

        html += `

            <div class="card">

                <p>
                    <strong>Instance:</strong>
                    ${item.instance_id}
                </p>

                <p>
                    <strong>CPU:</strong>
                    ${item.average_cpu}%
                </p>

                <p>
                    <strong>Recommendation:</strong>
                    ${item.recommendation}
                </p>

                <p>
                    <strong>Savings:</strong>
                    ₹${item.potential_savings}
                </p>

            </div>
        `;
    });

    document.getElementById(
        "reportContainer"
    ).innerHTML = html;
}


loadDashboard();