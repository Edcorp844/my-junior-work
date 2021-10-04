window.onload = function() {
    var canvas = document.getElementById('canvas'),
        context = canvas.getContext('2d'),
        height = canvas.height = window.innerHeight,
        width = canvas.width = window.innerWidth;

        context.translate(width/2, height/2);
        var k = Math.random(1) * 100;

    for(var a = 0; a < 2 * Math.PI; a += 0.001){
        var radius = 200 * Math.cos(k * a);
            x = radius * Math.cos(a),
            y = radius * Math.sin(a);

            context.fillStyle = 'rgba('+ (20 *(a+ 0.25)) + ','+ (Math.random() * (a + 0.25)) +',' + Math.random() * (a + 0.25)  +',' + (200 * Math.random() * (angle + 0.25 )) +')';
            context.fillRect(x, y, 3, 3);
    }
}