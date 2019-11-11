const express = require('express');
const app = express();
const port = 8080

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


app.listen(port, () => {
    console.log(`Example app listening on port ${port}!`)
});
