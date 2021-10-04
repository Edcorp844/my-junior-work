window.onload = function() {
    var canvas = document.getElementById('canvas'),
        context = canvas.getContext('2d'),
        height = canvas.height = window.innerHeight,
        width = canvas.width = window.innerWidth,
        speed = 0.3,
        radius = 300,
        centerX = width / 2,
        centerY = height / 2,
        angle = 0,
        x, y;

    render();

    function render(){
        x = radius * Math.cos(angle) + centerX;
        y = radius * Math.sin(angle) + centerY;
        //context.clearRect(0, 0, width, height);
        context.beginPath();
        context.arc(x, y, 100, 0, Math.PI * 2, false);
        context.fillStyle = 'rgba('+ (20 *(angle + 0.25)) + ','+ (Math.random() * (angle + 0.25)) +',' + Math.random() * (angle + 0.25)  +',' + (200 * Math.random() * (angle + 0.25 )) +')';
        context.fill();

        angle += speed;
        requestAnimationFrame(render);
    }
}
