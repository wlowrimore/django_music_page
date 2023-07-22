function toggle(id) {
    const el = document.getElementById('dropdown');

    if(el.style.display === 'none') {
        el.style.display = 'flex'
    } else {
        el.style.display = 'none'
    }
}
