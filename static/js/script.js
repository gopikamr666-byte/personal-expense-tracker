


const editModal = document.getElementById("editModal");
const editForm = document.getElementById("editForm");

const editButtons = document.querySelectorAll(".edit-btn");
const closeButton = document.getElementById("closeModal");

editButtons.forEach(button => {

    button.addEventListener("click", function () {

        const id = this.dataset.id;

        editForm.action = `/edit/${id}/`;

        document.getElementById("editTitle").value =
            this.dataset.title;

        document.getElementById("editAmount").value =
            this.dataset.amount;

        document.getElementById("editCategory").value =
            this.dataset.category;

        document.getElementById("editDate").value =
            this.dataset.date;

        document.getElementById("editNote").value =
            this.dataset.note;

        editModal.classList.add("show");
    });

});

closeButton.addEventListener("click", function () {
    editModal.classList.remove("show");
});

editModal.addEventListener("click", function (event) {
    if (event.target === editModal) {
        editModal.classList.remove("show");
    }
});

document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
        editModal.classList.remove("show");
    }
});



const chartCanvas = document.getElementById("expenseChart");

if (chartCanvas && typeof Chart !== "undefined") {

    const labels = JSON.parse(
        document.getElementById("chart-labels").textContent
    );

    const values = JSON.parse(
        document.getElementById("chart-values").textContent
    );

    const colors = JSON.parse(
        document.getElementById("chart-colors").textContent
    );

    const legend = document.getElementById("chartLegend");

    if (values.length > 0) {

        new Chart(chartCanvas, {

            type: "doughnut",

            data: {
                labels: labels,

                datasets: [{
                    data: values,
                    backgroundColor: colors,
                    borderWidth: 0,
                    hoverOffset: 8
                }]
            },

            options: {
                responsive: true,
                maintainAspectRatio: true,
                cutout: "72%",

                plugins: {
                    legend: {
                        display: false
                    },

                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return context.label + ": ₹" +
                                    Number(context.raw).toFixed(2);
                            }
                        }
                    }
                }
            }

        });

        labels.forEach((label, index) => {

            const item = document.createElement("div");
            item.className = "legend-item";

            const color = document.createElement("span");
            color.className = "legend-color";
            color.style.backgroundColor = colors[index];

            const text = document.createElement("span");
            text.textContent = label;

            item.appendChild(color);
            item.appendChild(text);

            legend.appendChild(item);
        });

    } else {
        legend.textContent = "No expenses recorded this month.";
    }
}
