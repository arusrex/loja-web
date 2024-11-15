document.addEventListener('DOMContentLoaded', () => {
    let table = new DataTable('#dataTable', {
        responsive: true,
        layout: {
            top0Start: 'buttons'
        },
        buttons: {
            name: 'primary',
            buttons: ['copy', 'csv', 'excel']
        }
    });
});