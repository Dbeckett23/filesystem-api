var express = require('express');
var router = express.Router();

// Doesn't work
router.post('/create-file/', (req, res, next) => {
    console.log(req.url);
    res.json(req.url);
});

router.get('/create-file/', (req, res, next) => {
    res.json(req.url);
});

module.exports = router;
