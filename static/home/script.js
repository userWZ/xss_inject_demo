let search = document.getElementById('search');
let results = document.getElementById('results');
let potentials = [];

const searchables = [
  {'name': 'A Random Post'},
];


function updateResults() {
  //console.log(potentials);
  while( results.firstChild ) {
  results.removeChild( results.firstChild );
  }

  if((potentials.length == 0) && (search.value != ''))
  {
    let message = document.createElement('p');
    let text = document.createTextNode('No results for ' + search.value);

    message.classList.add('mx-auto', 'mt-3');
    message.appendChild(text);

    results.appendChild(message);
  }

  for(let i = 0; i < potentials.length; i++)
  {
    let result = document.createElement('li');
    result.classList.add('result', 'list-group-item', 'mt-2');
    results.appendChild(result);
    result.innerHTML = potentials[i];
  }
}


function getSearchResults(search_string) {

  potentials = []

  if(search_string == '')
  {
    return
  }

  for(let i = 0; i < searchables.length; i++)
  {
    let term = searchables[i].name.toLowerCase();
    if(term.includes(search_string))
    {
      potentials.push(term);
    }
  }
}

search.addEventListener('keyup', (e) => {
  getSearchResults(search.value.toLowerCase());
  updateResults();
});