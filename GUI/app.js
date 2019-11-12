const express = require('express');
const fs = require('fs');
const timestamp = require('time-stamp');

const app = express();
const port = 8080


console.log('TimeStamp:\n',timestamp('YYYY/MM/DD mm:ss'));

app.set('view engine', 'pug');


app.get('/', (req, res) => {
    res.render('index');

});

app.get('/account', (req, res) => {
    res.render('account', {
        money: '$7,000',
        recTransaction: false
    });
});

app.get('/todo', (req, res) => {
    res.render('todoList');

});

app.get('/nav', (req, res) => {
    res.render('navbar');

});

const todo = fs.readFileSync('./todo-cozmo.yml', 'utf8')

app.get('/card', (req, res) => {
    res.render('card');
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}!`)
});
