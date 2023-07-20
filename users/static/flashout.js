function closeMsg() {
    const msg = document.getElementById('msg');
    msg.addEventListener("click", () => {
        msg.remove();
    })
}

function restorebg() {
    document.querySelector('inpt').style.backgroundColor = 'white';
}
