var express = require('express');
var app = express();
console.log("Hello World")

app.get("/", function(req, res) {
res.send('Hello Express');
});
app.listen(3001, function() {
console.log('Listening on port 3000');
});

app.get("/", function(req,res) {
  res.sendFile(__dirname + "/views/index.html");
});

app.use(express.static(__dirname + "/public"));

app.use("/public", express.static(__dirname + "/public"));

app.get('/json', (req, res) => {
    let message = 'Hello json'
    if (process.env.MESSAGE_STYLE === 'uppercase') {
      return res.json({"message" : message.toUpperCase()})
    }
    return res.status(200).json({"message": message})
  })



  app.use("/json", (req, res) => {
       let message = "Hello json";
      
       if(process.env.MESSAGE_STYLE==="uppercase"){
         message = message.toUpperCase();
       }
       else{
         message = message;
       }
       return res.json({"message":message})
     })

     app.get('/json', (req, res) => {
      let message = "Hello json"
      if (process.env.MESSAGE_STYLE === "uppercase") {
        res.json({"message": message.toUpperCase()})
      } else {
        res.json({"message": message})
      }
    })

app.use(function middleware(req, res, next) {
  console.log;(req.method + "" + req.path + "-" + req.ip)
  next();
});

app.get('/now', 
(req, res, next) => {
  req.time = new Date().toString();
  next();
},  
(req, res) => {
  res.json({time: req.time})
});

app.get("/:word/echo", (req, res) => {
  res.json({"echo": req.params.word});
});

app.get("/name", (req, res) => {
  res.json({name: `${req.query.first} ${req.query.last}`})
});

var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended: false}));

app.post("/name", function(req, res) {
  res.json({name: `${req.body.first} ${req.body.last}`})
});