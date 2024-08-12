$('document').ready(function() {
	$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
		const helloText = data.hello;
		$('#hello').text(helloText);
	});
});
