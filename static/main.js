const img = document.getElementById('img');
const fileNameLabel = document.getElementById('fileNameLabel');

function file_img(event) {
  let fileInput = event.target;
  var file = fileInput.files[0];
  return file;
}

function setUp(event) {
  const file = file_img(event);

  if (file) {
    fileNameLabel.textContent = file.name;
  }

  if (file) {
    const reader = new FileReader();

    reader.onload = function (event) {
      img.style.display = 'block';
      img.src = event.target.result;
    };

    reader.readAsDataURL(file);
  }
}

document.getElementById('inputPicture').addEventListener('change', setUp);
