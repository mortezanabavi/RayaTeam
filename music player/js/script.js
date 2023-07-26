const audio = document.querySelector('audio');
const durationTime = document.getElementById('duration');
const currentTime = document.getElementById('current-time');
const slider = document.getElementById('seek-slider');
const player = document.getElementById('audio-player-container');

function playingAudio() {
    if (!audio.paused) {
        slider.value = Math.floor(audio.currentTime);
        currentTime.textContent = calculateTime(slider.value);
    }
}
function play() {
    audio.play();
    document.querySelector('#play-icon i').className = 'fa fa-pause';
    document.querySelector('#play-icon').onclick = function () {pause()};
}
function pause() {
    audio.pause();
    document.querySelector('#play-icon i').className = 'fa fa-play';
    document.querySelector('#play-icon').onclick = function () {play()};
}
function calculateTime(secs) {
    const minutes = Math.floor(secs / 60);
    const seconds = Math.floor(secs % 60);
    const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
    return `${minutes}:${returnedSeconds}`;
}
function insertTimes() {
    durationTime.textContent = calculateTime(audio.duration);
    slider.max = Math.floor(audio.duration);
}
function resetAudio() {
    pause();
    currentTime.textContent = '0:00';
    slider.value = 0;
}
function next(id) {
    fetch(`musics/${Number(id) + 1}/detail.json`)
    .then(response => response.json())
    .then(data => {
        id = Number(id) + 1;
        resetAudio();
        audio.src = `musics/${id}/music.mp3`;
        document.querySelector('.box img').src = `musics/${id}/icon.jpg`
        document.querySelector('.box h2').textContent = data['Singer'];
        document.querySelector('.box p').textContent  = data['Name'];
        document.querySelector('#next').onclick = function () {next(id)};
        document.querySelector('#back').onclick = function () {back(id)};
        document.querySelector('audio').onended = function () {next(id)};
        play();
    }).catch(err => next('0'));
}
function back(id) {
    fetch(`musics/${Number(id)-1}/detail.json`)
    .then(response => response.json())
    .then(data => {
        id = Number(id) - 1;
        resetAudio();
        audio.src = `musics/${id}/music.mp3`;
        document.querySelector('.box img').src = `musics/${id}/icon.jpg`
        document.querySelector('.box h2').textContent = data['Singer'];
        document.querySelector('.box p').textContent  = data['Name'];
        document.querySelector('#back').onclick = function () {back(id)};
        document.querySelector('#next').onclick = function () {next(id)};
        document.querySelector('audio').onended = function () {next(id)};
        play();
    }).catch(err => next('5'));
}
setInterval(playingAudio, 1000);

if (audio.readyState > 0) {
    insertTimes();
}
else {
    audio.addEventListener('loadedmetadata', () => {
        insertTimes();
    });
}

slider.addEventListener('input', () => {
    currentTime.textContent = calculateTime(slider.value);
});

slider.addEventListener('change', () => {
    audio.currentTime = slider.value;
});
