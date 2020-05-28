// from https://scotch.io/tutorials/how-to-use-the-javascript-fetch-api-to-get-data

const url = 'http://localhost:5001/todo/api/v1.0/tasks';
fetch(url)
.then((resp) => resp.json())
.then(function(data) {
  API_result = JSON.stringify(data);
  document.getElementById('tasks').innerHTML = API_result;
  })
  .catch(function(error) {
    console.log(error);
  });
