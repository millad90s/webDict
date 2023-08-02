const addButton = document.getElementById('add-button');
const divContainer = document.getElementById('div-container');

let divCount = 0;

function createNewDiv() {
  divCount++;

  const newDiv = document.createElement('div');
  newDiv.setAttribute('class', 'input-group input-group-lg my-2 ms-5 rightfloat Option-part');

  const input = document.createElement('input');
  input.setAttribute('type', 'text');
  input.setAttribute('class', 'form-control persian-p');
  input.setAttribute('required', 'true');
  input.setAttribute('maxlength', '50');
  input.setAttribute('placeholder', 'گزینه ' + (divCount+1));
  input.setAttribute('name', 'Option' + (divCount+1));

  const clearDiv = document.createElement('div');
  clearDiv.setAttribute('class', 'clear');

  newDiv.appendChild(input);
  newDiv.appendChild(clearDiv);

  divContainer.appendChild(newDiv);
}

addButton.addEventListener('click', createNewDiv);
