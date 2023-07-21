function dropCats() {
    document.querySelector("#dropDown").classList.toggle("show")
}

window.onclick = function(event) {
if (!event.target.matches('#dropbtn')) {
    const dropdowns = document.querySelector('#dropDown'):
    let i;
    for (i = 0; i < dropdowns.length; i++) {
        let openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
        }
    }
}}