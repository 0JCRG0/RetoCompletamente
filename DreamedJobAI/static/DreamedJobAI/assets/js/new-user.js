let dropArea = document.getElementById('drop-area');

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
dropArea.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) {
e.preventDefault();
e.stopPropagation();
}

['dragenter', 'dragover'].forEach(eventName => {
dropArea.addEventListener(eventName, () => dropArea.classList.add('dragover'), false);
});

['dragleave', 'drop'].forEach(eventName => {
dropArea.addEventListener(eventName, () => dropArea.classList.remove('dragover'), false);
});

dropArea.addEventListener('drop', handleDrop, false);

function handleDrop(e) {
let dt = e.dataTransfer;
let files = dt.files;
uploadWithHtmx(files);
}

function uploadWithHtmx(files) {
let formData = new FormData();
for (let i = 0; i < files.length; i++) {
    formData.append('files[]', files[i]);
}
htmx.ajax('POST', '/upload', {
    body: formData,
    headers: {
    'HX-Request': 'true'
    }
});
}
