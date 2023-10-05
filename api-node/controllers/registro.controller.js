const db = require("../config/config").db;

const createRegistro = async (req, res) => {
    try{
        const { nombre } = req.body;
        await db.query(`call registrar('${nombre}');`);
        res.json({message: 'Registro creado',server:"nodejs"});
    }
    catch(e){
        res.json({message: 'Error al crear registro',server:"nodejs"});
    }
    
}

const getRegistros = async (req, res) => {
    try{
        const registros = await db.query('call getRegistros();');
        res.json({registros:registros[0][0],server:"nodejs"});
    }
    catch(e){
        res.json({message: 'Error al obtener registros',server:"nodejs"});
    }
}

module.exports = {createRegistro,getRegistros}
