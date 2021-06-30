const http = require("http");
const express = require("express");
var path = require("path");
const app = express();
const port = 3000;

app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: false }))
app.use(express.static(path.join(__dirname, 'public')));

app.listen(port, () => { 
    console.log(`Listening on port ${port}`)
})


app.get("/", (req, res) => {
    res.render("index", {
        quote: req.body
    })
})



app.post("/", (req, res) => {
    console.log(req.body)
    res.render("index", {
        quote: req.body
    })
})
