const express = require("express");
const axios = require("axios");
const https = require("https");

const app = express();
const PORT = process.env.PORT || 5000;

const handleObjectsRequest = async (req, res) => {
    try {
        const response = await axios({
            method: "GET",
            url: "https://api.restful-api.dev/objects",
            headers: {
                accept: "application/json"
            },
            httpsAgent: new https.Agent({ rejectUnauthorized: false }) // Ignore SSL certificate validation
        });

        // Log the entire response for debugging
        console.log(response.data);

        if (response.data) {
            res.send(response.data);
        } else {
            res.status(500).send("Unexpected response structure");
        }
    } catch (error) {
        console.error("Error fetching objects:", error);
        res.status(500).send("Error fetching objects");
    }
};

app.get("/products", handleObjectsRequest);

app.listen(PORT, () => {
    console.log(`Listening on port http://localhost:${PORT}`);
});
