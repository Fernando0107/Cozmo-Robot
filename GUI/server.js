const express = require('express')
const pug = require('pug')
const app = express()
const port = 8080

app.get('/', (req, res) => res.send('Hello From Express'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))