const form = document.getElementById('sales-forecast-form');
const yearSelect = document.getElementById('year-select');
const monthSelect = document.getElementById('month-select');
const fileInput = document.getElementById('csv-upload') as HTMLInputElement;

form.addEventListener('submit', (event) => {
    event.preventDefault();
    const year = yearSelect.value;
    const month = monthSelect.value;
    const file = fileInput.files[0];

    // Form data processing logic here (e.g., API call)
});
