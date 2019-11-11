const express = require('express');
const app = express();
const port = 5000

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


app.listen(port, () => {
    console.log(`Example app listening on port ${port}!`)
});
