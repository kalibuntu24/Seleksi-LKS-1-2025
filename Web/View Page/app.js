const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/view', (req, res) => {
  const page = req.query.page;
  const filePath = path.join(__dirname, page);

  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      return res.status(404).send('Page not found');
    }
    res.send(data);
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
