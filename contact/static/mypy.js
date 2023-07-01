function closeMsg() {
    const msg = document.getElementById('msg');
    msg.addEventListener("click", () => {
        msg.remove();
    })
}