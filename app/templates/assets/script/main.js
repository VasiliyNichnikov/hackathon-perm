

const videoBtn = document.querySelector('#btn-1');
const videoDiv = document.querySelector('.block-1');
const video = document.querySelector('.video-block');
const dictDiv = document.querySelector('.block-2');
const objDiv = document.querySelector('.block-3');

const graphBtn = document.querySelector('#btn-2');
const graphDiv = document.querySelector('.block-4');

videoBtn.addEventListener('click', () => {
    if (videoDiv.classList.contains('d-none')) {
        videoDiv.classList.remove('d-none');
        videoDiv.classList.add('d-flex');
        video.style.display = 'block';
        dictDiv.style.display = 'block';
        objDiv.style.display = 'block';
        graphDiv.style.display = 'none';
    }
});

graphBtn.addEventListener('click', () => {
    if (graphDiv.style.display === 'none') {
        graphDiv.style.display = 'block';
        video.style.display = 'none';
        videoDiv.classList.remove('d-flex');
        videoDiv.classList.add('d-none');
        dictDiv.style.display = 'none';
        objDiv.style.display = 'none';
    }
});