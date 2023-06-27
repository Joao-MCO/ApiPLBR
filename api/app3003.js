const express = require('express')
const app = express()
const port = 3003
const key = 'test85g57'
const idLiga = 2012

app.get('/', (req, res) => {
	url = 'https://api.football-data-api.com/league-season?key=' + key + '&season_id=' + idLiga
	fetch(url).then((response) => response.json()).then((data) => res.send(data))
})

app.listen(port, () => {
	console.log(`Example app listening on port ${port}`)
})

app.get('/times', (req, res) => {
	url = 'https://api.football-data-api.com/league-teams?key=' + key + '&season_id=' + idLiga + '&include=stat'
	fetch(url).then((response) => response.json()).then((data) => res.send(data))

})