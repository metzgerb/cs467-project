$(document).ready(function(){
    $('input[type=radio][name=search-type]').change(function() {
        if (this.value == 'bfs') {
            $('.page-limit').html('<label name="max-search-bfs" >Page limit (Range 1-3):</label><br><input id="page-limit-bfs" name="max" class="form-control" required type="number" min="1" max="3"/>');
        }
        else if (this.value == 'dfs') {
            $('.page-limit').html('<label name="max-search" >Page limit (Range 1-10):</label><br><input id="page-limit-dfs" name="max" class="form-control" required type="number" min="1" max="10"/>');
    }
    });
    /*
    $('#search').submit(function(event){
        event.preventDefault();

        var link = $('#link').val();
        var search_type = $("input[name='search-type']:checked").val();
        var max;
        if ($('#page-limit-dfs').val()){
            max = $('#page-limit-dfs').val();
        }
        else {
            max = $('#page-limit-bfs').val();
        }
        
        console.log(link, search_type, max);

        $.ajax({
            url : '/search',
            type : 'POST',
            data : {
                'link': link,
                'search_type': search_type,
                'max': max
            },
            success : function(results) {              
                window.location.replace("/results");
            },
            error : function(request,error)
            {
                console.log(error, request);
            }
        });
    });
    */
});