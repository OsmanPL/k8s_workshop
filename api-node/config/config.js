require("dotenv").config();
const createPool = require("mysql2/promise").createPool;


// Base de datos
const DB_HOST = process.env.DB_HOST;
const DB_USER = process.env.DB_USER;
const DB_PASSWORD = process.env.DB_PASSWORD;
const DB_DATABASE = process.env.DB_DATABASE;
const DB_PORT = process.env.DB_PORT;

// Crear de base de datos mysql
const db = createPool({
    host: DB_HOST,
    user: DB_USER,
    password: DB_PASSWORD,
    port: DB_PORT,
    database: DB_DATABASE,
    multipleStatements: true,
  });


module.exports={db,DB_DATABASE,DB_HOST,DB_PASSWORD,DB_PORT,DB_USER}

