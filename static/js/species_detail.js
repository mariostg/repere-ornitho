species = document.querySelectorAll(".species_name");

function toggle_display(elem) {
    if (elem.style.display == "none") {
        elem.style.display = "grid";
    } else {
        elem.style.display = "none";
    }
}
function close_all_detail() {
    let elems = document.querySelectorAll(".species_detail");
    for (const e of elems) {
        e.style.display = "none";
    }
}
for (const sp of species) {
    sp.addEventListener("click", function handleClick(event) {
        close_all_detail();
        let sib = sp.nextSibling.nextSibling;
        toggle_display(sib);
    });
}
