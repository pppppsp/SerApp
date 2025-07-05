let div_element = document.getElementById('window_journal');


$('#button-form').click((e) => {
    e.preventDefault();
    console.log('123');
    const dataFilter = {}
    dataFilter['csrfmiddlewaretoken'] = $('input[name="csrfmiddlewaretoken"]').val();
    dataFilter['level'] = $('#level').val();
    dataFilter['country'] = $('#country').val();
    dataFilter['open_access'] = $('#open_access').val();
    dataFilter['h_index'] = $('#h_index').val();

    $.ajax({
        type: "POST",
        url: window.location.href,
        data: dataFilter,
        success: (resp) => {
            console.log(resp);
            const div = document.createElement('div')
            div.style.fontFamily = 'Arial';
            div.style.backgroundColor = 'white';
            div.setAttribute("id", "window_temp"); // id 
            if (resp.got_journals.length == 0) {
                let p = `
                        <p style='text-align:center;'>Нет результатов</p>
                `
                div.innerHTML += p
                $('#window_temp').remove();
                div_element.appendChild(div);
            } else {
                resp.got_journals.forEach(elem => {
                    console.log(elem);
                    let p = `
                        <p class="text-gray-800"><b>Название научного журнала:</b> ${elem.title}</p>
                        <p class="text-gray-800"><b> ISSN:</b> ${elem.issn}</p>
                        <p class="text-gray-800"><b> Уровень:</b> ${elem.levels_id}</p>
                        <p class="text-gray-800"><b> Страна:</b> ${elem.country}</p>
                        <p class="text-gray-800"><b> Тип доступа:</b>${ elem.open_access == true ? 'Открытый' : 'Закрытый'}</span>
                           
                        </p>
                        <p class="text-gray-800"><b> Индекс Хирша:</b> ${elem.h_index}</p>
                `
                    div.innerHTML += p
                });
                $('#window_temp').remove();
                div_element.appendChild(div);
            }

        },
        errors: (resp) => {
            console.log(resp);
            const div = document.createElement('div')
            div.style.fontFamily = 'Arial';
            div.style.backgroundColor = 'white';
            div.setAttribute("id", "window_temp"); // id 
            resp.got_journals.forEach(elem => {
                console.log(elem);
                let p = `
                        <p> Ошибка на сервере </p>
                `
                div.innerHTML += p
            });
            $('#window_temp').remove();
            div_element.appendChild(div);
        },
    });


})