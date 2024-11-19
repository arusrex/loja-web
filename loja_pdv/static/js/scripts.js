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

// NAVBAR DROPDOWN

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

// SIDEBAR DROPDOWN

const sideDropDownToggler = document.querySelectorAll('.side-drop-toggler');

sideDropDownToggler.forEach((toggler) => {
    toggler.addEventListener('click', (event) => {
        event.stopPropagation();

        const togglerTarget = toggler.getAttribute('data-target');
        const togglerById = document.getElementById(togglerTarget);

        document.querySelectorAll('.side-drop-menu').forEach((menu) => {
            if (menu !== togglerById) {
                menu.classList.remove('show');
            }
        });

        sideDropDownToggler.forEach((active) => {
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
    const allDrops = document.querySelectorAll('.side-drop-menu');
    
    allDrops.forEach((menu) => {
        menu.classList.remove('show');
    });

    sideDropDownToggler.forEach((click) => {
        click.classList.remove('nav-item-active');
    });
});

const btnMenu = document.querySelector('#btn-menu');

btnMenu.addEventListener('click', () => {
    let siderbar = document.querySelector('.sidebar-container');
    if (siderbar.style.display === 'none') {
        siderbar.style.display = 'block'
    } else {
        siderbar.style.display = 'none'
    }
    
});