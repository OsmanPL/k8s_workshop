const axios = require("axios");

const getTraffic = async (req, res) => {
    for (let i = 0; i < 100; i++) {
        const { data } = await axios.get(
            "http://35.222.11.11.nip.io/getRegistros"
        );
        console.log(data.server);
    }
}

getTraffic();