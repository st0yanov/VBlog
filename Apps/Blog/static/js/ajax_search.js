$(function() {

    var search_field = $('#search_text');

    search_field.keyup(function() {
        var search_val = search_field.val();
        if(search_val.length > 1) {
            $.ajax({
                type: 'POST',
                url: '/search/',
                data: {
                    'search_text': search_val,
                    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
                },
                dataType: 'json',
                complete: searchComplete,
            });
        }
    });

    function searchComplete(data) {
        var json = $.parseJSON(data.responseText);
        var search_results = $('#search_results');
        var html_data = '';

        if(json.ok) {
            if(json.articles.length > 0) {
                html_data += '<ul>';
                $.each(json.articles, function(index, item) {
                    html_data += '<li><a href="'+item.url+'" class="dark">'+item.title+'</a></li>';
                });
                html_data += '</ul>';
            } else {
                html_data = '<strong>Не бяха открити резултати.</strong>';
            }
        } else {
            html_data = '<strong>Възникна грешка.</strong>';
        }

        search_results.html(html_data)
    }

});