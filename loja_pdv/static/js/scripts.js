document.addEventListener('DOMContentLoaded', () => {
    language = {
        "emptyTable": "Nenhum registro encontrado",
        "info": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
        "infoFiltered": "(Filtrados de _MAX_ registros)",
        "infoThousands": ".",
        "loadingRecords": "Carregando...",
        "zeroRecords": "Nenhum registro encontrado",
        "search": "Pesquisar",
        "paginate": {
            "next": "Próximo",
            "previous": "Anterior",
            "first": "Primeiro",
            "last": "Último"
        },
        "aria": {
            "sortAscending": ": Ordenar colunas de forma ascendente",
            "sortDescending": ": Ordenar colunas de forma descendente"
        },
        "select": {
            "rows": {
                "_": "Selecionado %d linhas",
                "1": "Selecionado 1 linha"
            },
            "cells": {
                "1": "1 célula selecionada",
                "_": "%d células selecionadas"
            },
            "columns": {
                "1": "1 coluna selecionada",
                "_": "%d colunas selecionadas"
            }
        },
        "buttons": {
            "copySuccess": {
                "1": "Uma linha copiada com sucesso",
                "_": "%d linhas copiadas com sucesso"
            },
            "collection": "Coleção  <span class=\"ui-button-icon-primary ui-icon ui-icon-triangle-1-s\"><\/span>",
            "colvis": "Visibilidade da Coluna",
            "colvisRestore": "Restaurar Visibilidade",
            "copy": "Copiar",
            "copyKeys": "Pressione ctrl ou u2318 + C para copiar os dados da tabela para a área de transferência do sistema. Para cancelar, clique nesta mensagem ou pressione Esc..",
            "copyTitle": "Copiar para a Área de Transferência",
            "csv": "CSV",
            "excel": "Excel",
            "pageLength": {
                "-1": "Mostrar todos os registros",
                "_": "Mostrar %d registros"
            },
            "pdf": "PDF",
            "print": "Imprimir",
            "createState": "Criar estado",
            "removeAllStates": "Remover todos os estados",
            "removeState": "Remover",
            "renameState": "Renomear",
            "savedStates": "Estados salvos",
            "stateRestore": "Estado %d",
            "updateState": "Atualizar"
        },
        "autoFill": {
            "cancel": "Cancelar",
            "fill": "Preencher todas as células com",
            "fillHorizontal": "Preencher células horizontalmente",
            "fillVertical": "Preencher células verticalmente"
        },
        "lengthMenu": "Exibir _MENU_ resultados por página",
        "searchBuilder": {
            "add": "Adicionar Condição",
            "button": {
                "0": "Construtor de Pesquisa",
                "_": "Construtor de Pesquisa (%d)"
            },
            "clearAll": "Limpar Tudo",
            "condition": "Condição",
            "conditions": {
                "date": {
                    "after": "Depois",
                    "before": "Antes",
                    "between": "Entre",
                    "empty": "Vazio",
                    "equals": "Igual",
                    "not": "Não",
                    "notBetween": "Não Entre",
                    "notEmpty": "Não Vazio"
                },
                "number": {
                    "between": "Entre",
                    "empty": "Vazio",
                    "equals": "Igual",
                    "gt": "Maior Que",
                    "gte": "Maior ou Igual a",
                    "lt": "Menor Que",
                    "lte": "Menor ou Igual a",
                    "not": "Não",
                    "notBetween": "Não Entre",
                    "notEmpty": "Não Vazio"
                },
                "string": {
                    "contains": "Contém",
                    "empty": "Vazio",
                    "endsWith": "Termina Com",
                    "equals": "Igual",
                    "not": "Não",
                    "notEmpty": "Não Vazio",
                    "startsWith": "Começa Com",
                    "notContains": "Não contém",
                    "notStartsWith": "Não começa com",
                    "notEndsWith": "Não termina com"
                },
                "array": {
                    "contains": "Contém",
                    "empty": "Vazio",
                    "equals": "Igual à",
                    "not": "Não",
                    "notEmpty": "Não vazio",
                    "without": "Não possui"
                }
            },
            "data": "Data",
            "deleteTitle": "Excluir regra de filtragem",
            "logicAnd": "E",
            "logicOr": "Ou",
            "title": {
                "0": "Construtor de Pesquisa",
                "_": "Construtor de Pesquisa (%d)"
            },
            "value": "Valor",
            "leftTitle": "Critérios Externos",
            "rightTitle": "Critérios Internos"
        },
        "searchPanes": {
            "clearMessage": "Limpar Tudo",
            "collapse": {
                "0": "Painéis de Pesquisa",
                "_": "Painéis de Pesquisa (%d)"
            },
            "count": "{total}",
            "countFiltered": "{shown} ({total})",
            "emptyPanes": "Nenhum Painel de Pesquisa",
            "loadMessage": "Carregando Painéis de Pesquisa...",
            "title": "Filtros Ativos",
            "showMessage": "Mostrar todos",
            "collapseMessage": "Fechar todos"
        },
        "thousands": ".",
        "datetime": {
            "previous": "Anterior",
            "next": "Próximo",
            "hours": "Hora",
            "minutes": "Minuto",
            "seconds": "Segundo",
            "amPm": [
                "am",
                "pm"
            ],
            "unknown": "-",
            "months": {
                "0": "Janeiro",
                "1": "Fevereiro",
                "10": "Novembro",
                "11": "Dezembro",
                "2": "Março",
                "3": "Abril",
                "4": "Maio",
                "5": "Junho",
                "6": "Julho",
                "7": "Agosto",
                "8": "Setembro",
                "9": "Outubro"
            },
            "weekdays": [
                "Dom",
                "Seg",
                "Ter",
                "Qua",
                "Qui",
                "Sex",
                "Sáb"
            ]
        },
        "editor": {
            "close": "Fechar",
            "create": {
                "button": "Novo",
                "submit": "Criar",
                "title": "Criar novo registro"
            },
            "edit": {
                "button": "Editar",
                "submit": "Atualizar",
                "title": "Editar registro"
            },
            "error": {
                "system": "Ocorreu um erro no sistema (<a target=\"\\\" rel=\"nofollow\" href=\"\\\">Mais informações<\/a>)."
            },
            "multi": {
                "noMulti": "Essa entrada pode ser editada individualmente, mas não como parte do grupo",
                "restore": "Desfazer alterações",
                "title": "Multiplos valores",
                "info": "Os itens selecionados contêm valores diferentes para esta entrada. Para editar e definir todos os itens para esta entrada com o mesmo valor, clique ou toque aqui, caso contrário, eles manterão seus valores individuais."
            },
            "remove": {
                "button": "Remover",
                "confirm": {
                    "_": "Tem certeza que quer deletar %d linhas?",
                    "1": "Tem certeza que quer deletar 1 linha?"
                },
                "submit": "Remover",
                "title": "Remover registro"
            }
        },
        "decimal": ",",
        "stateRestore": {
            "creationModal": {
                "button": "Criar",
                "columns": {
                    "search": "Busca de colunas",
                    "visible": "Visibilidade da coluna"
                },
                "name": "Nome:",
                "order": "Ordernar",
                "paging": "Paginação",
                "scroller": "Posição da barra de rolagem",
                "search": "Busca",
                "searchBuilder": "Mecanismo de busca",
                "select": "Selecionar",
                "title": "Criar novo estado",
                "toggleLabel": "Inclui:"
            },
            "emptyStates": "Nenhum estado salvo",
            "removeConfirm": "Confirma remover %s?",
            "removeJoiner": "e",
            "removeSubmit": "Remover",
            "removeTitle": "Remover estado",
            "renameButton": "Renomear",
            "renameLabel": "Novo nome para %s:",
            "renameTitle": "Renomear estado",
            "duplicateError": "Já existe um estado com esse nome!",
            "emptyError": "Não pode ser vazio!",
            "removeError": "Falha ao remover estado!"
        },
        "infoEmpty": "Mostrando 0 até 0 de 0 registro(s)",
        "processing": "Carregando...",
        "searchPlaceholder": "Buscar registros"
    }

    let tableClientes = new DataTable('#dataTableClientes', {
        responsive: true,
        pageLength: 50,
        lengthChange: false,
        autoWidth: false,
        layout: {
            topStart: 'search',
            topEnd: null,
        },

        language, 
    });

    let tableProdutos = new DataTable('#dataTableProdutos', {
        responsive: true,
        ordering: false,
        autoWidth: false,     
        language,
    });

    let tableVenda = new DataTable('#dataTableVenda', {
        responsive: true,
        search: false,
        lengthChange: false,
        paging: false,
        layout: {
            topEnd: null,
            bottomStart: null,
        },
        language, 
    });

    let table = new DataTable('#dataTable', {
        responsive: true,
        ordering: false,
        buttons: {
            buttons: [
                'copy',
                'excel',
                'pdf',
                'print',
            ],
        },
        layout: {
            top0Start: 'buttons',
        },
        language, 
    });

    function removeMessages () {
        let messages = document.querySelectorAll('.messages');
        
        if (messages) {
            messages.forEach((message) => {
                message.remove();
                document.body.classList.remove('backdrop');
            });
        }
    };

    setTimeout(removeMessages, 2000);

    function removeLoader () {
        let loader = document.querySelector('#loader');
        if (loader) {
            loader.remove()
        }
    };

    setInterval(removeLoader, 0.500);
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

