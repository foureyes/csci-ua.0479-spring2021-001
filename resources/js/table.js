function main() {
const uls = document.querySelectorAll("ul.table");
  for(const ul of uls) {
    const table = document.createElement('table')
    table.classList.add('data-table');
    if(ul.classList.contains('fragment')) {
      table.classList.add('fragment');
    }
    const lis = ul.querySelectorAll('li');
    for(const li of lis) {
      console.log(li.className);
      const tr = document.createElement('tr');
      const parts = li.textContent.split(', ');
      for(const part of parts) {
        let cellTagName = 'td';
        if(li.classList.contains('header')) {
          cellTagName = 'th';
        }

        const cell = document.createElement(cellTagName);
        cell.textContent = part;
        tr.appendChild(cell);

        if(li.classList.contains('colspan')) {
          // TODO: fix this hack!
          cell.colSpan = "1000";
          cell.classList.add('colspan');
        }
      }
      table.appendChild(tr);
    }
    ul.parentNode.replaceChild(table, ul);
  }
}
document.addEventListener("DOMContentLoaded", main);
