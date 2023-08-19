function next(id=Math.floor(Math.random() * 100)+1) {
    fetch(`https://api.adviceslip.com/advice/${id}`)
    .then(response => response.json())
    .then(data => {
        document.querySelector('#next').onclick = function() {next(id+1)};
        document.querySelector('#back').onclick = function() {back(id-1)};
        document.querySelector('#adviceid').innerHTML = `Advice #${id}`;
        document.querySelector('p').innerHTML = `"${data['slip']['advice']}"`;
    })
    .catch(err => console.log(err));
}
function back(id) {
    if (id < 1) {
        alert('دیگه نداریم');
    }
    else {
        fetch(`https://api.adviceslip.com/advice/${id}`)
        .then(response => response.json())
        .then(data => {
            document.querySelector('#next').onclick = function() {next(id+1)};
            document.querySelector('#back').onclick = function() {back(id-1)};
            document.querySelector('#adviceid').innerHTML = `Advice #${id}`;
            document.querySelector('p').innerHTML = `"${data['slip']['advice']}"`;
        })
        .catch(err => console.log(err));
    }
}

next();