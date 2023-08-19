function mode(type) {
    if (type == 'dark') {
        document.querySelector('body').style.backgroundColor = '#1e1e1e';
        document.querySelector('.box').style.backgroundColor = '#3e3e42';
        document.querySelector('p').style.color = 'white';
        document.querySelector('span').style.color = 'white';
        document.querySelector('.mode').innerHTML = 'light_mode';
        document.querySelector('.bm').onclick = function() { mode('light')};
    }
    else {
        document.querySelector('body').style.backgroundColor = 'beige';
        document.querySelector('.box').style.backgroundColor = 'white';
        document.querySelector('p').style.color = 'black';
        document.querySelector('span').style.color = 'black';
        document.querySelector('.mode').innerHTML = 'dark_mode';
        document.querySelector('.bm').onclick = function() { mode('dark')};
    }
}