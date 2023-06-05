const axios = require('axios').default;

axios.get('http://localhost:3000/sum/6/2').then(function (response) {
	console.log(response.data);
}).catch(function (error) {console.log(error);})

axios.get('http://localhost:3000/sub/6/2').then(function (response) {
	console.log(response.data);
}).catch(function (error) {console.log(error);})

axios.get('http://localhost:3000/mlt/6/2').then(function (response) {
	console.log(response.data);
}).catch(function (error) {console.log(error);})

axios.get('http://localhost:3000/div/6/2').then(function (response) {
	console.log(response.data);
}).catch(function (error) {console.log(error);})