const express = require('express');
const cors = require('cors'); // Import the cors middleware
const app = express();
const port = +process.env.PORT || 9000;
const expressFileUpload = require('express-fileupload');
const path = require('path');
const assetsPath = path.resolve(__dirname, 'assets');
const router = express.Router();

router.use(expressFileUpload());
// Use the cors middleware with specific origin(s)
app.use(cors({
  origin: 'http://localhost:5184' // Allow requests from this origin
  // You can add more origins or use '*' to allow requests from any origin (not recommended for production)
}));
const file = router.post('/',(req, res) => {
  const { file } = req.files;
  file.mv(path.join(assetsPath, file.name));
  res.status(200).json({ message: 'File received' , path: file.name});
});
app.use('/file', file);


app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
