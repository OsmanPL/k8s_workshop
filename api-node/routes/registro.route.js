const express = require("express")
const router = express.Router()
const registroController = require("../controllers/registro.controller")

router.get("/getRegistros", registroController.getRegistros);
router.post("/addRegistro", registroController.createRegistro);


module.exports = router