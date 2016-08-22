
//
// Common functions, JS code injected in every page
//

function has_class(el, className) {
    if (el.classList)
        return el.classList.contains(className);
    else
        return new RegExp('(^| )' + className + '( |$)', 'gi').test(el.className);
}

function add_class(el, className) {
    if (el.classList)
        el.classList.add(className);
    else
        el.className += ' ' + className;
}

function remove_class(el, className) {
    if (el.classList)
        el.classList.remove(className);
    else
        el.className = el.className.replace(new RegExp('(^|\\b)' + className.split(' ').join('|') + '(\\b|$)', 'gi'), ' ');
}

function toggle_class(el, className) {
    if (el.classList) {
        el.classList.toggle(className);
    } else {
        var classes = el.className.split(' ');
        var existingIndex = classes.indexOf(className);

        if (existingIndex >= 0)
            classes.splice(existingIndex, 1);
        else
            classes.push(className);

        el.className = classes.join(' ');
    }
}

var nav = document.getElementById('js-site-navigation');
var nav_toggle = document.getElementById('js-navigation-toggle');

nav_toggle.addEventListener('click', function(e) {
    e.preventDefault();

    toggle_class(nav_toggle, 'active');
    toggle_class(nav, 'active');
});

