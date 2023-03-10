
function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}

function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

function eraseCookie(name) {   
    document.cookie = name+'=; Max-Age=-99999999;';  
}

function scrapeFilters() {

	let currentURL = new URL(document.location);
	let qparams = currentURL.searchParams;
	qparams.delete('iid');
	qparams.delete('tag');

	var groups = [];
	var groupsForCookie = [];
	var kws;
	if ($('#ingredientChooser').val().length>0) {
		groups.push('.'+$('#ingredientChooser').val());
		groupsForCookie.push($('#ingredientChooser').val());
		qparams.append('iid',$('#ingredientChooser').val());
	}
	for (var x=1;x<$('fieldset').length+1;x++) {
		kws = '';
		$('#filtergroup'+x+' input:checked').each(function() {
			if (kws.length>0) {
				kws = kws + ', .'+($(this).val().replace(' ','_').replace('/','_'));	
			} else {
				kws = '.'+($(this).val().replace(' ','_').replace('/','_'));
			}
			groupsForCookie.push($(this).val().replace(' ','_').replace('/','_'))
			qparams.append('tag',$(this).val().replace(' ','_').replace('/','_'))
		});
		if (kws.length>0) {
			groups.push(kws);
		}
	}

	// cookie!
	setCookie('logicrecipes',groupsForCookie.join(),1);

	// update the querystring in the browser
	window.history.pushState({}, '', currentURL);

	return groups;
}

function restoreFilters(vals) {

	// fetch the URL and querystring; sanitize
	let currentURL = new URL(document.location);
	let qparams = currentURL.searchParams;
	qparams.delete('iid');
	qparams.delete('tag');

	$.each(vals,function(idx,val){
		if (val.indexOf('iid')==0) {
			$("#ingredientChooser").val(val);
			qparams.append('iid',val);
	
		} else {
			$("input[name="+val+"]").each(function() {$(this).prop("checked", true);});
			qparams.append('tag',val)
		}
	});

	// update the querystring in the browser
	window.history.pushState({}, '', currentURL);

}

function resetFilters() {
	$("input").prop("checked",false);
	$("#ingredientChooser").val("");
	eraseCookie('logicrecipes');
}

function refilterRecipes() {
	var filterGroups = scrapeFilters();

	if (filterGroups.length===0) {
		$('.entry').show();
		$('#matchesAnnotation').text($('.entry').length + ' recipes');
	}
	else {
		var matches = $('.entry');
		matches.hide();
		for (var groupIdx=0; groupIdx < filterGroups.length; groupIdx++) {
			matches = matches.filter($(filterGroups[groupIdx]));
		}
		matches.show();
		if (matches.length>1) {
			$('#matchesAnnotation').text(matches.length + ' matches out of '+$('.entry').length);	
			$('#matchesAnnotation').append($('<button style="margin-left: 1em;">RESET / SHOW ALL</button>'));
		} else {
			$('#matchesAnnotation').text(matches.length + ' match out of '+$('.entry').length);
			$('#matchesAnnotation').append($('<button style="margin-left: 1em;">RESET / SHOW ALL</button>'));
		}

	}

}


jQuery(document).ready(function() {

	// fetch the querystring
	let currentURL = new URL(document.location);
	let qparams = currentURL.searchParams;

	// if we have incoming querystring parameters for filtration, use them
	if (qparams.has('iid') || qparams.has('tag')) {
		    restoreFilters(Array.from(qparams.values()));
    // look for a cookie to restore filtration state with
	} else {
		var x = getCookie('logicrecipes');
		if (x) {
		    restoreFilters(x.split(','));
		}
	}
	refilterRecipes();  // doing this regardless, to force rebuilding of the tabular nav

	$('#recipefilters input').change(function() {
		refilterRecipes();
	});
	$('#recipefilters select').change(function() {
		refilterRecipes();
	});

	$("#matchesAnnotation").click(function() {
		resetFilters();
		refilterRecipes();
	});

});

