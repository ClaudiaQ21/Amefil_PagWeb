document.addEventListener("DOMContentLoaded", (event) => {
    gsap.registerPlugin(Draggable);

    Draggable.create(".producto", {
        type: "x",
        bounds: ".contenedor_producto", // Limitar el arrastre al contenedor
        edgeResistance: 0.65,
        throwProps: true,
        onDragStart: function() {
            gsap.to(this.target, {cursor: "grabbing"});
        },
        onDragEnd: function() {
            gsap.to(this.target, {cursor: "grab"});
        }
    }); 
});
