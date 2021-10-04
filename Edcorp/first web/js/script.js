(function (window, document) {
	var canvas = document.getElementById('canvas');
	var context = canvas.getContext('2d');
	var width = canvas.width = window.innerWidth;
	var height = canvas.height = window.innerHeght;
	
	context.fillRect(0, 0, width, height);

})(window, document);