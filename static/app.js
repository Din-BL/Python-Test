document.addEventListener('DOMContentLoaded', () => {
  const resetBtn = document.getElementById('reset');
  const form = document.getElementById('my_form');
  const mainElements = document.getElementsByTagName('main');

  resetBtn.addEventListener('click', () => {
    if (mainElements.length > 0) {
      const main = mainElements[0];
      main.style.display = 'none';
      removeAllChildren(main);
    }
  });

  const loader = document.getElementById('loader');
  form.addEventListener('submit', () => {
    loader.style.display = 'flex';
    if (mainElements.length > 0) {
      const main = mainElements[0];
      main.style.display = 'none';
      removeAllChildren(main);
    }
  });
});

function removeAllChildren(element) {
  while (element.firstChild) {
    element.removeChild(element.firstChild);
  }
}
