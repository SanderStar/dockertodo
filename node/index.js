const app = require('express')()
const MongoClient = require('mongodb').MongoClient
const bodyParser = require('body-parser')

let tododb


app.set('views', './views')
app.set('view engine', 'pug')
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: true}))


app.get('/todo.js', (req, res) => {
    tododb.find().toArray().then(items => {
        res.render('todo', {items})
    })
})

app.post('/todo.js/new', (req, res) => {
    tododb.insertOne(req.body).then(() => res.redirect('/todo.js'))
})

// the second mongodb refers to the mongodb definition in the docker-compose.yml
MongoClient.connect('mongodb://mongodb:27017/tododb')
	// tzt
    .then(db => {
        let server
        tododb = db.collection('tododb')
        server = app.listen(3000, console.log)
        return [db, server]
    })
    .then(([db,server]) => {
        process.on('SIGTERM', () => {
            server.close()
            db.close()
        })
    })
