$( "#search-input" ).autocomplete({

    source: function( request, response ) {

        $.ajax( {
            url: $SCRIPT_ROOT +  "/search/" + request.term,
            success: function( data ) {
                response( data.results );
            }
        } );

    },
    minLength: 1,
    select: function( event, ui ) {

        console.log( "name " + ui.item.name + " name " + ui.item.name );

    }
} )
.autocomplete( "instance" )._renderItem = function( ul, item ) {
    return $( "<li>" )
        .append( $( "<div>" ).text( item.name) )
        .appendTo( ul );
};
