$(document).ready(function() {

    // JQuery code to be added in here.

    $(function() {

        var path_name = location.pathname;
        // console.log(path_name);

        $('ul.nav-pills li a').each(function(index){
            // console.log(index + ': ' + $(this).text() + ', href: ' + $(this).attr('href')) ;

            var a_href = $(this).attr('href');
            if(a_href == path_name){
                console.log('Matched')
                $(this).parent().siblings().removeClass('active');
                $(this).parent().addClass('active');
            }


        })


    });

    $('select[name = "module_name"]').on('change', function(){
        
        var selected_option_index = $( "select option:selected" ).val();
        console.log(selected_option_index);
        url_str = "get_module_by_id/?id=" + selected_option_index;
        $.get(url_str, function( data ) {
            console.log(data[0]);
            $('#id_num_of_students').val(data[0].fields.num_of_student);
            $('#id_teacher_name').val(data[0].fields.teacher);
        });
    })
    
      


});