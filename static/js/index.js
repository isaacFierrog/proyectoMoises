const d = document;
const w = window;


const mostrarBotonInicio = () => {
    w.addEventListener('scroll', e => {
        console.log(e)
    });
};


d.addEventListener('DOMContentLoaded', e => {
    mostrarBotonInicio();
});