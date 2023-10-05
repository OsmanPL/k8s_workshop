const registroRoute = require('./routes/registro.route')

var express = require('express')
const bodyParser = require('body-parser');
require('dotenv').config();

var app = express();

const port = process.env.PORT


// Middlewares
app.use(bodyParser.json({ limit: '50mb' }))
app.use(bodyParser.urlencoded({extended: true}))

app.use("/", registroRoute)

app.get('/', function (req, res) {
    res.send('hello, world!')
  })

app.listen(port, function () {
    console.log(`Server on port http://localhost:${port}`);
  });

