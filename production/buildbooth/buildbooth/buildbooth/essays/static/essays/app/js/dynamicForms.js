/**
 * by: wpl
 * Date: 9/21/13
 * Time: 9:06 PM
 */
    function updateElementIndex(el, prefix, ndx, field) {
		var id_regex = new RegExp('(' + prefix + '-__prefix__-' + field + ')');
        console.log(id_regex);
		var replacement = prefix + '-' + ndx + '-' + field;
        console.log(replacement);
		if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
		if (el.id) el.id = el.id.replace(id_regex, replacement);
		if (el.name) el.name = el.name.replace(id_regex, replacement);
	}

var item;
    function addForm(btn, prefix) {
        var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
        var row = $('#' + prefix + '-__prefix__').clone(true).get(0);
        $(row).attr('id', prefix + '-' + formCount).insertAfter($('.dynamic-form:last')).removeClass('hide');
        $(row).children().not(':last').each(function() {
            console.log($(this)[0]);
            item= $(this)[0];
            var field_tag = $(this)[0].id.split('-');
            field_tag = field_tag[field_tag.length-1];
            console.log(field_tag);
    	    updateElementIndex($(this)[0], prefix, formCount, field_tag);
    	    $(this).val('');
        });
        $(row).children(':last').remove();
        $(row).find('[for$="DELETE"]').remove();
        $(row).find('[id$="DELETE"]').remove();
        $(row).prepend('<a class="lead text-error pull-right delete-row" href="javascript:void(0)" id="remove-'
            + prefix
            + '-'
            + formCount
            + '-row"><i class="icon-remove-circle"></i></a>');
        $(row).find('.delete-row').click(function() {
    	    deleteForm(this, prefix);
        });

        $('#id_' + prefix + '-TOTAL_FORMS').val(formCount + 1);
        return false;
    }

    function deleteForm(btn, prefix) {
        $(btn).parents('.dynamic-form').remove();
        var forms = $('.dynamic-form');
        $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
        for (var i=0, formCount=forms.length; i<formCount; i++) {
    	    $(forms.get(i)).children().children().find('input').each(function() {
                var field_tag = $(this)[0].id.split('-');
                field_tag = field_tag[field_tag.length-1];
    	        updateElementIndex(this[0], prefix, i, field_tag);
    	    });
        }
        return false;
    }

 $(function () {
        $('.add-row').click(function() {
    	    return addForm(this, 'thesispart_set');
        });
        $('.delete-row').click(function() {
    	    return deleteForm(this, 'thesispart_set');
        });
     $('.thesis-dynamic-forms-holder').html($('.thesis-dynamic-forms'));
    })
