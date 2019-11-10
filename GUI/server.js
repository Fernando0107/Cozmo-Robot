const express = require('express')
const pug = require('pug')
const app = express()
var cons = require('consolidate');

var bodyParser = require('body-parser');
const port = 8080


// view engine setup
app.engine('html', cons.swig)
app.use(express.static('views'))
app.set('view engine', 'html');


app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/', (req, res) => res.send('Hello From Express'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))