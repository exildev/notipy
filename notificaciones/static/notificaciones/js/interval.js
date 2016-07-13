$(document).ready(function () {
	var name = $("#interval-input-name").val();
	var val = $('[name="' + name + '"]').val();

	if (val.indexOf("dias[") > -1) {
		val = val.replace("dias[", "").replace("]", "");
		var lista = val.split(",");
		
		for (var val in lista){
			$('[name="interval-day-input"][value=' + lista[val] + ']').prop( "checked", true );
		}
		$("#interval-input-select").val("dias");
		$("#repeat-widget").parent().hide();
		$("#interval-input").hide();
		$("#interval-days").show();
		$("#interval-mes").hide();
	}else
	if (val.indexOf("mes[") > -1) {
		val = val.replace("mes[", "").replace("]", "");
		var lista = val.split(",");
		
		for (var val in lista){
			$('[name="interval-mes-input"][value=' + lista[val] + ']').prop("checked", true );
		}
		$("#interval-input-select").val("mes");
		$("#repeat-widget").parent().hide();
		$("#interval-input").hide();
		$("#interval-mes").show()
		$("#interval-days").hide();
	}else{
		var lista = [];
		$("#interval-input-select").val("range");
		$("#repeat-widget").parent().show();
		$("#interval-days").hide();
		$("#interval-input").show();
		$("#interval-mes").hide();
	}
	var cache = "";
	$("#interval-input-select").change(function(){
		var vv = $(this).val();
		if (vv == 'dias'){
			$("#repeat-widget").parent().hide();
			$("#interval-input").hide();
			$("#interval-days").show();
			$("#interval-mes").hide();

			lista = [];
			$('[name="' + name + '"]').val("");
		}else
		if (vv == 'mes'){
			$("#repeat-widget").parent().hide();
			$("#interval-input").hide();
			$("#interval-mes").show();
			$("#interval-days").hide();

			lista = [];
			$('[name="' + name + '"]').val("");
		}else{
			$("#repeat-widget").parent().show();
			$("#interval-days").hide();
			$("#interval-mes").hide();
			$("#interval-input").show();
			//cache = $('[name="' + name + '"]').val();
			$('[name="' + name + '"]').val("");
		}
	});
	$('[name="interval-day-input"]').change(function(){
		if ($(this).is(':checked')){
			lista.push($(this).val());
		}else{
			var i = lista.indexOf($(this).val());
			lista.splice(i, 1);
		}
		lista.sort();
		$('[name="' + name + '"]').val("dias[" + lista + "]");
		console.log(lista, this.checked);
	});
	$('[name="interval-mes-input"]').change(function(){
		if ($(this).is(':checked')){
			lista.push($(this).val());
		}else{
			var i = lista.indexOf($(this).val());
			lista.splice(i, 1);
		}
		lista.sort();
		$('[name="' + name + '"]').val("mes[" + lista + "]");
		console.log(lista, this.checked);
	});
});