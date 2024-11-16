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

const dropDownToggler = document.querySelectorAll('.drop-toggler');

dropDownToggler.forEach((toggler) => {
    toggler.addEventListener('click', (event) => {
        event.stopPropagation();

        const togglerTarget = toggler.getAttribute('data-target');
        const togglerById = document.getElementById(togglerTarget);

        document.querySelectorAll('.drop-menu').forEach((menu) => {
            if (menu !== togglerById) {
                menu.classList.remove('show');
            }
        });

        dropDownToggler.forEach((active) => {
            if (active !== toggler) {
                active.classList.remove('nav-item-active');
            }
        });

        
        if (togglerById) {
            togglerById.classList.toggle('show');
            toggler.classList.add('nav-item-active');
        }
    });
});

document.addEventListener('click', () => {
    const allDrops = document.querySelectorAll('.drop-menu');
    
    allDrops.forEach((menu) => {
        menu.classList.remove('show');
    });

    dropDownToggler.forEach((click) => {
        click.classList.remove('nav-item-active');
    });
});